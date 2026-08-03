# Lonely Integer - Bash!

---

| Field | Value |
|---|---|
| **Slug** | `lonely-integer-2` |
| **Domain** | shell |
| **Difficulty** | Hard |
| **Score** | 10 |
| **URL** | https://www.hackerrank.com/challenges/lonely-integer-2 |

---

## Preview

Find the integer that occurs only once in the Array

## Problem Statement

There are $N$ integers in an array $A$. All but one integer occur in pairs. Your task is to find the number that occurs only once.

**Input Format**

The first line of the input contains an integer $N$, indicating the number of integers. The next line contains $N$ space-separated integers that form the array $A$.

**Constraints**

$1 \le N < 100$

$N$ % $2 = 1$ ($N$ is an odd number)

$0 \le A[i] \le 100, ∀ i ∈ [1, N]$

**Output Format**

Output $S$, the number that occurs only once.

**Sample Input:1**

    1
    1

**Sample Output:1**

    1

**Sample Input:2**

    3
    1 1 2

**Sample Output:2**

    2

**Sample Input:3**

    5
    0 0 1 2 1

**Sample Output:3**

    2

**Explanation**

In the first input, we see only one element (_1_) and that element is the answer.

In the second input, we see three elements; _1_ occurs at two places and _2_ only once. Thus, the answer is _2_.

In the third input, we see five elements. _1_ and _0_ occur twice. The element that occurs only once is _2_.

## Sample Tests

### Test 1

```
1
1
```

### Test 2

```
1
```

### Test 3

```
3
1 1 2
```

### Test 4

```
2
```

### Test 5

```
5
0 0 1 2 1
```

### Test 6

```
2
```
