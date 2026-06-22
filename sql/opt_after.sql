-- Optimized: add a dedicated 'role' column or normalized title search via an indexed column
-- For demo, create a computed column 'is_engineer' and index it, then query that column.
select * from jobs where salary > 90000 order by salary desc;
