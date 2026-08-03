# Guga's Function

---

| Field | Value |
|---|---|
| **Slug** | `gugas-function` |
| **Contest** | hourrank-2 |
| **Difficulty** | Easy |
| **Score** | 40 |
| **URL** | https://www.hackerrank.com/challenges/gugas-function |

---

## Problem Statement

Guga has a function $F$ where $F(x)$ is a number of *interesting* segments in the [binary representation](https://en.wikipedia.org/wiki/Binary_number) of $x$.<br>

A segment is *interesting* if it has the following properties:

- The first and last characters are $1$'s.
- All the other characters are $0$'s. 
- It has a length of at least $3$.

For example, the binary representation of $37$ is $100101$, and it contains two *interesting* segments: $1001$ and $101$. So $F(37)=2$.

Guga defined a variable $M$ by following equation:

$M=F(0)+F(1)+F(2)+...+F(2^N)$.

Given the value of $N$ can you help Guga to calculate $M$. As the answer can be very big, calculate just $M$ modulo $(10^{9}+9)$.

## Input Format

A single line of input contains one number, $N$.

**Constraints:**<br>

For full score: $3 \le N \le 10^6$<br>
For $40\%$ score: $3 \le N \le 20$

## Output Format

Print the value of $M$ % $(10^{9}+9)$ in a single line.

**Sample Input 1**

	4

**Sample Output 1**
	
    5
    
**Sample Input 2**

	5

**Sample Output 2**

	17
