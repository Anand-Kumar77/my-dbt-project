# Stg_Customers Model Documentation
=====================================

## Overview
------------

The `stg_customers` model is a staging model that cleans and standardizes raw customer information from the `raw.customers` table. This model ensures data quality by filtering out inactive customers, null email addresses, and null phone numbers.

## Business Purpose
------------------

This model serves to provide high-quality customer data for downstream analysis and reporting purposes. By filtering out irrelevant or incomplete data, this model enables more accurate insights into customer behavior and preferences.

## Data Sources
-------------

The `stg_customers` model reads from the `raw.customers` table in the database.

## Transformation Logic
----------------------

Here is a step-by-step explanation of the SQL transformations applied by this model:

1. **Source**: The raw customer data is retrieved from the `raw.customers` table.
2. **Renamed**: The raw data is renamed to improve readability and clarity. This includes selecting only relevant columns such as `customer_id`, `customer_name`, `email`, `phone`, `created_at`, `updated_at`, and `customer_status`.
3. **Filtered**: The renamed data is filtered to exclude inactive customers, null email addresses, and null phone numbers.

## Output Schema
----------------

The output schema of the `stg_customers` model includes the following columns:

* `customer_id`: Unique identifier for each customer.
* `customer_name`: Name of the customer.
* `email`: Email address of the customer.
* `phone`: Phone number of the customer.
* `created_at`: Date and time when the customer was created.
* `updated_at`: Date and time when the customer was last updated.
* `customer_status`: Status of the customer (e.g., active, inactive).

## Usage Examples
-----------------

To use this model in downstream queries, you can simply reference it as a table. For example:

```sql
SELECT *
FROM {{ ref('stg_customers') }}
WHERE customer_status = 'active'
AND email LIKE '%@example.com';
```

This query retrieves all active customers with an email address containing the `@example.com` domain.

## Data Quality Notes
--------------------

* The model assumes that the `raw.customers` table has already been cleaned and validated. If this is not the case, additional data quality checks may be necessary.
* The model filters out inactive customers, but does not perform any further validation on customer status. Depending on your business requirements, you may need to add additional logic to handle these cases.
* The model assumes that email addresses are in a standard format (e.g., `@example.com`). If this is not the case, you may need to modify the filter condition accordingly.