# Akhil and GF

---

| Field | Value |
|---|---|
| **Slug** | `akhil-and-gf` |
| **Domain** | mathematics |
| **Difficulty** | Hard |
| **Score** | 40 |
| **URL** | https://www.hackerrank.com/challenges/akhil-and-gf |

---

## Preview

Help Akhil in impressing his girlfriend

## Problem Statement

After dating for a long time, Akhil is finally going to propose to his girlfriend. She is very strong in mathematics, and will accept his proposal, if and only if Akhil solves a problem given by her. The problem is given below. Help Akhil solve it.

Akhil is given two numbers N and M, and he has to tell her the remainder when $111\cdots \text{(N times)}$ is divided by $M$.


**Input Format**

The first line contains an integer $T$ i.e. the number of test cases.

Each of the next $T$ lines contain two space separated integers, $N$ and $M$.


**Output Format**

$T$ lines each containing ouptut for the corresponding test case. 

**Constraints**

$1 \le T \le 10001$

$1 \le N \le 10^{16}$

$2 \le M \le 10^9$


**Sample Input 00**


	3
	3 3
	4 7
	5 18
  

**Sample Output 00**


	0
	5	
	5
  

**Explanation** 

  111 % 3  = 0

  1111 % 7 = 5

  11111%18 = 5

## Sample Tests

### Test 1

```
3
3 3
4 7
5 18
```

### Test 2

```
0
5 
5
```
