# PLSQL: Railway Profits

## Metadata

- **ID:** 1192792
- **Type:** database
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Easy, Range, PL/SQL, Interviewer Guidelines
- **Skills:** PL/SQL (Basic)
- **Languages:** o, r, a, c, l, e

## Summary

This database question evaluates PL/SQL, fare calculation, and discount application concepts, ideal for junior-level roles. The problem requires writing a PL/SQL block to find the passenger who paid the highest fare after applying discounts.

## Problem Statement

Write a PL/SQL block to find the passenger who paid the highest fare after discount was applied. The query should:

	
- Calculate the fare after discount for each passenger subject to the maximum discount limit
	
- Display the passenger ID and the fare after discount, separated by a colon (:)

 

Schema

 

There are 2 tables: railway_rev_details, category_details

	
		
			RAILWAY_REV_DETAILS
		
		
			Name
			Type
			Description
		
		
			PASSENGER_ID
			INTEGER
			The ID of the passenger
		
		
			CATEGORY_ID
			INTEGER
			Category ID of the passenger
		
		
			FARE
			NUMBER
			Amount (in $)
		
	

	
		
			
			
CATEGORY_DETAILS

			
		
		
			Name
			Type
			Description
		
		
			CATEGORY_ID
			INTEGER
			The ID of the category
		
		
			CATEGORY_DESC
			VARCHAR2
			 Description of the category
		
		
			PRC_DISCOUNT
			NUMBER
			 Percentage Discount
		
		
			MAX_LIMIT
			  NUMBER
			The maximum discount value that can be offered
		
	

 

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
			 ARMY GOVT. SERVANT
			 50
			 500
		
	

  

       

Output: 1002:1532

 

 

Explanation:

 

The minimum price a passenger can pay is fare - maximum_discount.

 

The passenger '1001' paid MAX(600 - (600 * 0.4) = 600 - 240 = 360, 600 - 400 = 200) = 360

Passenger '1002' paid 2032 MAX(2032 - (2032 * 0.5) = 1016, 2032 - 500 = 1532) = 1532

## Sample Input/Output

## Preview

Write a PL/SQL block to find the passenger who paid the highest fare after dis
