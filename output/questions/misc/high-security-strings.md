# High Security Strings

---

| Field | Value |
|---|---|
| **Slug** | `high-security-strings` |
| **Domain** | misc |
| **Difficulty** | Easy |
| **Score** | 10 |
| **Contest** | hack-the-interview-global |
| **URL** | https://www.hackerrank.com/challenges/high-security-strings |

---

## Preview

Determining the strength of a given password in terms of weights assigned to its characters.

## Problem Statement

Estimating the strength of any password is an important aspect of Information Security. In this challenge, your task is to calculate the strength of a given password in terms of weights assigned to the characters.

- A password consists of English lowercase letters only.
- Each English lowercase letter has assigned an integer weight in the range from 0 to 25 inclusive in such a way that the weight of letter $a$ is given explicitly and weights of other letters follow in cyclic order. For example, if $weight(a)=5$, then $weight(b)=6$, $weight(c)=7$, $\ldots$, $weight(u)=25$, $weight(v)=0$, $\ldots$, $weight(z) = 4$.
- The strength of a password is the sum of weights of all characters the password consists of 

Consider the following example. Let the password be $hackerrank$ and the weight of letter $a$ be 10. Then, the weights of all letters of the password are: $weight(h) = 17$, $weight(a) = 10$, $weight(c) = 12$, $weight(k) = 20$, $weight(e) = 14$, $weight(r) = 1$, $weight(n) = 23$, so the strength of the password is $17+10+12+20+14+1+1+10+23+20=128$.

## Input Format

In the first line, there is a string $password$ denoting the password.

In the second line, there is an integer $weight\_a$ denoting the weight of letter $a$

## Output Format

The only line of the output must contain an integer denoting the strength of the password.

## Constraints

- $1 \le |password| \le 100$
- $password$ consists of English lowercase letters only
- $0 \le weight\_a \le 25$

## Sample Tests

### Test 1

```
hellomrz
2
```

### Test 2

```
91
```

### Test 3

```
aaaaa
1
```

### Test 4

```
5
```
