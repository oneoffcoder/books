CREATE DATABASE IF NOT EXISTS ecsdb;

CREATE USER IF NOT EXISTS 'oneoffcoder'@'localhost' IDENTIFIED BY 'isthebest';
CREATE USER IF NOT EXISTS 'oneoffcoder'@'%' IDENTIFIED BY 'isthebest';

GRANT ALL PRIVILEGES ON ecsdb.* TO 'oneoffcoder'@'localhost';
GRANT ALL PRIVILEGES ON ecsdb.* TO 'oneoffcoder'@'%';

USE ecsdb;

CREATE TABLE IF NOT EXISTS person (
    id smallint unsigned not null auto_increment, 
    first_name varchar(50) not null, 
    last_name varchar(50) not null, 
    gender char(1) not null, 
    age smallint not null,
    constraint pk_example primary key (id) 
);

-- INSERT INTO person (id, first_name, last_name, gender, age) VALUES 
-- (1, 'John', 'Doe', 'M', 32),
-- (2, 'Jane', 'Smith', 'F', 31),
-- (3, 'Joe', 'Smith', 'M', 28),
-- (4, 'Joyce', 'Doe', 'F', 29)
-- ON DUPLICATE KEY UPDATE 
--     first_name=VALUES(first_name),
--     last_name=VALUES(last_name),
--     gender=VALUES(gender),
--     age=VALUES(age)
-- ;
