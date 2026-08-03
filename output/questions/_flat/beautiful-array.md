# Beautiful Array

---

| Field | Value |
|---|---|
| **Slug** | `beautiful-array` |
| **Contest** | hourrank-1 |
| **Difficulty** | Easy |
| **Score** | 30 |
| **URL** | https://www.hackerrank.com/challenges/beautiful-array |

---

## Problem Statement

Shafaet did an excellent job of organizing the first HourRank round. As a reward, his professor gave him an array of numbers to play with. But Shafaet prefers playing with "beautiful" arrays, which are arrays that have equal elements.
 
The professor has one array $a$ with $n$ elements, and that array isn't always "beautiful.” To ensure array $a$ has equal elements, the professor has 2 options:

1. Choose two elements of array $a$. DECREASE the first element by 1 and INCREASE the second element by 1. This operation costs $k$ coins. 

2. Choose one element of array $a$ and INCREASE it by 1. This operation costs $l$ coins.

What’s the minimum number of coins the professor needs to turn his array into a “beautiful” array for Shafaet? 

**Input Format**<br>

The first line of input contains three space-separated integers: $n$, $k$, $l$. Integer $n$ is the size of array $a$. Integer $k$ is the number of coins needed to perform the first operation. Integer $l$ is the number of coins needed to perform the second operation. 

The second line contains $n$ integers $a_1, a_2, \ldots, a_n$, representing array $a$.

**Constraints:**<br>

$1\leq n, k, l \leq 1000$<br>
$1 \leq a_i \leq 1000$

 **Output Format**<br>
 
In single line, print one integer number: the minimum number of coins required to make the "beautiful" array.

**Sample Input 1:**<br>

    4 1 2
    3 4 2 2

**Sample Output 1:**<br>

    3
    
**Sample Input 2:**<br>

    3 2 1
    5 5 5

**Sample Output 2:**<br>

    0
