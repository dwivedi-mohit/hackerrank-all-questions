# Combo Meal

- **Domain:** c
- **Difficulty:** Easy
- **Max Score:** 15
- **Success Ratio:** 0.9806009488666315
- **Total Submissions:** 9485
- **Solved Count:** 9301
- **URL:** https://www.hackerrank.com/challenges/combo-meal

## Problem Statement

A fast-food chain menu is selling a burger, a can of soda, and a combo meal containing a burger and a can of soda, at prices known to you. 

They have chosen the selling price for each item by first determining the *total cost* of making the individual items and then adding a *fixed* value to it, representing their *profit*. Assume that the cost of making a regular burger is fixed and the cost of making a regular soda is fixed.

For example, if the cost of making a regular burger is $206$, the cost of making a regular soda is $145$ and the fixed profit is $69$, then the fast-food chain will set selling prices as:

![image](https://s3.amazonaws.com/hr-assets/0/1517211598-f70d149c95-combomeal1.png)

Given the price of a burger, a can of soda and a combo meal on the menu, your task is to compute the fixed profit. 

Complete the function named `profit` which takes in three integers denoting selling price of a burger, a can of soda and a combo meal respectively, and returns an integer denoting the fixed profit. 


## Input Format

The first line contains $t$, the number of scenarios. The following lines describe the scenarios.  

Each scenario is described by a single line containing three space-separated integers, $b$, $s$ and $c$, denoting how much a burger, a can of soda and a combo meal cost respectively.


## Output Format

For each scenario, print a single line containing a single integer denoting the profit that the fast-food chain gets from every purchase. It is guaranteed that the answer is positive.  


## Constraints

- $1 \le t \le 100$  
- $3 \le c \le 2000$  
- $2 \le b, s < c$  
- It is guaranteed that the cost of making each item and the profit are positive.  


## Sample Input

3
275 214 420
6 9 11
199 199 255

## Sample Output

69
4
143

## Explanation

Case 1: Refer to the problem statement for this case.

Case 2: The selling price of a burger is , soda is , and combo meal is . If the cost to make a burger is , the cost to make a can of soda is  and the fixed profit is , you can verify the given selling prices as,  and . Hence, the answer is .

Case 3: The selling price of a burger is , soda is , and combo meal is . If the cost to make a burger is , the cost to make a can of soda is  and the fixed profit is , you can verify the given selling prices as,  and . Hence, the answer is .
