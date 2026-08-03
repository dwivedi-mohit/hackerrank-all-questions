# SQL: Antivirus Database Quarantine Report

## Metadata

- **ID:** 1590507
- **Type:** database
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Database, SQL, Easy, Interviewer Guidelines, Joins, Filtering
- **Skills:** SQL (Basic)
- **Languages:** m, y, s, q, l, ,, o, r, a, c

## Summary

This database question evaluates SQL, joins, and filtering concepts, ideal for junior-level roles. The problem requires creating a query to analyze quarantined URLs and return specific threat-related data sorted by user impact.

## Problem Statement

Create a query for a cyber-security company that analyzes quarantined URLs. The query should return:

	
- domain_name
	
- 
threat_identified - Type of threat identified
	
- 
total_occurrences - Total number of times the domain was quarantined for that threat
	
- 
total_users_affected - Total number of users affected by the threat from that domain

Only URLs with status "Quarantined" should be included. Results should be sorted in descending order by users affected, then in ascending order by domain name.

 

Schema

 

	
		
			threat_types
		
		
			name
			type
			constraint
			description
		
		
			id
			INT
			PRIMARY KEY
			Threat type ID
		
		
			threat_type
			VARCHAR(255)
			 
			Type of threat (e.g., Malware, Phishing)
		
	

 

	
		
			quarantine_urls
		
		
			name
			type
			constraint
			description
		
		
			id
			INT
			PRIMARY KEY
			URL ID
		
		
			threat_id
			INT
			FOREIGN KEY(threat_id => threat_types.id)
			Reference to the type of threat
		
		
			domain_name
			VARCHAR(255)
			 
			Domain name of the quarantined URL
		
		
			status
			ENUM('Quarantined','Safe','Deleted')
			 
			URL status in the system
		
		
			users_affected
			INT
			 
			Number of users affected by the quarantined URL
		
	

 

Sample Data Tables

 

	
		
			threat_types
		
		
			id
			threat_type
		
		
			1
			Phishing
		
		
			2
			Rootkit
		
		
			3
			Malware
		
	

 

	
		
			quarantine_urls
		
		
			id
			threat_id
			domain_name
			status
			users_affected
		
		
			17
			1
			amazon.com
			Quarantined
			862
		
		
			16
			1
			google.com
			Quarantined
			63
		
		
			9
			1
			amazon.com
			Quarantined
			41
		
		
			18
			2
			amazon.com
			Quarantined
			149
		
		
			12
			2
			yahoo.com
			Quarantined
			967
		
		
			4
			3
			amazon.com
			Quarantined
			377
		
		
			10
			3
			yahoo.com
			Quarantined
			721
		
		
			11
			1
			yahoo.com
			Deleted
			551
		
		
			20
			1
			amazon.com
			Safe
			407
		
		
			19
			1
			amazon.com
			Deleted
			665
		
		
			15
			1
			facebook.com
			Safe
			52
		
		
			2
			1
			google.com
			Safe
			309
		
		
			1
			2
			twitter.com
			Safe
			562
		
		
			13
			2
			facebook.com
			Safe
			208
		
		
			14
			2
			google.com
			Deleted
			731
		
		
			8
			2
			twitter.com
			Safe
			924
		
		
			7
			2
			twitter.com
			Safe
			982
		
		
			6
			2
			google.com
			Deleted
			864
		
		
			3
			2
			facebook.com
			Safe
			136
		
		
			5
			3
			yahoo.com
			Safe
			949
		
	

 

Expected Output

 

	
		
			domain_name
			threat_type
			total_occurrences
			total_users_affected
		
		
			yahoo.com
			Rootkit
			1
			967
		
		
			amazon.com
			Phishing
			2
			903
		
		
			yahoo.com
			Malware
			1
			721
		
		
			amazon.com
			Malware
			1
			377
		
		
			amazon.com
			Rootkit
			1
			149
		
		
			google.com
			Phishing
			1
			63

## Sample Input/Output

## Preview

Create a query for a cyber-security company that analyzes quarantined URLs. Th
