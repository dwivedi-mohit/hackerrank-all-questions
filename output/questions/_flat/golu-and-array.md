# A Perfect Array

---

| Field | Value |
|---|---|
| **Slug** | `golu-and-array` |
| **Domain** | misc |
| **Difficulty** | Easy |
| **Score** | 20 |
| **Contest** | adobe-hackathon |
| **URL** | https://www.hackerrank.com/challenges/golu-and-array |

---

## Preview

Help us find the perfect array.

## Problem Statement

You have an array $A$ with $N$ elements (assume *1-based indexing*). All the elements in this array are unique, positive integers with the number of odd-value integers equal to the number of even-value integers. For example: {1,2,3,4}. We are introducing a new concept of a *perfect* array.

A *perfect* array is an array with the following properties:

* It has an equal number of odd and even elements.
* Odd elements occupy odd positions, and Even elements occupy the even positions in this array.
* Odd elements are in the sorted order.
* Even elements are in the sorted order.

For example: $\{1, 2, 7, 12, 9, 20, 15, 22\}$ is a perfect array.<br>

Your task: How many swaps would it take to turn an array $A$ into a *perfect* array?<br>
A  _Swap_ can be performed between any two elements of an array.

## Input Format

The first line of input contains an integer $N$.

The next line contains $N$ integers separated by a space. Here, $i_{th}$ of these integers represents $A_{i}$, the _i<sup>th</sup>_ element of the array $A$.

## Output Format

The only line of output consists of one integer: the minimum number of swaps required to turn $A$ into a _perfect_ array.

## Constraints

$2 \leq N \leq 10^5$<br>
$1 \leq A_i \leq 10^9$

## Sample Tests

### Test 1

```
4
2 3 1 4
```

### Test 2

```
2
```

### Test 3

```
1 2 3 4
```
