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

