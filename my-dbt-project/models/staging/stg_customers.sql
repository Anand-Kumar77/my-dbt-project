-- Staging model for customer data
-- Cleans and standardizes raw customer information

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

)

select * from filtered
