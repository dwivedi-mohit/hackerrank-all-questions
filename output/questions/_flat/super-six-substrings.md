# Super Six Substrings

---

| Field | Value |
|---|---|
| **Slug** | `super-six-substrings` |
| **Contest** | hourrank-18 |
| **Difficulty** | Medium |
| **Score** | 30 |
| **URL** | https://www.hackerrank.com/challenges/super-six-substrings |

---

## Problem Statement

David loves numeric strings. He considers a substring of a numeric sequence to be *super* if both of the following conditions are satisfied:

* The substring's integer representation is divisible by $6$.
* It does not contain [leading zeroes](https://en.wikipedia.org/wiki/Leading_zero) (e.g., `6` is super, but `06` is not).

In addition, he considers the one-character substring `0` to be super.

For example, $s = \texttt{"606"}$ has five super substrings: `6`, `0`, `6`, `60`, and `606`.

Given $s$, find and print the total number of super substrings in $s$.

**Note:** The length of the numbers represented by $s$ and its substrings are likely to be outside of the bounds of what numeric data types can represent.

## Input Format

A single numeric string denoting $s$.

## Output Format

Print an integer denoting the number of super substrings.

## Constraints

- $1 \le |s| \le 10^5$
