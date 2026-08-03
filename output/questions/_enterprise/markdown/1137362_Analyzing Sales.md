# Analyzing Sales

## Metadata

- **ID:** 1137362
- **Type:** database
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Windowing, SQL, Hard, Database, Interviewer Guidelines
- **Skills:** SQL (Advanced)
- **Languages:** m, y, s, q, l, ,, o, r, a, c

## Summary

This database question evaluates SQL, windowing functions, and data aggregation concepts, ideal for senior-level roles. The problem requires calculating the sum of sale amounts based on specific criteria involving distinct purchase amounts and date pairs.

## Problem Statement

The data of purchases and sales is maintained in a database. Return the sum of the sale amounts that meet the following criteria.

	
- The purchase amount must not be distinct.
	
- The (year, month) pair must be distinct.

 

Schema

There is 1 table: `sales_purchase`.

	
		
			sales_purchase
		
		
			Name
			Type
			Description
		
		
			oid
			int
			This is the order id. It is the primary key.
		
		
			purchase
			int
			Amount at which the product was purchased.
		
		
			sale
			int
			Amount at which the product was sold.
		
		
			year
			int
			Year in which the transaction happened.
		
		
			month
			char(3)
			Month in which the transaction happened.
		
	

Sample Data Tables

	
		
			sales_purchase
		
		
			oid
			purchase
			sale
			year
			month
		
		
			747
			240
			276
			2019
			JAN
		
		
			425
			240
			248
			2019
			JUN
		
		
			878
			200
			267
			2019
			APR
		
		
			904
			230
			279
			2018
			MAY
		
		
			107
			230
			270
			2018
			MAR
		
		
			227
			370
			388
			2020
			APR
		
		
			534
			330
			394
			2018
			MAR
		
		
			305
			300
			367
			2019
			JAN
		
		
			145
			260
			308
			2020
			MAY
		
		
			202
			370
			451
			2019
			APR
		
	

 

 

	
		
			OUTPUT
		
		
			sum
		
		
			915
		
	

 

The records where dates are not distinct are excluded from the report. Of the records with distinct dates, the ones that have non-distinct purchase amounts are included.

OID  Purchase    Sale    Date         Match
Duplicate dates
878  200         267     2019 APR    
202  370         451     2019 APR     1
747  240         276     2019 JAN     2
305  300         367     2019 JAN    
107  230         270     2018 MAR     3
534  330         394     2018 MAR     

Disinct dates
227  370        388      2020 APR     1 (this purchase amount matches the purchase amount for the row marked 1 above)
425  240        248      2019 JUN     2
904  230        279      2018 MAY     3
145  260        308      2020 MAY     No match

```

 

There are three sales values in the table with the same purchase value but unique year and month pairs: 248, 279, and 388, the sum of which is 915.

## Sample Input/Output

## Preview

The data of purchases and sales is maintained in a database. Return the sum of
