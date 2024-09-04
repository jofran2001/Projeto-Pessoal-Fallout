-- Active: 1716336190886@@127.0.0.1@3306

create database sorteio;
use sorteio;
create table sorteio (
id INT auto_increment primary key,
email VARCHAR(100) NOT NULL,
texto VARCHAR(100) NOT NULL
);

