# Choosing White Balls

- **Domain:** ai
- **Difficulty:** Hard
- **Max Score:** 60
- **Success Ratio:** 0.7390873015873016
- **Total Submissions:** 2016
- **Solved Count:** 1490
- **URL:** https://www.hackerrank.com/challenges/choosing-white-balls

## Problem Statement

There are $n$ balls in a row, and each ball is either *black* (`B`) or *white* (`W`). Perform $k$ removal operations with the goal of *maximizing the number of white balls* picked. For each operation $i$ (where $1 \le i \le k$):

1. Choose an integer, $x_i$, uniformly and independently from $1$ to $n - i + 1$ (inclusive).
2. Remove the ${x_i}^{th}$ ball from either the left end or right end of the row, which decrements the number of available balls in the row by $1$. You can choose to remove the ball from whichever end in each step maximizing the expected total number of white balls picked at the end.

Given a string describing the initial row of balls as a sequence of $n$ `W`'s and `B`'s, find and print the [expected](https://en.wikipedia.org/wiki/Expected_value) number of *white* balls providing that you make all choices optimally. A correct answer has an _absolute_ error of *at most* $10^{-6}$.  

## Input Format

The first line contains two space-separated integers describing the respective values of $n$ (the number of balls) and $k$ (the number of operations).		
The second line describes the initial sequence balls as a single string of $n$ characters; each character is either `B` or `W` and describes a *black* or *white* ball, respectively.

## Output Format

Print a single floating-point number denoting the expected number of *white* balls picked. Your answer is considered to be correct if it has an _absolute_ error of *at most* $10^{-6}$.  


## Constraints

+ $1 \le k \le n < 30$

## Sample Input

3 1
BWW

## Sample Output

1.0000000000

## Explanation

Independent of your choice of , one white ball will always be picked so the expected number of white balls chosen after  operation is . Thus, we print  as our answer.
