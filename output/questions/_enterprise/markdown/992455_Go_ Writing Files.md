# Go: Writing Files

## Metadata

- **ID:** 992455
- **Type:** code
- **Difficulty:** 8.055555555555555
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Medium, File Handling, Go
- **Skills:** Go (Intermediate)
- **Languages:** g, o

## Summary

This coding question evaluates file handling, Go programming, and memory management concepts, ideal for mid-level roles. The problem requires developing a function to write strings from an array to a file with minimal memory allocations.

## Problem Statement

Given an array of strings, develop a function that:

	
- Creates a file.
	
- Sends nil to errChannel to signal the main function that it can start sending data.
	
- Receives strings from an array, converts them to byte arrays, and writes them to the file.
	
- This should be done with minimal memory allocations.

 

The file name is stored in a global variable called filename.

 

Example

inputArray = ["Lorem ", "ipsum ", "dolor ", "sit ", "amet"] 

 

The resulting file should contain "Lorem ipsum dolor sit amet".

 

Function Description

Complete the function writeToFile in the editor with the following parameters:

    bytesChannel chan []byte: a channel for receiving bytes from the main function for writing them to the file.

    doneChannel chan bool: a channel for receiving the signal from the main function that all data is sent.

    errChannel chan error: a channel through errors will be sent to the main function (including nil).

 

Returns

    void: no return value is expected

 

Constraints

	
- The length of the input array does not exceed 1000.

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains an integer, m, denoting the size of the byte array which should be read from the file at every iteration.

The second line contains an integer, n, denoting m + the number of bytes which should be skipped after reading at every iteration.

The third line contains a string inputString denoting the contents of the file.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

2
Hello
World

```

Sample Output

HelloWorld

```

Explanation

2 strings are sent to the writeToFile function, which writes them to the file, then the main function will read them from this file, where they get joined.

Sample Case 1

Sample Input For Custom Testing

5
Lorem
 ipsum
 dolor
 sit
 amet

```

Sample Output

Lorem ipsum dolor sit amet
```

Explanation

5 strings are sent to the writeToFile function, which writes them to the file. The main function then reads them from this file, where they get joined.

## Sample Input/Output

## Preview

Given an array of strings, develop a function that:
