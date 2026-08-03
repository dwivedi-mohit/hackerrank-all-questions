# GCD Sequence

---

| Field | Value |
|---|---|
| **Slug** | `gcd-sequence` |
| **Domain** | mathematics |
| **Difficulty** | Hard |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/gcd-sequence |

---

## Preview

Help Devu in finding number of sequences.

## Problem Statement

How many non decreasing sequences are there of length $K$, with the condition that numbers in sequence can take values only from $1,2,3, \cdots N$ and gcd of all numbers in the sequence must be $1$.

**Input Format**

The first line contains an integer $T$ i.e. the number of test cases.<br>
$T$ lines follow, each line containing two integers $N$ and $K$ separated by a single space.


**Output Format**

For each testcase, print in a newline the answer $\mod(10^9+7)$. 

**Constraints**


$ 1 \le T \le 5$

$ 1 \le N \le  10^5$

$ 1 \le K \le 10^5$



**Sample Input**

	4
    2 4 
    3 4
    5 2
    1 10


**Sample Output**

	4
    13
    10
    1


**Explanation**

For the first testcase, the sequences are 
  

    (1,1,1,1), (1,1,1,2), (1,1,2,2), (1,2,2,2) = 4

For the second testcase, the sequences are 

    (1,1,1,1), (1,1,1,2), (1,1,1,3), (1,1,2,2), (1,1,2,3), (1,1,3,3)
    (1,3,3,3), (1,2,2,2), (1,2,2,3), (1,2,3,3), (2,2,2,3), (2,2,3,3), (2,3,3,3)
  

which are 13 in number.

  

For the third testcase, the sequences are


    (1,1), (1,2), (1,3), (1,4), (1,5), (2,3), (2,5), (3, 4), (3, 5), (4, 5) = 10
  

for the fourth testcase, the only sequence is 

    (1,1,1,1,1,1,1,1,1,1)

## Sample Tests

### Test 1

```
4
2 4 
3 4
5 2
1 10
```

### Test 2

```
4
13
10
1
```

### Test 3

```
(1,1,1,1), (1,1,1,2), (1,1,2,2), (1,2,2,2) = 4
```

### Test 4

```
(1,1,1,1), (1,1,1,2), (1,1,1,3), (1,1,2,2), (1,1,2,3), (1,1,3,3)
(1,3,3,3), (1,2,2,2), (1,2,2,3), (1,2,3,3), (2,2,2,3), (2,2,3,3), (2,3,3,3)
```

### Test 5

```
(1,1), (1,2), (1,3), (1,4), (1,5), (2,3), (2,5), (3, 4), (3, 5), (4, 5) = 10
```

### Test 6

```
(1,1,1,1,1,1,1,1,1,1)
```
