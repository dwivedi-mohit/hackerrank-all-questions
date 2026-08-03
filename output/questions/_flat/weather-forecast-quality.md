# Weather Forecast Quality

---

| Field | Value |
|---|---|
| **Slug** | `weather-forecast-quality` |
| **Domain** | misc |
| **Difficulty** | Easy |
| **Score** | 15 |
| **Contest** | 101hack54 |
| **URL** | https://www.hackerrank.com/challenges/weather-forecast-quality |

---

## Preview

Explore a quality of a weather forecast.

## Problem Statement

In a weather forecast, given the actual and forecasted temperatures for each day of a week, find the sum of the weather forecast inaccuracies across all $7$ days. The *weather forecast inaccuracy* on any day is the absolute difference of the actual temperature and the forecasted temperature. 

Complete the function `totalForecastInaccuracy` which takes in two integer arrays $t$, denoting actual temperatures, and $f$, denoting forecasted temperatures, across $7$ days and returns the sum of the weather forecast inaccuracies across $7$ days.

## Input Format

The first line contains $7$ space-separated integers $t_1$, $t_2$, ..., $t_7$.

The second line contains $7$ space-separated integers $f_1$, $f_2$, ..., $f_7$.

## Output Format

Print a single integer denoting the answer.

## Constraints

- $-100 \leq t_i, f_i \leq 100$

## Sample Tests

### Test 1

```
14 13 12 13 16 18 21
15 11 12 11 16 19 24
```

### Test 2

```
9
```
