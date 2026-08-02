# Matchstick Warehouse Thief

- **Domain:** ai
- **Difficulty:** Easy
- **Max Score:** 100
- **Success Ratio:** 0.5
- **Total Submissions:** 10
- **Solved Count:** 5
- **URL:** https://www.hackerrank.com/challenges/matchstick-warehouse-thief

## Problem Statement

A thief broke into a matchstick warehouse and wants to steal as many matchsticks as possible. The warehouse has $c$ crates, and each crate $i$ contains $b_{i}$ matchboxes with exactly $m_{i}$ matchsticks per box. The matchboxes are of uniform size, but the number of matchsticks per box can vary from crate to crate. The thief's bag can hold no more than $n$ matchboxes. 

Given $n$ and the description of each crate's contents, find and print the maximum number of total *matchsticks* that the thief can steal by optimally choosing which boxes to take.

## Input Format

The first line contains two space-separated integers describing the respective values of $n$ (the number of matchboxes the thief can carry) and $c$ (the number of crates in the warehouse).		
Each line $i$ of the $c$ subsequent lines contains a pair of space-separated integers describing the respective values of $b_{i}$ (the number of matchboxes in crate $i$) and $m_{i}$ (the number of matchsticks per box in crate $i$). 

## Output Format

Print a single integer denoting the maximum number of *matchsticks* that the thief can escape with.

## Constraints

- $1 \leq n \leq 2 \times 10^{8}$  
- $1 \leq c \leq 20$  
- $1 \leq b_{i} \leq 10^{8}$  
- $1 \leq m_{i} \leq 10$

## Sample Input

3 3
1 3
2 2
3 1

## Sample Output

7

## Explanation

The thief can carry a maximum of  matchboxes selected from the warehouse's  crates. We maximize the number of stolen matchsticks by taking the  thickly outlined matchboxes in the diagram below:

We then calculate and print the maximum number of stolen matchsticks, which is .

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
