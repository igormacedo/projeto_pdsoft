/*
 * my first mysql script - testscript.sql.
 * you need to run this script with an authorized user.
 */
drop database if exists include;

create database include
    DEFAULT CHARACTER SET utf8;             -- creates working database

show databases;                             -- show server databases
use include;                                -- set system database 'include' as the current database
select database();                          -- shows current database

create table members                        -- creates the members tables
    (uniid int,
    name varchar(200) not null ,
    course varchar(50),
    street varchar(200),
    housenumber varchar(10),
    neighborhood varchar(20),
    city varchar(20),
    state varchar(2),
    cep varchar(9),
    housephone varchar(14),
    mobilephone varchar(14),
    birth date,
    email varchar(200) not null,
    picture varchar(300) not null,
    login varchar(200) not null,
    password varchar(200) not null,
    PRIMARY KEY (login));

describe members;                           -- shows table "members" structure
