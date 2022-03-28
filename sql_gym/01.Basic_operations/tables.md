# Content

[0. Create table](#0-create-table)

[1. Numeric types](#1-numeric-types)

[2. Text types](#2-text-types)

[3. Datetime types](#3-datetime-types)

[4. NULL](#4-null)

[5. BOOL, ENUM, SET](#5-bool-enum-set)

[6. DEFAULT VALUES](#6-default-values)


## 0. Create table

syntax:
```sql
create table db_name (
    column_name_1 type_1,
    column_name_2 type_2,
    ...
);
```

Example (with inserting new values):
```sql
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

## 1. Numeric types

- int:
    - tinyint: up to 255
    - smallint: up to 65535
    - mediumint: up to 16777215
    - int: up to 4294967295
    - bigint: up to 2^64 - 1
  
- float
- decimal(n, k): `n` - total number of digits,
  `k` - number of digits after point
  
**ZEROFILL** - add leading zeros to numeric data types
  
Example:
```sql
create table orders (
    id int unsigned,
    product_id int unsigned,
    sale tinyint unsigned,
    amount decimal(8, 2)
);
insert into orders (id, product_id, sale, amount)
values (1, 245, 0, 230.5);
insert into orders (id, product_id, sale, amount)
values (2, 17, 15, 999999.99);
insert into orders (id, product_id, sale, amount)
values (3, 145677, 21, 1240.00);
```

## 2. Text types

- varchar(n): text with no more than `n` letters
- text:
  - text: `n` < 65535
  - mediumtext: `n` < 16777215
  - longtext: `n` < 4294967295
  
Example:

```sql
create table books (
    id int unsigned,
    name varchar(100),
    description varchar(1000),
    isbn varchar(13)
);
insert into books (id, name, description, isbn)
values (1, 'MySQL 5', 'Хорошая книга.', '5941579284');
insert into books (id, name, description, isbn)
values (2, 'Изучаем SQL', 'Полезная книга.', '5932860510');
insert into books (id, name, description, isbn)
values (3, 'Изучаем Python. 4-е издание', 'Подробная книга о Python.', '9785932861592');
```

## 3. Datetime types



## 4. NULL

NULL is a special data type. We can set restriction about `null` 
for our row's values. Also `null` is special case for `select`.

Example (creation):
```sql
create table users (
    id int unsigned not null,
    email varchar(100) not null
);
```

## 5. BOOL, ENUM, SET

- bool: data type for `True`, `False`
- enum: data type for separate predefined values
- set: data type for predefined values in the set

Example (create `enum` and `set`):
```sql
create table orders (
    id int unsigned not null,
    user_id int unsigned not null,
    amount decimal(10, 2),
    created datetime not null,
    state enum('new', 'cancelled', 'in_progress', 'delivered', 'completed'),
    options set('pack', 'fitting', 'call', 'intercom')
);
insert into orders (id, user_id, amount, created, state, options)
values (456, 763, 14299.00, '2018-02-01 17:45:59', 'completed', 'pack,call');
insert into orders (id, user_id, amount, created, state, options)
values (457, 1987, 249.50, '2018-02-01 18:23:04', 'delivered', 'pack,intercom');
insert into orders (id, user_id, amount, created, state, options)
values (459, 78, 2300.12, '2018-02-01 22:12:09', 'in_progress', '');
```

Example (find `enum` values):
```sql
select name, price, country from products
where (find_in_set('RU', country) or find_in_set('BY', country))
and category_id is not null
order by price desc
```

## 6. DEFAULT VALUES

Example:
```sql
create table logs (
    date datetime not null default current_timestamp,
    browser varchar(500) not null default '',
    is_bot bool not null default false
);
insert into logs (date, browser, is_bot)
values ('2018-03-19 19:50:01', 'Chrome 64.0.1.417', false);
insert into logs (date, browser, is_bot)
values ('2018-03-19 19:55:11', 'Firefox 55 (yandex bot)', true);
insert into logs (date, browser, is_bot)
values ('2018-03-19 19:56:12', 'Chrome 63.0.0.471', false);
```
