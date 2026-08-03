# Condensed List

## Metadata

- **ID:** 161023
- **Type:** code
- **Difficulty:** 9.444444444444445
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Lists, Easy, Data Structures, Algorithms, Problem Solving, Interviewer Guidelines
- **Skills:** Problem Solving (Basic)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates linked lists, data structures, and algorithms concepts, ideal for junior-level roles. The problem requires modifying a singly linked list to retain only the first occurrence of each value while removing duplicates.

## Problem Statement

You are given a singly linked list of integers.

 

Your task is to modify the list so that:

	
- You keep only the first occurrence of each value.
	
- You remove any node whose value has already appeared earlier in the list.
	
- You then return the head of the updated linked list.

 

Note:. A LinkedListNode has two attributes: data, an integer, and next, a reference to the next item in the list or the language equivalent of null at the tail.

 

Example 1

In the following list, the value 3 appears as a duplicate initially:

 

Remove the node at position 2 in the list above, 0-based indexing.

 

Example 2

List values in order are 3, 4, 3, 2, 6, 1, 2, 6.  The list looks like this:

 

From the first list in the diagram, remove:

	
- 
list[2] = 3
	
- 
list[6] = 2 
	
- 
list[7] = 6

 

Constraints

	
- 1 ≤ number of nodes n ≤ 105

	
- 0 ≤ LinkedListNode[i].val ≤ 1000

Test Case Input Format

The first line contains an integer n, the size of the array list.

Each of the next n lines contains an integer list[i] where 0 ≤ i < n.

## Sample Input/Output

## Preview

You are given a singly linked list of integers.
