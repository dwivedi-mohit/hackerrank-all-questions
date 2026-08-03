# GCD Groups

---

| Field | Value |
|---|---|
| **Slug** | `gcd-groups` |
| **Contest** | hourrank-1 |
| **Difficulty** | Medium |
| **Score** | 60 |
| **URL** | https://www.hackerrank.com/challenges/gcd-groups |

---

## Problem Statement

Gukiz has an easy task for you:

You are given an array $a$ of even length $n$. We want to split it into two disjoint groups with $\frac{n}{2}$ elements each, so that the Greatest Common Divisor (GCD) of all numbers in each group is greater than $1$. Is this possible?

**Note:** A disjoint group means that each element of array $a$ is located in exactly one group.


**Input Format**<br>

The first line of the input contains a single integer $T$, denoting the number of test cases.

The first line of each testcase contains one even number $n$: the length of the array in the testcase.

The second line of each testcase contains $n$ separated integers $a_1, a_2, \ldots, a_n$ , representing array $a$.

**Constraints:**<br>

$1 \leq T \leq 10$<br>
$1 \leq n \leq 5·10^5$<br>
$1 \leq a_i \leq 5·10^5$<br>
$1 \leq Sum(n) \leq 10^6$<br>

*Note*: The scoring for this problem is *binary*. You have to pass all the test-cases to get a positive score.


**Output Format**<br>

For each testcase, print a single line "YES" (without the quotes) if it is possible to make a split with the aforementioned described properties. If it's not possible, print a single line "NO".

**Sample Input:**<br>

    2
    6
    8 10 24 20 45 30
    2
    25 1

**Sample Output:**<br>

    YES
    NO
