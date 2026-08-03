# Scoring System 

## Metadata

- **ID:** 380496
- **Type:** database
- **Difficulty:** 5.833333333333333
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** SQL, Easy, Interviewer Guidelines, Database
- **Skills:** SQL (Basic)
- **Languages:** m, y, s, q, l, ,, o, r, a, c

## Summary

This database question evaluates SQL, sorting, and querying concepts, ideal for junior-level roles. The problem requires writing a query to retrieve the IDs and names of the three highest scoring students, sorted by score and ID.

## Problem Statement

Write a query to print the ID and NAME of each of the three highest scoring students.

Print the records in descending order by SCORE. For matching scores, sort by ID in ascending order.

 

Schema

	
		
			STUDENT
		
		
			Name
			Type
			Description
		
		
			ID
			Integer
			unique ID, the primary key
		
		
			NAME
			String
			student name
		
		
			SCORE
			Float
			the Math score of the student
		
	

 

 

Sample Input

	
		
			STUDENT
		
		
			ID
			NAME
			SCORE
		
		
			1
			Bob
			50
		
		
			2
			John
			65.5
		
		
			3
			Harry
			45
		
		
			4
			Dick
			85
		
		
			5
			Dev
			25
		
		
			6
			Sid
			98
		
		
			7
			Tom
			90
		
		
			8
			Julia
			70.5
		
		
			9
			Erica
			81
		
		
			10
			Jerry
			85
		
	

 

Sample Output

6 Sid
7 Tom
4 Dick

```

 

Explanation

The students are arranged in the descending order of their math scores, followed by the ascending order of their IDs, as shown below:

 

`Sid > Tom > Dick > Jerry > Erica > Julia > John > Bob > Harry > Dev`

 

Dick's and Jerry's scores were the same, so they are shown in ID order.

## Preview

Write a query to print the ID and NAME of each of the three highest scoring stud
