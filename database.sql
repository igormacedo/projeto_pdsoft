/*
 * my first mysql script - testscript.sql.
 * you need to run this script with an authorized user.
 */
drop database if exists include;

create database include;                  -- creates working database
show databases;                           -- show server databases
use include;                              -- set system database 'include' as the current database
select database();                        -- shows current database

create table members                      -- creates the members tables
                  (uniid int,
                  name varchar(100),
                  course varchar(50),
                  street varchar(200),
                  housenumber varchar(10),
                  neighborhood varchar(20),
                  city varchar(20),
                  state varchar(2),
                  cep varchar(9),
                  birth date);            -- list all users by querying table 'user'
describe members;                -- shows table "members" structure
