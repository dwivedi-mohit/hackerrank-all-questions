# LIS Arrays

---

| Field | Value |
|---|---|
| **Slug** | `lis-arrays` |
| **Domain** | misc |
| **Difficulty** | Advanced |
| **Score** | 120 |
| **Contest** | 101hack33 |
| **URL** | https://www.hackerrank.com/challenges/lis-arrays |

---

## Preview

Compute a function over all valid arrays.

## Problem Statement

We define a function, $f$, on a sequence of integers $a_0, a_1, \cdots, a_{n-1}$ to be:

$f([a_0,a_1,\cdots,a_{n-1}]) = \sum \limits _{l=0}^{n-1} \sum \limits _{r=l}^{n-1} \textrm{max}(a_l,a_{l+1}, \cdots, a_r)$  <br>
 

Now, $\textrm{LIS}(A)$ defines an array of size $n$ for a given array $A_0, A_1, \cdots, A_{n-1}$ consisting of distinct elements.<br>
 $\textrm{LIS}(A)_i$ is defined as the length of the longest increasing subsequence among sequence $A_0, A_1, \cdots ,A_i$ and containing $A_{i}$. <br>
 
 For example: <br>
$\textrm{LIS}([2,4,5,3]) = [1,2,3,2]$.
 
 
For a positive integer $n$, define:

$S_{n} = \{ \textrm{LIS}(A) \ | \  A \textrm{ is an array of size } n \textrm{ with distinct integers} \}$


$S_n$ is a set of all distinct $\textrm{LIS}(A)$ for all possible arrays $A$ of distinct integers and size $n$.  

**Note:** Even though there are infinitely many $A$ arrays, there are only a finite amount $\textrm{LIS}$ arrays possible. Thus, $S_{n}$ is finite.

Given an input $N$ and a modulo value $M$, compute:

$\sum \limits_{x \in S_N}^{}f(x)$

Formally, find the sum of $f(x)$ over all arrays $x$ that are in $S_{N}$. <br>
Print the answer modulo $M$.  <br>
You can assume that $M$ is prime. <br>

## Input Format

The first line contains an integer $T$, denoting the number of test cases.<br>
The next line contains the modulo value $M$. <br>
Each of the next $T$ lines contains an integer representing the value of $N$.

## Output Format

For each test case, print the required answer in one line.

## Constraints

- $1 \le T \le 200$ 

- $1 \le N \le 200$	
- $10^8 \le M \le 10^9 + 7$
- For $20\%$ of the test cases, $T <= 16, N <= 16, MOD = 10^9 + 7 $
- For $50\%$ of the test cases $T <= 100, N <= 100, MOD = 10^9 + 7 $
- For $100\%$ of the test cases, refer to the main constraints.

## Sample Tests

### Test 1

```
3
1000000007
1
2
3
```

### Test 2

```
1
8
50
```
