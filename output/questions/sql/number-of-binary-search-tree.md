# Number of Binary Search Tree

- **Domain:** sql
- **Difficulty:** Medium
- **Max Score:** 20
- **Success Ratio:** 0.8338557993730408
- **Total Submissions:** 1276
- **Solved Count:** 1064
- **URL:** https://www.hackerrank.com/challenges/number-of-binary-search-tree

## Problem Statement

A binary tree is a tree which is characterized by any of the following properties:  

1. It can be empty (null).
2. It can contain a root node which contain some value and two subtree, left subtree and right subtree, which are also binary tree.

A binary tree is a binary search tree (BST) if all the non-empty nodes follows both two properties:

  1. If node has a left subtree, then all the values in its left subtree are smaller than the value of the current node.
  2. If node has a right subtree, then all the value in its right subtree are greater than the value of the current node.

You are given _N_ nodes, each having unique value ranging from `[1, N]`, how many different binary search tree can be created using all of them.

**Input**  
First line will contain an integer, _T_, number of test cases. Then _T_ lines follow, where each line represent a test case. Each test case consists a single integer, _N_, where _N_ is the number of nodes in the binary search tree. 

**Output**  
For each test case, find the number of different binary search trees that can be created using these nodes. Print the answer modulo (10<sup>8</sup>+7).

**Constraints**  
1 <= _T_ <= 1000   
1 <= _N_ <= 1000  

**Sample Input**  

    5
    1
    2
    3
    4
    100

**Sample Output**  

    1
    2
    5
    14
    25666077



**Explanation**  
_Test Case #1:_ We have only one tree.

    1

_Test Case #2:_ Two trees can be created using two nodes.

    1          2
     \        /
      2      1

_Test Case #3:_

    1          1         2         3        3
     \          \       / \       /	       /
      2          3     1   3     1        2
       \        /                 \      /
        3      2                   2    1

## Constraints

1 <= T <= 1000

1 <= N <= 1000

## Sample Input

1
2
3
4
100

## Sample Output

2
5
14
25666077

## Explanation

Test Case #1: We have only one tree.

1

Test Case #2: Two trees can be created using two nodes.

1          2
 \        /
  2      1

Test Case #3:

1          1         2         3        3
 \          \       / \       /        /
  2          3     1   3     1        2
   \        /                 \      /
    3      2                   2    1
