# SQL: Bond Valuation Analysis

## Metadata

- **ID:** 1609255
- **Type:** database
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Database, SQL, Easy, Theme: Finance, Aggregation
- **Skills:** SQL (Basic)
- **Languages:** m, y, s, q, l, ,, o, r, a, c

## Summary

This database question evaluates SQL, data aggregation, and financial analysis concepts, ideal for junior-level roles. The problem requires creating a query to analyze customer bond holdings and return specific valuation metrics for investors.

## Problem Statement

Create a query for a financial services company that analyzes customer bond holdings. The query should return:

 

	
- 
email - Investor email
	
- 
investments - Total number of investments
	
- 
min_valuation - Minimum bond valuation
	
- 
max_valuation - Maximum bond valuation
	
- 
avg_valuation - Average bond valuation, rounded to two decimal places, e.g., 5.00

 

Only investors with an average bond valuation greater than 100,000 should be included. All valuation amounts should have two decimal places. Results should be sorted in ascending order by email.

 

     Schema

 

	
		
			investors
		
		
			name
			type
			constraint
			description
		
		
			id
			INT
			PRIMARY KEY
			Investor ID
		
		
			email
			VARCHAR(255)
			UNIQUE
			Email address
		
	

 

	
		
			investments
		
		
			name
			type
			constraint
			description
		
		
			investor_id
			INT
			FOREIGN KEY(investor_id => investors.id)
			Reference to the investor
		
		
			valuation
			DECIMAL(8,2)
			 
			Bond's market value
		
	

 

     Sample Data Tables

 

	
		
			investors
		
		
			id
			email
		
		
			1
			gcordel0@t.co
		
		
			3
			mpolycote2@is.gd
		
		
			2
			tdye1@edublogs.org
		
	

 

	
		
			investments
		
		
			investor_id
			valuation
		
		
			1
			136397.66
		
		
			1
			100088.28
		
		
			1
			71534.17
		
		
			1
			117418.73
		
		
			1
			30466.29
		
		
			1
			164102.40
		
		
			2
			112209.07
		
		
			2
			57327.83
		
		
			2
			89859.84
		
		
			2
			45081.15
		
		
			3
			66453.81
		
		
			3
			64627.86
		
		
			3
			156862.58
		
		
			3
			175030.76
		
		
			3
			61761.07
		
		
			3
			31505.41
		
		
			3
			150005.29
		
		
			3
			126345.36
		
		
			3
			151254.58
		
		
			3
			153121.53
		
	

 

Expected Output

 

	
		
			email
			investments
			min_valuation
			max_valuation
			avg_valuation
		
		
			gcordel0@t.co
			6
			30466.29
			164102.40
			103334.59
		
		
			mpolycote2@is.gd
			10
			31505.41
			175030.76
			113696.83

## Sample Input/Output

## Preview

Create a query for a financial services company that analyzes customer bond ho
