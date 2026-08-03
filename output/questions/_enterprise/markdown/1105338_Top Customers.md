# Top Customers

## Metadata

- **ID:** 1105338
- **Type:** database
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Medium, SQL, Database, Interviewer Guidelines
- **Skills:** SQL (Intermediate)
- **Languages:** m, y, s, q, l, ,, o, r, a, c

## Summary

This database question evaluates SQL, data aggregation, and query optimization concepts, ideal for mid-level roles. The problem requires writing a query to find the customer with the highest total order value for each year-month, ensuring correct output formatting and ordering.

## Problem Statement

Write a query to get the customer with the highest total order value for each year-month.

 

The result should include the columns year, month, customerid, total_monthly_order_value. See the output under the sample data tables below for the correct data format to use. Be sure to match the format exactly. The output should be ordered by year and month in ascending order.

 

Note: In case, there are 2 customers with equal highest total order value, return the one with a lower customerid.

 

Table definitions and a data sample are given below.

Schema

Table: orders

	
		
			column name
			column type
			key / NULL
		
		
			orderid
			int
			PK
		
		
			customerid
			int
			NOT NULL
		
		
			orderdate
			date
			NOT NULL
		
	

 

Table: order_details

	
		
			column name
			column type
			key / NULL
		
		
			orderid
			int
			PK
		
		
			productid
			int
			NOT NULL
		
		
			unitprice
			int
			NOT NULL
		
		
			quantity
			int
			NOT NULL
		
	

 

orders.orderid references order_details.orderid

 

Sample Data Tables

 

Table: orders

	
		
			orderid
			customerid
			orderdate
		
		
			10248
			3
			1996-07-04
		
		
			10249
			1
			1996-07-05
		
		
			10253
			2
			1996-07-10
		
		
			10274
			3
			1996-08-06
		
		
			10275
			4
			1996-08-07
		
		
			10296
			5
			1996-09-03
		
	

 

Table: order_details

	
		
			orderid
			productid
			unitprice
			quantity
		
		
			10248
			11
			14
			12
		
		
			10248
			42
			9
			10
		
		
			10248
			72
			34
			5
		
		
			10249
			14
			18
			9
		
		
			10249
			51
			42
			40
		
		
			10253
			31
			10
			20
		
		
			10253
			39
			14
			42
		
		
			10253
			49
			16
			40
		
		
			10274
			71
			17
			20
		
		
			10274
			72
			27
			7
		
		
			10275
			24
			3
			12
		
		
			10275
			59
			44
			6
		
		
			10296
			11
			16
			12
		
		
			10296
			16
			13
			30
		
		
			10296
			69
			28
			15
		
	

 

 

The results should be:

`1996 7 1 1842`

`1996 8 3 529`

`1996 9 5 1002`

## Sample Input/Output

## Preview

Write a query to get the customer with the highest total order value for each
