# Manasa and Stones

---

| Field | Value |
|---|---|
| **Slug** | `manasa-and-stones` |
| **Domain** | algorithms |
| **Difficulty** | Easy |
| **Score** | 30 |
| **URL** | https://www.hackerrank.com/challenges/manasa-and-stones |

---

## Preview

Calculate the possible values of the last stone where consecutive values on the stones differ by a value 'a' or a value 'b'.

## Problem Statement

Manasa is out on a hike with friends. She finds a trail of stones with numbers on them. She starts following the trail and notices that any two consecutive stones' numbers differ by one of two values.  Legend has it that there is a treasure trove at the end of the trail.  If Manasa can guess the value of the last stone, the treasure will be hers.

**Example**

$n = 2$

$a = 2$

$b = 3$


She finds $2$ stones and their differences are $a = 2$ or $b = 3$.  We know she starts with a $0$ stone not included in her count.  The permutations of differences for the two stones are $[2,2], [2,3], [3,2]$ or $[3,3]$.  Looking at each scenario, stones might have $[2,4], [2,5], [3,5]$ or $[3,6]$ on them.  The last stone might have any of  $4, 5$, or $6$ on its face. 

Compute all possible numbers that might occur on the last stone given a starting stone with a $0$ on it, a number of additional stones found, and the possible differences between consecutive stones.  Order the list ascending.

**Function Description**

Complete the *stones* function in the editor below. 


stones has the following parameter(s):


- *int n:* the number of non-zero stones

- *int a:* one possible integer difference

- *int b:* another possible integer difference


**Returns**


- *int[]:* all possible values of the last stone, sorted ascending

## Input Format

The first line contains an integer $T$, the number of test cases.


Each test case contains $3$ lines:

- The first line contains $n$, the number of non-zero stones found.

- The second line contains $a$, one possible difference

- The third line contains $b$, the other possible difference.

## Constraints

+ $1 \le T \le 10$

+ $1 \le n, a, b \le 10^3$

## Sample Tests

### Test 1

```
STDIN Function
----- --------
2 T = 2 (test cases)
3 n = 3 (test case 1)
1 a = 1
2 b = 2
4 n = 4 (test case 2)
10 a = 10
100 b = 100
```

### Test 2

```
2 3 4 
30 120 210 300
```
