# The Most Elegant Sequence

---

| Field | Value |
|---|---|
| **Slug** | `the-most-elegant-sequence` |
| **Contest** | hourrank-28 |
| **Difficulty** | Medium |
| **Score** | 50 |
| **URL** | https://www.hackerrank.com/challenges/the-most-elegant-sequence |

---

## Problem Statement

In this problem, every string has a *beauty* value which is represented as a positive integer.  

The *elegance* of a sequence of strings $(t_1, t_2, \ldots, t_k)$ is defined as $$B_{t_1} + (B_{t_1} \oplus B_{t_2}) + (B_{t_2} \oplus B_{t_3}) + \ldots + (B_{t_{k - 1}} \oplus B_{t_k})$$ where $B_{t_i}$ denotes the beauty of string $t_i$, and $\oplus$ represents the [bitwise XOR operation](https://en.wikipedia.org/wiki/Bitwise_operation#XOR). In particular, the elegance of a sequence of just one string is just the beauty value of that string. Also, the elegance of an empty sequence is $0$.  

Diane has $n$ strings $s_1, s_2, \ldots, s_n$, each consisting of the digits $0$ to $9$, and $s_i$ has beauty value $B_{s_i}$. She would like to form the most *elegant* sequence of strings among them. She can write any string with her *digit cards*; for every digit $d$ from $0$ to $9$, she has exactly $q$ cards in which the digit $d$ is written, so she has $10q$ cards in total. For example, 1 digit card each for every number $0$ to $9$ would be,

![image](https://s3.amazonaws.com/hr-assets/0/1528011426-b029eb2563-digitcards.png)

Furthermore:

- She may write the strings in any order, but she can only form each string at most once.
- To write a string, she has to use the cards. But each card can only be used once, so it may not be possible to write all strings. 

Given the above restrictions, what is the maximum elegance of any sequence that Diane can form?  

Complete the function `maximumElegance` which takes in an integer $q$, an array $s$ consisting of $n$ strings, and an array $b$ consisting of $n$ integers denoting their respective beauty values and returns the maximum elegance of any sequence that Diane can form.

## Input Format

The first line contains two space-separated integers $n$ and $q$.  

The second line contains $n$ space-separated integers $B_{s_1}, B_{s_2}, \ldots, B_{s_n}$ denoting the beauty values of the $n$ strings.  

The $i^\text{th}$ of the next $n$ lines contains the $i^\text{th}$ string, $s_i$.

## Output Format

Print a single integer denoting the maximum elegance which can be obtained by Diane.

## Constraints

- $1 \le n \le 19$  
- $1 \le q \le 10^5$  
- $1 \le |s_i| \le 10^4$  
- $s_i$ is a string of digits $0$-$9$.  
- $1 \le B_{s_i} \le 10^5$  

**Subtask**  

- For ~20% of the total score, $n \le 9$
