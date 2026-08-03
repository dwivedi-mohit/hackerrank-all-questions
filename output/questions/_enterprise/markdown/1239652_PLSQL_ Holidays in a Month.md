# PLSQL: Holidays in a Month

## Metadata

- **ID:** 1239652
- **Type:** database
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Hard, PL/SQL, Loops, Cursor, Database, Interviewer Guidelines
- **Skills:** PL/SQL (Advanced)
- **Languages:** o, r, a, c, l, e

## Summary

This database question evaluates PL/SQL, loops, and cursors concepts, ideal for senior-level roles. The problem requires writing a PL/SQL block to list holidays and their counts for each month based on a specific table structure.

## Problem Statement

A table contains a record for each month of the year. For each month, there is a string of 'W' and 'H' characters that represent workdays and holidays in the month.

 

Write a PLSQL block that lists each holiday as well as the total holidays per month.

 

For each holiday, print

    There is a holiday on <month> <day>.

 

For each month,

If there is no holiday in a month, print

    There is no holiday in <month>.

Otherwise, print

    The number of holidays in <month> is <count>.

 

Schema

There is 1 table: HOLIDAY_DETAILS

	
		
			HOLIDAY_DETAILS
		
		
			Name
			Type
			Description
		
		
			MONTH_NAME
			VARCHAR2(4)
			Name of the month
		
		
			WORKING_NOTATION
			VARCHAR2(31)
			Working Notation
		
	

Sample Data Tables

	
		
			HOLIDAY_DETAILS 
		
		
			MONTH_NAME
			WORKING_NOTATION
		
		
			JAN
			WWWWWHHWWWWWHHWWWWWHHWWWWWHHWW
		
		
			FEB
			WWWHHWWWWWHHWWWWWHHWWWWWHHWW
		
		
			MAR
			HHWWWWWHHWWWWWHHWWWWWHHWWWWWHH
		
		
			AUG
			WWWWWWWWWWWWWWWWWWWWWWWWWWWW
		
	

 

Output:

There is a holiday on JAN 6.
There is a holiday on JAN 7.
There is a holiday on JAN 13.
There is a holiday on JAN 14.
There is a holiday on JAN 20.
There is a holiday on JAN 21.
There is a holiday on JAN 27.
There is a holiday on JAN 28.
The number of holidays in JAN is 8.
There is a holiday on FEB 4.
There is a holiday on FEB 5.
There is a holiday on FEB 11.
There is a holiday on FEB 12.
There is a holiday on FEB 18.
There is a holiday on FEB 19.
There is a holiday on FEB 25.
There is a holiday on FEB 26.
The number of holidays in FEB is 8.
There is a holiday on MAR 1.
There is a holiday on MAR 2.
There is a holiday on MAR 8.
There is a holiday on MAR 9.
There is a holiday on MAR 15.
There is a holiday on MAR 16.
There is a holiday on MAR 22.
There is a holiday on MAR 23.
There is a holiday on MAR 29.
There is a holiday on MAR 30.
The number of holidays in MAR is 10.

There is no holiday in AUG.

## Sample Input/Output

## Preview

A table contains a record for each month of the year. For each month, there
