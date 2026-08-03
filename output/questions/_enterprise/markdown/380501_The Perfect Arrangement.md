# The Perfect Arrangement

## Metadata

- **ID:** 380501
- **Type:** database
- **Difficulty:** 5.833333333333333
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** SQL, Easy, Interviewer Guidelines, Database, String Manipulation, Multi-Level Sorting
- **Skills:** SQL (Basic)
- **Languages:** m, y, s, q, l, ,, o, r, a, c

## Summary

This database question evaluates SQL, string manipulation, and multi-level sorting concepts, ideal for junior-level roles. The problem requires writing a query to select customer details based on the length of their concatenated names and sorting the results accordingly.

## Problem Statement

Write a query to print the ID, FIRST_NAME, and LAST_NAME of customers whose concatenated first and last names are less than 12 letters long.

 

Sort the results by:

	
- Combined name length (ascending)
	
- Combined name alphabetically (case insensitive, ascending)
	
- ID (ascending)

 

Schema

CUSTOMER

	
		
			Name
			Type
			Description
		
		
			ID
			Integer
			unique id, primary key.
		
		
			FIRST_NAME
			String
			 
		
		
			LAST_NAME
			String
			 
		
		
			COUNTRY
			String
			 
		
		
			CREDIT_LIMIT
			Float
			 
		
	

 

 

Sample Input

 

CUSTOMER

	
		
			ID
			FIRST_NAME
			LAST_NAME
			COUNTRY
			CREDIT_LIMIT
		
		
			1
			Alex
			White
			USA
			200350.54
		
		
			2
			Tyler
			Hanson
			UK
			15354.23
		
		
			3
			Jordan
			Fernandez
			France
			359200.67
		
		
			4
			Drew
			Bradley
			Albania
			1060.57
		
		
			5
			Blake
			Fuller
			USA
			14789.00
		
		
			6
			Spencer
			Johnston
			China
			100243.35
		
		
			7
			Ellis
			Gutierrez
			USA
			998999.20
		
		
			8
			Morgan
			Thomas
			Canada
			500500.23
		
		
			9
			Riley
			Garza
			UK
			18782.44
		
		
			10
			Peyton
			Harris
			USA
			158367.00
		
	

 

 

Sample Output

1	Alex White
9	Riley Garza
5	Blake Fuller
4	Drew Bradley
2	Tyler Hanson

```

 

Explanation

 

AlexWhite is 9 letters, so it is included in the results. JordanFernandez is 15 letters, so it is omitted. The last 3 names are the same length, so they are sorted alphabetically ascending.

 

Names that are excluded and their lengths

MorganThomas	12
PeytonHarris	12
EllisGutierrez	14
JordanFernandez	15
SpencerJohnston	15

```

## Preview

Write a query to print the ID, FIRST_NAME, and LAST_NAME of customers whose co
