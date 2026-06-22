with source as (
  select * from {{ ref('orders') }}
)

select
  cast(order_id as integer) as order_id,
  cast(customer_id as integer) as customer_id,
  date(order_date) as order_date,
  cast(amount as numeric) as amount,
  lower(trim(status)) as status
from source
