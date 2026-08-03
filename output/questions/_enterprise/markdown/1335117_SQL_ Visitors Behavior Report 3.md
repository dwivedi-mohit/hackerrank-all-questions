# SQL: Visitors Behavior Report 3

## Metadata

- **ID:** 1335117
- **Type:** database
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Windowing, SQL, Conditional Aggregation, Hard, Database, Interviewer Guidelines
- **Skills:** SQL (Advanced)
- **Languages:** m, y, s, q, l, ,, o, r, a, c

## Summary

This database question evaluates SQL, conditional aggregation, and windowing concepts, ideal for senior-level roles. The problem requires generating a report that lists the longest sequence of events by day of the week in May 2022, based on specific criteria.

## Problem Statement

To develop visitor tracking software that lists the lengths of the longest sequence of events by day of the week in May 2022, generate a report with the following structure:

 

Report Structure

	
- 
Columns:

	
		
- 
type: Represents the event type.
		
- 
Sunday .. Saturday: Columns for each day of the week, showing the longest sequence length of a specific event type on that day in May 2022.
	
	

 

Requirements

	
- Sequence Definition: A sequence consists of two or more events of the same type that occur at intervals of three hours or less.
	
- Filter: Only include events from May 2022.
	
- Order: Sort the report by event type in ascending order.

 

Each day of the week starts with "Sunday," so ensure the report uses this order.

 

Schema

 

	events Table Schema
	
		
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

 

	events Sample Data
	
		
			events
		
		
			dt
			type
		
		
			2022-04-29 21:50:31
			sell
		
		
			2022-05-04 13:55:56
			other
		
		
			2022-05-08 23:56:28
			buy
		
		
			2022-05-11 21:13:42
			other
		
		
			2022-05-12 21:02:55
			sell
		
		
			2022-05-13 21:15:22
			buy
		
		
			2022-05-16 04:01:27
			other
		
		
			2022-05-18 17:53:13
			buy
		
		
			2022-05-18 19:10:39
			buy
		
		
			2022-05-18 22:13:48
			buy
		
		
			2022-05-19 02:19:09
			sell
		
		
			2022-05-19 21:09:33
			sell
		
		
			2022-05-21 19:30:55
			buy
		
		
			2022-05-22 12:44:26
			buy
		
		
			2022-05-23 19:46:33
			sell
		
		
			2022-05-27 08:35:44
			sell
		
		
			2022-05-29 10:52:03
			sell
		
		
			2022-05-31 06:05:42
			sell
		
		
			2022-06-01 04:26:53
			sell
		
		
			2022-06-01 14:52:01
			other
		
	

 

Expected Output

 

	Sample Output
	
		
			type
			Sunday
			Monday
			Tuesday
			Wednesday
			Thursday
			Friday
			Saturday
		
		
			buy
			1
			NULL
			NULL
			2
			NULL
			1
			1
		
		
			other
			NULL
			1
			NULL
			1
			NULL
			NULL
			NULL
		
		
			sell
			1
			1
			1
			NULL
			1
			1
			NULL

## Sample Input/Output

## Preview

To develop visitor tracking software that lists the lengths of the longest seq
