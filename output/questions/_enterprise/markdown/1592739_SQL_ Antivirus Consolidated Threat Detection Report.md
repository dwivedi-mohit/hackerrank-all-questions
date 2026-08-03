# SQL: Antivirus Consolidated Threat Detection Report

## Metadata

- **ID:** 1592739
- **Type:** database
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Database, Medium, SQL, Complex Joins, Sub-Queries
- **Skills:** SQL (Intermediate)
- **Languages:** m, y, s, q, l, ,, o, r, a, c

## Summary

This database question evaluates SQL, complex joins, and sub-queries concepts, ideal for mid-level roles. The problem requires creating a consolidated report of antivirus detections, distinguishing sources and file types, specifically for July 2023.

## Problem Statement

Two antivirus products, "QuantumSafe" and "WebGuardian", have separate tables to record suspicious files. A company wants to create a consolidated report of these detections, distinguishing threats based on product source and file type. The database contains information from June through August, 2023.

 

The result should have the following columns: extension | quantumsafe_total_detections | webguardian_total_detections.

	
- 
extension - the file extension (e.g., *.txt, *.doc)
	
- 
quantumsafe_total_detections - the total number of detections from the "QuantumSafe" database
	
- 
webguardian_total_detections - the total number of detections from the "WebGuardian" database

 

The result should be sorted in ascending order by extension.

 

Note:

	
- Only detections in July, 2023 should be included in the report.

 

Schema

 

	
		
			file_types
		
		
			name
			type
			constraint
			description
		
		
			id
			INT
			PRIMARY KEY
			File type ID
		
		
			extension
			VARCHAR(255)
			UNIQUE
			File extension (e.g., *.txt, *.doc)
		
	

 

	
		
			quantumsafe_detections
		
		
			name
			type
			constraint
			description
		
		
			filetype_id
			INT
			FOREIGN KEY(filetype_id => file_types.id)
			File type ID reference
		
		
			dt
			VARCHAR(19)
			 
			Detection datetime
		
	

 

	
		
			webguardian_detections
		
		
			name
			type
			constraint
			description
		
		
			filetype_id
			INT
			FOREIGN KEY(filetype_id => file_types.id)
			File type ID reference
		
		
			dt
			VARCHAR(19)
			 
			Detection datetime
		
	

 

Sample Data Tables

 

	
		
			file_types
		
		
			id
			extension
		
		
			1
			*.txt
		
		
			2
			*.doc
		
		
			3
			*.pdf
		
	

 

	
		
			quantumsafe_detections
		
		
			filetype_id
			dt
		
		
			1
			2023-06-26 01:17:50
		
		
			1
			2023-06-27 02:17:16
		
		
			3
			2023-06-29 02:20:45
		
		
			1
			2023-07-14 23:55:15
		
		
			1
			2023-07-19 15:42:24
		
		
			1
			2023-07-21 23:09:52
		
		
			1
			2023-07-13 22:02:16
		
		
			1
			2023-07-24 20:48:17
		
		
			2
			2023-07-12 23:24:37
		
		
			2
			2023-07-30 06:51:58
		
		
			2
			2023-07-20 05:44:05
		
		
			3
			2023-07-27 20:33:29
		
		
			3
			2023-07-04 07:02:14
		
		
			3
			2023-07-11 23:41:55
		
		
			1
			2023-08-04 04:45:24
		
		
			1
			2023-08-01 22:43:07
		
		
			1
			2023-08-04 17:12:03
		
		
			2
			2023-08-02 23:47:40
		
		
			3
			2023-08-04 09:24:51
		
		
			3
			2023-08-04 01:12:32
		
	

 

	
		
			webguardian_detections
		
		
			filetype_id
			dt
		
		
			2
			2023-06-27 05:47:41
		
		
			3
			2023-06-27 21:33:48
		
		
			1
			2023-07-08 15:20:00
		
		
			1
			2023-07-12 12:34:59
		
		
			1
			2023-07-08 15:11:47
		
		
			1
			2023-07-24 16:34:24
		
		
			1
			2023-07-23 17:45:16
		
		
			2
			2023-07-09 11:35:14
		
		
			2
			2023-07-29 13:12:22
		
		
			2
			2023-07-29 22:50:15
		
		
			3
			2023-07-16 16:44:23
		
		
			3
			2023-07-09 07:09:54
		
		
			3
			2023-07-21 13:40:45
		
		
			3
			2023-07-14 09:26:13
		
		
			3
			2023-07-02 04:25:56
		
		
			3
			2023-07-29 10:22:25
		
		
			2
			2023-08-03 03:23:29
		
		
			2
			2023-08-02 15:35:55
		
		
			2
			2023-08-03 15:29:04
		
		
			3
			2023-08-03 09:16:56
		
	

 

Expected Output

 

	
		
			extension
			quantumsafe_total_detections
			webguardian_total_detections
		
		
			*.doc
			3
			3
		
		
			*.pdf
			3
			6
		
		
			*.txt
			5
			5

## Sample Input/Output

## Preview

Two antivirus products, "QuantumSafe" and "WebGuardian", have separate tables
