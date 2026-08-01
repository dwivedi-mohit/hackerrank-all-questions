# Utopian Tree

- **Domain:** mathematics
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.9797713779755486
- **Total Submissions:** 440465
- **Solved Count:** 431555
- **URL:** https://www.hackerrank.com/challenges/utopian-tree

## Problem Statement

The Utopian Tree goes through _2_ cycles of growth every year. Each spring, it _doubles_ in height. Each summer, its height increases by _1_ meter.

A Utopian Tree sapling with a height of *1* meter is planted at the onset of spring. How tall will the tree be after $n$ growth cycles?

For example, if the number of growth cycles is $n = 5$, the calculations are as follows:

    Period  Height
    0          1
    1          2
    2          3
    3          6
    4          7
    5          14
    
**Function Description**

Complete the *utopianTree* function in the editor below.   

utopianTree has the following parameter(s):

- *int n*:  the number of growth cycles to simulate  

**Returns**  

- *int:* the height of the tree after the given number of cycles  


## Input Format

The first line contains an integer, $t$, the number of test cases.	
$t$ subsequent lines each contain an integer, $n$, the number of cycles for that test case.



## Constraints

$1 \le t \le 10$  
$0 \le n \le 60$

## Sample Input

0
1
4

## Sample Output

2
7

## Explanation

There are 3 test cases.

In the first case (), the initial height () of the tree remains unchanged.

In the second case (), the tree doubles in height and is  meters tall after the spring cycle.

In the third case (), the tree doubles its height in spring (, ), then grows a meter in summer (, ), then doubles after the next spring (, ), and grows another meter after summer (, ). Thus, at the end of 4 cycles, its height is  meters.
