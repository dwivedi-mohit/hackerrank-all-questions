# Error Log Extraction

## Metadata

- **ID:** 1486049
- **Type:** code
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Easy, Real-World
- **Skills:** Problem Solving (Basic)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates sorting, string manipulation, and data filtering concepts, ideal for junior-level roles. The problem requires implementing a function to extract and sort log entries with specific statuses from a 2D array of strings.

## Problem Statement

You are given a 2D array of strings logs, where each entry has exactly 4 fields:

	
- 
logs[i][0]: date in DD-MM-YYYY format
	
- 
logs[i][1]: time in HH:MM format
	
- 
logs[i][2]: status
	
- 
logs[i][3]: message

Implement a function extractErrorLogs that:

	
- Returns only the log entries whose status is "ERROR" or "CRITICAL"
	
- Sorts the filtered logs by arrival time in ascending order
	
- Arrival time is determined by the date and time fields together
	
- Preserves the original input order for logs that have the same arrival time (stable ordering)

 

Note: Do not use datetime modules.

 

Example

Suppose logs = [["01-01-2023", "14:00", "ERROR", "failed"], ["01-01-2023", "15:00", "INFO", "established"], ["01-01-2023", "01:30", "ERROR", "failed"]].

Output: [["01-01-2023", "01:30", "ERROR", "failed"], ["01-01-2023", "14:00", "ERROR", "failed"]].

Explanation:

	
		
			Log Index
			Date
			Time
			Status
			Message
		
	
	
		
			1
			01-01-2023
			01:30
			ERROR
			failed
		
		
			2
			01-01-2023
			14:00
			ERROR
			failed
		
		
			3
			01-01-2023
			15:00
			INFO
			established
		
	

 

The input contains two log entries with ERROR status. They are sorted in ascending order by the time they arrived.

 

Constraints

	
- 1 ≤ n (size of logs) ≤ 105

	
- 01 ≤ DD (day) ≤ 31
	
- 01 ≤ MM (month) ≤ 12
	
- 2000 ≤ YYYY (year) ≤ 3000
	
- 00 ≤ HH (hour) ≤ 23
	
- 00 ≤ MM (minutes)  ≤ 59

Test Case Input Format

The first line contains an integer, n, the number of elements in logs.

The next line contains an integer, 4, the number of columns in logs.

Each line i of the n subsequent lines (where 0 ≤ i < n) contains 4 strings describing logs[i].

## Sample Input/Output

## Preview

You are given a 2D array of strings logs, where each entry has exactly 4 field
