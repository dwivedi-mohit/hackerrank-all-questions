# PLSQL: Employee Salary

## Metadata

- **ID:** 1231141
- **Type:** database
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Oracle, Easy, Loops, Database, PL/SQL, Interviewer Guidelines
- **Skills:** PL/SQL (Basic)
- **Languages:** o, r, a, c, l, e, ,, p, o, s

## Summary

This database question evaluates PL/SQL, data analysis, and sorting concepts, ideal for junior-level roles. The problem requires writing a PL/SQL block to analyze employee salary data and display relevant information for employees with a total salary of at least 20,000.

## Problem Statement

Write a PL/SQL block to analyze employee salary data across multiple months. Your query should:

	
- Display name, department, and total salary for each employee
	
- Include only employees with total salary of at least 20,000
	
- Sort results alphabetically by employee name

 

Schema

You are provided 2 tables: EMP and SAL

	
		
			EMP
		
		
			Name
			Type
			Description
		
		
			EID
			INTEGER
			Employee Id.
		
		
			NAME
			VARCHAR2
			Name of the employee.
		
		
			DEP
			VARCHAR2
			Department of the employee.
		
	

	
		
			SAL
		
		
			Name
			Type
			Description
		
		
			EID
			INTEGER
			Employee ID.
		
		
			JAN
			INTEGER
			Salary in January
		
		
			FEB
			INTEGER
			Salary in February
		
		
			MAR
			INTEGER
			Salary in March
		
	

   Sample Data Tables

	
		
			EMP
		
		
			EID
			NAME
			DEP
		
		
			1
			Alex
			D1
		
		
			2
			Chris
			D2
		
		
			3
			Sam 
			D3
		
		
			4
			Pat
			D4
		
	

 

	
		
			SAL
		
		
			EID
			JAN
			FEB
			MAR
		
		
			1
			10000
			5000
			8000
		
		
			2
			4000
			9000
			9000
		
		
			3
			4000
			6000
			4000
		
		
			4
			7000
			3000
			5000
		
	

 

Output:

Chris D2 22000

Alex D1 23000

 

Explanation:

The output returns name, department ID, and total salary of senior employees having a total salary greater than 20,000 for three months in alphabetical order.

## Sample Input/Output

## Preview

Write a PL/SQL block to analyze employee salary data across multiple months. Y
