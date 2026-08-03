# SQL: Finance Bonds and Stocks Cash Flows Stats

## Metadata

- **ID:** 1645038
- **Type:** database
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Database, SQL, Medium, Union, Theme: Finance, Aggregation
- **Skills:** SQL (Intermediate)
- **Languages:** m, y, s, q, l, ,, o, r, a, c

## Summary

This database question evaluates SQL, aggregation, and financial asset analysis concepts, ideal for mid-level roles. The problem requires calculating the sum of cash flows for financial assets and filtering results based on specific criteria.

## Problem Statement

A company manages various financial assets, including bonds and stocks, and wants to calculate statistics on historical cash flows for each asset. The statistic required is the sum of cash flows per asset.

 

The result should have the following columns: name | asset_type | sum_cash_flows.

	
- 
name - name of the bond or stock
	
- 
asset_type - type of the asset ("Bond" or "Stock")
	
- 
sum_cash_flows - the sum of cash flows for a specific asset with two places after the decimal, e.g., 10.00.

 

The results should be sorted in ascending order by name.

 

Note:

	
- Only assets that have a sum of cash flows greater than 2000.00 should be included in the result.

 

     Schema

 

	
		
			bonds
		
		
			name
			type
			constraint
			description
		
		
			id
			INT
			PRIMARY KEY
			Bond ID
		
		
			name
			VARCHAR(255)
			UNIQUE
			Name of the bond
		
	

 

	
		
			bond_payments
		
		
			name
			type
			constraint
			description
		
		
			bond_id
			INT
			FOREIGN KEY(bond_id => bonds.id)
			Reference to the bond
		
		
			cash_flow
			DECIMAL(5,2)
			 
			Cash flow for the bond
		
	

 

	
		
			stocks
		
		
			name
			type
			constraint
			description
		
		
			id
			INT
			PRIMARY KEY
			Stock ID
		
		
			name
			VARCHAR(255)
			UNIQUE
			Name of the stock
		
	

 

	
		
			stock_payments
		
		
			name
			type
			constraint
			description
		
		
			stock_id
			INT
			FOREIGN KEY(stock_id => stocks.id)
			Reference to the stock
		
		
			dividend
			DECIMAL(5,2)
			 
			Dividend paid for the stock
		
	

 

     Sample Data Tables

 

	
		
			bonds
		
		
			id
			name
		
		
			1
			ABC Bond
		
		
			2
			XYZ Bond
		
		
			3
			Global Bond
		
	

 

	
		
			bond_payments
		
		
			bond_id
			cash_flow
		
		
			1
			62.00
		
		
			1
			129.00
		
		
			1
			276.00
		
		
			1
			369.00
		
		
			1
			483.00
		
		
			2
			86.00
		
		
			2
			229.00
		
		
			2
			240.00
		
		
			2
			319.00
		
		
			2
			325.00
		
		
			2
			365.00
		
		
			2
			433.00
		
		
			2
			463.00
		
		
			3
			85.00
		
		
			3
			108.00
		
		
			3
			169.00
		
		
			3
			185.00
		
		
			3
			341.00
		
		
			3
			454.00
		
		
			3
			499.00
		
	

 

	
		
			stocks
		
		
			id
			name
		
		
			1
			Apple Inc.
		
		
			2
			Microsoft Corporation
		
		
			3
			Amazon.com Inc.
		
	

 

	
		
			stock_payments
		
		
			stock_id
			dividend
		
		
			1
			71.00
		
		
			1
			189.00
		
		
			1
			195.00
		
		
			1
			341.00
		
		
			1
			456.00
		
		
			2
			52.00
		
		
			2
			55.00
		
		
			2
			145.00
		
		
			2
			211.00
		
		
			2
			236.00
		
		
			2
			319.00
		
		
			2
			324.00
		
		
			2
			334.00
		
		
			2
			482.00
		
		
			3
			97.00
		
		
			3
			124.00
		
		
			3
			210.00
		
		
			3
			372.00
		
		
			3
			398.00
		
		
			3
			400.00
		
	

 

Expected Output

 

	
		
			name
			asset_type
			sum_cash_flows
		
		
			Microsoft Corporation
			Stock
			2158.00
		
		
			XYZ Bond
			Bond
			2460.00

## Sample Input/Output

## Preview

A company manages various financial assets, including bonds and stocks, and wa
