# Go: Merge Readers

## Metadata

- **ID:** 929538
- **Type:** code
- **Difficulty:** 8.055555555555555
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Easy, Strings, Go
- **Skills:** Go (Basic)
- **Languages:** g, o

## Summary

This coding question evaluates string manipulation, input/output handling, and function implementation concepts, ideal for junior-level roles. The problem requires merging two strings by alternating their characters while handling different lengths.

## Problem Statement

Implement a function that takes two input readers (io.Reader), each containing a string, and merges them by alternating characters.

Read one character byte at a time from each reader alternately and push these characters to the resulting string's reader. If the strings have different lengths, trim the longer string to match the length of the shorter one.

 

Example

r1 reads "ABCDE" from STDIN

r2 reads "abcde" from STDIN

 

The resulting string "AaBbCcDdEe".

 

Function Description

Complete the function MergeReaders in the editor with the following parameters:

r1:  an io.Reader

r2:  an io.Reader

 

Returns

    io.Reader and error interfaces

 

Constraints

	
- 1 ≤ length of string ≤ 2000

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

Each line contains a string read by r1 and r2.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

abc
ABC

```

Sample Output

aAbBcC
```

Explanation

The readers are merged, alternately taking characters from r1 and r2.

Sample Case 1

Sample Input For Custom Testing

Hello
World!!!
```

Sample Output

HWeolrllod
```

Explanation

The second string is cropped to 5 characters, "World", and the readers are merged.

## Sample Input/Output

## Preview

Implement a function that takes two input readers (io.Reader), each containing
