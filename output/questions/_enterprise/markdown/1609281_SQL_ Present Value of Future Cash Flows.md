# SQL: Present Value of Future Cash Flows

## Metadata

- **ID:** 1609281
- **Type:** database
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Database, Easy, SQL, Theme: Finance, Functions, Arithmetic Calculation
- **Skills:** SQL (Basic)
- **Languages:** m, y, s, q, l, ,, o, r, a, c

## Summary

This database question evaluates SQL, financial calculations, and data aggregation concepts, ideal for junior-level roles. The problem requires creating a query to calculate the present value of zero-coupon bonds for investors, filtering results based on total present value.

## Problem Statement

Create a query for a financial services company that calculates the present value of zero-coupon bonds using a 5% discount rate. The query should return:

	
- 
email - Investor email
	
- 
investment_count - Total number of investments
	
- 
total_present_value - Sum of present values of expected cash flows, rounded to two decimal places, e.g., 1000.00
	
- 
avg_present_value - Average present value of expected cash flows, rounded to two decimal places, e.g., 1000.00

 

The results should be sorted in ascending order by email.

 

Note:

	
- To calculate the present value, use the formula:    present_value  =  (  expected_flow    ( 1 + discount_rate )  periods    ) . For example, the expected cash flow is 105 after 1 period. The present value is    present_value  =  (  105    ( 1 + 0.05 )  1    )  = 100. 

	
- Use a discount_rate of 0.05 and assume each cash flow has a different period ranging from 1 to the number of cash flows per investor.
	
- Trailing zeros after the decimal should be included.
	
- Only investors who have a total_present_value greater than 1,000,000 should be included in the result.

 

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
		
	

 

	
		
			cash_flows
		
		
			name
			type
			constraint
			description
		
		
			investor_id
			INT
			FOREIGN KEY(investor_id => investors.id)
			Reference to the investor
		
		
			expected_flow
			DECIMAL(8,2)
			 
			Expected cash flow amount
		
		
			cash_flow_period
			INT
			 
			The period of the cash flow
		
	

 

     Sample Data Tables

 

	
		
			investors
		
		
			id
			email
		
		
			1
			bdunkerley0@ustream.tv
		
		
			2
			amaclaine1@oracle.com
		
		
			3
			mhenstone2@csmonitor.com
		
	

 

	
		
			cash_flows
		
		
			investor_id
			expected_flow
			cash_flow_period
		
		
			1
			467424.93
			4
		
		
			1
			473197.72
			2
		
		
			1
			325032.12
			3
		
		
			1
			384188.89
			1
		
		
			1
			89190.85
			3
		
		
			1
			306760.94
			2
		
		
			1
			96429.87
			4
		
		
			1
			67530.35
			5
		
		
			1
			173542.87
			4
		
		
			1
			230858.63
			2
		
		
			2
			225836.56
			5
		
		
			2
			492465.14
			3
		
		
			2
			242523.52
			2
		
		
			2
			75880.55
			2
		
		
			2
			436683.99
			4
		
		
			3
			120612.96
			4
		
		
			3
			249090.59
			3
		
		
			3
			163647.03
			1
		
		
			3
			69478.04
			5
		
		
			3
			419617.32
			2
		
	

 

Expected Output

 

	
		
			email
			investment_count
			total_present_value
			avg_present_value
		
		
			amaclaine1@oracle.com
			5
			1250421.63
			250084.33
		
		
			bdunkerley0@ustream.tv
			10
			2300127.32
			230012.73

## Sample Input/Output

## Preview

Create a query for a financial services company that calculates the present va
