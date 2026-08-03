# Scheduling Errors

## Metadata

- **ID:** 327879
- **Type:** database
- **Difficulty:** 5.833333333333333
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** SQL, Easy, Interviewer Guidelines, Simple Joins, Database
- **Skills:** SQL (Basic)
- **Languages:** m, y, s, q, l, ,, o, r, a, c

## Summary

This database question evaluates SQL joins, distinct queries, and data retrieval concepts, ideal for junior-level roles. The problem requires querying professor names and their courses, ensuring no duplicates and filtering by department mismatches.

## Problem Statement

Query a list of professor names and the respective courses they teach (or have taught).

Find all professors who teach courses outside of their departments. Return a list with professor names and their associated courses. No duplicate rows should appear in the results.

 

The output should contain two columns: professor.name, course.name.

 

Schema

	
		
			PROFESSOR
		
		
			Name
			Type
			Description
		
		
			ID
			Integer
			unique id, primary key
		
		
			NAME
			String
			 
		
		
			DEPARTMENT_ID
			Integer
			foreign key, department.id

		
		
			SALARY
			Integer
			 
		
	

	
		
			DEPARTMENT
		
		
			Name
			Type
			Description
		
		
			ID
			Integer
			unique id, primary key
		
		
			NAME
			String
			 
		
	

 

	
		
			COURSE
		
		
			Name
			Type
			Description
		
		
			ID
			Integer
			unique id, primary key
		
		
			NAME
			String
			 
		
		
			DEPARTMENT_ID
			Integer
			foreign key, department.id

		
		
			CREDITS
			Integer
			 
		
	

	
		
			SCHEDULE
		
		
			Name
			Type
			Description
		
		
			PROFESSOR_ID
			Integer
			foreign key, professor.id

		
		
			COURSE_ID
			Integer
			foreign key, course.id

		
		
			SEMESTER
			Integer
			 
		
		
			YEAR
			Integer
			 
		
	

 

 

Sample Data Tables

 

	
		
			PROFESSOR
		
		
			ID
			NAME
			DEPARTMENT_ID
			SALARY
		
		
			1
			Alex Daniels
			4
			7169
		
		
			2
			Drew Knight
			1
			9793
		
		
			3
			Jordan Myers
			4
			25194
		
		
			4
			Tyler Rodriguez
			3
			9686
		
		
			5
			Blake Gome
			2
			30860
		
		
			6
			Spencer George
			5
			10487
		
		
			7
			Ellis Vasquez
			4
			6353
		
		
			8
			Morgan Flores
			1
			25796
		
		
			9
			Riley Gilbert
			5
			35678
		
		
			10
			Peyton Stevens
			2
			26648
		
	

	
		
			DEPARTMENT
		
		
			ID
			NAME
		
		
			3
			Biological Sciences
		
		
			5
			Technology
		
		
			6
			Humanities & Social Sciences
		
		
			2
			Clinical Medicine
		
		
			4
			Arts and Humanities
		
		
			1
			Physical Sciences
		
	

 

	
		
			COURSE
		
		
			ID
			NAME
			DEPARTMENT_ID
			CREDITS
		
		
			9
			Clinical Biochemistry
			2
			3
		
		
			4
			Astronomy
			1
			6
		
		
			10
			Clinical Neuroscience
			2
			5
		
		
			1
			Pure Mathematics and Mathematical Statistics
			1
			3
		
		
			6
			Geography
			1
			7
		
		
			8
			Chemistry
			1
			1
		
		
			5
			Physics
			1
			8
		
		
			3
			Earth Science
			1
			7
		
		
			7
			Materials Science and Metallurgy
			1
			5
		
		
			2
			Applied Mathematics and Theoretical Physics
			1
			5
		
	

	
		
			SCHEDULE
		
		
			PROFESSOR_ID
			COURSE_ID
			SEMESTER
			YEAR
		
		
			4
			4
			3
			2003
		
		
			3
			3
			1
			2011
		
		
			1
			7
			5
			2011
		
		
			7
			7
			1
			2010
		
		
			4
			6
			1
			2001
		
		
			9
			3
			1
			2012
		
		
			10
			2
			4
			2009
		
		
			1
			1
			3
			2014
		
		
			1
			2
			3
			2008
		
		
			1
			7
			5
			2007
		
	

 

Sample Output

Tyler Rodriguez Astronomy
Jordan Myers Earth Sciences
Alex Daniels Materials Science and Metallurgy
Ellis Vasquez Materials Science and Metallurgy
Tyler Rodriguez Geography
Riley Gilbert Earth Sciences
Peyton Stevens Applied Mathematics and Theoretical Physics
Alex Daniels Pure Mathematics and Mathematical Statistics
Alex Daniels Applied Mathematics and Theoretical Physics
Alex Daniels Materials Science and Metallurgy 
```

 

Explanation

 

Example logic

	
- Professor Tyler Rodriguez's department_id is 3, but the Astronomy course's department_id is 1.
	
- Professor Jordan Myers's department_id is 4, but the Earth Sciences course's department_id is 1

## Preview

Query a list of professor names and the respective courses they teach (or have
