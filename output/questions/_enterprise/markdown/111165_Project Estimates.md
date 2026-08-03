# Project Estimates

## Metadata

- **ID:** 111165
- **Type:** code
- **Difficulty:** 9.722222222222221
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Binary Search, Easy, Data Structures, Algorithms, Arrays, Problem Solving, Theme:  Finance
- **Skills:** Problem Solving (Basic)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates binary search, data structures, and algorithms concepts, ideal for junior-level roles. The problem requires determining the number of distinct pairs of project bid costs with an absolute difference equal to a specified target.

## Problem Statement

You are given a list of project bid costs and a target value. Your task is to determine how many distinct pairs of bids have an absolute difference equal to the target.

 

A pair (x, y) is counted if:

	
- |x - y| = target

Each pair must be unique — two pairs are distinct if they differ in at least one of the values.

 

Example 1

Suppose  there are n = 5 projects, projectCosts = [1, 5, 3, 4, 2], and target= 2.

Output: 3

There are three pairs with a difference of target = 2: (1, 3), (5, 3), and (4, 2).

 

Example 2

Suppose  there are n = 10 projects, projectCosts = [363374326, 364147530, 61825163, 107306571, 128124602, 139946991, 428047635, 491595254, 879792181, 106926279], and target= 1

Output: 0

There are no pairs with a difference of target = 1.

 

Constraints

	
- 5 ≤ n ≤ 105

	
- 0 < projectCosts[i] ≤ 2 × 109

	
- Each projectCosts[i] is distinct, i.e., unique within projectCosts.

	
- 1 ≤ target ≤ 109

Test Case Input Format

The first line contains an integer n.

The next n lines contain an integer element of projectCosts.

The next line contains an integer target.

## Sample Input/Output

## Preview

You are given a list of project bid costs and a target value. Your task is to
