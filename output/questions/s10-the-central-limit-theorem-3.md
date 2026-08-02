# Day 6: The Central Limit Theorem III

- **Domain:** ai
- **Difficulty:** Easy
- **Max Score:** 30
- **Success Ratio:** 0.981143310837634
- **Total Submissions:** 15114
- **Solved Count:** 14829
- **URL:** https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-3

## Problem Statement

**Objective** 		
In this challenge, we practice solving problems based on the *Central Limit Theorem*. We recommend reviewing the [Central Limit Theorem Tutorial](/challenges/s10-the-central-limit-theorem-1/tutorial) before attempting this challenge.

**Task**		
You have a sample of $100$ values from a population with mean $\mu = 500$ and with standard deviation $\sigma = 80$. Compute the interval that covers the middle $95\%$ of the distribution of the sample mean; in other words, compute $A$ and $B$ such that $P(A \lt x \lt B) = 0.95$. Use the value of $z = 1.96$. Note that $z$ is the [z-score](https://en.wikipedia.org/wiki/Standard_score).



## Input Format

There are five lines of input (shown below):

    100
    500
    80
    .95
    1.96

The first line contains the sample size. The second and third lines contain the respective mean ($\mu$) and standard deviation ($\sigma$). The fourth line contains the distribution percentage we want to cover (as a decimal), and the fifth line contains the value of $z$.

If you do not wish to read this information from stdin, you can hard-code it into your program.

## Output Format

Print the following two lines of output, rounded to a scale of $2$ decimal places (i.e., $1.23$ format):

1. On the first line, print the value of $A$.
2. On the second line, print the value of $B$.

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
