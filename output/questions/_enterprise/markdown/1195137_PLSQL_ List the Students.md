# PLSQL: List the Students

## Metadata

- **ID:** 1195137
- **Type:** database
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Easy, PL/SQL, Conditionals, Loops, Interviewer Guidelines
- **Skills:** PL/SQL (Basic)
- **Languages:** o, r, a, c, l, e

## Summary

This database question evaluates PL/SQL, conditionals, and loops concepts, ideal for junior-level roles. The problem requires analyzing student exam performance to identify students with negative total marks based on a specified scoring system.

## Problem Statement

Analyze student exam performance from the student_results table. Your PL/SQL block should:

	
- List students whose total marks across three questions is negative.
	
- Apply the scoring system:
	
		
- Correct answer (C): +1 point
		
- Wrong answer (W): -1 point
		
- Unattempted question (U): 0 points
	
	
	
- Sort results by student ID in ascending order
	
- Format output as STUDENT_ID: TOTAL_MARKS

 

Schema

You are provided 1 table: student_results

	
		
			student_results
		
		
			Name
			Type
			Description
		
		
			Student_ID
			VARCHAR2
			Student ID
		
		
			Q1
			VARCHAR2
			Question 1
		
		
			Q2
			VARCHAR2
			Question 2
		
		
			Q3
			VARCHAR2
			Question 3
		
	

Sample Data Tables

	
		
			TABLE_ONE
		
		
			STUDENT_ID
			Q1
			Q2
			Q3
		
		
			101
			C
			W
			W
		
		
			102
			W
			W
			W
		
		
			
			
103

			
			W
			W
			U
		
	

 

Output:

101: -1

102: -3

103: -2

 

Explanation:

All three students got negative total marks.

## Sample Input/Output

## Preview

Analyze student exam performance from the student_results table. Your PL/SQL b
