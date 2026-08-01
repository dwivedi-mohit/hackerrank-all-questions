# Day 5: Normal Distribution II

- **Domain:** c
- **Difficulty:** Easy
- **Max Score:** 30
- **Success Ratio:** 0.980004243131431
- **Total Submissions:** 18854
- **Solved Count:** 18477
- **URL:** https://www.hackerrank.com/challenges/s10-normal-distribution-2

## Problem Statement

**Objective**		
In this challenge, we go further with normal distributions. We recommend reviewing the previous challenge's [Tutorial](/challenges/s10-normal-distribution-1/tutorial) before attempting this problem.

**Task**	
The final grades for a Physics exam taken by a large group of students have a mean of $\mu = 70$ and a standard deviation of $\sigma = 10$. If we can approximate the distribution of these grades by a normal distribution, what percentage of the students:

1. Scored higher than $80$ (i.e., have a $grade \gt 80$)?
2. Passed the test (i.e., have a $grade \ge 60$)?
3. Failed the test (i.e., have a $grade \lt 60$)?

Find and print the answer to each question on a new line, rounded to a scale of $2$ decimal places.

## Input Format

There are $3$ lines of input (shown below):

    70 10
    80
    60
    
The first line contains $2$ space-separated values denoting the respective mean and standard deviation for the exam. The second line contains the number associated with question $1$. The third line contains the pass/fail threshold number associated with questions $2$ and $3$.

If you do not wish to read this information from stdin, you can hard-code it into your program.

## Output Format

There are three lines of output. Your answers must be rounded to a scale of $2$ decimal places (i.e., $1.23$ format):

1. On the first line, print the answer to question $1$ (i.e., the percentage of students having $grade \gt 80$).
2. On the second line, print the answer to question $2$ (i.e., the percentage of students having $grade \ge 60$).
3. On the third line, print the answer to question $3$ (i.e., the percentage of students having $grade \lt 60$).
