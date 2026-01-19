# Customer Data Definitions

## Overview

This document defines customer-related data entities and their business meaning.

## Customer Status

- **active**: Customer has made a purchase in the last 12 months
- **inactive**: Customer has not made a purchase in over 12 months
- **churned**: Customer explicitly requested account closure

## Key Fields

### customer_id

- **Type**: Integer
- **Description**: Unique identifier for each customer
- **Source**: Auto-generated in CRM system

### customer_name

- **Type**: String
- **Description**: Full name of the customer
- **Format**: "First Last"

### email

- **Type**: String
- **Description**: Primary email address
- **Validation**: Must be valid email format
- **Required**: Yes for active customers

```

**Save:** `Ctrl + S`

---

## **PART 6: Initialize Git in VS Code**

### **Step 1: Open Source Control**
```

In VS Code:

1. Click the Source Control icon (left sidebar - looks like a branch)
   OR press Ctrl + Shift + G

You'll see: "No source control providers registered"

```

### **Step 2: Initialize Repository**
```

1. Click "Initialize Repository" button
2. VS Code will initialize Git

You'll now see all your files listed as changes (with "U" for untracked)

```

---

## **PART 7: Connect to GitHub and Push**

### **Step 1: Sign in to GitHub in VS Code**
```

1. Click the Account icon (bottom left, looks like a person)
2. Click "Sign in to Sync Settings"
3. Choose "Sign in with GitHub"
4. Browser will open
5. Click "Authorize Visual-Studio-Code"
6. Return to VS Code

```

**You're now signed in!** ✅

---

### **Step 2: Create Repository on GitHub from VS Code**
```

In Source Control panel:

1. You'll see all your files with "U" (untracked)
2. At the top, in the message box, type:

   Initial commit - project setup

3. Click the ✓ (checkmark) button to commit
   OR press Ctrl + Enter

4. After commit, you'll see "Publish Branch" button
5. Click "Publish Branch"

A dialog appears:

```

**Choose repository visibility:**
```

┌─────────────────────────────────────────┐
│ Publish to GitHub │
│ ─────────────────────────────────────── │
│ │
│ Repository Name: │
│ my-dbt-project │
│ │
│ ⦿ Publish to GitHub public repository │
│ ○ Publish to GitHub private repository │
│ │
│ [Publish Repository] │
└─────────────────────────────────────────┘

Choose:

- Public (free, anyone can see)
- OR Private (only you can see, but GitHub Actions might have limits)

Click "Publish Repository"

```

**VS Code will:**
1. Create repository on GitHub
2. Push all your files
3. Show notification: "Successfully published"

---

### **Step 3: Verify on GitHub**
```

1. In VS Code, bottom left, click "main" (branch name)
2. You'll see "Open on GitHub" option
3. Click it

OR

1. Go to: https://github.com/your-username
2. You'll see "my-dbt-project" repository
3. Click on it

```

**You should see all your files on GitHub!** 🎉
```

my-dbt-project/
├── .github/
│ ├── config/
│ ├── scripts/
│ │ └── doc_generator/
│ │ └── main.py
│ └── workflows/
│ └── sql-doc-generator.yml
├── business_docs/
│ └── customer_definitions.md
├── models/
│ ├── intermediate/
│ ├── marts/
│ └── staging/
│ └── stg_customers.sql
├── .gitignore
├── dbt_project.yml
└── README.md

```

---

## **PART 8: Enable GitHub Actions**
```

On GitHub website:

1. Go to your repository
2. Click "Actions" tab
3. You'll see: "Get started with GitHub Actions"
4. Click "I understand my workflows, go ahead and enable them"

OR

If you see workflows listed, they're already enabled ✅

```

---

## **Complete Checklist**
```

✅ Project folder created: C:\Projects\my-dbt-project
✅ Opened in VS Code
✅ VS Code extensions installed (Git, Python, YAML)
✅ Folder structure created
✅ All files created:
✅ dbt_project.yml
✅ .gitignore
✅ README.md
✅ sql-doc-generator.yml (workflow)
✅ main.py (generator script)
✅ stg_customers.sql (example SQL)
✅ customer_definitions.md (business doc)
✅ Git initialized in VS Code
✅ Signed in to GitHub in VS Code
✅ Repository published to GitHub
✅ All files synced to GitHub
✅ GitHub Actions enabled

```

---

## **VS Code Shortcuts Reference**

| Action | Shortcut |
|--------|----------|
| Open Terminal | `Ctrl + `` |
| Save File | `Ctrl + S` |
| Source Control | `Ctrl + Shift + G` |
| Explorer | `Ctrl + Shift + E` |
| New File | `Ctrl + N` |
| Command Palette | `Ctrl + Shift + P` |
| Find in Files | `Ctrl + Shift + F` |

---

## **Your Current Project Structure (In VS Code)**
```

MY-DBT-PROJECT
├── .github
│ ├── config
│ ├── scripts
│ │ └── doc_generator
│ │ └── main.py ← Python generator
│ └── workflows
│ └── sql-doc-generator.yml ← GitHub Action
├── business_docs
│ └── customer_definitions.md ← Business docs
├── models
│ ├── intermediate
│ ├── marts
│ └── staging
│ └── stg_customers.sql ← Example SQL
├── .gitignore ← Git ignore file
├── dbt_project.yml ← dbt config
└── README.md ← Project readme
