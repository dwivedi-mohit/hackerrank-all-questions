# Sherlock and Weird  Sum

---

| Field | Value |
|---|---|
| **Slug** | `sherlock-and-weird-sum` |
| **Domain** | misc |
| **Difficulty** | Hard |
| **Score** | 50 |
| **Contest** | 101hack26 |
| **URL** | https://www.hackerrank.com/challenges/sherlock-and-weird-sum |

---

## Problem Statement

_You know my methods, Watson._

In elementary schools, while adding two positive integers we start from the right most digit and carry forward the overhead. If there are less digits in one of the numbers, we add leading zeroes to it. For example, for adding $39$ and $9$, first we add one leading zero to $9$.

			carry    1
					 3 9
				+	 0 9
				    ---------
				   	 4 8

Now, Watson defines Weird sum as the sum if we ignore carry at each step. For example, Weird sum of $39$ and $9$ would be $38$.

Watson wants Sherlock to generate two numbers $A$ and $B$ such that $1 \le A \le N$ and $1 \le B \le M$ and their weird sum is maximum. Note that $A$ and $B$ can be the same number also.

## Input Format

First line contains $T$, the number of test cases.

Each test case consists of $N$ and $M$ in one line. None of the number in input has leading zeroes.

## Output Format

For each test case, in one line, output the maximum Non-Carry sum possible of two integers $A$ and $B$ such that $1 \le A \le N$ and $1 \le B \le M$. Output number shouldn't have leading zeroes.

**Constraints**

$1 \le T \le 100$

$1 \le N, M \le 10^{16}$

## Sample Tests

### Test 1

```
carry 1
 3 9
 + 0 9
 ---------
 4 8
```

### Test 2

```
2
3 5
16 9
```

### Test 3

```
8
19
```
