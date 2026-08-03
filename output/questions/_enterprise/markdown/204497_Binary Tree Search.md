# Binary Tree Search

## Metadata

- **ID:** 204497
- **Type:** code
- **Difficulty:** 9.722222222222221
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Data Structures, Binary Trees, Easy, Algorithms, Problem Solving, Interviewer Guidelines
- **Skills:** Problem Solving (Basic)
- **Languages:** c, ,, c, p, p, ,, c, p, p, 1

## Summary

This coding question evaluates binary search trees, algorithms, and problem-solving concepts, ideal for junior-level roles. The problem requires determining if specific values exist in a given binary search tree and returning appropriate results.

## Problem Statement

Determine if an element is present in a Binary Search Tree.

You are given a binary search tree (BST), where:

	
- Each node has a value.
	
- The left child contains a value less than its parent.
	
- The right child contains a value greater than or equal to its parent.

 

You are also given a list of query values.

 

For each query value, determine whether it exists in the BST:

	
- Return 1 if the value is found.
	
- Return 0 if it is not found.

 

Example

Suppose node values are [20, 10, 30, 8, 12, 25, 40, 6, 11, 13, 23] and the values to search for, val = [30, 10, 12, 15].

Output: [1, 1, 1, 0]

Provided code creates the tree structure based on node values. Nodes marked "Nil" have no value and are placeholders to make left and right clear.

	
- Search for val[0] = 30. Start from the root of a tree. 30 > 20: Search in the right subtree which has the root = 30. The item is found, return 1.
	
- Search for val[1] = 10. Start from the root of a tree. 10 < 20: Search in the left subtree which has the root = 10. The item is found, return 1.
	
- Search for val[2] = 12. Start from the root of a tree. 12 < 20: Search in the left subtree which has the root = 10. 12 > 10 : Search in the right subtree which has the root = 12. The item is found, return 1.
	
- Search for val[3] = 15. Start from the root of a tree. 15 < 20: Search in the left subtree which has the root = 10. 15 > 10 : Search in the right subtree which has the root = 12. 15 > 12: Search in the right subtree which has the root = 13. End of the tree and the item is not found, return 0.

 

Constraints

	
- 1 ≤ number of nodes, number of queries ≤ 105

	
- 1 ≤ val[i] ≤ 5 × 104

 

Test Case Input Format

 

The first line contains an integer, n, the number of elements in the tree.

Each of the next n lines contains an integer, the value of node[i], where 0 ≤ i ≤ n, and node[0] is the root.

The next line contains an integer, q, the number of queries

Each of the next q lines contains an integer to search for.

## Sample Input/Output

## Preview

Determine if an element is present in a Binary Search Tree.
