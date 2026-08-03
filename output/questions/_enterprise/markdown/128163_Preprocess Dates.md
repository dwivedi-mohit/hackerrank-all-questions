# Preprocess Dates

## Metadata

- **ID:** 128163
- **Type:** code
- **Difficulty:** 9.444444444444445
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Implementation, Medium, Data Structures, Algorithms, Problem Solving, Theme:  E-commerce, Strings, Interviewer Guidelines
- **Skills:** Problem Solving (Basic)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates problem solving, string formatting, and data structures concepts, ideal for junior-level roles. The task requires converting date strings from a specific format into a standardized format for storage.

## Problem Statement

Convert a date string to a given format.

Users enter dates as text in a web form, and these dates must be converted into a consistent format before being saved.

 

You are given date strings in the format:

"Day Month Year"

where:

	
- Day is written with an ordinal suffix, such as "1st", "2nd", "3rd", "4th", "12th", "21st", "31st", etc.
	
- Month is the three-letter abbreviation of the English month name ("Jan" to "Dec").
	
- Year is a 4-digit number between 1900 and 2100.

Your task is to convert each date into the standard format:

"YYYY-MM-DD"

(4-digit year, 2-digit month, 2-digit day)

 

You must write a function that takes an array of such date strings and returns an array of the converted formats.

 

Example

	
- 
1st Mar 1974 → 1974-03-01

	
- 
22nd Jan 2013 → 2013-01-22

	
- 
7th Apr 1904 → 1904-04-07

 

Function Description 

Complete the function preprocessDate in the editor with the following parameter(s):

    string dates[n]:  date strings in the format Day Month Year

	
		
			Name
			Type
			Description
		
		
			dates
			string array
			An array of date strings in the format Day Month Year.
		
	

The function must return an array of strings where each index i contains the value of datesi converted to the format YYYY-MM-DD.

-->

 

Returns:

    string[n]: array of converted date strings

 

Constraints

	
- The values of Day, Month, and Year are restricted to the value ranges specified above.
	
- The given dates are guaranteed to be valid, so no error handling is necessary.
	
- 1 ≤ n ≤ 104

 

 DO NOT REMOVE THIS LINE-->

Input Format for Custom Testing

Input from stdin will be processed as follows and passed to the function.

 

The first line contains an integer n, the size of the array dates.

Each of the next n lines contains a string, dates[i] where 0 ≤ i < n.

Sample Case 0

Sample Input 0

STDIN               Function 
-----               -------- 
10              →   dates[] size n = 10
20th Oct 2052   →   dates = ["20th Oct 2052", "6th Jun 1933", "26th May 1960", "20th Sep 1958", "16th Mar 2068", "25th May 1912", "16th Dec 2018", 
6th Jun 1933                 "26th Dec 2061", "4th Nov 2030", "28th Jul 1963"]
26th May 1960
20th Sep 1958
16th Mar 2068
25th May 1912
16th Dec 2018
26th Dec 2061
4th Nov 2030
28th Jul 1963

```

Sample Output 0

2052-10-20
1933-06-06
1960-05-26
1958-09-20
2068-03-16
1912-05-25
2018-12-16
2061-12-26
2030-11-04
1963-07-28
```

Explanation

The conversions are:

20th Oct 2052 → 2052-10-20
 6th Jun 1933 → 1933-06-06
26th May 1960 → 1960-05-26
20th Sep 1958 → 1958-09-20
16th Mar 2068 → 2068-03-16
25th May 1912 → 1912-05-25
16th Dec 2018 → 2018-12-16
26th Dec 2061 → 2061-12-26
 4th Nov 2030 → 2030-11-04
28th Jul 1963 → 1963-07-28

```

## Sample Input/Output

## Preview

Convert a date string to a given format.
