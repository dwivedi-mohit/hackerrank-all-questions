# Website Traffic

## Metadata

- **ID:** 645397
- **Type:** database
- **Difficulty:** 5.0
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** SQL, Aggregation, Medium, Simple Joins, Interviewer Guidelines, Sub-Queries, Database
- **Skills:** SQL (Intermediate)
- **Languages:** m, y, s, q, l, ,, o, r, a, c

## Summary

This database question evaluates SQL, aggregation, and sub-queries concepts, ideal for mid-level roles. The problem requires writing an SQL query to calculate the 3-day moving average of time spent on a website by users of type 'user'.

## Problem Statement

There is a database that contains a website's traffic data over a period of 30 days. The first table contains users' information including the user type (user, crawler, admin). The second table consists of the time of each visit to the website, the id of the visitor, time spent on the website in seconds. Write an SQL query to show the 3 day moving average of time spent on the website for users.user_type = 'user'.

Note: avg time spent must have 4 decimal digits and rounded off (example: 5/3 = 1.6667, 5/2 = 2.5000 and 1/3 = 0.3333)

 

Schema

There are 2 tables: `users`, `traffic`

	
		
			users
		
		
			Name
			Type
			Description
		
		
			id
			INTEGER
			The user's unique id. It is the primary key.
		
		
			name
			VARCHAR
			This is the second column and the name of the user.
		
		
			user_type
			VARCHAR
			Type of the user
		
	

	
		
			traffic
		
		
			Name
			Type
			Description
		
		
			user_id
			INTEGER
			id of the user from the users table.
		
		
			visited_on
			DATE
			date on which the user visited the website
		
		
			time_spent   
			    INTEGER    
			time spent on website in seconds
		
	

Sample Data Tables

	
		
			users
		
		
			id
			name
			user_type
		
		
			1
			Matt
			user
		
		
			2
			John
			user
		
		
			3
			Louis
			admin
		
	

	
		
			traffic
		
		
			user_id
			visited_on
			time_spent
		
		
			1
			2019-05-01
			15
		
		
			2
			2019-05-02
			20
		
		
			2
			2019-05-03
			10
		
	

 

Output

visited_on avg_time_spent

2019-05-01 15.0000

2019-05-02 17.5000

2019-05-03 15.0000

 

Explanation

Row 1 : 15/1 = 15.0000

Row 2 : (15+20)/2 = 17.5000

Row 3 : (15+20+10)/3 = 15.0000

## Sample Input/Output

## Preview

There is a database that contains a website's traffic data over a period of 30
