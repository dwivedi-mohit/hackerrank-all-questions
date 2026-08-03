# Stacy numbers

---

| Field | Value |
|---|---|
| **Slug** | `stacy-numbers` |
| **Contest** | hourrank-5 |
| **Difficulty** | Hard |
| **Score** | 80 |
| **URL** | https://www.hackerrank.com/challenges/stacy-numbers |

---

## Problem Statement

Stacy loves playing with numbers. She made a sequence of digits and wrote down all its *valid sub-segments* as a new array $A$. 

A *sub-segment* is defined here as a consecutive part of an $N$-digit sequence. Sub-segments with leading zeros are not valid. For example valid sub-segments of the sequence $1205$ are $\{1,12,120,1205,2,20,205,0, 5\}$. Note that $0$ is a valid sub-segment, but $05$ is not.

Stacy sorts her new array $A$ in *ascending* order, about which she has $Q$ questions. $I^{th}$ question is,"Which number is $A_{B_I}$?" (In other words, which number is in $B_I^{th}$ position in array $A$?)

Help Stacy answer her questions and print each $answer_I$  modulo $(10^9+7)$ on a new line. 

*Note*: Position of array $A$ starts from $1$.

## Input Format

The first line contains $N$ (size of the sequence) and $Q$ (number of questions).<br>
The second line contains $N$ digits (Stacy's initial sequence).<br>
The $Q$ subsequent lines each contain a question: an integer corresponding to some index $B_I$.<br>

**Constraints**<br>
$1\le N \le 10^5$<br>
$1\le Q \le 10^5$<br>
It's guaranteed that the ${B_i}^{th}$ number exists.<br>
$1 \le B_i < B_{i+1}$ for $1\le i <Q $

## Output Format

For each question, find the number in index $B_I$ and print the $answer_I$  modulo $(10^9+7)$ on a new line.
