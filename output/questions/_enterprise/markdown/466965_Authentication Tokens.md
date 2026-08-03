# Authentication Tokens

## Metadata

- **ID:** 466965
- **Type:** code
- **Difficulty:** 9.722222222222221
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Easy, Algorithms, Implementation, Problem Solving, Hash Map
- **Skills:** Problem Solving (Basic)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates problem solving, algorithms, and hash map concepts, ideal for junior-level roles. The problem requires determining the number of active authentication tokens after executing a series of commands with a specified expiration limit.

## Problem Statement

A system grants access to users through authentication tokens. Each token is generated with a fixed lifetime and becomes active immediately. Tokens can be renewed any number of times before they expire, but once expired, they can no longer be renewed.

 

The system processes authentication tokens using two commands: create and reset.

Given a list of commands and a global expiration limit (expiryLimit) determine how many tokens are still active after all commands have been executed.

 

Command format: [type, token_id, T]

	
- 
create type = 0; generates a token with id token_id at time T. Its expiry is set to T + expiryLimit

	
- 
reset type = 1; resets the expiry time of an existing token with id token_id to T + expiryLimit. If the token does not exist or has already expired, the command is ignored

 

Example

Suppose expiryLimit = 4

commands = [[0, 1, 1], [0, 2, 2], [1, 1, 5], [1, 2, 7]]

The latest time is T = 7, so we check which tokens remain active at that point.

Step-by-step:

	
- [0, 1, 1]: Create token 1 at time 1 → expires at 5
	
- [0, 2, 2]: Create token 2 at time 2 → expires at 6
	
- [1, 1, 5]: Reset token 1 at time 5 → new expiry at 9
	
- [1, 2, 7]: Reset token 2 at time 7 → ignored (token expired at 6)

At time T = 7, only token 1 is still active. Therefore, return 1.

 

Constraints

	
- The commands array is given sorted ascending by T (commands[i][2]).

	
- 1 ≤ expiryLimit < 108

	
- 1 ≤ n < 105

	
- 1 ≤ token_id < 108

	
- 1 ≤ T < 108

 

Test Case Input Format

The first line contains the integer, expiryLimit.

The second line contains the integer n, the number of elements in commands.

The third line contains the integer 3, the number of details required to describe each command.

Each line i of the n subsequent lines (where 0 ≤ i < n) contains three space-separated integers that represent commands[i].

## Sample Input/Output

## Preview

A system grants access to users through authentication tokens. Each token is g
