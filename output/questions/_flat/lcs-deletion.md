# LCS Deletion

---

| Field | Value |
|---|---|
| **Slug** | `lcs-deletion` |
| **Domain** | misc |
| **Difficulty** | Hard |
| **Score** | 80 |
| **Contest** | 101hack22 |
| **URL** | https://www.hackerrank.com/challenges/lcs-deletion |

---

## Preview

Help Manasa in LCS Deletion

## Problem Statement

You are given two lists, each containg $N$ numbers. The numbers in both lists are a permuation of $1,2,3 \cdots N$. In an operation, Akhil will have to choose the longest common subsequence of both strings and delete that subsequence from the first list. The process is repeated as long as the first list has one or more numbers.

So, for the given input, find the minimal number of operations that will be executed.

**Input Format**

The first line contains an integer $N$.

The next two lines contain $N$ integers.

**Constraints**

$ 1\le N \le 5 \times 10^5$

**Output Format**

Print the mimimal number of required operations.


**Sample Input 00**

	3
    1 2 3
    1 2 3

**Sample Output 00**

	1
    

**Sample Input 01**

	4
    1 3 2 4
    3 1 4 2

**Sample Output 01**

	2

## Sample Tests

### Test 1

```
3
1 2 3
1 2 3
```

### Test 2

```
1
```

### Test 3

```
4
1 3 2 4
3 1 4 2
```

### Test 4

```
2
```
