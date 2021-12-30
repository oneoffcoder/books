CREATE DATABASE ecsdb;
CREATE USER 'oneoffcoder'@'localhost' IDENTIFIED BY 'isthebest';
CREATE USER 'oneoffcoder'@'%' IDENTIFIED BY 'isthebest';
GRANT ALL PRIVILEGES ON ecsdb.* TO 'oneoffcoder'@'localhost';
GRANT ALL PRIVILEGES ON ecsdb.* TO 'oneoffcoder'@'%';

USE ecsdb;

CREATE TABLE person (
    id smallint unsigned not null auto_increment, 
    first_name varchar(50) not null, 
    last_name varchar(50) not null, 
    gender char(1) not null, 
    age smallint not null,
    constraint pk_example primary key (id) 
);

INSERT INTO person (first_name, last_name, gender, age) VALUES 
('John', 'Doe', 'M', 32),
('Jane', 'Smith', 'F', 31),
('Joe', 'Smith', 'M', 28),
('Joyce', 'Doe', 'F', 29)
;
