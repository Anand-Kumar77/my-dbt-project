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
