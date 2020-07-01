use sakila;

/* How to extract date, month and year.
In sqlite, its strfitme() instead of date_format() and arguments in reverses order.*/
select last_update
, date_format(last_update, '%Y')
, date_format(last_update, '%m')
, date_format(last_update, '%d')
from actor;

/* How to know the current date*/
select (last_update - now()) as diff
from actor;


