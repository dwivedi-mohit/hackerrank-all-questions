# Hosts and the Total Number of Requests

## Metadata

- **ID:** 336895
- **Type:** approx
- **Difficulty:** 9.166666666666668
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** File Manipulation, Scripting, Medium, Problem Solving
- **Skills:** Problem Solving (Basic)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This approximate solution question evaluates file manipulation, scripting, and problem-solving concepts, ideal for junior-level roles. The problem requires consolidating HTTP request logs from a file and summarizing the number of requests per host in an output file.

## Problem Statement

Consolidate records from a file and output them to another file.

 

In this challenge, write a program to analyze a log file and summarize the results.  Given a text file of an http requests log, list the number of requests from each host.  Output should be directed to a file as described in the Program Description below.

 

The format of the log file, a text file with a .txt extension, follows.  Each line contains a single log record with the following columns (in order):

	
- The hostname of the host making the request.
	
- This column's values are missing and were replaced by a hyphen.
	
- This column's values are missing and were replaced by a hyphen.
	
- A timestamp enclosed in square brackets following the format [DD/mmm/YYYY:HH:MM:SS -0400], where DD is the day of the month, mmm is the name of the month, YYYY is the year, HH:MM:SS is the time in 24-hour format, and -0400 is the time zone.
	
- The request, enclosed in quotes (e.g., "GET /images/NASA-logosmall.gif HTTP/1.0").
	
- The HTTP response code.
	
- The total number of bytes sent in the response.

 

Example log file entry

Given the following log record:

	unicomp6.unicomp.net - - [01/Jul/1995:00:00:06 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985
```

We can label each column in the record like so:

	
		
		
		
		
		
		
		
	
	
		
			Hostname
			-
			-
			Timestamp
			Request
			HTTP Response Code
			Bytes
		
		
			unicomp6.unicomp.net
			-
			-
			[01/Jul/1995:00:00:06 -0400]
			"GET /shuttle/countdown/ HTTP/1.0"
			200
			3985
		
	

Function Description 

Your function must create a unique list of hostnames with their number of requests and output to a file named records_filename where filename is replaced with the input filename. Each hostname should be followed by a space, the number of requests, and a newline. Order does not matter.

 

Constraints

	
- The log file has a maximum of 2 × 105 lines of records.

 

 DO NOT REMOVE THIS LINE-->

Input Format

 

There is one line of input which contains the string filename read from STDIN.

Sample Case 0

Sample Input 0

hosts_access_log_00.txt
```

Sample Output 0

Given filename = "hosts_access_log_00.txt", process the records in hosts_access_log_00.txt and create an output file named records_hosts_access_log_00.txt which contains the following rows in any order:

burger.letters.com 3
d104.aa.net 3
unicomp6.unicomp.net 4
```

Explanation 0

The log file hosts_access_log_00.txt contains the following log records:

unicomp6.unicomp.net - - [01/Jul/1995:00:00:06 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985
burger.letters.com - - [01/Jul/1995:00:00:11 -0400] "GET /shuttle/countdown/liftoff.html HTTP/1.0" 304 0
burger.letters.com - - [01/Jul/1995:00:00:12 -0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 304 0
burger.letters.com - - [01/Jul/1995:00:00:12 -0400] "GET /shuttle/countdown/video/livevideo.gif HTTP/1.0" 200 0
d104.aa.net - - [01/Jul/1995:00:00:13 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985
unicomp6.unicomp.net - - [01/Jul/1995:00:00:14 -0400] "GET /shuttle/countdown/count.gif HTTP/1.0" 200 40310
unicomp6.unicomp.net - - [01/Jul/1995:00:00:14 -0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 200 786
unicomp6.unicomp.net - - [01/Jul/1995:00:00:14 -0400] "GET /images/KSC-logosmall.gif HTTP/1.0" 200 1204
d104.aa.net - - [01/Jul/1995:00:00:15 -0400] "GET /shuttle/countdown/count.gif HTTP/1.0" 200 40310
d104.aa.net - - [01/Jul/1995:00:00:15 -0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 200 786
```

When the data is consolidated, it confirms the following:

	
- The host unicomp6.unicomp.net made 4 requests.
	
- The host burger.letters.com made 3 requests.
	
- The host d104.aa.net made 3 requests.

## Sample Input/Output

## Preview

Consolidate records from a file and output them to another file.
