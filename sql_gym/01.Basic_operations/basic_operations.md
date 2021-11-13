# 0. How DB is work?

# 1. SELECT * FROM DB

select target rows at bd /

additional flags:
- where "something"": select rows with this/these condition/conditions
- order by "column_name": sort rows by this/these column/columns;
  flag "desc" 
- limit: how many rows should be shown

example:
```angular2html
select name, price from products
where count != 0
order by name
limit 12,2
```

# 2. INSERT INTO DB (columns) VALUES (values)

# 3. UPDATE DB

# 4. DELETE FROM DB