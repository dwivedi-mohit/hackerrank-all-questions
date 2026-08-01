# Day 19: Interfaces

- **Domain:** c
- **Difficulty:** Easy
- **Max Score:** 30
- **Success Ratio:** 0.9949828222493874
- **Total Submissions:** 172607
- **Solved Count:** 171741
- **URL:** https://www.hackerrank.com/challenges/30-interfaces

## Problem Statement

**Objective**	
Today, we're learning about Interfaces. Check out the [Tutorial](/challenges/30-interfaces/tutorial) tab for learning materials and an instructional video!	

**Task**	
The `AdvancedArithmetic` interface and the method declaration for the abstract  `divisorSum(n)` method are provided for you in the editor below. 

Complete the implementation of `Calculator` class, which implements the `AdvancedArithmetic` interface. The implementation for the `divisorSum(n)` method must return the sum of all divisors of $n$.

**Example**   
$n = 25$  

The divisors of $25$ are $1, 5, 25$.  Their sum is $31$.  

------------
$n = 20$  

The divisors of $20$ are $1, 2, 4, 5, 10, 20$ and their sum is $42$.  

## Input Format

A single line with an integer, $n$.

## Output Format

You are not responsible for printing anything to stdout. The locked template code in the editor below will call your code and print the necessary output.

## Constraints

- $1 \le n \le 1000$ 

## Sample Output

I implemented: AdvancedArithmetic
12

## Explanation

The integer  is evenly divisible by , , , and . Our divisorSum method should return the sum of these numbers, which is . The Solution class then prints  on the first line, followed by the sum returned by divisorSum (which is ) on the second line.
