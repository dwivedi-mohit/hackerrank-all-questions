# Calculate It

---

| Field | Value |
|---|---|
| **Slug** | `calculate-it` |
| **Domain** | mathematics |
| **Difficulty** | Expert |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/calculate-it |

---

## Preview

Help Tom solve the function hRank

## Problem Statement

Little Tom loves to solve interesting math challenges. One day he bumped onto an interesting function called _hRank_.

Given a positive integer **k**, _hRank_ maps a non-negative integer **x** to another integer.


    hRank(x) = 1 if 0 <= x < k
    hRank(x) = hRank(x – k) + hRank(x / k) if x >= k and k | x  (i.e., x modulo k = 0)
    hRank(x) = hRank(x – 1) otherwise.

Because  x  and hRank(x) may be very large, Tom comes to you for help. Given k and x, can you calculate hRank(x)?

**Input Format**

The input contains only one line with 2 space separated integers, k and x.

**Output Format**

For each test case output the result in a single line.

**Constraints**

2 <= k <= 10 

1 <= x <= k<sup>50</sup>


**Sample Input #00**

    2 1

**Sample Output #00**

    1

**Sample Input #01**

    3 9

**Sample Output #01**

    5

**Explanation**

For the first sample input, when k = 2 and x = 1, the answer is 1 since hRank(x) = 1 as 1 < 2

For the second sample input, when k = 3 and x = 9, we have 

    hRank(9) = hRank(9-3) + hRank(9/3)  = hRank(6) + hRank(3) as 9 > 3 and 9 modulo 3 = 0. 
    hRank(6) = hRank(6-3) + hRank(6/3) = hRank(3) + hRank(2) as 6 > 3 and 6 modulo 3 = 0. 
    hRank(3) = hRank(3-3) + hRank(3/3)  = hRank(0) + hRank(1) as 3 >=3 and 3 modulo 3 = 0. 
    hRank(3) = hRank(0) + hRank(1)
    hRank(3) = 1 + 1 = 2
    hRank(6) = 2 + 1 = 3
    hRank(9) = 3 + 2 = 5

## Sample Tests

### Test 1

```
hRank(x) = 1 if 0 <= x < k
hRank(x) = hRank(x – k) + hRank(x / k) if x >= k and k | x (i.e., x modulo k = 0)
hRank(x) = hRank(x – 1) otherwise.
```

### Test 2

```
2 1
```

### Test 3

```
1
```

### Test 4

```
3 9
```

### Test 5

```
5
```

### Test 6

```
hRank(9) = hRank(9-3) + hRank(9/3) = hRank(6) + hRank(3) as 9 > 3 and 9 modulo 3 = 0. 
hRank(6) = hRank(6-3) + hRank(6/3) = hRank(3) + hRank(2) as 6 > 3 and 6 modulo 3 = 0. 
hRank(3) = hRank(3-3) + hRank(3/3) = hRank(0) + hRank(1) as 3 >=3 and 3 modulo 3 = 0. 
hRank(3) = hRank(0) + hRank(1)
hRank(3) = 1 + 1 = 2
hRank(6) = 2 + 1 = 3
hRank(9) = 3 + 2 = 5
```
