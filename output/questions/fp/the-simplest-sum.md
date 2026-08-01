# The Simplest Sum

- **Domain:** fp
- **Difficulty:** Medium
- **Max Score:** 50
- **Success Ratio:** 0.552
- **Total Submissions:** 250
- **Solved Count:** 138
- **URL:** https://www.hackerrank.com/challenges/the-simplest-sum

## Problem Statement

You are just learning to code and are finished with loops and functions. Now, you are given the following pseudocode:

```cpp
/*
 * The function has two integer parameters: k and n
 * The function returns the value of sum
 */
function f(k, n) {
    sum = 0;

    for (i = 1; i ≤ n; i += 1) {
        sum += i;
        i *= k;
    }

    return sum;
}
```

For three given integers $k$, $a$, and $b$, find the value of $S \bmod \left(10^{9} + 7\right)$, where $S$ is defined as:
$$S = \sum_{n\ =\ a}^{b} f(k,\ n)$$

## Input Format

The first line of the input is an integer $Q$, the total number of queries. Each of the next $Q$ lines contains three space separated integers $k$, $a$, and $b$.

## Output Format

For each query, print the value of $S \bmod \left(10^{9} + 7\right)$ on a new line.

## Constraints

- $1 \le Q \le 10^{5}$
- $2 \le k \le 10^{5}$
- $1 \le a \le b \le 10^{18}$

## Sample Input

2 1 5
3 1 5
4 1 5
5 1 5

## Sample Output

13
10
5

## Explanation

- Query 2 1 5

So,

- Query 3 1 5

So,

- Query 4 1 5

So,

- Query 5 1 5

So,
