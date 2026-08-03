# SQL: Credentials Manager Activity Analysis

## Metadata

- **ID:** 1521639
- **Type:** database
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Windowing, Sequence Detection, MySQL, Hard, Database
- **Skills:** SQL (Advanced)
- **Languages:** m, y, s, q, l, ,, o, r, a, c

## Summary

This database question evaluates SQL, windowing functions, and sequence detection concepts, ideal for senior-level roles. The problem requires creating a query to list sequences of three or more consecutive 'ERROR' results for user accounts in a credential management platform.

## Problem Statement

A credential management platform maintains a list of 'ERROR' and 'SUCCESS' result types and their timestamps for user accounts. As part of the maintenance process, a report must be generated that lists all sequences of three or more consecutive 'ERROR' results for each account.

 

Create a query that returns a list of all accounts and their associated error sequences.

 

The result should have the following columns: mac | type | started_at | ended_at | activities.

	
- 
mac - account MAC address
	
- 
type - activity result
	
- 
started_at - date and time the sequence started
	
- 
ended_at - date and time the sequence ended
	
- 
activities - number of activities in a sequence

 

The report should be sorted in ascending order by mac, then in ascending order by started_at.

 

Note:

	
- Only sequences of 3 or more consecutive 'ERROR' results for an account should be included in the result.

 

Schema

 

	
		
			accounts
		
		
			name
			type
			constraint
			description
		
		
			id
			INT
			PRIMARY KEY
			Account ID
		
		
			mac
			VARCHAR(255)
			 
			MAC address
		
	

 

	
		
			activities
		
		
			name
			type
			constraint
			description
		
		
			account_id
			INT
			FOREIGN KEY (account_id => accounts.id)
			Account ID
		
		
			dt
			VARCHAR(19)
			 
			Datetime
		
		
			type
			ENUM('SUCCESS','ERROR')
			 
			Activity type
		
	

 

Sample Data Tables

 

	
		
			accounts
		
		
			id
			mac
		
		
			1
			C4-85-20-F3-E9-CD
		
		
			2
			CB-5D-05-EE-05-97
		
		
			3
			5C-40-A9-D4-25-77
		
	

 

	
		
			activities
		
		
			account_id
			dt
			type
		
		
			1
			2023-04-05 05:46:06
			SUCCESS
		
		
			1
			2023-04-05 07:07:17
			ERROR
		
		
			1
			2023-04-05 08:35:24
			ERROR
		
		
			1
			2023-04-05 10:33:44
			ERROR
		
		
			1
			2023-04-05 13:00:02
			ERROR
		
		
			1
			2023-04-05 18:09:50
			SUCCESS
		
		
			1
			2023-04-05 20:23:35
			ERROR
		
		
			1
			2023-04-05 21:29:59
			ERROR
		
		
			1
			2023-04-05 23:14:00
			ERROR
		
		
			1
			2023-04-05 23:31:21
			SUCCESS
		
		
			2
			2023-04-05 05:04:25
			ERROR
		
		
			2
			2023-04-05 05:52:53
			ERROR
		
		
			2
			2023-04-05 07:34:24
			ERROR
		
		
			2
			2023-04-05 16:33:08
			SUCCESS
		
		
			2
			2023-04-05 18:05:42
			SUCCESS
		
		
			2
			2023-04-05 22:58:08
			SUCCESS
		
		
			3
			2023-04-05 02:03:47
			ERROR
		
		
			3
			2023-04-05 03:18:29
			ERROR
		
		
			3
			2023-04-05 06:18:17
			SUCCESS
		
		
			3
			2023-04-05 22:38:07
			SUCCESS
		
	

 

Expected Output

 

	
		
			mac
			type
			started_at
			ended_at
			activities
		
		
			C4-85-20-F3-E9-CD
			ERROR
			2023-04-05 07:07:17
			2023-04-05 13:00:02
			4
		
		
			C4-85-20-F3-E9-CD
			ERROR
			2023-04-05 20:23:35
			2023-04-05 23:14:00
			3
		
		
			CB-5D-05-EE-05-97
			ERROR
			2023-04-05 05:04:25
			2023-04-05 07:34:24
			3

## Sample Input/Output

## Preview

A credential management platform maintains a list of 'ERROR' and 'SUCCESS' res
