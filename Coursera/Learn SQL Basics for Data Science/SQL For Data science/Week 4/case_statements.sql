use sakila;

/* CASE
WHEN >>>>>>> THEN >>>>>
ELSE
END column_name*/
select address_id
, address
, address2
, city_id
, case district
		when 'Alberta' then 'Alberta'
        else 'other'
end Alberta
from address
order by address_id;

