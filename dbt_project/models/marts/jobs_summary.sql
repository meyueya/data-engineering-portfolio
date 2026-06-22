{# Aggregate jobs per company #}

select
  company,
  count(*) as openings,
  avg(salary) as avg_salary,
  min(salary) as min_salary,
  max(salary) as max_salary
from {{ ref('stg_jobs') }}
group by company
