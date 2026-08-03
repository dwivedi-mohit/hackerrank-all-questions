# XOR Groups

---

| Field | Value |
|---|---|
| **Slug** | `xor-groups` |
| **Contest** | hourrank-1 |
| **Difficulty** | Easy |
| **Score** | 40 |
| **URL** | https://www.hackerrank.com/challenges/xor-groups |

---

## Problem Statement

Gukiz is obsessed with binary operations. He is trying to solve a task with the binary operation $XOR$, but he can’t seem to figure out one problem. Can you help?

You are given an array $a$ with $n$ elements. Calculate the number of ways to split this array into 2 disjoint non-empty groups with equal $XOR$ value between their elements.

A $disjoint$ group means that each element of array $a$ is located in exactly 1 group. 
The answer can be very large, so print it by modulo $(10^9 + 7)$.

**Input Format**<br>

The first line of input contains one integer $n$: the size of array $a$.
The second line contains $n$ separated integers $a_1, a_2, \ldots, a_n$, representing array $a$.

**Constraints:**<br>

$1\leq n\leq 10^5$<br>
$0 \leq a_i \leq 10^9$

*Note*: The scoring for this problem is *binary*. You have to pass all the testcases to get a positive score.

**Output Format**<br>

In a single line, print one integer - number of ways for splitting the array into two groups with equal $XOR$ by modulo $10^9 + 7$.

**Sample Input 1**<br>

	3
    0 1 1

**Sample Output 1**<br>

	3

**Sample Input 2**<br>

    4
    5 2 3 2


**Sample Output 2**<br>

	0
