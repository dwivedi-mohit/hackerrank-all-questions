# Day 3: Throw

---

| Field | Value |
|---|---|
| **Slug** | `js10-throw` |
| **Domain** | tutorials |
| **Difficulty** | Easy |
| **Score** | 15 |
| **URL** | https://www.hackerrank.com/challenges/js10-throw |

---

## Preview

Practice throwing errors` in JavaScript.

## Problem Statement

**Objective**

In this challenge, we practice using *throw* and *catch* statements to work with custom error messages. 

**Task**

Complete the *isPositive* function below. It has one integer parameter, $a$. If the value of $a$ is positive, it must return the string `YES`. Otherwise, it must *throw* an *Error* according to the following rules:

- If $a$ is $0$, *throw* an *Error* with $message = $ `Zero Error`.
- If $a$ is negative, *throw* an *Error* with $message = $ `Negative Error`.

## Input Format

Locked stub code in the editor reads the following input from stdin and passes each value of $a$ to the function as an argument:		
The first line is an integer, $n$, denoting the number of times the function will be called with some $a$.		
Each line $i$ of the $n$ subsequent lines contains an integer denoting some $a$.

## Output Format

If the value of $a$ is positive, the function must return the string `YES`. Otherwise, it must *throw* an *Error* according to the following rules:

- If $a$ is $0$, *throw* an *Error* with $message = $ `Zero Error`.
- If $a$ is negative, *throw* an *Error* with $message = $ `Negative Error`.

## Constraints

- $1 \le n \le 5$
- $-100 \le a \le 100$

## Sample Tests

### Test 1

```
3
1
2
3
```

### Test 2

```
YES
YES
YES
```

### Test 3

```
3
2
0
6
```

### Test 4

```
YES
Zero Error
YES
```

### Test 5

```
2
-1
20
```

### Test 6

```
Negative Error
YES
```
