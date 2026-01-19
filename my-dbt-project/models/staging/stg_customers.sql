-- Staging model for customer data
-- Cleans and standardizes raw customer information
-- Updated: Added phone number validation

with source as (
    
    select * from {{ source('raw', 'customers') }}

),

renamed as (

    select
        customer_id,
        customer_name,
        email,
        phone,
        created_at,
        updated_at,
        customer_status
        
    from source

),

filtered as (

    select *
    from renamed
    where customer_status = 'active'
    and email is not null
    and phone is not null  -- ← Add this new line

)

select * from filtered
```

**Save the file:** `Ctrl + S`

---

## **STEP 3: Commit the Changes**

### **Using VS Code Source Control:**
```
1. Click Source Control icon (left sidebar)
   OR press Ctrl + Shift + G

2. You'll see "stg_customers.sql" with an "M" (modified)

3. Hover over the file and click the "+" icon to stage it
   OR click the "+" next to "Changes" to stage all

4. In the message box at top, type:
   Add phone validation to customer staging

5. Click the ✓ (checkmark) button
   OR press Ctrl + Enter
```

**The change is committed locally** ✅

---

## **STEP 4: Push the Branch to GitHub**
```
1. Look at bottom-left corner
2. You'll see a cloud icon with an up arrow
3. Click "Publish Branch"

OR in terminal: