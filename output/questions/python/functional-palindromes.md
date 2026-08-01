# Functional Palindromes

- **Domain:** python
- **Difficulty:** Advanced
- **Max Score:** 80
- **Success Ratio:** 0.7857514300572023
- **Total Submissions:** 1923
- **Solved Count:** 1511
- **URL:** https://www.hackerrank.com/challenges/functional-palindromes

## Problem Statement

Let's define a function, $f$, on a string, $p$, of length $l$ as follows:

$$f(p) = (p_1 \cdot a^{l-1} + p_2 \cdot a^{l-2} + \dots + p_l \cdot a^0) \bmod m$$

where $p_i$ denotes the [ASCII value](http://ascii.cl/) of the $i^{th}$ character in string $p$, $a=100001$, and $m=10^9+7$. 

Nikita has a string, $s$, consisting of $n$ lowercase letters that she wants to perform $q$ queries on. Each query consists of an integer, $k$, and you have to find the value of $f(w_k)$ where $w_k$ is the $k^{th}$ [alphabetically smallest](https://en.wikipedia.org/wiki/Lexicographical_order) [palindromic](https://en.wikipedia.org/wiki/Palindrome) [substring](https://en.wikipedia.org/wiki/Substring) of $s$. If $w_k$ doesn't exist, print $-1$ instead.


## Input Format

The first line contains $2$ space-separated integers describing the respective values of $n$ (the length of string $s$) and $q$ (the number of queries).	
The second line contains a single string denoting $s$. 		
Each of the $q$ subsequent lines contains a single integer denoting the value of $k$ for a query. 

## Output Format

For each query, print the value of function $f(w_{k})$ where $w_{k}$ is the $k^{th}$ *alphabetically smallest palindromic substring* of $s$; if $w_{k}$ doesn't exist, print $-1$ instead.

## Constraints

* $1 \le n, q \le 10^5$  
* $1 \le k \le \frac{n \cdot (n + 1)}{2}$  
* It is guaranteed that string $s$ consists of lowercase English alphabetic letters only (i.e., $\texttt{a}$ to $\texttt{z}$).
- $a = 10^5 + 1$
- $m = 10^9 + 7$. 

**Scoring**

* $1 \le n, q \le 10^3$ for $\text{25%}$ of the test cases.
* $1 \le n, q \le 10^5$ for $\text{100%}$ of the test cases.

## Sample Input

5 7
abcba
1
2
3
4
6
7
8

## Sample Output

97
696207567
98
29493435
99
-1

## Explanation

There are  palindromic substrings of . Let's list them in lexicographical order and find value of :

- ,

- ,

- ,

- ,

- ,

- ,

- ,

-  doesn't exist, so we print  for .
