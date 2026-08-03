# PLSQL: New Salaries

## Metadata

- **ID:** 1255856
- **Type:** database
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** PL/SQL, Oracle, Medium, Database, Nested For Loop, Interviewer Guidelines
- **Skills:** PL/SQL (Intermediate)
- **Languages:** o, r, a, c, l, e

## Summary

This database question evaluates PL/SQL, salary calculations, and data manipulation concepts, ideal for mid-level roles. The problem requires creating a PL/SQL block to update employee salaries based on specific rules and generate a report with salary descriptions.

## Problem Statement

Create a PL/SQL block to report an updated salary and salary description of all employees per the following rules.

The mid-range of salaries for a job is (max_salary - min_salary)/2

 

If the salary is greater than or equal to the mid-range salary for the job, increase the salary by 8%.

Otherwise, raise the salary to equal the mid-range salary for the job.

 

The salary description is based on the salary prior to the update and should be one of

	
- ‘SALARY_HIGHER_THAN_MID_RANGE’
	
- ‘SALARY_LOWER_THAN_MID_RANGE’
	
-  ‘SALARY_EQUALS_MID_RANGE’

 

The first line of output should be 'EMPNO ENAME JOB DEPTNO SALARY SALARY_DESCRIPTION'.

 

Schema

There are 2 tables: `EMPLOYEE_DETAILS,``SALARY_RANGE`.

	
		
			EMPLOYEE_DETAILS
		
		
			Name
			Type
			Description
		
		
			
			
EMPNO

			
			
			
NUMBER

			
			Number of the employee
		
		
			ENAME
			VARCHAR2(100)
			Name of the employee
		
		
			JOB
			VARCHAR2(200)
			Job profile of the employee
		
		
			DEPTNO
			NUMBER
			Department number of the employee
		
		
			SALARY
			NUMBER (6,2)
			Salary of the employee
		
		
			
			
SALARY_DESCRIPTION

			
			
			
VARCHAR2(4000) DEFAULT NULL

			
			Description of the salary
		
	

	
		
			SALARY_RANGE
		
		
			Name
			Type
			Description
		
		
			
			
JOB

			
			
			
VARCHAR2(200)

			
			Job profile of the employee
		
		
			MIN_SALARY
			NUMBER (6,0)
			Minimum salary of the employee
		
		
			MAX_SALARY
			
			
NUMBER (6,0)

			
			Maximum salary of the emp
		
	

Sample Data Tables

	
		
			EMPLOYEE_DETAILS
		
		
			
			
EMPNO

			
			ENAME
			JOB
			DEPTNO
			SALARY
			SALARY_DESCRIPTION
		
		
			
			
7839

			
			
			
KING

			
			
			
PRESIDENT

			
			
			
10

			
			
			
5500

			
			
			
NULL

			
		
		
			7698
			BLAKE
			MANAGER
			30
			2850
			NULL
		
		
			7782
			CLARK
			MANAGER
			10
			2450
			NULL
		
		
			7566
			JONES
			MANAGER
			20
			2975
			NULL
		
		
			7788
			SCOTT
			ANALYST
			20
			3000
			NULL
		
		
			7902
			FORD
			ANALYST
			20
			3000
			NULL
		
		
			7369
			
			
SMITH

			
			CLERK
			20
			800
			NULL
		
	

	
		
			SALARY_RANGE
		
		
			
			
JOB

			
			MIN_SALARY
			MAX_SALARY
		
		
			
			
PRESIDENT

			
			
			
5000

			
			
			
6000

			
		
		
			MANAGER
			2500
			3000
		
		
			ANALYST
			3000
			4000
		
		
			CLERK
			500
			1500
		
		
			SALESMAN
			1500
			2000
		
	

 

Output:

EMPNO ENAME JOB DEPTNO SALARY SALARY_DESCRIPTION

7839 KING PRESIDENT 10 5940 SALARY_EQUALS_MID_SALARY

7698 BLAKE MANAGER 30 3078 SALARY_HIGHER_THAN_MID_SALARY

7782 CLARK MANAGER 10 2750 SALARY_LOWER_THAN_MID_SALARY

7566 JONES MANAGER 20 3213 SALARY_HIGHER_THAN_MID_SALARY

7788 SCOTT ANALYST 20 3500 SALARY_LOWER_THAN_MID_SALARY

7902 FORD ANALYST 20 3500 SALARY_LOWER_THAN_MID_SALARY

7369 SMITH CLERK 20 1000 SALARY_LOWER_THAN_MID_SALARY

## Sample Input/Output

## Preview

Create a PL/SQL block to report an updated salary and salary description of al
