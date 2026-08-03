# Youngest Employees

## Metadata

- **ID:** 380498
- **Type:** database
- **Difficulty:** 5.833333333333333
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** SQL, Easy, Interviewer Guidelines, Simple Joins, Database
- **Skills:** SQL (Basic)
- **Languages:** m, y, s, q, l, ,, o, r, a, c

## Summary

This database question evaluates SQL, simple joins, and sorting concepts, ideal for junior-level roles. The problem requires writing a query to list employees under 25 years old, sorted by name and employee ID, including their UIN.

## Problem Statement

Write a query to generate a list of all employees who are less than 25 years old.

 

Sort the results first by NAME, then by employee ID, both in ascending order. The result should include the UIN followed by the NAME.

 

Schema

	
		
			EMPLOYEE
		
		
			Name
			Type
			Description
		
		
			ID
			Integer
			The ID of the employee. This is a primary key.
		
		
			NAME
			String
			The name of the employee having [1, 20] characters.
		
		
			AGE
			Integer   
			The age of the employee.
		
		
			ADDRESS
			String
			The address of the employee having [1, 25] characters.
		
		
			SALARY
			Integer
			The salary of the employee.
		
	

	
		
			EMPLOYEE_UIN
		
		
			Name
			Type
			Description
		
		
			ID
			Integer
			The ID of the employee. This is a primary key.
		
		
			UIN
			String
			The unique identification number of the employee.
		
	

Sample Data Tables

Sample Input

	
		
			EMPLOYEE
		
		
			ID
			NAME
			AGE
			ADDRESS
			SALARY
		
		
			1
			Sherrie
			23
			Paris
			74635
		
		
			2
			Paul
			30
			Sydney
			72167
		
		
			3
			Mary
			24
			Paris
			75299
		
		
			4
			Sam
			47
			Sydney
			46681
		
		
			5
			Dave
			22
			Texas
			11843
		
	

	
		
			EMPLOYEE_UIN
		
		
			ID
			UIN
		
		
			1
			57520-0440
		
		
			2
			49638-001
		
		
			3
			63550-194
		
		
			4
			68599-6112
		
		
			5
			63868-453
		
	

 

Sample Output

63868-453 Dave
63550-194 Mary
57520-0440 Sherrie
```

 

 

Explanation

	
- 
Sherrie is 23 years old and has UIN 57520-0440.  This record is printed.
	
- 
Paul is 30 years old and has UIN 49638-001.  This record is not printed.
	
- A similar analysis is done on the remaining records.

None of the three names of people less than 25 years old is repeated, so print them in alphabetical order.  There is no additional sorting by ID in this case.

## Preview

Write a query to generate a list of all employees who are less than 25 years o
