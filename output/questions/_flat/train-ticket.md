# Train Ticket

---

| Field | Value |
|---|---|
| **Slug** | `train-ticket` |
| **Domain** | misc |
| **Difficulty** | Easy |
| **Score** | 10 |
| **Contest** | 101hack53 |
| **URL** | https://www.hackerrank.com/challenges/train-ticket |

---

## Preview

Given the seat number, determine the type of seat.

## Problem Statement

You have to identify the type of berth of a given seat in the sleeper class of the [Indian Railways](http://en.wikipedia.org/wiki/Indian_Railways).


Every coach has $72$ seats, divided into nine compartments. Each compartment has:

- Six long berths: a pair of lower, a pair of middle and a pair of upper.
- Two side berths: a side-lower and a side-upper.

The starting seat number in any compartment is one more than the seat number of the last berth in the previous compartment. In particular, the $1^\text{st}$ berth (i.e lower) in the $1^\text{st}$ compartment is numbered $1$ . **See the diagram** below for the layout of the coach.

![image](https://s3.amazonaws.com/hr-assets/0/1511374256-27fde0b6e5-sleeper1.png)

Given a seat with number $n$, determine the type of berth it is.

Complete the function `berthType` which takes in an integer $n$ and returns a string identifying the type of berth, as described in the output format section.

## Input Format

The input consists of a single line containing a single integer $n$ denoting the seat number.

## Output Format

Print a single line containing the type of berth:

- Print `LB` if it is a lower berth.
- Print `MB` if it is a middle berth.
- Print `UB` if it is an upper berth.
- Print `SLB` if it is a side-lower berth.
- Print `SUB` if it is a side-upper berth.

## Constraints

- $1 \le n \le 72$

## Sample Tests

### Test 1

```
1
```

### Test 2

```
LB
```

### Test 3

```
72
```

### Test 4

```
SUB
```
