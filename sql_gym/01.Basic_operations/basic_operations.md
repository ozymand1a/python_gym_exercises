# Content

[1. SELECT * FROM DB](#1-select--from-db)

[2. INSERT INTO DB (columns) VALUES (values)](#2-insert-into-db-columns-values-values)

[3. UPDATE DB](#3-update-db)

[4. DELETE FROM DB](#4-delete-from-db)


## 1. SELECT * FROM DB

Select target rows at DB

syntax:
```sql
select row_name from table
```

additional flags:
- where "something": select rows with this/these condition/conditions
- order by "column_name": sort rows by this/these column/columns;
  - flag "desc" 
- limit: how many rows should be shown

Example:
```sql
select name, price from products
where count != 0
order by name
limit 12,2
```

## 2. INSERT INTO DB (columns) VALUES (values)

Insert row/rows at DB.

syntax: 
```sql
insert into table (col_name_1, col_name_2)
values 
(val_1, val_2)
```


Example:
```sql
insert into products (id, name, count, price)
values
(8, 'iPhone 7', 1, 59990),
(9, 'iPhone 8', 3, 64990),
(10, 'iPhone X', 2, 79900)
```

## 3. UPDATE DB

Update row by some condition or another restriction.

syntax:
```sql
update table
set col_name = something
```

Example:
```sql
update products
set price = price + price * 0.05
order by price
limit 5
```

## 4. DELETE FROM DB

Delete row/rows from db by condition.

syntax:
```sql
delete from table
where condition
```

Example:
```sql
delete from cars
where country = 'JP' and (power <= 80 or power >= 130)
```

Example of deleting all table:
```sql
truncate table cars
```