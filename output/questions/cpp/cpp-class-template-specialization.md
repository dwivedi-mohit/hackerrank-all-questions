# C++ Class Template Specialization

---

| Field | Value |
|---|---|
| **Slug** | `cpp-class-template-specialization` |
| **Domain** | cpp |
| **Difficulty** | Medium |
| **Score** | 35 |
| **URL** | https://www.hackerrank.com/challenges/cpp-class-template-specialization |

---

## Preview

Class templates in C++ create specializations for certain types.  These can be used when difficult to provide a generic implementation.

## Problem Statement

You are given a *main* function which reads the enumeration values for two different types as input, then prints out the corresponding  [enumeration](http://en.cppreference.com/w/cpp/language/enum) names. Write a class template that can provide the names of the enumeration values for both types. If the enumeration value is not valid, then print `unknown`.

## Input Format

The first line contains $t$, the number of test cases.		
Each of the $t$ subsequent lines contains two space-separated integers. The first integer is a color value, $c$, and the second integer is a fruit value, $f$.

## Output Format

The locked stub code in your editor prints $t$ lines containing the *color* name and the *fruit* name corresponding to the input enumeration index.

## Constraints

- $1 \le t \le 100$

- $-2 \times 10^9 \le c \le 2 \times 10^9$

- $-2 \times 10^9 \le f \le 2 \times 10^9$

## Sample Tests

### Test 1

```
2
1 0
3 3
```

### Test 2

```
green apple
unknown unknown
```
