# John's Subway Commute

---

| Field | Value |
|---|---|
| **Slug** | `johns-subway-commute` |
| **Domain** | misc |
| **Difficulty** | Medium |
| **Score** | 50 |
| **Contest** | 101hack42 |
| **URL** | https://www.hackerrank.com/challenges/johns-subway-commute |

---

## Preview

Help John choose a *good* seat that will remain *good* for as long as possible.

## Problem Statement

John takes the subway to work every day. A subway car consists of a single line of zero-indexed seats, and we define a _good_ seat to be a seat that is empty on one or both sides; in other words, a *good* seat is *not* surrounded by occupied seats on *both* sides. 

A new passenger enters a subway car every $1$ minute until every seat in the car is occupied. John and all the subway passengers who enter the car after him choose their subway seats according to the following rules:

1. The best seats are the ones located at either end of the subway car (i.e., the very first and very last seats), because they will always be *good*. If both end seats are available, they choose the rightmost (last) one.
2. If an end seat isn't available, they choose a *good* seat that will remain *good* for as long as possible. 
3. If multiple seats will remain *good* for the same amount of time, then they choose the rightmost *good* seat. 

John wants to choose a seat keeping in mind that the passengers who enter after him will choose their seats in the same manner. Given a string, $s$, denoting the configuration of seats when John enters the subway car, find and print the zero-indexed seat number where he will choose to sit. Each string $s$ consists of the characters `E` (denoting an empty seat where John or a subsequent passenger may sit) and `O` (denoting a seat that is occupied by a passenger), only.

## Input Format

A single string, $s$, where each character is either an `E` (denoting an empty seat) or an `O` (denoting an occupied seat) describing the subway car's seating configuration at the time when John enters the car.

## Output Format

Print the zero-indexed seat number where John will choose to sit.

## Constraints

- $1 \le \text{ length of } s \le 10^{5}$
- It is guaranteed that there is at least one empty seat on the subway.

## Sample Tests

### Test 1

```
EEOEE
```

### Test 2

```
4
```

### Test 3

```
OEEEEO
```

### Test 4

```
2
```
