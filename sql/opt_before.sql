-- Example: inefficient query (scans and string operations)
select * from jobs where lower(title) like '%engineer%';
