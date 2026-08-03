# Valid Email Addresses

## Metadata

- **ID:** 338956
- **Type:** code
- **Difficulty:** 8.88888888888889
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Regex, Easy, Problem Solving
- **Skills:** Problem Solving (Basic)
- **Languages:** c, p, p, ,, c, p, p, 1, 4, ,

## Summary

This coding question evaluates regular expressions, problem solving, and validation concepts, ideal for junior-level roles. The task requires writing a RegEx to validate HackerRank email addresses based on specific formatting rules.

## Problem Statement

Write a RegEx to validate email addresses.

A valid HackerRank email address must follow this format:

user@hackerrank.com

The user portion must satisfy all of the following rules:

	
- Starts with 1 to 6 lowercase letters (a–z)
	
- May include an optional underscore (_) appearing at most once
	
- May include 0 to 4 digits (0–9) after the letters and optional underscore

Your task is to write the regular expression that matches valid email addresses according to these rules.

 

Example

Inputs have the number of strings in the first row, then one string per row.

Input

5
robin@hackerrank.com
robin_@hackerrank.com
robin_0@hackerrank.com
robin0_@hackerrank.com
robin@gmail.com

```

Output

True
True
True
False
False

```

Stub code tests each string with your regex and prints the result. The last two email addresses do not match. "robin0_@hackerrank.com" has a digit before the underline, and "robin@gmail.com" has the wrong domain.

 

Constraints

	
- 1 ≤ query ≤ 103

	
- 1 ≤ string length ≤ 103

## Sample Input/Output

## Preview

Write a RegEx to validate email addresses.
