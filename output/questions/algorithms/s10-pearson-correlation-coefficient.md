# Day 7: Pearson Correlation Coefficient I

- **Domain:** algorithms
- **Difficulty:** Easy
- **Max Score:** 30
- **Success Ratio:** 0.9863703895097216
- **Total Submissions:** 15481
- **Solved Count:** 15270
- **URL:** https://www.hackerrank.com/challenges/s10-pearson-correlation-coefficient

## Problem Statement

**Objective** <br>
In this challenge, we practice calculating the *Pearson correlation coefficient*. Check out the [Tutorial](/challenges/s10-pearson-correlation-coefficient/tutorial) tab for learning materials!

**Task**<br>
Given two $n$-element data sets, $X$ and $Y$, calculate the value of the Pearson correlation coefficient.

## Input Format

The first line contains an integer, $n$, denoting the size of data sets $X$ and $Y$. 	
The second line contains $n$ space-separated real numbers (scaled to *at most* one decimal place), defining data set $X$. 		
The third line contains $n$ space-separated real numbers (scaled to *at most* one decimal place), defining data set $Y$.

## Output Format

Print the value of the Pearson correlation coefficient, rounded to a scale of $3$ decimal places. 

## Constraints

- $10 \le n \le 100$
- $1 \le x_{i} \le 500$, where $x_{i}$ is the $i^{th}$ value of data set $X$.
- $1 \le y_{i} \le 500$, where $y_{i}$ is the $i^{th}$ value of data set $Y$.
- Data set $X$ contains unique values.
- Data set $Y$ contains unique values.

## Sample Input

10 9.8 8 7.8 7.7 7 6 5 4 2
200 44 32 24 22 17 15 12 8 4

## Sample Output

0.612

## Explanation

The mean and standard deviation of data set  are:

-

-

The mean and standard deviation of data set  are:

-

-

We use the following formula to calculate the Pearson correlation coefficient:
