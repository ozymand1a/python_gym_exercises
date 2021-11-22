# 0. Create table

syntax:
```angular2html
create table db_name (
    column_name_1 type_1,
    column_name_2 type_2,
    ...
);
```

example (with inserting new values):
```angular2html
create table orders (
    id int,
    state varchar(10),
    amount int
);
insert into orders (id, state, amount)
values (1, 'new', 10000);
insert into orders (id, state, amount)
values (2, 'new', 3400);
insert into orders (id, state, amount)
values (3, 'delivery', 7300)
```

# 1. Numeric types

- int:
    - tinyint: up to 255
    - smallint: up to 65535
    - mediumint: up to 16777215
    - int: up to 4294967295
    - bigint: up to 2^64 - 1

# 2. Text types

# 3. Date types

# 4. NULL

# 5. BOOL, ENUM, SET

# 6. DEFAULT VALUES