# SQL: Monthly Financial Summary for Online Budgeting Application

## Metadata

- **ID:** 1767553
- **Type:** database
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Database, SQL, Medium, Unions
- **Skills:** SQL (Intermediate)
- **Languages:** m, y, s, q, l, ,, o, r, a, c

## Summary

This database question evaluates SQL, unions, and data aggregation concepts, ideal for mid-level roles. The problem requires generating a summary report of financial transactions for March 2024, categorizing them into expenses and income with total counts and amounts.

## Problem Statement

In personal finance, understanding monthly financial activities is essential. The development team of an online budgeting application is creating a detailed summary of a user's financial transactions for March 2024. The report has two rows, one for expenses and another for income.

 

The result should have the following columns: category | total_transactions | total_amount.

	
- 
category - the derived column that shows either `Expenses` or `Income` indicating the type of transaction
	
- 
total_transactions - the total number of transactions for the category
	
- 
total_amount - the cumulative amount of transactions for the category, with two decimal places, including trailing zeros if necessary, e.g., 500.00

 

The result should have two rows, one for each transaction type, "Expenses" and "Income", in that order.

 

Note:

	
- Only transactions that occurred in March 2024 should be included.

 

Schema

	expenses
	
		
			Name
			Type
			Constraints
			Description
		
		
			dt
			VARCHAR(19)
			 
			The date and time of the expense
		
		
			amount
			DECIMAL(6,2)
			 
			The expense amount
		
	

	income
	
		
			Name
			Type
			Constraints
			Description
		
		
			dt
			VARCHAR(19)
			 
			The date and time of the income
		
		
			amount
			DECIMAL(6,2)
			 
			The income amount
		
	

Sample Data Tables

	expenses
	
		
			dt
			amount
		
		
			2024-03-05 04:38:39
			266.45
		
		
			2024-03-08 03:12:22
			720.24
		
		
			2024-03-11 04:02:04
			18.79
		
		
			2024-03-13 00:43:13
			613.75
		
		
			2024-03-13 22:02:51
			854.44
		
		
			2024-03-27 03:20:35
			801.97
		
		
			2024-04-01 16:26:07
			648.78
		
		
			2024-04-04 10:07:35
			154.68
		
		
			2024-04-06 06:27:52
			98.49
		
		
			2024-04-08 05:56:28
			633.58
		
	

 

	income
	
		
			dt
			amount
		
		
			2024-02-22 06:46:24
			424.91
		
		
			2024-02-24 20:23:05
			388.45
		
		
			2024-03-01 11:25:11
			720.80
		
		
			2024-03-10 18:28:51
			166.38
		
		
			2024-03-10 22:59:17
			720.99
		
		
			2024-03-10 23:59:41
			215.81
		
		
			2024-03-17 14:23:05
			113.14
		
		
			2024-03-19 15:29:48
			377.75
		
		
			2024-03-27 22:09:48
			869.59
		
		
			2024-04-05 10:13:38
			109.18
		
	

Sample Output

+--------+------------------+------------+
|category|total_transactions|total_amount|
+--------+------------------+------------+
|Expenses|6                 |3275.64     |
|Income  |7                 |3184.46     |
+--------+------------------+------------+

```

## Sample Input/Output

## Preview

In personal finance, understanding monthly financial activities is essential.
