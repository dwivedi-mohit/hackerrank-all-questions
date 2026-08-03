# Turn Off the Lights

---

| Field | Value |
|---|---|
| **Slug** | `turn-off-the-lights` |
| **Domain** | algorithms |
| **Difficulty** | Hard |
| **Score** | 70 |
| **URL** | https://www.hackerrank.com/challenges/turn-off-the-lights |

---

## Preview

Find the minimum cost of turning off all the bulbs.

## Problem Statement

There are $n$ bulbs in a straight line, numbered from $0$ to $n - 1$. 
Each bulb $i$ has a button associated with it, and there is a *cost*, $c_i$, for pressing this button. When some button $i$ is pressed, all the bulbs at a distance $\le k$ from bulb $i$ will be toggled(off->on, on->off). 

Given $n$, $k$, and the costs for each button, find and print the minimum cost of turning off all $n$ bulbs if they're all on initially.

## Input Format

The first line contains two space-separated integers describing the respective values of $n$ and $k$.		
The second line contains $n$ space-separated integers describing the respective costs of each bulb (i.e., $c_0, c_1, \ldots, c_{n - 1}$).

## Output Format

Print a long integer denoting the minimum cost of turning off all $n$ bulbs.

## Constraints

* $3 \le n \le 10^4$
* $0 \le k \le 1000$
* $0 \le c_i \le 10^9$

## Sample Tests

### Test 1

```
3 1
1 1 1
```

### Test 2

```
1
```
