# Suspicious Activity From Logs

## Metadata

- **ID:** 749431
- **Type:** code
- **Difficulty:** 8.61111111111111
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Easy, Problem Solving, Strings, Arrays, Sorting, Hash Map
- **Skills:** Problem Solving (Basic)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates problem solving, hash maps, and string parsing concepts, ideal for junior-level roles. The task involves identifying suspicious users from log entries based on their transaction counts, ensuring accurate counting and sorting of user IDs.

## Problem Statement

You are given an array of log entries, where each entry represents a money transfer in the format:

"sender_user_id recipient_user_id amount"

 

Each log entry contains:

	
- sender_user_id – the user who sent the money
	
- recipient_user_id – the user who received the money
	
- amount – the transferred amount

All three fields are numeric, 1–9 digits long, contain only 0–9, and cannot start with zero.

 

Logs are not guaranteed to be in order.

 

Your task is to identify suspicious users—those who appear in at least threshold log entries, whether as a sender or recipient.

	
- If a user appears on both sides of the same transaction, it counts as one log entry for that user.
	
- Return all suspicious user IDs as strings, sorted in ascending numerical order.

 

Example

Suppose logs = ["88 99 200", "88 99 300", "99 32 100", " 12 12 15"] and threshold = 2.

Output: ["88", "99"]

	The transactions count for each user, regardless of role
	
		
			ID
			Transactions Count
		
	
	
		
			99
			3
		
		
			88
			2
		
		
			12
			1
		
		
			32
			1
		
	

 

 

Note:  In the last log entry, user 12 was on both sides of the transaction. This counts as only 1 transaction for user 12.

 

Constraints

	
- 1 ≤ n ≤ 105

	
- 1 ≤ threshold ≤ n

	
- The sender_user_id, recipient_user_id, and amount contain only characters in the range ascii['0'-'9'].
	
- The sender_user_id, recipient_user_id, and amount start with a non-zero digit.
	
- 0 < length of sender_user_id, recipient_user_id, amount ≤ 9.
	
- The result will contain at least one element.

Test Case Input Format

The first line contains the integer n.

The next n lines contain a string element of logs[].

The last line contains the integer threshold.

## Sample Input/Output

## Preview

You are given an array of log entries, where each entry represents a money tra
