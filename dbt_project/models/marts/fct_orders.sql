select
  orders.order_id,
  orders.customer_id,
  orders.order_date,
  orders.amount,
  orders.status
from {{ ref('stg_orders') }} as orders
inner join {{ ref('dim_customers') }} as customers
  on orders.customer_id = customers.customer_id
