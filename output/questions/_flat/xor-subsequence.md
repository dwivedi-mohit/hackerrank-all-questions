# XOR Subsequences

---

| Field | Value |
|---|---|
| **Slug** | `xor-subsequence` |
| **Domain** | algorithms |
| **Difficulty** | Advanced |
| **Score** | 80 |
| **URL** | https://www.hackerrank.com/challenges/xor-subsequence |

---

## Preview

Find the most frequent number in the recorded list and how
 many times it appears.

## Problem Statement

Consider an array, $A$, of $n$ integers ($A = a_0, a_1, \ldots, a_{n-1}$). 
We take all consecutive subsequences of integers from the array that satisfy the following:
$$\{a_i, a_{i+1}, \ldots, a_{j-1}, a{j}\} \text{, where } 0 \le i \le j \lt n$$ 

For example, if $n = 3$ our subsequences will be:

1. $a_0$
2. $a_1$  

3. $a_2$  

4. $a_0, a_1$
5. $a_1, a_2$
6. $a_0, a_1, a_2$ 
  

For each subsequence, we apply the bitwise *XOR* ($\oplus$) operation on all the integers and record the resultant value. Since there are $n \times \frac{(n + 1)}{2}$ subsequences, this will result in $n \times \frac{(n + 1)}{2}$ numbers. 


Given array $A$, find the XOR sum of every subsequence of $A$ and determine the frequency at which each number occurs. Then print the number and its respective frequency as two space-separated values on a single line.

## Input Format

The first line contains an integer, $n$, denoting the size of the array.	
Each line $i$ of the $n$ subsequent lines contains a single integer describing element $a_i$.

## Output Format

Print $2$ space-separated integers on a single line. The first integer should be the number having the highest frequency, and the second integer should be the number's frequency (i.e., the number of times it appeared). If there are multiple numbers having maximal frequency, choose the smallest one.

## Constraints

- $1 \le n \le 10^5$
- $1 \le a_i \lt 2^{16}$

## Sample Tests

### Test 1

```
4
2
1
1
3
```

### Test 2

```
1 3
```
