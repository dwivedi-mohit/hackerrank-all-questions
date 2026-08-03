# Sign-in Sign-out Logs

## Metadata

- **ID:** 749426
- **Type:** code
- **Difficulty:** 8.61111111111111
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Easy, Problem Solving, Theme:  E-commerce, Hash Map, Arrays, Strings, Sorting, Interviewer Guidelines
- **Skills:** Problem Solving (Basic)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates problem solving, hash maps, and sorting concepts, ideal for junior-level roles. The task is to identify users who signed out within a specified time span after signing in, based on application log entries.

## Problem Statement

You are given application log entries in the format: "user_id timestamp action"

 

Where:

	
- 
user_id and timestamp are numeric strings
	
- 
action is either "sign-in" or "sign-out"

You are also given an integer maxSpan.

Your task is to find all users who:

	
- Have both a sign-in and a sign-out
	
- Signed out within maxSpan seconds of signing in.

Return:

	
- A list of user IDs (as strings) that meet the condition
	
- Sorted in ascending numerical order

Notes:

	
- Log entries are unordered
	
- Each user signs in at most once
	
- Users who do not sign out are ignored

 

Example

Suppose there are n = 7 entries, logs = ["30 99 sign-in", "30 105 sign-out", "12 100 sign-in", "20 80 sign-in", "12 120 sign-out", "20 101 sign-out", "21 110 sign-in"], and maxSpan = 20.

Output: ["12", "30"]

Explanation:

	
- Users with IDs 30 and 12 were not signed in for more than maxSpan = 20 seconds.
	
- User 21 has not signed out, and user 20 was signed in for too long.
	
- The return array contains IDs as strings, sorted in numerical order.

	Time delta calculations
	
		
			ID
			Sign in
			Sign out
			Time delta
		
	
	
		
			30
			99
			105
			6
		
		
			12
			100
			120
			20
		
		
			20
			80
			101
			21
		
		
			21
			110
			 
			 
		
	

 

Constraints

	
- 1 ≤ n ≤ 105

	
- 1 ≤ maxSpan ≤ 109

	
- 0 < timestamp ≤ 109

	
- Each user_id's sign-in timestamp < sign-out timestamp

	
- Each user signs in for only 1 session. 
	
- The results will contain at least one element. DO NOT REMOVE THIS LINE-->

Test Case Input Format

The first line contains the integer n.

The next n lines contain a string element of logs[].

The last line contains the integer maxSpan.

## Sample Input/Output

## Preview

You are given application log entries in the format: "user_id timestamp action
