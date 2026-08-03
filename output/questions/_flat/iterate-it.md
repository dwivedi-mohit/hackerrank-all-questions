# Iterate It

---

| Field | Value |
|---|---|
| **Slug** | `iterate-it` |
| **Domain** | algorithms |
| **Difficulty** | Expert |
| **Score** | 90 |
| **URL** | https://www.hackerrank.com/challenges/iterate-it |

---

## Preview

print the number of loops it takes for the array to be empty.

## Problem Statement

Consider the following pseudocode, run on an array $A = [a_0, a_1, \ldots, a_{n - 1}]$ of length $n$:

```pascal
rep := 0
while A not empty:
    B := []
    for x in A, y in A:
        if x != y: append absolute_value(x - y) to B
    A := B
    rep := rep + 1
```

Given the values of $n$ and array $A$, compute and print the final value of $rep$ after the pseudocode above terminates; if the loop will never terminate, print `-1` instead.

## Input Format

The first line contains a single integer, $n$, denoting the length of array $A$. 	 
The second line contains $n$ space-separated integers describing the respective values of $a_0, a_1, \ldots, a_{n - 1}$.

## Output Format

Print the final value of $rep$ after the pseudocode terminates; if the loop will never terminate, print `-1` instead.

## Constraints

+ $1 \le n \le 10^5$

+ $1 \le a_i \le 5 \times 10^4 ~ \forall ~ 1 \le i \le n$

## Sample Tests

### Test 1

```
rep
:=
0
while
A
not
empty
:
B
:=
[]
for
x
in
A
,
y
in
A
:
if
x
!
=
y
:
append
absolute_value
(
x
-
y
)
to
B
A
:=
B
rep
:=
rep
+
1
```

### Test 2

```
3
1 3 4
```

### Test 3

```
4
```
