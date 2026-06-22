with source as (
  select * from {{ ref('customers') }}
)

select
  cast(customer_id as integer) as customer_id,
  trim(first_name) as first_name,
  trim(last_name) as last_name,
  lower(trim(email)) as email,
  date(created_at) as created_at
from source
