# Content

[1. Primary key](#1-primary-key)

[2. Unique index](#2-unique-index)

[3. Base index](#3-base-index)

[4. Add and delete index](#4-add-and-delete-index)


## 1. Primary key

Primary key is a special attribute to a column
that uniquely identifies an entry in the table.

additional attribute:
- auto_increment: allow auto counting of column values

syntax:
```sql
create table table(
    id int unsigned not null primary key auto_increment,
    ...
)
```

Example (with auto_increment):
```sql
create table files (
    id int unsigned not null primary key auto_increment,
    film_id int unsigned not null,
    size bigint unsigned,
    filename varchar(100)
);
insert into files (film_id, size, filename)
values (356, 28668906700, 'silicon_valley_s02_1080p.zip');
insert into files (film_id, size, filename)
values (4514, 2684354560, 'dunkirk.mp4');
insert into files (film_id, size, filename)
values (87145, 734003200, 'milk.mp4');
```

Example (with adding new primary key based on many columns):
```sql
create table passports (
    series varchar(4) not null,
    number varchar(6) not null,
    user_id int unsigned not null,
    date_issue date,
    CONSTRAINT passport_id PRIMARY KEY (series, number)
);
```

## 2. Unique index

Unique index is an index that is present in the column only once.
Can check uniqueness for many columns.

syntax:
```sql
create table table(
    ean13 varchar(13) not null,
    ...,
    unique key ean13 (ean13),
)
```

Example:
```sql
create table products (
    id int unsigned not null primary key auto_increment,
    category_id int unsigned null,
    name varchar(100) not null,
    slug varchar(50) not null,
    ean13 varchar(13) not null,
    unique key ean13 (ean13),
    unique key category_slug (category_id, slug)
)
```

## 3. Base index

Base index allows you to speed up queries.

syntax:
```sql
create table table (
    user_id int unsigned not null,
    ...,
    index user_id (user_id)
)
```

Example: \
(most popular query)
```sql
SELECT * FROM orders WHERE city_id = 5 AND state = "new";
```
(index)
```sql
create table orders (
    id int unsigned not null primary key auto_increment,
    user_id int unsigned not null,
    city_id int unsigned not null,
    state enum('new', 'cancelled', 'delivered', 'completed') not null default 'new',
    amount mediumint unsigned not null default 0,
    key main_search (city_id, state), -- simple composite index
    index user_id (user_id) -- simple index
)
```

## 4. Add and delete index

Example:
```sql
-- create table
create table passports (
    id int unsigned not null auto_increment primary key,
    user_id int unsigned not null,
    series varchar(4) not null,
    number varchar(6) not null,
    state enum('active','expired') not null default 'active',
    unique key series (series),
    unique key number (number)
);

-- drop indexes and create index
drop index series on passports;
drop index number on passports;
create unique index series_number on passports(series, number)
```
