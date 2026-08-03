# Devu and a Wonderful Game

---

| Field | Value |
|---|---|
| **Slug** | `devu-and-wonderful-game` |
| **Domain** | misc |
| **Difficulty** | Medium |
| **Score** | 40 |
| **Contest** | 101hack25 |
| **URL** | https://www.hackerrank.com/challenges/devu-and-wonderful-game |

---

## Preview

Play a wonderful game with Devu.

## Problem Statement

Devu has a series of red and blue balloons, which is given by a string $s$ where each character of $s$ is either 'R' or 'B'. Here 'R' denotes a red-colored balloon and 'B' denotes a blue-colored one.

He arranges the balloons in the same order as given in the string $s$. If a configuration of balloons has two or more balloons of the same color appearing adjacently in the string $s$, they all disappear instantly. Also the procedure of disappearing is recursive. Please see the following examples to understand the disappearing process.

Examples:

   - RRBBRR will disappear completely.
   - RBBR will first turn into RR which will disappear completely.
   - RBBRBBBR, In this 2nd and 4th consecutive parts i.e. BB and BBB will vanish simultaneously, then the balloons will turn into RRR which will completely vanish. 

Now given a configuration of balloons, he would like to turn the configuration into the configuration having less than or equal to two balloons. To achieve this, he is allowed to perform the following operations on the string. In a single operation, he can swap any two differently colored balloons. Note that such an operation will be valid only if it actually decreases the size of the string, e.g. in "RB", you can swap R and B and get BR in one operation, but this operation is not valid as it is not decreasing the size of string $s$.

Find out the minimum and maximum number of valid operations he can perform in order to achieve the desired configuration (i.e. the configuration with ≤ 2 balloons).

## Input Format

-	The first line of the input contains a single integer, $T$, denoting the number of test cases.
-	For each test case, a single line contains string $s$ ($1 \le$ length of string $s  \le 500$). Each character of $s$ is either 'R' or 'B'.

## Output Format

For each test case, print a single line containing two single space-separated integers representing the minimum and maximum number of valid operations, respectively.
 
 **Constraints**

-	$1 \leq T \leq 100$
-	$1 \leq $ size of $s \leq 500$ 
-	Each character of $s$ is either 'R' or 'B'

## Sample Tests

### Test 1

```
5
RB
B
RBR
RRBRRB
BRBR
```

### Test 2

```
0 0
0 0
1 1
0 0
1 1
```
