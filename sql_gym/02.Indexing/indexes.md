# 1. Primary key

Primary key is a special attribute to a column
that uniquely identifies an entry in the table.

additional attribute:
- auto_increment: allow auto counting of column values

Example (with auto_increment):
```angular2html
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
```angular2html
create table passports (
    series varchar(4) not null,
    number varchar(6) not null,
    user_id int unsigned not null,
    date_issue date,
    CONSTRAINT passport_id PRIMARY KEY (series, number)
);
```

# 2. Unique index

Unique index is an index that is present in the column only once.
Can check uniqueness for many columns.

Example:
```angular2html
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

# 3. Base index

Base index allows you to speed up queries.

Example: \
(most popular query)
```angular2html
SELECT * FROM orders WHERE city_id = 5 AND state = "new";
```
(index)
```angular2html
create table orders (
    id int unsigned not null primary key auto_increment,
    user_id int unsigned not null,
    city_id int unsigned not null,
    state enum('new', 'cancelled', 'delivered', 'completed') not null default 'new',
    amount mediumint unsigned not null default 0,
    key main_search (city_id, state),
    index user_id (user_id)
)
```

# 4. Add and delete index

Example:
```angular2html
drop index series on passports;
drop index number on passports;
create unique index series_number on passports(series, number)
```