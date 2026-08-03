# Repetitive K-Sums

---

| Field | Value |
|---|---|
| **Slug** | `repeat-k-sums` |
| **Domain** | algorithms |
| **Difficulty** | Advanced |
| **Score** | 150 |
| **URL** | https://www.hackerrank.com/challenges/repeat-k-sums |

---

## Preview

Given a set of K repetitive sum of N elements sum. Find the set

## Problem Statement

Alice thinks of a non-decreasing sequence of non-negative integers and wants Bob to guess it by providing him the set of all its **K**-sums with repetitions. 

What is this? Let the sequence be {A[1], A[2], ..., A[N]} and **K** be some positive integer that both Alice and Bob know. Alice gives Bob the set of all possible values that can be genereated by this - **A[i<sub>1</sub>] + A[i<sub>2</sub>] + ... + A[i<sub>K</sub>]**, where **1 ≤ i<sub>1</sub> ≤ i<sub>2</sub> ≤ ... ≤ i<sub>K</sub> ≤ N**. She can provide the values generated in any order she wishes to. Bob's task is to restore the initial sequence.

Consider an example. Let **N = 3** and **K = 2**. The sequence is {A[1], A[2], A[3]}. The sequence of its **2**-sums with repetitions is {A[1] + A[1], A[1] + A[2], A[1] + A[3], A[2] + A[2], A[2] + A[3], A[3] + A[3]}. But its elements could be provided in any order. For example any permutation of **{2, 3, 4, 4, 5, 6}** corresponds to the sequence **{1, 2, 3}**.

## Input Format

The first line of the input contains an integer **T** denoting the number of test cases.

The description of **T** test cases follows.

The first line of each test case contains two space separated integers **N** and **K**.

The second line contains the sequence **S**<sub>i</sub> of all **K**-sums with repetitions of the sequence Alice initially thought of.

## Output Format

For each test case, output a single line containing the space separated list of elements of the non-decreasing sequence Alice thinks of. If there are several possible outputs you can output any of them.

## Constraints

+ $1 \le T \le 10^5$

+ $1 \le N \le 10^5$

+ $1 \le K \le 10^9$

+ $2 \le S_i \le 10^{18}$


**Note**

The total number of elements in any input sequence does not exceed **10<sup>5</sup>**

Each element of each input sequence is non-negative integer not exceeding **10<sup>18</sup>**.

Each input sequence is a correct sequence of all **K**-sums with repetitions of some non-decreasing sequence of non-negative integers.

## Sample Tests

### Test 1

```
3
1 3
3
2 2
12 34 56
3 2
2 3 4 4 5 6
```

### Test 2

```
1
6 28
1 2 3
```
