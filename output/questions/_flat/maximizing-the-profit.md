# Maximizing the Profit

---

| Field | Value |
|---|---|
| **Slug** | `maximizing-the-profit` |
| **Contest** | hourrank-27 |
| **Difficulty** | Medium |
| **Score** | 50 |
| **URL** | https://www.hackerrank.com/challenges/maximizing-the-profit |

---

## Problem Statement

A hardware company is building a machine with exactly $3$ hardware components. There are many components available, and the profit factor of each component is known. The profit obtained by the machine is the product of the profit factors of the $3$ hardware components used to build that machine.

However, there is a catch. Three different components with numbers $i < j < k$ can be used to build the machine if and only if their profit factors are $p_i < p_j < p_k$.
 
Calculate the maximum possible profit that a valid machine consisting of three components can have, or decide that it's impossible to build any machine. Complete the function `maximumProfit` which takes in the integer array denoting the profit factors of all components and returns a single integer denoting the answer.

## Input Format

The first line contains a single integer $n$, denoting the number of available components. Components are numbered $0$ to $n-1$.  
The second line contains $n$ space-separated integers $p_0, p_1, \ldots, p_{n-1}$, i.e the integer array  $p$ denoting the profit factors of the components.

## Output Format

Print $-1$ if it's impossible to build any machine. Otherwise, print a single integer denoting the maximum possible profit that a valid machine consisting of $3$ components can have.

## Constraints

- $1 \leq n \leq 3 \cdot 10^{5}$
- $-10^{6} \leq p_i \leq 10^{6}$
