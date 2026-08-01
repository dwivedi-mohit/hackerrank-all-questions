# Day 14: Scope

- **Domain:** regex
- **Difficulty:** Easy
- **Max Score:** 30
- **Success Ratio:** 0.9922435681384114
- **Total Submissions:** 222525
- **Solved Count:** 220799
- **URL:** https://www.hackerrank.com/challenges/30-scope

## Problem Statement

**Objective**	
Today we're discussing *scope*. Check out the [Tutorial](/challenges/30-scope/tutorial) tab for learning materials and an instructional video!

****

The *absolute difference* between two integers, $a$ and $b$, is written as $|a - b|$. The *maximum absolute difference* between two integers in a set of positive integers, $elements$, is the largest absolute difference between any two integers in $\text{__}elements$.

The *Difference* class is started for you in the editor. It has a private integer array ($elements$) for storing $N$ non-negative integers, and a public integer ($maximumDifference$) for storing the maximum absolute difference.

**Task**	
Complete the *Difference* class by writing the following:

- A class constructor that takes an array of integers as a parameter and saves it to the $\text{__}elements$ instance variable.
- A *computeDifference* method that finds the maximum absolute difference between any $2$ numbers in $\text{__}elements$ and stores it in the $maximumDifference$ instance variable. 

## Input Format

You are not responsible for reading any input from stdin. The locked *Solution* class in the editor reads in $2$ lines of input.  The first line contains $N$, the size of the elements array.  The second line has $N$ space-separated integers that describe the $\text{__}elements$ array.

## Output Format

You are not responsible for printing any output; the *Solution* class will print the value of the $maximumDifference$ instance variable.


## Constraints

- $1 \le N \le 10$  
- $1 \le \text{__}elements[i]\le 100$, where $ 0\le i \le N - 1 $ 

## Sample Input

STDIN   Function
-----   --------
3       __elements[] size N = 3
1 2 5   __elements = [1, 2, 5]

## Explanation

The scope of the  array and  integer is the entire class instance. The class constructor saves the argument passed to the constructor as the  instance variable (where the computeDifference method can access it).

To find the maximum difference, computeDifference checks each element in the array and finds the maximum difference between any  elements:

The maximum of these differences is , so it saves the value  as the  instance variable. The locked stub code in the editor then prints the value stored as , which is .
