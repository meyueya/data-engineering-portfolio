{# Staging model: normalize and select from seed 'jobs' #}

with raw as (
  select * from {{ ref('jobs') }}
)

select
  id,
  title,
  company,
  cast(salary as integer) as salary,
  date(posted_date) as posted_date
from raw
