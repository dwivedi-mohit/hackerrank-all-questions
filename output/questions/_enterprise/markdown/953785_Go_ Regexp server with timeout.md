# Go: Regexp server with timeout

## Metadata

- **ID:** 953785
- **Type:** code
- **Difficulty:** 7.777777777777778
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Medium, Regex, Channels, Go
- **Skills:** Go (Intermediate)
- **Languages:** g, o

## Summary

This coding question evaluates regular expressions, concurrency in Go, and server communication concepts, ideal for mid-level roles. The problem requires implementing a server that matches strings against regex patterns with timeout handling.

## Problem Statement

Implement a server that matches a regular expression with a string, each provided by a separate server. The server should return a Boolean string result. The servers calculate the expected response time based on a given timeout factor multiplied by the string length. If the request exceeds the time specified in the maxDelay variable, an error should be recorded in timeoutErr.

 

The main function accepts two string arrays and two integers:

	
- 
stringsData contains strings to be sent to the server
	
- 
regexpData contains regular expressions to be sent to the server
	
- 
steps denotes the number of results to be requested from the server
	
- 
timeoutFactor denotes the timeout period in milliseconds per letter (not passed to your function)

The server should accept five arguments as described in the example below:

 

If the main function receives ["abc", "cde", "123abc456", "xyz"] as stringsData, [".*b.*", ".*f.*", "^[0-9]*", ".*"] as regexpData, 3 as steps, and 50 milliseconds per letter as timeoutFactor, the server should return ['true', 'false', 'true'] to the main function via the channel received as the first argument. Note that only 3 matches are performed.

 

Function Description

Complete the function ServerWithTimeout in the editor with the following parameters:

	
- 
matchChan chan bool: the channel used to return match results to the main function
	
- 
errChan chan error: the channel used to return errors to the main function in case of timeouts
	
- 
requestStrChan chan bool: the channel used to request strings from the strings server
	
- 
resultStrChan chan string: the channel that receives results from the strings server
	
- 
requestRegChan chan bool: the channel used to request regular expressions from the regexp server
	
- 
resultRegChan chan *regexp.Regexp: the channel that receives results from the regexp server

Returns

The function should not return anything, as all results will be returned asynchronously via channels.

 

Constraints

	
- 1 ≤ the total number of requests ≤ 50

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains an integer, n, the number of elements in stringsData.

Each line i of the n subsequent lines (where 0 ≤ i < n) contains a string, stringsData[i].

The next line contains an integer, n, the number of elements in regexpsData.

Each line i of the n subsequent lines (where 0 ≤ i < n) contains a string, regexpsData[i].

The next line contains an integer, steps, the number of results that will be requested from the server.

The next line contains an integer, ratio, the number of milliseconds the servers can spend on every letter of an incoming string.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

STDIN        Function    
-----        --------
3       →    stringsData[] size n = 3
abc     →    stringsData = ['abc', 'def', '123']
def
123
3       →    regexpData[] size n = 3
.*      →    regexpData = ['.*', 'd+', '[A-Z]+']
d+
[A-Z]+
3       →    steps = 3
50      →    timeoutFactor = 50
```

Sample Output

true
true
false

```

Explanation

There are three string/pattern pairs, and steps = 3.  Strings and patterns, aligned by index, are ('abc', '.*'), ('def', 'd+'), and ('123', '[A-Z]+').  Nothing causes a timeout because the maximum delay is caused by 50 * len('[A-Z]+') = 50 * 6 = 300, which is less than maxDelay.

Sample Case 1

Sample Input For Custom Testing

3
short
longer
a very long string
3
.*
.*
.*
3
50
```

Sample Output

true
true
Timeout error

```

Explanation

The first two elements match, but the last string causes a delay of more than maxDelay, which causes ServerWithTimeout to send an error to the main function.

## Sample Input/Output

## Preview

Implement a server that matches a regular expression with a string, each provi
