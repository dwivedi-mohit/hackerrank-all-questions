# Employee Working Hours 

## Metadata

- **ID:** 1010714
- **Type:** database
- **Difficulty:** 5.0
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Windowing, SQL, Simple Joins, Analytics Function, Hard, Database, Interviewer Guidelines
- **Skills:** SQL (Advanced)
- **Languages:** m, y, s, q, l, ,, o, r, a, c

## Summary

This database question evaluates SQL, windowing functions, and analytics concepts, ideal for senior-level roles. The problem requires writing a query to calculate working hours between employee 'In' and 'Out' timestamps, ensuring proper formatting and ordering of results.

## Problem Statement

Write a query to calculate the working hours, minutes, and seconds between each 'In' and 'Out' for each employee.

 

Results should include the columns employee_id, employee_name, department, designation, at_date and at_time (In), at_data and at_time (Out), and working hours. See the output under Sample Data Tables below for the correct format to use. Be sure to match the format exactly. The output should be ordered by the employee id, then by the working hours start date/time, both ascending.

 

Note: The requirement is to calculate the amount of time in hours, minutes, and seconds between each In and Out, for each Employee. While there is usually a matching Out row for each In, sometimes there is an In with no Out or an Out with no In. In either of these cases, omit the data from the result.

 

Table definitions and a data sample are given below.

Schema

Table: department_master

	
		
			column name
			column type
			key / NULL
		
	
	
		
			department_id
			int
			PK
		
		
			department
			varchar(255)
			NOT NULL
		
	

 

Table: designation_master

	
		
			column name
			column type
			key / NULL
		
	
	
		
			designation_id
			int
			PK
		
		
			designation
			varchar(255)
			NOT NULL
		
	

 

Table: employee_master

	
		
			column name
			column type
			key / NULL
		
	
	
		
			employee_id
			int
			PK
		
		
			employee_name
			varchar(255)
			NOT NULL
		
		
			department_id
			int
			FK
		
		
			designation_id
			int
			FK
		
	

employee_master.department_id references department_master.department_id

employee_master.designation_id references designation_master.designation_id

 

Table: employee_attendance

	
		
			column name
			column type
			key / NULL
		
	
	
		
			employee_id
			int
			FK
		
		
			at_date
			date
			NOT NULL
		
		
			at_time
			varchar(30)
			NOT NULL
		
		
			punch_type
			varchar(5)
			NULL
		
	

employee_attendance.employee_id references employee_master.employee_id

 

Sample Data Tables

Table: department_master

	
		
			department_id
			department
		
	
	
		
			1
			Accounts
		
		
			2
			Human Resource
		
	

 

Table: designation_master

	
		
			designation_id
			designation
		
	
	
		
			1
			Manager
		
		
			2
			Sr. Manager
		
	

 

Table: employee_master

	
		
			employee_id
			employee_name
			department_id
			designation_id
		
	
	
		
			1
			Sunil Kumar Goel
			2
			1
		
		
			2
			Kamli  Dawar
			1
			2
		
	

 

Table: employee_attendance

 

	
		
			employee_id
			at_date
			at_time
			punch_type
		
	
	
		
			1
			2021-02-01
			08:00
			In
		
		
			2
			2021-02-01
			08:10
			  In
		
		
			1
			2021-02-01
			11:30
			Out
		
		
			1
			2021-02-01
			11:35
			Out
		
		
			1
			2021-02-01
			12:45
			In
		
		
			2
			2021-02-01
			16:45
			Out
		
		
			1
			2021-02-01
			17:30
			Out
		
		
			1
			2021-02-01
			01:00
			Out
		
	

 

First three rows results should be:

 

 

1    Sunil Kumar Goel    Human Resource    Manager     2021-02-01 08:00:00.000    2021-02-01 11:35:00.000    03:35:00

1    Sunil Kumar Goel    Human Resource    Manager     2021-02-01 12:45:00.000    2021-02-01 17:30:00.000    04:45:00

2    Kamli  Dawar     Accounts    Sr. Manager     2021-02-01 08:10:00.000    2021-02-01 16:45:00.000    08:35:00

## Sample Input/Output

## Preview

Write a query to calculate the working hours, minutes, and seconds between eac
