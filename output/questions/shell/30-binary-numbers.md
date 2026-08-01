# Day 10: Binary Numbers

- **Domain:** shell
- **Difficulty:** Easy
- **Max Score:** 30
- **Success Ratio:** 0.9523041672633539
- **Total Submissions:** 349150
- **Solved Count:** 332497
- **URL:** https://www.hackerrank.com/challenges/30-binary-numbers

## Problem Statement

**Objective**	 
Today, we're working with binary numbers. Check out the [Tutorial](/challenges/30-binary-numbers/tutorial) tab for learning materials and an instructional video!	

**Task**	
Given a base-$10$ integer, $n$, convert it to binary (base-$2$). Then find and print the base-$10$ integer denoting the maximum number of consecutive $1$'s in $n$'s binary representation. When working with different bases, it is common to show the base as a subscript.   

**Example**  
$n = 125$  

The binary representation of $125_{10}$ is $1111101_2$.  In base $10$, there are $5$ and $1$ consecutive ones in two groups.  Print the maximum, $5$.  

## Input Format

A single integer, $n$.	

## Output Format

Print a single base-$10$ integer that denotes the maximum number of consecutive $1$'s in the binary representation of $n$.

**Sample Input 1**

	5
    
**Sample Output 1**

	1
    
**Sample Input 2**

	13
    
**Sample Output 2**

	2

## Constraints

- $1 \le n \le 10^{6}$

## Sample Input

5

## Sample Output

1

## Explanation

Sample Case 1:

The binary representation of  is , so the maximum number of consecutive 's is .

Sample Case 2:

The binary representation of  is , so the maximum number of consecutive 's is .
