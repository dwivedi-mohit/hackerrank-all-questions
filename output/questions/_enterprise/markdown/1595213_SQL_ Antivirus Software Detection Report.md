# SQL: Antivirus Software Detection Report

## Metadata

- **ID:** 1595213
- **Type:** database
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Windowing, SQL, Conditional Filtering, Hard, Database
- **Skills:** SQL (Advanced)
- **Languages:** m, y, s, q, l, ,, o, r, a, c

## Summary

This database question evaluates SQL, windowing functions, and conditional filtering concepts, ideal for senior-level roles. The problem requires developing a query to analyze antivirus software detection rates based on scan reports, focusing on specific output columns and sorting criteria.

## Problem Statement

An organization uses multiple antivirus software across its computer systems. A query needs to be developed to analyze the detection rate of each software based on scan reports.

 

The statistic required is a list of all antivirus software and the number of detections in the last scan, as well as the change in detections compared to the previous scan.

 

The result should have the following columns: title | last_detections | change_in_detections.

	
- 
title - product title of the antivirus software
	
- 
last_detections - total number of detections in the most recent scan for that software
	
- 
change_in_detections - difference in detections between the most recent scan and the previous scan

 

The result should be sorted in descending order by last_detections, then in ascending order by title.

 

Note:

	
- Only antivirus software whose most recent scan reported more than 10 detections should be included in the report.

 

Schema

 

	
		
			softwares
		
		
			name
			type
			constraint
			description
		
		
			id
			INT
			PRIMARY KEY
			Antivirus software ID
		
		
			title
			VARCHAR(255)
			UNIQUE
			Product title of the antivirus software
		
	

 

	
		
			scans
		
		
			name
			type
			constraint
			description
		
		
			software_id
			INT
			FOREIGN KEY(software_id => softwares.id)
			Antivirus software ID reference
		
		
			dt
			VARCHAR(19)
			 
			Scan datetime
		
		
			detections
			INT
			 
			Number of detections in the scan
		
	

 

Sample Data Tables

 

	
		
			softwares
		
		
			id
			title
		
		
			1
			SecureShield
		
		
			2
			DefenderPro
		
		
			3
			SafeGuard
		
	

 

	
		
			scans
		
		
			software_id
			dt
			detections
		
		
			1
			2023-06-26 03:51:52
			4
		
		
			1
			2023-07-03 22:28:37
			8
		
		
			1
			2023-07-10 05:51:31
			2
		
		
			1
			2023-07-11 20:49:45
			12
		
		
			1
			2023-07-24 00:21:44
			13
		
		
			1
			2023-07-24 07:35:17
			9
		
		
			1
			2023-07-25 10:56:12
			2
		
		
			1
			2023-07-26 15:12:36
			12
		
		
			2
			2023-07-02 20:06:09
			17
		
		
			2
			2023-07-21 10:03:18
			13
		
		
			2
			2023-07-24 10:15:22
			6
		
		
			2
			2023-07-27 15:10:20
			18
		
		
			2
			2023-08-04 08:54:55
			3
		
		
			2
			2023-08-06 15:21:06
			4
		
		
			2
			2023-08-07 16:41:19
			8
		
		
			3
			2023-07-06 07:06:48
			3
		
		
			3
			2023-07-13 00:28:19
			2
		
		
			3
			2023-07-15 04:19:28
			20
		
		
			3
			2023-07-19 21:06:56
			8
		
		
			3
			2023-07-21 07:22:24
			9
		
	

 

Expected Output

 

	
		
			title
			last_detections
			change_in_detections
		
		
			SecureShield
			12
			10

## Sample Input/Output

## Preview

An organization uses multiple antivirus software across its computer systems.
