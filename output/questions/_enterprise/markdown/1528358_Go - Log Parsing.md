# Go - Log Parsing

## Metadata

- **ID:** 1528358
- **Type:** code
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Interviewer Guidelines, Hard, Go, Goroutines, File Handling
- **Skills:** Go (Advanced)
- **Languages:** g, o

## Summary

This coding question evaluates goroutines, file handling, and log processing concepts, ideal for senior-level roles. The task requires implementing a function to parse a log file and separate error messages from normal messages into different output files.

## Problem Statement

Write a program that processes a large log file containing many lines of text using goroutines. The log file has the following format:

 

Timestamp | Type | Message | IP

 

`2023-05-20 10:15:23 | INFO | Application started successfully | IP: 192.168.1.100
2023-05-20 12:30:45 | ERROR | Invalid input received | IP: 192.168.1.200
2023-05-20 15:18:12 | INFO | User logged in | IP: 192.168.1.50
2023-05-20 18:55:02 | WARNING | Low disk space detected | IP: 192.168.1.75`
```

 

 

Implement a function logParser that reads the log file and processes each line of text using these steps.

	
- Read a line of text from the log file.
	
- Parse the line of text to extract the message.
	
- Determine if the message is an error message.
	
- If it is an error message, write it to a separate log file for errors.
	
- If the message is not an error message, write it to a separate log file for normal messages.

 

In the function implementation, read from the channel, parse the line of text, and write the message to the appropriate log file. 

The function should take the name of the input file and the names of the output log files for errors and normal messages as input arguments.

Also, implement and use the function logWriter to write to the appropriate log file.

 

Example

inputFile contents

`2023-05-20 09:12:34 | INFO | Data backup completed successfully | IP: 192.168.1.10
2023-05-20 11:45:21 | ERROR | Connection timeout | IP: 192.168.1.20
2023-05-20 14:27:55 | WARNING | Disk space usage exceeded 90% | IP: 192.168.1.30
2023-05-20 17:59:12 | INFO | New user registered | IP: 192.168.1.40`
```

 

errorFile should contain 

`2023-05-20 11:45:21 | ERROR | Connection timeout | IP: 192.168.1.20`
```

 

The rest of the lines should be in normalFile.

 

`2023-05-20 09:12:34 | INFO | Data backup completed successfully | IP: 192.168.1.10
2023-05-20 14:27:55 | WARNING | Disk space usage exceeded 90% | IP: 192.168.1.30
2023-05-20 17:59:12 | INFO | New user registered | IP: 192.168.1.40`
```

 

Function Description

Complete the functions logParser and logWriter in the editor below. The functions must not return a value, i.e. void result. Normal and error log lines should be written to their corresponding files.

 

logParser has the following parameters:

    string inputFile: the name of the file that contains the log lines

    string errorFile: the name of the file where error log lines are written

    string normalFile: the name of the file where normal log lines are written

 

logWriter has the following parameters:

    ioWriter for the logFile

    channel for the appropriate lines to be written to the file

 

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

4
2023-05-20 10:15:23 | INFO | Application started successfully | IP: 192.168.1.100
2023-05-20 12:30:45 | ERROR | Invalid input received | IP: 192.168.1.200
2023-05-20 15:18:12 | INFO | User logged in | IP: 192.168.1.50
2023-05-20 18:55:02 | WARNING | Low disk space detected | IP: 192.168.1.75

```

Sample Output

ERROR:
2023-05-20 12:30:45 | ERROR | Invalid input received | IP: 192.168.1.200

NORMAL:
2023-05-20 10:15:23 | INFO | Application started successfully | IP: 192.168.1.100
2023-05-20 15:18:12 | INFO | User logged in | IP: 192.168.1.50
2023-05-20 18:55:02 | WARNING | Low disk space detected | IP: 192.168.1.75

```

Sample Case 1

Sample Input For Custom Testing

4
2023-05-20 08:30:15 | ERROR | Database connection failed | IP: 192.168.1.5
2023-05-20 10:45:55 | ERROR | File not found: "document.pdf" | IP: 192.168.1.15
2023-05-20 13:20:30 | ERROR | Invalid username or password | IP: 192.168.1.25
2023-05-20 16:05:42 | ERROR | Internal server error | IP: 192.168.1.35

```

Sample Output

ERROR:
2023-05-20 08:30:15 | ERROR | Database connection failed | IP: 192.168.1.5
2023-05-20 10:45:55 | ERROR | File not found: "document.pdf" | IP: 192.168.1.15
2023-05-20 13:20:30 | ERROR | Invalid username or password | IP: 192.168.1.25
2023-05-20 16:05:42 | ERROR | Internal server error | IP: 192.168.1.35

NORMAL:
```

## Sample Input/Output

## Preview

Write a program that processes a large log file containing many lines of text
