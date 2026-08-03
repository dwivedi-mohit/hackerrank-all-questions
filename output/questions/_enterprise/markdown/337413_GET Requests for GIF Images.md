# GET Requests for GIF Images

## Metadata

- **ID:** 337413
- **Type:** approx
- **Difficulty:** 8.88888888888889
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** File Manipulation, Scripting, Regex, Medium, Problem Solving, Back-End Development
- **Skills:** Problem Solving (Basic)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This approximate solution question evaluates file manipulation, regex, and problem-solving concepts, ideal for junior-level roles. The problem requires generating a file containing unique GIF filenames from log records based on specific GET request criteria and response codes.

## Problem Statement

Find the names of GIF files satisfying some criteria in request logs.

You are given a log file with a list of responses, some of the records in the log file may contain filenames.

Generate a new file containing the unique names of all gif files that were requested via GET and that had a response code of 200.

A sample and the structure of the text file containing the responses are given below.

 

Sample log record:

burger.letters.com - - [01/Jul/1995:00:00:12 -0400] "GET /shuttle/countdown/video/livevideo.GIF HTTP/1.0" 200 0
burger.letters.com - - [01/Jul/1995:00:00:12 -0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 304 0

```

 

Log File Structure:

	
		
		
		
		
		
		
		
	
	
		
			Hostname
			-
			-
			Timestamp
			Request
			HTTP Response Code
			Bytes
		
		
			burger.letters.com
			-
			-
			[01/Jul/1995:00:00:12 -0400]
			"GET /shuttle/countdown/video/livevideo.GIF HTTP/1.0"
			200
			0
		
		
			Hostname of the host that made the request
			-
			-
			Timestamp Format
			The request is enclosed in quotes
			The HTTP response code.
			 
		
	

Missing column values are denoted by a hyphen (i.e. -).
Timestamp Format: DD: day of the month, mmm: name of the month, YYYY: year, HH:MM:SS - 24-hour time format, -0400 is the time zone

 

Given a filename that denotes a text file in the current working directory. Create an output file with the name "gifs_" prefixed to the filename (gifs_filename) which stores the unique gif filenames that match the requirements.

 

Example: filename = "hosts_access_log_00.txt", process the records in hosts_access_log_00.txt and create an output file named gifs_hosts_access_log_00.txt. 

 

Write the name of a GIF file (without its path) to the output file, for each of the records in the input file which satisfy the below:

	
- The GIF file was requested by a GET request.
	
- The record has an HTTP response code of 200.

 

Note: 
The output file has to be written to the current directory.
The line order in the output file does not matter.

There must not be any duplicates (if duplicates exist, you will receive only 70% of the score).

 

Constraints

	
- The log file contains no more than 2 × 105 records.

 

 DO NOT REMOVE THIS LINE-->

Input Format for Custom Testing

Input from stdin will be processed as follows and passed to the function.

 

The only line contains a string filename, the name of the log file.

gifs_filename (where filename is the file name string) to store the file names of certain GIF files (i.e., file names with .GIF or .gif extensions). Each line of the created file must contain the distinct name of a GIF file (i.e., the file name and extension, not including the file path) that was requested by a GET request and has an HTTP response code of 200 for a record in filename. The line order in the output file does not matter, but there must not be any duplicates. If your output has duplicates, you will receive only 70% of the full score. 

-->

Sample Case 0

Sample Input 0

hosts_access_log_00.txt
```

Sample Output 0

Given filename = "hosts_access_log_00.txt", process the records in hosts_access_log_00.txt and create an output file named gifs_hosts_access_log_00.txt that contains the following rows:

livevideo.GIF
count.gif
NASA-logosmall.gif
KSC-logosmall.gif

```

Explanation 0

The log file hosts_access_log_00.txt contains the following log records:

unicomp6.unicomp.net - - [01/Jul/1995:00:00:06 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985
burger.letters.com - - [01/Jul/1995:00:00:11 -0400] "GET /shuttle/countdown/liftoff.html HTTP/1.0" 304 0
burger.letters.com - - [01/Jul/1995:00:00:12 -0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 304 0
burger.letters.com - - [01/Jul/1995:00:00:12 -0400] "GET /shuttle/countdown/video/livevideo.GIF HTTP/1.0" 200 0
d104.aa.net - - [01/Jul/1995:00:00:13 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985
unicomp6.unicomp.net - - [01/Jul/1995:00:00:14 -0400] "GET /shuttle/countdown/count.gif HTTP/1.0" 200 40310
unicomp6.unicomp.net - - [01/Jul/1995:00:00:14 -0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 200 786
unicomp6.unicomp.net - - [01/Jul/1995:00:00:14 -0400] "GET /images/KSC-logosmall.gif HTTP/1.0" 200 1204
d104.aa.net - - [01/Jul/1995:00:00:15 -0400] "GET /shuttle/countdown/count.gif HTTP/1.0" 200 40310
d104.aa.net - - [01/Jul/1995:00:00:15 -0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 200 786
```

A review of the data above:

	
- 
	
The fourth log record:

	
burger.letters.com - - [01/Jul/1995:00:00:12 -0400] "GET /shuttle/countdown/video/livevideo.GIF HTTP/1.0" 200 0
```

	
A GET request requested a file named livevide.GIF and the HTTP response code was 200.

	
	
- 
	
The sixth log record:

	
unicomp6.unicomp.net - - [01/Jul/1995:00:00:14 -0400] "GET /shuttle/countdown/count.gif HTTP/1.0" 200 40310
```

	
And the ninth log record:

	
d104.aa.net - - [01/Jul/1995:00:00:15 -0400] "GET /shuttle/countdown/count.gif HTTP/1.0" 200 40310
```

	
In both records, a GET request requested a file named count.gif and the HTTP response code was 200.

	
	
- 
	
The seventh log record:

	
unicomp6.unicomp.net - - [01/Jul/1995:00:00:14 -0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 200 786
```

	
A GET request requested a file named NASA-logosmall.gif and the HTTP response code was 200.

	
	
- 
	
The eighth log record:

	
unicomp6.unicomp.net - - [01/Jul/1995:00:00:14 -0400] "GET /images/KSC-logosmall.gif HTTP/1.0" 200 1204
```

	
A GET request requested a file named KSC-logosmall.gif and the HTTP response code was 200.

	

Append the four distinct GIF file names satisfying our conditions to the output file.

## Sample Input/Output

## Preview

Find the names of GIF files satisfying some criteria in request logs.
