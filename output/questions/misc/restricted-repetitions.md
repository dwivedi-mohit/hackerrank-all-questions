# Restricted Repetitions

---

| Field | Value |
|---|---|
| **Slug** | `restricted-repetitions` |
| **Domain** | misc |
| **Difficulty** | Expert |
| **Score** | 100 |
| **Contest** | regular-expresso |
| **URL** | https://www.hackerrank.com/challenges/restricted-repetitions |

---

## Preview

Write a regex expression to identify "hack" under the conditions.

## Problem Statement

<img src="https://s3.amazonaws.com/hr-challenge-images/15166/1449469605-358e06d0d1-Capture.PNG" title="Capture.PNG" />
The string $S$ is a variation of the word __hack__ with the following properties: 

- $S$ should consist of __`h`__, __`a`__, __`c`__ and __`k`__ only.

- __`h`__ should be repeated a _composite_ (not prime) number of times, and __`h`__ should repeat at least $4$ times.
- __`a`__ should be repeated a *composite* (not prime) number of times, and __`a`__ should repeat at least $6$ times.

- __`c`__ should be repeated *even* number of times and the number of repetitions must be greater than $0$.

- __`k`__ should be repeated an *odd* number of times, and __`k`__ should repeat at least $5$ and at most $21$ times. 

- $S$ must start with __`h`__ and end with __`k`__.
- **`h`**'s should be followed by **`a`**'s.

- **`a`**'s should be followed by **`c`**'s.

- **`c`**'s should be followed by **`k`**'s. 
- **`k`**'s should __not__ be followed by any other character.

Your task is to write a regex that will match the string $S$ from start to end.

## Sample Tests

### Test 1

```
hhhhaaaaaacckkkkk
```

### Test 2

```
true
```
