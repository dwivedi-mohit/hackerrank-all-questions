# Linked Lists: Detect a Cycle

- **Domain:** algorithms
- **Difficulty:** Easy
- **Max Score:** 25
- **Success Ratio:** 0.9741815711155131
- **Total Submissions:** 104499
- **Solved Count:** 101801
- **URL:** https://www.hackerrank.com/challenges/ctci-linked-list-cycle

## Problem Statement

A linked list is said to contain a *cycle* if any node is visited more than once while traversing the list. For example, in the following graph there is a cycle formed when node $5$ points back to node $3$.  

![image](https://s3.amazonaws.com/hr-assets/0/1527604250-43ac8fbfaf-filtrationExample.png)

**Function Description**

Complete the function *has_cycle* in the editor below. It must return a boolean *true* if the graph contains a cycle, or *false*.  

has_cycle has the following parameter(s):

- *head*: a pointer to a *Node* object that points to the head of a linked list.

**Returns**   

- *boolean:* True if there is a cycle, False if there is not  


**Note:** If the list is empty, $head$ will be *null*.

## Input Format

There is no input for this challenge.  A random linked list is generated at runtime and passed to your function.

## Constraints

- $0 \le \textit{ list size } \le 100$

## Sample Input

The following linked lists are passed as arguments to your function:

## Sample Output

1

## Explanation

- The first list has no cycle, so we return false and the hidden code checker prints  to stdout.

- The second list has a cycle, so we return true and the hidden code checker prints  to stdout.
