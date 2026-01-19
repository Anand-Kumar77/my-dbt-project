#!/usr/bin/env python3
import os
import sys
import json
import requests
from pathlib import Path
import re

class FreeDocGenerator:
    def __init__(self):
        self.ollama_host = os.getenv('OLLAMA_HOST', 'http://localhost:11434')
        self.model = "llama3.2:3b"
    
    def generate_all(self):
        """Generate docs for all changed SQL files"""
        changed_files = os.getenv('CHANGED_FILES', '').split()
        
        if not changed_files:
            print("No SQL files changed")
            return
        
        for sql_file in changed_files:
            if not sql_file.endswith('.sql'):
                continue
            
            print(f"\n{'='*70}")
            print(f"Processing: {sql_file}")
            print(f"{'='*70}")
            
            try:
                self.generate_doc(sql_file)
                print(f"✅ Success: {sql_file}")
            except Exception as e:
                print(f"❌ Error: {sql_file} - {e}")
                print("⚠️ Using fallback template generation")
                self.generate_template_based(sql_file)
    
    def generate_doc(self, sql_file):
        """Generate documentation for a single SQL file"""
        # Read SQL content
        with open(sql_file, 'r', encoding='utf-8') as f:
            sql_content = f.read()
        
        model_name = Path(sql_file).stem
        dependencies = self.extract_dependencies(sql_content)
        
        # Build prompt for LLM
        prompt = self.build_prompt(model_name, sql_content, dependencies)
        
        # Try to generate with Ollama
        try:
            print("🤖 Generating with Ollama LLM...")
            documentation = self.generate_with_ollama(prompt)
        except Exception as e:
            print(f"⚠️ Ollama failed: {e}")
            print("📝 Using template-based generation...")
            documentation = self.template_doc(model_name, sql_content, dependencies)
        
        # Save documentation
        output_path = Path(sql_file).with_suffix('.md')
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(documentation)
        
        print(f"✅ Documentation saved: {output_path}")
    
    def extract_dependencies(self, sql_content):
        """Extract dbt dependencies from SQL"""
        deps = []
        
        # Find ref() calls
        ref_pattern = r"ref\(['\"]([^'\"]+)['\"]\)"
        deps.extend(re.findall(ref_pattern, sql_content))
        
        # Find source() calls
        source_pattern = r"source\(['\"]([^'\"]+)['\"],\s*['\"]([^'\"]+)['\"]\)"
        sources = re.findall(source_pattern, sql_content)
        deps.extend([f"{s[0]}.{s[1]}" for s in sources])
        
        return list(set(deps))
    
    def build_prompt(self, model_name, sql_content, dependencies):
        """Build prompt for LLM"""
        deps_text = ', '.join(dependencies) if dependencies else 'None'
        
        return f"""You are a technical documentation expert. Generate comprehensive documentation for this dbt SQL model.

Model Name: {model_name}

SQL Code:
```sql
{sql_content}
```

Dependencies: {deps_text}

Generate documentation with these sections:

1. **Overview** (2-3 sentences explaining what this model does)
2. **Business Purpose** (Why this model exists, what business need it serves)
3. **Data Sources** (What tables/models it reads from)
4. **Transformation Logic** (Step-by-step explanation of the SQL transformations)
5. **Output Schema** (Description of output columns)
6. **Usage Examples** (How to use this model in downstream queries)
7. **Data Quality Notes** (Any important caveats or quality considerations)

Format the documentation in clean Markdown. Be specific and technical but also accessible to new team members.
"""
    
    def generate_with_ollama(self, prompt):
        """Call Ollama API to generate documentation"""
        response = requests.post(
            f"{self.ollama_host}/api/generate",
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.3,
                    "top_p": 0.9
                }
            },
            timeout=300  # 5 minutes
        )
        
        response.raise_for_status()
        result = response.json()
        return result.get('response', '')
    
    def template_doc(self, model_name, sql_content, dependencies):
        """Generate basic documentation using template (fallback)"""
        deps_list = '\n'.join([f"- `{dep}`" for dep in dependencies]) if dependencies else "*No dependencies*"
        
        return f"""# {model_name}

*Auto-generated documentation*

## Overview

This dbt model transforms data for downstream analytics and reporting use.

## Data Sources

### Dependencies

{deps_list}

## SQL Code
```sql
{sql_content}
```

## Transformation Logic

This model performs the following transformations:
1. Reads from source tables/models
2. Applies business logic and data transformations
3. Outputs a cleaned, structured dataset

## Usage

To use this model in other dbt models:
```sql
select * from {{{{ ref('{model_name}') }}}}
```

## Notes

- Review the SQL code above for detailed transformation logic
- Ensure upstream dependencies are refreshed before running this model
- Test data quality after any changes to this model

---

*Generated by Free SQL Documentation Generator*
*Powered by Template Engine (Ollama unavailable)*
"""
    
    def generate_template_based(self, sql_file):
        """Fallback: Generate docs using template only"""
        try:
            with open(sql_file, 'r', encoding='utf-8') as f:
                sql_content = f.read()
            
            model_name = Path(sql_file).stem
            dependencies = self.extract_dependencies(sql_content)
            documentation = self.template_doc(model_name, sql_content, dependencies)
            
            output_path = Path(sql_file).with_suffix('.md')
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(documentation)
            
            print(f"✅ Template documentation saved: {output_path}")
        except Exception as e:
            print(f"❌ Template generation also failed: {e}")

if __name__ == '__main__':
    print("="*70)
    print("FREE SQL DOCUMENTATION GENERATOR")
    print("="*70)
    
    generator = FreeDocGenerator()
    generator.generate_all()
    
    print("\n" + "="*70)
    print("GENERATION COMPLETE")
    print("="*70)
