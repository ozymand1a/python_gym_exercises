# 0. Create table

syntax:
```angular2html
create table db_name (
    column_name_1 type_1,
    column_name_2 type_2,
    ...
);
```

Example (with inserting new values):
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
  
- float
- decimal(n, k): `n` - total number of digits,
  `k` - number of digits after point

# 2. Text types

- varchar(n): text with no more than `n` letters
- text:
  - text: `n` < 65535
  - mediumtext: `n` < 16777215
  - longtext: `n` < 4294967295

# 3. Datetime types



# 4. NULL

NULL is a special data type. We can set restriction about `null` 
for our row's values.

Example (creation):
```angular2html
create table users (
    id int unsigned not null,
    email varchar(100) not null
);
```

# 5. BOOL, ENUM, SET

- bool: data type for `True`, `False`
- enum: data type for predefined values separately
- set: data type for predefined values in the set

Example (create `enum` and `set`):
```angular2html
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
```angular2html
select name, price, country from products
where (find_in_set('RU', country) or find_in_set('BY', country))
and category_id is not null
order by price desc
```

# 6. DEFAULT VALUES

Example:
```angular2html
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