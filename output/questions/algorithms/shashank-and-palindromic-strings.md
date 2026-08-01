# Shashank and the Palindromic Strings

- **Domain:** algorithms
- **Difficulty:** Advanced
- **Max Score:** 60
- **Success Ratio:** 0.8443181818181819
- **Total Submissions:** 1760
- **Solved Count:** 1486
- **URL:** https://www.hackerrank.com/challenges/shashank-and-palindromic-strings

## Problem Statement

Shashank loves strings, but he loves palindromic strings the most. He has a list of $n$ strings, $A = [a_0, a_1, \ldots, a_{n - 1}]$, where each string, $a_i$, consists of lowercase English alphabetic letters. Shashank wants to count the number of ways of choosing non-empty [subsequences](https://en.wikipedia.org/wiki/Subsequence) $s_0, s_1, s_2, \ldots, s_{n - 1}$ such that the following conditions are satisfied:

1. $s_0$ is a subsequence of string $a_0$, $s_1$ is a subsequence of string $a_1$, $s_2$ is a subsequence of string $a_2$, $\ldots$, and $s_{n - 1}$ is a subsequence of string $a_{n - 1}$.
2. $s_0 + s_1 + s_2 + \ldots + s_{n - 1}$ is a palindromic string, where `+` denotes the string concatenation operator.

You are given $q$ queries where each query consists of some list, $A$. For each query, find and print the number of ways Shashank can choose $n$ non-empty subsequences satisfying the criteria above, modulo $10^9 + 7$, on a new line.

**Note:** Two subsequences consisting of the same characters are considered to be different if their characters came from different indices in the original string.

## Input Format

The first line contains a single integer, $q$, denoting the number of queries. The subsequent lines describe each query in the following format:

- The first line contains an integer, $n$, denoting the size of the list. 
- Each line $i$ of the $n$ subsequent lines contains a non-empty string describing $a_i$.

## Output Format

For each query, print the number of ways of choosing non-empty subsequences, modulo $10^9 + 7$, on a new line.

## Constraints

* $1 \le q \le 50$  
* $1 \le n \le 50$  
* $\sum_{i=0}^{n - 1} |a_i| \le 1000$ over a test case.

For $\text{40%}$ of the maximum score:

* $1 \le n \le 5$  
* $\sum_{i=0}^{n - 1} |a_i| \le 250$ over a test case.


## Sample Input

3
3
aa
b
aa
3
a
b
c
2
abc
abc

## Sample Output

5
0
9

## Explanation

The first two queries are explained below:

- We can choose the following five subsequences:

- , , , where  is the first character of  and  is the first character of .

- , , , where  is the second character of  and  is the second character of .

- , , , where  is the first character of  and  is the second character of .

- , , , where  is the second character of  and  is the first character of .

- , ,

Thus, we print the result of  on a new line.

- There is no way to choose non-empty subsequences such that their concatenation results in a palindrome, as each string contains unique characters. Thus, we print  on a new line.
