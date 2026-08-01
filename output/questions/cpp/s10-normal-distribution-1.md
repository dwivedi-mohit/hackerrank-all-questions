# Day 5: Normal Distribution I

- **Domain:** cpp
- **Difficulty:** Easy
- **Max Score:** 30
- **Success Ratio:** 0.9601761056633981
- **Total Submissions:** 19988
- **Solved Count:** 19192
- **URL:** https://www.hackerrank.com/challenges/s10-normal-distribution-1

## Problem Statement

**Objective**	
In this challenge, we learn about normal distributions. Check out the [Tutorial](/challenges/s10-normal-distribution-1/tutorial) tab for learning materials!

**Task**	
In a certain plant, the time taken to assemble a car is a random variable, $X$, having a normal distribution with a mean of $20$ hours and a standard deviation of $2$ hours. What is the probability that a car can be assembled at this plant in:

1. Less than $19.5$ hours?
2. Between $20$ and $22$ hours?

## Input Format

There are $3$ lines of input (shown below):

    20 2
    19.5
    20 22
    
The first line contains $2$ space-separated values denoting the respective mean and standard deviation for $X$. The second line contains the number associated with question $1$. The third line contains $2$ space-separated values describing the respective lower and upper range boundaries for question $2$.

If you do not wish to read this information from stdin, you can hard-code it into your program.

## Output Format

There are two lines of output. Your answers must be rounded to a scale of $3$ decimal places (i.e., $1.234$ format):

1. On the first line, print the answer to question $1$ (i.e., the probability that a car can be assembled in less than $19.5$ hours).
2. On the second line, print the answer to question $2$ (i.e., the probability that a car can be assembled in between $20$ to $22$ hours).
