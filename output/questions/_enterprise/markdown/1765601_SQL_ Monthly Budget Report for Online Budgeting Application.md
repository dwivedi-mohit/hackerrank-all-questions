# SQL: Monthly Budget Report for Online Budgeting Application

## Metadata

- **ID:** 1765601
- **Type:** database
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** SQL, Easy, Sub-Queries, Database, Filtering
- **Skills:** SQL (Basic)
- **Languages:** m, y, s, q, l, ,, o, r, a, c

## Summary

This database question evaluates SQL, sub-queries, and data filtering concepts, ideal for junior-level roles. The problem requires generating a report of total expenses and income for customers in March, sorted by email.

## Problem Statement

Generate a report for each customer that provides insights into their total expenses and total income for an online budgeting application. This helps customers better manage their finances.

 

The result should include these columns:

	
- 
email - the email address of the customer
	
- 
total_expenses - the sum of all expenses recorded for the customer, showing two decimal places, for example, 500.00
	
- 
total_income - the sum of income recorded for the customer, showing two decimal places, for example, 500.00

The results should be sorted in ascending order by email.

 

Note:

	
- Only include expenses and incomes recorded in March.

 

Schema

	customers
	
		
			Name
			Type
			Constraint
			Description
		
		
			id
			INT
			PRIMARY KEY
			The identifier of the customer
		
		
			email
			VARCHAR(255)
			 
			The email address of the customer
		
	

	expenses
	
		
			Name
			Type
			Constraint
			Description
		
		
			customer_id
			INT
			FOREIGN KEY(customer_id => customers.id)
			The reference to the customer
		
		
			dt
			VARCHAR(19)
			 
			The date and time of expense
		
		
			amount
			DECIMAL(6,2)
			 
			The expense amount
		
	

	income
	
		
			Name
			Type
			Constraint
			Description
		
		
			customer_id
			INT
			FOREIGN KEY(customer_id => customers.id)
			The reference to the customer
		
		
			dt
			VARCHAR(19)
			 
			The date and time of income
		
		
			amount
			DECIMAL(6,2)
			 
			The income amount
		
	

Sample Data Tables

	customers
	
		
			id
			email
		
		
			1
			otoohey0@elpais.com
		
		
			2
			egrebbin1@state.gov
		
		
			3
			arides2@sohu.com
		
	

 

	expenses
	
		
			customer_id
			dt
			amount
		
		
			1
			2024-02-21 22:12:12
			90.41
		
		
			1
			2024-02-27 06:48:37
			792.88
		
		
			1
			2024-03-10 05:19:43
			442.01
		
		
			1
			2024-03-11 19:48:25
			327.35
		
		
			1
			2024-03-24 22:03:06
			639.62
		
		
			1
			2024-03-29 00:37:46
			150.12
		
		
			1
			2024-04-02 03:36:50
			257.67
		
		
			2
			2024-02-21 06:11:26
			400.22
		
		
			2
			2024-03-11 15:34:19
			298.41
		
		
			2
			2024-03-25 04:36:27
			376.87
		
		
			2
			2024-03-29 19:05:51
			530.07
		
		
			2
			2024-03-30 07:07:28
			287.84
		
		
			2
			2024-04-02 15:44:22
			868.03
		
		
			3
			2024-03-01 16:02:47
			33.30
		
		
			3
			2024-03-06 11:53:42
			838.51
		
		
			3
			2024-03-20 23:34:48
			968.08
		
		
			3
			2024-03-21 21:18:08
			35.36
		
		
			3
			2024-03-30 06:51:13
			956.12
		
		
			3
			2024-03-31 10:11:56
			896.32
		
		
			3
			2024-03-31 22:36:57
			740.94
		
	

 

	income
	
		
			customer_id
			dt
			amount
		
		
			1
			2024-02-20 21:00:55
			366.66
		
		
			1
			2024-03-11 03:25:04
			769.38
		
		
			1
			2024-03-15 00:49:53
			84.10
		
		
			1
			2024-03-21 18:32:51
			839.48
		
		
			1
			2024-03-29 15:34:13
			333.97
		
		
			1
			2024-04-01 00:34:24
			253.13
		
		
			1
			2024-04-02 11:13:49
			263.56
		
		
			2
			2024-02-20 15:03:26
			822.75
		
		
			2
			2024-02-26 14:57:39
			277.23
		
		
			2
			2024-03-19 09:24:47
			24.08
		
		
			2
			2024-03-20 15:54:24
			988.34
		
		
			2
			2024-04-02 08:28:38
			990.54
		
		
			3
			2024-02-21 10:23:33
			430.82
		
		
			3
			2024-02-29 08:25:32
			482.85
		
		
			3
			2024-03-01 05:10:42
			962.60
		
		
			3
			2024-03-04 08:27:34
			30.21
		
		
			3
			2024-03-19 12:12:01
			80.00
		
		
			3
			2024-03-21 00:32:10
			674.76
		
		
			3
			2024-03-23 14:14:32
			863.79
		
		
			3
			2024-04-09 13:37:07
			51.42
		
	

Sample Output

+-------------------+--------------+------------+
|email              |total_expenses|total_income|
+-------------------+--------------+------------+
|arides2@sohu.com   |4468.63       |2611.36     |
|egrebbin1@state.gov|1493.19       |1012.42     |
|otoohey0@elpais.com|1559.10       |2026.93     |
+-------------------+--------------+------------+

```

## Sample Input/Output

## Preview

Generate a report for each customer that provides insights into their total ex
