# Count Strings

---

| Field | Value |
|---|---|
| **Slug** | `count-strings` |
| **Domain** | algorithms |
| **Difficulty** | Hard |
| **Score** | 80 |
| **URL** | https://www.hackerrank.com/challenges/count-strings |

---

## Preview

Given a regular expression and an integer L, count how many strings of length L it can generate.

## Problem Statement

A regular expression is used to describe a set of strings. For this problem the alphabet is limited to 'a' and 'b'.

We define $R$ to be a valid regular expression if:

1) $R$ is "$a$" or "$b$".

2) $R$ is of the form "$(R_1R_2)$", where $R_1$ and $R_2$ are regular expressions.

3) $R$ is of the form "$(R_1|R_2)$" where $R_1$ and $R_2$ are regular expressions.

4) $R$ is of the form "$(R_1*)$" where $R_1$ is a regular expression.

Regular expressions can be nested and will always have have two elements in the parentheses. ('$*$' is an element, '$|$' is not; basically, there will always be pairwise evaluation) Additionally, '$*$' will always be the second element; '$(*a)$' is invalid.

  

The set of strings recognized by $R$ are as follows:

1) If $R$ is "$a$", then the set of strings recognized $= {a}$.

2) If $R$ is "$b$", then the set of strings recognized $= {b}$.

3) If $R$ is of the form "$(R_1R_2)$" then the set of strings recognized = all strings which can be obtained by a concatenation of strings $s_1$ and $s_2$, where $s_1$ is recognized by $R_1$ and $s_2$ by $R_2$.

4) If $R$ is of the form "$(R1|R2)$" then the set of strings recognized = union of the set of strings recognized by $R_1$ and $R_2$.

5) If $R$ is of the form "$(R_1*)$" then the the strings recognized are the empty string and the concatenation of an arbitrary number of copies of any string recognized by $R_1$.

**Task**  	
Given a regular expression and an integer, $L$, count how many strings of length $L$ are recognized by it.

## Input Format

The first line contains the number of test cases $T$. $T$ test cases follow.

Each test case contains a regular expression, $R$, and an integer, $L$.

## Output Format

Print $T$ lines, one corresponding to each test case containing the required answer for the corresponding test case. As the answers can be very big, output them modulo $10^9 + 7$.

## Constraints

- $1 \le T \le 50$

- $1 \le |R| \le 100$

- $1 \le L \le 10^9$
- It is guaranteed that $R$ will conform to the definition provided above.

## Sample Tests

### Test 1

```
3 
((ab)|(ba)) 2 
((a|b)*) 5 
((a*)(b(a*))) 100
```

### Test 2

```
2 
32 
100
```
