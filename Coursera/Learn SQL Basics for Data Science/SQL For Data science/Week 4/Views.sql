/*
- A stored query
- Can add or remove without changing the schema
- use it to encapsulate queries
-my_view_tmy_view_tcustomer_list The view will be removed after database connection is over
*/
use sakila;

create view my_view
as
select actor.first_name
, actor.last_name
, fa.film_id
, ft.title
from actor
inner join film_actor fa on fa.actor_id = actor.actor_id
inner join film_text ft on ft.film_id = fa.film_id;

select * 
from my_view;
drop view my_view_t;