# PLSQL: Railway Database

## Metadata

- **ID:** 1189890
- **Type:** database
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** PL/SQL, Medium, Interviewer Guidelines
- **Skills:** PL/SQL (Intermediate)
- **Languages:** o, r, a, c, l, e

## Summary

This database question evaluates PL/SQL, revenue calculation, and discount application concepts, ideal for mid-level roles. The problem requires writing a PL/SQL block to compute total revenue from passenger fare data while applying applicable discounts.

## Problem Statement

You are the database engineer at railways. There is a database named Railway_info with tables railway_rev_details having columns passenger_id, disc_category_id, fair and another table named category_details having columns category_id, category_details, percentage_discount and max_discount_limit. 

 

Write a PL/SQL block to calculate total revenue for a railway department. Passenger information is provided in two tables. The FARE column contains the gross fare for the passenger ticket. The fare actually paid is that FARE less the discount listed in category_details. The fare cannot be less than the gross fare less 'MAX_LIMIT'.

 

Schema

There are 2 tables: RAILWAY_REV_DETAILS and CATEGORY_DETAILS

	
		
			RAILWAY_REV_DETAILS
		
		
			Name
			Type
			Description
		
		
			PASSENGER_ID
			INTEGER
			unique id of the passenger
		
		
			CATEGORY_ID
			INTEGER
			foreign key, passenger category id
		
		
			FARE
			NUMBER
			gross fare for the trip
		
	

	
		
			CATEGORY_DETAILS
		
		
			Name
			Type
			Description
		
		
			CATEGORY_ID
			INTEGER
			primary key, category id
		
		
			CATEGORY_DESC
			VARCHAR2
			description of the category
		
		
			PRC_DISCOUNT
			NUMBER
			% discount to apply
		
		
			MAX_LIMIT
			NUMBER
			maximum discount amount
		
	

Sample Data Tables

	
		
			RAILWAY_REV_DETAILS
		
		
			PASSENGER_ID
			CATEGORY_ID
			FARE
		
		
			1001
			10
			600
		
		
			1002
			20
			2032
		
	

	
		
			CATEGORY_DETAILS
		
		
			CATEGORY_ID
			CATEGORY_DESC
			PRC_DISCOUNT
			MAX_LIMIT
		
		
			10
			SENIOR CITIZEN
			40
			400
		
		
			20
			ARMY GOVT. SERVENT
			50
			500
		
	

 

Output: TOTAL REVENUE:1892

 

Explanation:

Passenger '1001' is a senior citizen and qualifies for up to a 40% discount. The discount amount is 0.4 * 600 = 240 which is less than the max_limit of 400. Revenue from this passenger is 600 - 240 = 360.

 

Passenger '1002' qualifies for up to a 50% discount. The maximum discount allowed is 500 so the minimum allowable net fare is 2032 - 500 = 1532.

The calculated discount amount is 0.5 * 2032 = 1016, and the net fare is 2032 - 1016 = 1016, below the minimum allowable fare.

Revenue from this passenger is 1532.

 

 

Total revenue is 360 + 1532 = 1892. The report should look exactly like TOTAL REVENUE:1892

## Sample Input/Output

## Preview

You are the database engineer at railways. There is a database named Railway_i
