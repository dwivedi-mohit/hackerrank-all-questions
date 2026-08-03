# Xor-sequence

---

| Field | Value |
|---|---|
| **Slug** | `xor-se` |
| **Domain** | algorithms |
| **Difficulty** | Medium |
| **Score** | 40 |
| **URL** | https://www.hackerrank.com/challenges/xor-se |

---

## Preview

xor

## Problem Statement

An array, $A$, is defined as follows: 

* $A_0=0$
* $A_x=A_{x-1} ⊕ x$ for $x>0$, where $⊕$ is the symbol for [XOR](https://en.wikipedia.org/wiki/Exclusive_or)

You will be given a left and right index $l \ r$.  You must determine the XOR sum of the segment of $A$ as $A[l]⊕A[l+1]⊕...⊕A[r-1]⊕A[r]$. 

For example, $A=[0,1,3,0,4,1,7,0,8]$.  The segment from $l=1$ to $r=4$ sums to $1 \oplus 3 \oplus 0 \oplus 4 =6$. 

Print the answer to each question.

**Function Description**


Complete the *xorSequence* function in the editor below.  It should return the integer value calculated.


xorSequence has the following parameter(s):


- *l*: the lower index of the range to sum

- *r*: the higher index of the range to sum

## Input Format

The first line contains an integer $q$, the number of questions.

Each of the next $q$ lines contains two space-separated integers, $l[i]$ and $r[i]$, the inclusive left and right indexes of the segment to query.

## Output Format

On a new line for each test case, print the *XOR-Sum* of $A$'s elements in the inclusive range between indices $l[i]$ and $r[i]$.

## Constraints

$1 \le q \le 10^5$

 $1 \le l[i] \le r[i] \le 10^{15}$

## Sample Tests

### Test 1

```
3
2 4
2 8
5 9
```

### Test 2

```
7
9
15
```

### Test 3

```
3
3 5
4 6
15 20
```

### Test 4

```
5
2
22
```
