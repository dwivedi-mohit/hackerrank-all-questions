# SQL: Visitors Behavior Report

## Metadata

- **ID:** 1331561
- **Type:** database
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Database, Easy, SQL, Interviewer Guidelines, Filtering, Aggregation
- **Skills:** SQL (Basic)
- **Languages:** m, y, s, q, l, ,, o, r, a, c

## Summary

This database question evaluates SQL, filtering, and aggregation concepts, ideal for junior-level roles. The problem requires calculating the total number of purchase events labeled as 'buy' that occurred in May 2022.

## Problem Statement

Calculate the total number of purchase events that occurred in May 2022.

 

Your result should include:

	
- The total count of purchase events

Requirements:

	
- Only count events with "buy" in the type field.
	
- Only include events from May 2022.

 

Schema

 

	
		
			events
		
		
			name
			type
			description
		
		
			dt
			VARCHAR(19)
			Event timestamp
		
		
			type
			VARCHAR(64)
			Event type
		
	

 

Sample Data Tables

 

	
		
			events
			 
		
		
			dt
			type
		
		
			2022-04-04 03:36:00
			buy
		
		
			2022-04-21 07:05:09
			buy
		
		
			2022-04-02 11:34:24
			sell
		
		
			2022-05-27 16:12:50
			buy
		
		
			2022-05-20 09:09:07
			buy
		
		
			2022-05-22 09:06:37
			buy
		
		
			2022-05-31 07:49:36
			buy
		
		
			2022-05-14 22:29:10
			buy
		
		
			2022-05-13 15:00:54
			sell
		
		
			2022-05-24 15:40:54
			sell
		
		
			2022-05-13 01:20:05
			sell
		
		
			2022-05-16 07:07:44
			sell
		
		
			2022-05-01 16:57:00
			sell
		
		
			2022-06-02 09:42:02
			buy
		
		
			2022-06-01 06:34:59
			buy
		
		
			2022-06-06 17:14:47
			buy
		
		
			2022-06-05 13:37:23
			buy
		
		
			2022-06-17 19:10:13
			buy
		
		
			2022-06-15 21:40:13
			sell
		
		
			2022-06-11 12:26:43
			sell
		
	

 

Expected Output

 

	
		
			purchases
		
		
			5

## Sample Input/Output

## Preview

Calculate the total number of purchase events that occurred in May 2022.
