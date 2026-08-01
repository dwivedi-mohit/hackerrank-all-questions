# Java Loops II

- **Domain:** databases
- **Difficulty:** Easy
- **Max Score:** 10
- **Success Ratio:** 0.9747979640474183
- **Total Submissions:** 1038924
- **Solved Count:** 1012741
- **URL:** https://www.hackerrank.com/challenges/java-loops

## Problem Statement

We use the integers $a$, $b$, and $n$ to create the following series:

$$(a+2^{0} \cdot b), (a+2^{0} \cdot b + 2^{1} \cdot b), \ldots , (a + 2^{0} \cdot b+2^{1} \cdot b + \ldots + 2^{n-1} \cdot b)$$

You are given $q$ queries in the form of $a$, $b$, and $n$. For each query, print the series corresponding to the given $a$, $b$, and $n$ values as a single line of $n$ space-separated integers. 

## Input Format

The first line contains an integer, $q$, denoting the number of queries. 	
Each line $i$ of the $q$ subsequent lines contains three space-separated integers describing the respective $a_i$, $b_i$, and $n_i$ values for that query. 

## Output Format

For each query, print the corresponding series on a new line. Each series must be printed in order as a single line of $n$ space-separated integers.

## Constraints

* $0 \le q \le 500$
* $0 \le a, b \le 50$
* $1 \le n \le 15$

## Sample Input

0 2 10
5 3 5

## Sample Output

2 6 14 30 62 126 254 510 1022 2046
8 14 26 50 98

## Explanation

We have two queries:

- We use , , and  to produce some series :

-

-

-

... and so on.

Once we hit , we print the first ten terms as a single line of space-separated integers.

- We use , , and  to produce some series :

-

-

-

-

-

We then print each element of our series as a single line of space-separated values.
