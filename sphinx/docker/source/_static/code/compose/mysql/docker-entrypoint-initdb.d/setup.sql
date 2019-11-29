CREATE DATABASE school;

USE school;

CREATE TABLE student (
    id smallint unsigned not null auto_increment, 
    first_name varchar(50) not null, 
    last_name varchar(50) not null, 
    gender char(1) not null, 
    constraint pk_example primary key (id) 
);

INSERT INTO student (first_name, last_name, gender) VALUES 
('John', 'Doe', 'M'),
('Jane', 'Smith', 'F'),
('Joe', 'Smith', 'M'),
('Joyce', 'Doe', 'F')
;

CREATE USER 'oneoffcoder'@'localhost' IDENTIFIED BY 'isthebest';
CREATE USER 'oneoffcoder'@'%' IDENTIFIED BY 'isthebest';
GRANT ALL PRIVILEGES ON school.* TO 'oneoffcoder'@'localhost' WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON school.* TO 'oneoffcoder'@'%' WITH GRANT OPTION;