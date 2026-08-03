# SQL: Dashboard for Tax Calculation Application

## Metadata

- **ID:** 1767743
- **Type:** database
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** SQL, Database, Medium, Aggregation, Date Functions, Pivot
- **Skills:** SQL (Intermediate)
- **Languages:** m, y, s, q, l, ,, o, r, a, c

## Summary

This database question evaluates SQL, aggregation, and date functions concepts, ideal for mid-level roles. The problem requires creating a dashboard feature to display total income per account segmented by quarters for 2023, aiding in financial planning and tax calculations.

## Problem Statement

In the evolving landscape of financial technology, quickly assessing financial performance over time is crucial. A development team is enhancing a tax calculation application to include a dashboard feature. This feature will provide users with a clear view of their financial inflows over the quarters of 2023, facilitating better financial planning and tax calculation.

 

The dashboard will display the total income for each account, segmented by the four quarters of 2023, and will also include the total yearly income. This breakdown will help users understand their earnings pattern and prepare for tax calculations.

 

The result should have the following columns: email | q1_income .. q4_income | total_yearly_income.

	
- 
email - the email associated with the account
	
- 
q1_income .. q4_income - the total income for the specific quarter, with two decimal places, including trailing zeros if necessary, e.g., 500.00
	
- 
total_yearly_income - the sum of all quarters’ incomes for the year, with two decimal places, including trailing zeros if necessary, e.g., 500.00

 

The results should be sorted in ascending order by email.

 

Note:

	
- Only income recorded in 2023 should be included.

 

Schema

	accounts
	
		
			Name
			Type
			Constraints
			Description
		
		
			id
			INT
			PRIMARY KEY
			The identifier of the account
		
		
			email
			VARCHAR(255)
			 
			The email address of the account
		
	

	reports
	
		
			Name
			Type
			Constraints
			Description
		
		
			account_id
			INT
			FOREIGN KEY(account_id => accounts.id)
			The reference to the account
		
		
			dt
			VARCHAR(19)
			 
			The date and time of report
		
		
			amount
			DECIMAL(6,2)
			 
			The report amount
		
	

Sample Data Tables

	accounts
	
		
			id
			email
		
		
			1
			tmacphail0@narod.ru
		
		
			2
			smoulin1@berkeley.edu
		
		
			3
			tdezamudio2@moonfruit.com
		
	

 

	reports
	
		
			account_id
			dt
			amount
		
		
			1
			2023-01-05 18:32:10
			4944.74
		
		
			1
			2023-02-05 20:54:01
			1399.73
		
		
			1
			2023-07-14 21:36:10
			4161.43
		
		
			1
			2023-09-07 11:22:35
			256.70
		
		
			1
			2023-10-08 07:17:32
			4757.01
		
		
			1
			2023-10-24 13:57:06
			2989.13
		
		
			2
			2022-12-15 22:01:24
			3135.94
		
		
			2
			2023-03-04 11:34:32
			3202.60
		
		
			2
			2023-03-24 13:01:40
			937.40
		
		
			2
			2023-04-06 12:40:12
			4248.14
		
		
			2
			2023-04-20 20:47:16
			1285.63
		
		
			2
			2023-06-12 09:07:18
			257.53
		
		
			2
			2023-09-09 08:08:09
			3658.44
		
		
			2
			2023-09-15 05:41:38
			2625.76
		
		
			2
			2023-10-03 21:16:02
			2147.86
		
		
			2
			2023-11-14 02:50:05
			4622.11
		
		
			2
			2024-01-04 20:21:16
			682.17
		
		
			2
			2024-01-23 21:48:25
			2260.45
		
		
			3
			2023-04-04 01:27:33
			1949.98
		
		
			3
			2023-06-28 14:02:00
			3123.70
		
	

Sample Output

+-------------------------+---------+---------+---------+---------+-------------------+
|email                    |q1_income|q2_income|q3_income|q4_income|total_yearly_income|
+-------------------------+---------+---------+---------+---------+-------------------+
|smoulin1@berkeley.edu    |4140.00  |5791.30  |6284.20  |6769.97  |22985.47           |
|tdezamudio2@moonfruit.com|0.00     |5073.68  |0.00     |0.00     |5073.68            |
|tmacphail0@narod.ru      |6344.47  |0.00     |4418.13  |7746.14  |18508.74           |
+-------------------------+---------+---------+---------+---------+-------------------+

```

## Sample Input/Output

## Preview

In the evolving landscape of financial technology, quickly assessing financial
