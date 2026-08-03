# Orders Query

## Metadata

- **ID:** 660939
- **Type:** database
- **Difficulty:** 5.0
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Medium, Language Proficiency, SQL, Simple Joins, Interviewer Guidelines, Database
- **Skills:** SQL (Intermediate)
- **Languages:** m, y, s, q, l, ,, o, r, a, c

## Summary

This database question evaluates SQL, simple joins, and subquery concepts, ideal for mid-level roles. The problem requires finding customers with the highest order price within 10 years of their first order date in the database.

## Problem Statement

Company X has a record of its customers and their orders. Find the customer(s) with the highest order price for orders placed within 10 years of the first order (earliest order_date) in the database. Print the customer name and order price. If multiple records are returned, they can be in any order.

 

Schema

There are 2 tables: CUSTOMERS, ORDERS.

	
		
			CUSTOMERS
		
		
			Name
			Type
			Description
		
		
			ID
			STRING
			ID of the customer. This is the primary key.
		
		
			NAME
			STRING
			Name of the customer.
		
		
			ORDER_ID
			STRING
			ID of the customer's order.
		
	

	
		
			ORDERS
		
		
			Name
			Type
			Description
		
		
			ID
			STRING
			ID of the order.
		
		
			PRICE
			INTEGER
			Price of the order.
		
		
			ORDER_DATE
			DATE
			Date of the order.
		
	

Sample Data Tables

## Sample Input

	
		
			CUSTOMERS
		
		
			ID
			NAME
			ORDER_ID
		
		
			0a66e2bba8d5401b8d707ad9fc35394a
			Jennifer Palmer
			3223c7dfda384470aed77b1db46fe29b
		
		
			57bc0e2554ea4dd1910b11ee1131f4cb
			Susan Gonzalez
			eb173d2bc0214cfc8727c00fe62ac96d
		
		
			d880a48bf4844c99a3bafac53612119e
			Judith Smith
			65b36940385a40fcaa13ecb9c8394150
		
	

	
		
			ORDERS
		
		
			ID
			PRICE
			ORDER_DATE
		
		
			3223c7dfda384470aed77b1db46fe29b
			100
			1987-10-02
		
		
			65b36940385a40fcaa13ecb9c8394150
			5
			1987-08-01
		
		
			eb173d2bc0214cfc8727c00fe62ac96d
			500
			1998-08-01
		
	

##  

## Sample Output

Jennifer Palmer 100
```

## Preview

Company X has a record of its customers and their orders. Find the customer(s)
