# Day 29: Look at Everything We've Learned!

---

| Field | Value |
|---|---|
| **Slug** | `day-29-look-at-everything-weve-learned` |
| **Contest** | 30-days-of-code |
| **Difficulty** | Medium |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/day-29-look-at-everything-weve-learned |

---

## Problem Statement

Welcome to Day 29! Check out the tutorial on [programming language fundamentals](https://youtu.be/nc6nJYdGUAU), or just jump right into the problem. Congratulations on finishing the series, and good luck!

Suppose you have some string $S$ having length $N$ that is indexed from $0$ to $N-1$. You also have some string $R$ that is *the reverse* of string $S$. $S$ is *funny* if the condition $|S_i-S_{i-1}| = |R_i-R_{i-1}|$ is true for every $i$ from $1$ to $N-1$.

**Note:** For some string $str$, $str_i$ denotes the [ASCII](https://en.wikipedia.org/wiki/ASCII) value of the $i^{th}$ $0$-indexed character in $str$. The *absolute value* of some integer, $x$, is written as $|x|$.

## Input Format

The first line contains an integer, $T$ (the number of test cases). 	
The $T$ subsequent lines each contain one string $S$.  

**Constraints**  	
$1 \leq T \leq 10$  	
$2 \leq \text{length of }S \leq 10000$

## Output Format

For each string $S$, print whether it is **Funny** or **Not Funny** on a new line (i.e.: the $i^{th}$ line of output should be the answer for input string $S_i$).
