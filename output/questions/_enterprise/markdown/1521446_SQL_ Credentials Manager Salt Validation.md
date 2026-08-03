# SQL: Credentials Manager Salt Validation

## Metadata

- **ID:** 1521446
- **Type:** database
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** MySQL, Database, Easy, String Manipulation, Conditional Logic
- **Skills:** SQL (Basic)
- **Languages:** m, y, s, q, l, ,, o, r, a, c

## Summary

This database question evaluates SQL, string manipulation, and conditional logic concepts, ideal for junior-level roles. The problem requires creating a query to identify accounts with short salt strings in active encryptions for a security audit.

## Problem Statement

Create a query for a credential management platform security audit that identifies accounts using short salt strings in their active encryptions. The query should return:

	
- Account MAC address
	
- Number of encryption salts that are too short (length less than 8)

Only active encryptions should be considered. Results should be sorted in ascending order by MAC address.

 

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
		
	

 

	
		
			encryptions
		
		
			name
			type
			constraint
			description
		
		
			account_id
			INT
			FOREIGN KEY (account_id => accounts.id)
			Account ID
		
		
			salt
			VARCHAR(255)
			 
			Salt
		
		
			is_active
			BOOLEAN
			 
			Activity flag
		
	

 

Sample Data Tables

 

	
		
			accounts
		
		
			id
			mac
		
		
			1
			0C-6B-27-2E-E0-49
		
		
			2
			01-51-06-EC-7C-FB
		
		
			3
			7F-43-FD-22-2E-94
		
	

 

	
		
			encryptions
		
		
			account_id
			salt
			is_active
		
		
			1
			cc20ad47815
			0
		
		
			1
			eb4a0bb0
			0
		
		
			1
			3be6c4d2a1644b
			0
		
		
			1
			339c8ee8856c28
			0
		
		
			1
			27d2075
			0
		
		
			1
			960c872e5dc
			0
		
		
			1
			531ca7f4d
			1
		
		
			1
			4101965
			1
		
		
			1
			f2707
			1
		
		
			1
			7a1c7adbe686e
			1
		
		
			2
			5d98604bbfb
			0
		
		
			2
			f617f
			0
		
		
			2
			013c49b42bee9
			1
		
		
			3
			599f71b43c9
			0
		
		
			3
			ea7b576a4b
			0
		
		
			3
			99a57e
			1
		
		
			3
			be2d70bb850
			1
		
		
			3
			d1b48f27ecdba
			1
		
		
			3
			0fd088f68
			1
		
		
			3
			1bc22ee
			1
		
	

 

Expected Output

 

	
		
			mac
			salts
		
		
			0C-6B-27-2E-E0-49
			2
		
		
			7F-43-FD-22-2E-94
			2

## Preview

Create a query for a credential management platform security audit that identi
