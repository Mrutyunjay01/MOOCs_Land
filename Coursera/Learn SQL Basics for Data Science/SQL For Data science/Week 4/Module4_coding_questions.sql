/*
Pull a list of customer ids with the customer’s full name, and address, 
along with combining their city and country together. Be sure to make a 
space in between these two and make it UPPER CASE.
What is the city and country result for CustomerID 16?
*/
select customerid
, (firstname || ' ' || lastname) as full_name
, upper(city || ' ' || country)
from customers
where customerid = 16;

/*
Create a new employee user id by combining the first 4 letters of the 
employee’s first name with the first 2 letters of the employee’s last 
name. Make the new field lower case and pull each individual step to show your work.
What is the final result for Robert King?
*/
select 
(substr(firstname, 1, 4) || substr(lastname, 1, 2)) as new_user_id
, (firstname, ' ', lastname) as full_name
from employees
where full_name = 'Robert King';

/*
Show a list of employees who have worked for the company for 15 or more
 years using the current date function. Sort by lastname ascending.
 What is the lastname of the last person on the list returned?
*/
select lastname,
hiredate
from employees
order by lastname Asc;

/*
Profiling the Customers table, answer the following question.
Are there any columns with null values? Indicate any below. Select all that apply.
*/
select *
from customers
where fax is null;

/*
Find the cities with the most customers and rank in descending order.
Which of the following cities indicate having 2 customers?
*/
select count(customerid) as cc, city
from customers
group by city
having cc = 2;

/*
Create a new customer invoice id by combining a customer’s 
invoice id with their first and last name while ordering your
 query in the following order: firstname, lastname, and invoiceID.
Select all of the correct "AstridGruber" entries that are 
returned in your results below. Select all that apply.
*/
select invoiceid
, c.lastname
, c.firstname
, (c.firstname || c.lastname || invoiceid) as customer_invoice_id
from invoices
inner join customers c
on c.customerid = invoices.customerid
order by customer_invoice_id;