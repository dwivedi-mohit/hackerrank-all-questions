# SQL: Exchange Rates

## Metadata

- **ID:** 1239603
- **Type:** database
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Simple Joins, Theme:  Finance, Easy, Database, Interviewer Guidelines
- **Skills:** SQL (Basic)
- **Languages:** m, y, s, q, l, ,, o, r, a, c

## Summary

This database question evaluates SQL, simple joins, and fee calculation concepts, ideal for junior-level roles. The problem requires writing a query to calculate and display the total fees paid by customers for stock exchange transactions based on their buy and sell orders.

## Problem Statement

"Write a query to calculate the fees paid by customers for their stock exchange transactions. The exchange charges 0.1% for buy orders and 0.15% for sell orders.

 

Display the customer name and their total fees paid, rounded to 2 decimal places, e.g., 5.004 is shown as 5.00. Order the results alphabetically ascending by customer name.

 

To round the data:

In MySQL, Oracle, or DB2, use ROUND(val, 2).

In MS SQL use FORMAT(val, 'N2').

 

Schema

You are provided 2 tables: `customers`, `orders`.

	
		
			CUSTOMERS
		
		
			Name
			Type
			Description
		
		
			id
			int
			Unique id of the customer.
		
		
			customer_name
			varchar(30)
			Name of the customer.
		
	

	
		
			ORDERS
		
		
			Name
			Type
			Description
		
		
			order_id
			int
			Unique id of the order.
		
		
			customer_id
			int
			Id of the customer referring to the customers table.
		
		
			order_type
			varchar(5)
			Type of order placed (Buy or Sell).
		
		
			order_amount
			decimal(18,2)
			Amount of the order.
		
	

Sample Data Tables

 

	
		
			CUSTOMERS
		
		
			id
			customer_name
		
		
			401
			Hubert Keesler
		
		
			402
			Devin Vert
		
		
			403
			Lashawna Bowerman
		
		
			404
			Brigid Wellborn
		
		
			405
			Josefine Perl
		
	

 

	
		
			ORDERS
		
		
			order_id
			customer_id
			order_type
			order_amount
		
		
			4361
			401
			Sell
			912.77
		
		
			3478
			405
			Sell
			741.69
		
		
			7292
			405
			Sell
			436.05
		
		
			5833
			405
			Sell
			231.30
		
		
			3472
			402
			Buy
			950.92
		
		
			4472
			401
			Sell
			367.70
		
		
			2624
			404
			Buy
			218.15
		
		
			7198
			405
			Buy
			797.29
		
		
			7660
			403
			Buy
			131.18
		
		
			5192
			401
			Buy
			362.44
		
		
			5260
			402
			Buy
			636.26
		
		
			2726
			403
			Sell
			138.15
		
		
			6594
			401
			Buy
			234.51
		
		
			4657
			404
			Buy
			427.30
		
		
			9744
			402
			Sell
			623.36
		
	

 

	
		
			OUTPUT
		
		
			customer_name
			total_fees
		
		
			Brigid Wellborn
			0.65
		
		
			Devin Vert
			2.52
		
		
			Hubert Keesler
			2.52
		
		
			Josefine Perl
			2.91
		
		
			Lashawna Bowerman
			0.34
		
	

 

Explanation

For Devin Vert, total amount of buy orders was 1587.18 and total amount of buy orders was 623.36. Fee applied on buy and sell orders will be 1.58718 and 0.93504 with rate of 0.1% and 0.15% respectively. Total fee would be 2.52222 after rounding final fee would be 2.52.

## Sample Input/Output

## Preview

"Write a query to calculate the fees paid by customers for their stock exchang
