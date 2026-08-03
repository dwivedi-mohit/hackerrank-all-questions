# Keyboard

## Metadata

- **ID:** 313922
- **Type:** code
- **Difficulty:** 10.0
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Easy, Algorithms, Problem Solving, Arrays, Interviewer Guidelines
- **Skills:** Problem Solving (Basic)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates problem solving, algorithms, and string manipulation concepts, ideal for junior-level roles. The problem requires calculating the minimum time needed to type a string of digits on a custom numeric keypad layout.

## Problem Statement

Given a string of digits and a layout for a numeric keypad, calculate the minimum amount of time needed to type the string.

You are given a 9-character string keypad representing a scrambled numeric keypad layout.

 

Each character is a digit from 1 to 9, arranged in a 3×3 grid in row-major order.

 

You must compute the minimum time required to type a digit string s, following these rules:

	
- Moving to the first key you press takes 0 seconds
	
- Pressing a key where your finger already is takes 0 seconds
	
- Moving to an adjacent key (including diagonally) takes 1 second
	
- Moving to a non-adjacent key requires multiple adjacent moves

Using this keypad layout, determine the fastest possible typing time for the string s and return that time.

 

This diagram depicts the minimum amount of time it takes to move from the current location to all other locations on the keypad.

Example

Suppose s = "423692" and keypad = "923857614"

Output: 8

Explanation:

The keypad looks like this:

 

Calculate the time it takes to type s = "423692" as follows:

	
- 4: Start here, so it takes 0 seconds.
	
- 2: It takes 2 seconds to move from 4 → 2
	
- 3: It takes 1 second to move from 2 → 3
	
- 6: It takes 2 seconds to move from 3 → 6
	
- 9: It takes 2 seconds to move from 6 → 9
	
- 2: It takes 1 second to move from 9 → 2

 

Constraints

	
- 1 ≤ length of s ≤ 105

	
- length of keypad = 9
	
- 
keypad[i] is in the range [1-9]

Test Case Input Format

The first line contains the string s.

The next line contains the string keypad.

## Sample Input/Output

## Preview

Given a string of digits and a layout for a numeric keypad, calculate the mini
