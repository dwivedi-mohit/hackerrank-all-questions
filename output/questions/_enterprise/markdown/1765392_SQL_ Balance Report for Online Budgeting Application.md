# SQL: Balance Report for Online Budgeting Application

## Metadata

- **ID:** 1765392
- **Type:** database
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** SQL, Aggregation, Easy, Sub-Queries, Database
- **Skills:** SQL (Basic)
- **Languages:** m, y, s, q, l, ,, o, r, a, c

## Summary

This database question evaluates SQL, aggregation, and sub-queries concepts, ideal for junior-level roles. The task requires creating a balance report that shows the difference between each customer's total income and total expenses, focusing on those with a negative balance.

## Problem Statement

Create a balance report showing the difference between each customer's total income and total expenses for an online budgeting application. This provides insights into financial health.

 

The result should include these columns:

	
- 
email - the email address of the customer
	
- 
balance - the difference between the total income and total expenses for the customer, showing two decimal places, for example, 500.00

The results should be sorted in ascending order by email.

 

Note:

	
- Only include customers who have a negative balance.

 

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
		
		
			amount
			DECIMAL(6,2)
			 
			The income amount
		
	

Sample Data Tables

	customers
	
		
			id
			email
		
		
			1
			dtollmache0@typepad.com
		
		
			2
			eclutterbuck1@baidu.com
		
		
			3
			mdensun2@ustream.tv
		
	

 

	expenses
	
		
			customer_id
			amount
		
		
			1
			136.18
		
		
			1
			323.28
		
		
			1
			383.37
		
		
			1
			505.41
		
		
			1
			841.21
		
		
			2
			5.23
		
		
			2
			408.33
		
		
			2
			489.45
		
		
			2
			545.40
		
		
			2
			591.43
		
		
			2
			706.13
		
		
			2
			716.82
		
		
			2
			761.75
		
		
			2
			796.30
		
		
			3
			152.26
		
		
			3
			211.30
		
		
			3
			447.57
		
		
			3
			685.03
		
		
			3
			966.89
		
		
			3
			967.30
		
	

 

	income
	
		
			customer_id
			amount
		
		
			1
			39.44
		
		
			1
			49.49
		
		
			1
			292.19
		
		
			1
			419.36
		
		
			1
			529.26
		
		
			1
			695.43
		
		
			1
			763.72
		
		
			1
			797.92
		
		
			1
			833.34
		
		
			2
			139.42
		
		
			2
			422.18
		
		
			2
			506.59
		
		
			2
			566.00
		
		
			2
			697.92
		
		
			2
			938.51
		
		
			3
			304.66
		
		
			3
			345.03
		
		
			3
			371.86
		
		
			3
			371.88
		
		
			3
			552.08
		
	

Sample Output

+-----------------------+--------+
|email                  |balance |
+-----------------------+--------+
|eclutterbuck1@baidu.com|-1750.22|
|mdensun2@ustream.tv    |-1484.84|
+-----------------------+--------+

```

## Sample Input/Output

## Preview

Create a balance report showing the difference between each customer's total i
