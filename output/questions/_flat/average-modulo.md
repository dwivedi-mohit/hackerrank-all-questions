# Average Modulo

---

| Field | Value |
|---|---|
| **Slug** | `average-modulo` |
| **Domain** | misc |
| **Difficulty** | Hard |
| **Score** | 80 |
| **Contest** | 101hack33 |
| **URL** | https://www.hackerrank.com/challenges/average-modulo |

---

## Preview

Find the subarray with the maximum g value.

## Problem Statement

We define function $g$ on an array as:	

$g([a_0,a_1,\cdots,a_{n-1}]) = \frac{(\Sigma_{l=0}^{n-1} a_l) ~ mod ~  p}{n}$

Here, $p$ is a given constant, and $n$ is the length of the array.	
You are given $p$ and an array $A$ and a length $k$.	
You need to find the maximum value of $g$ over all contiguous subarrays of $A$ that are of length $\ge$ $k$.

## Input Format

The first line of input contains $T$, the number of test cases.	
Each test case contains two lines.	
The first line of each test case contains $3$ integers: $N, p$ and $k$, respectively. 	
The second line of each test case contains $N$ integers contained in array $A$.

**Constraints** 


$1 \le T \le 5$ 

$1 \le N \le 5*10^4$	
$1 \le K \le min(300,N)$	
$1 \le P \le 10^9$		
$1 \le A_i \le 10^9$

## Output Format

For each test case, output $1$ line containing $2$ space separated integers: $p$ and $q$, respectively.		
If the answer is an integer $x$, then output $x$ and $1$ separated by a space.		
Otherwise, output $p$ and $q$ if $\frac{p}{q}$ is the answer is in its simplest form.

## Sample Tests

### Test 1

```
3 
3 100 2 
2 1 2 
5 2 1 
2 10 4 6 8 
5 1 2 
100 213142 3123 123 321
```

### Test 2

```
5 3 
0 1 
0 1
```
