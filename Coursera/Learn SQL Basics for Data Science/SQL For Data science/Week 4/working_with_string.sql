USE sakila;

SELECT first_name
, last_name
, CONCAT(first_name, ' ', last_name) as full_name
FROM actor;

SELECT TRIM(" You are the best. ") AS TrimmedString;

SELECT address
, SUBSTR(address, 1, 3) as sub_string 
FROM address;

SELECT district
, UPPER(district) as Udistrict
, LOWER(district) as Ldistrict
, UCASE(district) as UDistrict
, lCASE(district) as LDistrict
from address