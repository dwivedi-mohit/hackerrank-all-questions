# Digit Products

- **Domain:** sql
- **Difficulty:** Medium
- **Max Score:** 60
- **Success Ratio:** 0.2669172932330827
- **Total Submissions:** 266
- **Solved Count:** 71
- **URL:** https://www.hackerrank.com/challenges/digit-products

## Problem Statement

Let $D(X)$ be a function that calculates the digit product of $X$ in base $10$ without leading zeros. For instance:

$D(0) = 0$  
$D(234) = 2 \times 3 \times 4 = 24$  
$D(104) = 1 \times 0 \times 4 = 0$  

You are given three positive integers $A, B$ and $K$. Determine how many integers exist in the range $[A, B]$ whose digit product equals $K$. Formally speaking, you are required to count the number of distinct integer solutions of $X$ where $A \leqslant X \leqslant B$ and $D(X) = K$.



## Input Format

The first line contains $T$, the number of test cases. <br>
The next $T$ lines each contain three positive integers: $A$, $B$ and $K$, respectively.

**Constraints**  
$T \leqslant 10000$  
$1 \leqslant A \leqslant B \leqslant 10^{100}$  
$1 \leqslant K \leqslant 10^{18}$  

## Output Format

For each test case, print the following line:

*Case* $X$$: Y$

$X$ is the test case number, starting at $1$.  
$Y$ is the number of integers in the interval $[A, B]$ whose digit product is equal to $K$. 

Because $Y$ can be a huge number, print it modulo $(10^9 + 7)$.

## Sample Input

1 9 3
7 37 6

## Sample Output

Case 1: 1
Case 2: 3

## Explanation

In the first test case, there is only one number  in the interval .

In the second test case, there are three numbers  in the interval  whose digit product equals .
