# Short Palindrome

- **Domain:** algorithms
- **Difficulty:** Medium
- **Max Score:** 100
- **Success Ratio:** 0.7847976307996052
- **Total Submissions:** 1013
- **Solved Count:** 795
- **URL:** https://www.hackerrank.com/challenges/three-month-preparation-kit-short-palindrome

## Problem Statement

Consider a string, $s$, of $n$ lowercase English letters where each character, $s_i$ ($0 \le i \lt n)$, denotes the letter at index $i$ in $s$. We define an $(a, b, c, d)$ palindromic tuple of $s$ to be a sequence of indices in $s$ satisfying the following criteria:

* $s_a = s_d$, meaning the characters located at indices $a$ and $d$ are the same.
* $s_b = s_c$, meaning the characters located at indices $b$ and $c$ are the same.
* $0 \le a \lt b \lt c \lt d \lt |s|$, meaning that $a$, $b$, $c$, and $d$ are ascending in value and are valid indices within string $s$.

Given $s$, find and print the number of $(a, b, c, d)$ tuples satisfying the above conditions. As this value can be quite large, print it modulo $(10^9 + 7)$.  

**Function Description**  
Complete the function *shortPalindrome* in the editor below.  

*shortPalindrome* has the following paramter(s):  
- *string s:* a string  

**Returns**  
- *int:* the number of tuples, modulo $(10^9 + 7)$  

## Input Format

A single string, $s$. 

## Output Format

  

## Constraints

* $1 \le |s| \le 10^6$
* It is guaranteed that $s$ only contains lowercase English letters.  

**Sample Input 0**

	kkkkkkz

**Sample Output 0**

	15

**Explanation 0**

The letter `z` will not be part of a valid tuple because you need at least two of the same character to satisfy the conditions defined above. Because all tuples consisting of four `k`'s are valid, we just need to find the number of ways that we can [choose](https://en.wikipedia.org/wiki/Binomial_coefficient) four of the six `k`'s. This means our answer is ${6 \choose 4}\mod{(10^9 + 7)} = 15$.

**Sample Input 1**

	ghhggh

**Sample Output 1**

	4

**Explanation 1**

The valid tuples are:

1. $(0, 1, 2, 3)$
2. $(0, 1, 2, 4)$
3. $(1 ,3, 4, 5)$
4. $(2 ,3, 4, 5)$

Thus, our answer is $4\mod{(10^9 + 7)} = 4$.

## Sample Input

kkkkkkz

## Sample Output

15

## Explanation

The letter z will not be part of a valid tuple because you need at least two of the same character to satisfy the conditions defined above. Because all tuples consisting of four k's are valid, we just need to find the number of ways that we can choose four of the six k's. This means our answer is .
