# Modify The Sequence

---

| Field | Value |
|---|---|
| **Slug** | `modify-the-sequence` |
| **Domain** | algorithms |
| **Difficulty** | Advanced |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/modify-the-sequence |

---

## Preview

minimal number of integers that should be replaced to make the sequence strictly increasing

## Problem Statement

You are given a sequence of integers a<sub>1</sub>,a<sub>2</sub>,a<sub>3</sub>.....a<sub>n</sub>. You are free to replace any integer with any other positive integer. How many integers must be replaced to make the resulting sequence strictly increasing? 

**Input Format**

The first line of the test case contains an integer $N$ - the number of entries in the sequence.

The next line contains $N$ space separated integers where the $i^{th}$ integer is $a_i$.

**Output Format**  

Output the minimal number of integers that should be replaced to make the sequence strictly increasing.

**Constraints**

$0 < N \le 10^6$

$0 < a_i \le 10^9$


**Sample Input #00**

    3
    4 10 20

**Sample Output #00**

    0

**Sample Input #01**

    6
    1 7 10 2 20 22

**Sample Output #01**

    1

**Sample Input #02**

    5
    1 2 2 3 4 

**Sample Output #02**

    3

**Explanation**

In the first sample input, we need not replace anything, hence the output is 0. 

In the second sample input, we can replace 2 with any integer between 11 and 19 to make the sequence strictly increasing, hence the output is 1. 

In the third sample input, we can obtain 1, 2, 3, 4, 5 by changing the last three elements of the sequence.

## Sample Tests

### Test 1

```
3
4 10 20
```

### Test 2

```
0
```

### Test 3

```
6
1 7 10 2 20 22
```

### Test 4

```
1
```

### Test 5

```
5
1 2 2 3 4
```

### Test 6

```
3
```
