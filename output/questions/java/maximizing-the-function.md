# Maximizing the Function 

- **Domain:** java
- **Difficulty:** Hard
- **Max Score:** 70
- **Success Ratio:** 0.7589900535577658
- **Total Submissions:** 1307
- **Solved Count:** 992
- **URL:** https://www.hackerrank.com/challenges/maximizing-the-function

## Problem Statement

Consider an array of $n$ binary integers (i.e., $0$'s and $1$'s) defined as $A = [a_0, a_1, \ldots, a_{n-1}]$.

Let $f(i, j)$ be the [bitwise XOR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR) of all elements in the inclusive range between index $i$ and index $j$ in array $A$. In other words, $f(i, j) = a_i \oplus a_{i+1} \oplus \ldots \oplus a_{j}$. Next, we'll define another function, $g$:
$$g(x, y) = \sum \limits_{i = x}^y \sum \limits_{j = i}^y f(i, j)$$

Given array $A$ and $q$ independent queries, perform each query on $A$ and print the result on a new line. A query consists of three integers, $x$, $y$, and $k$, and you must find the maximum possible $g(x, y)$ you can get by changing *at most* $k$ elements in the array from $0$ to $1$ or from $1$ to $0$. 

**Note:** Each query is independent and considered separately from all other queries, so changes made in one query have no effect on the other queries. 

## Input Format

The first line contains two space-separated integers denoting the respective values of $n$ (the number of elements in array $A$) and $q$ (the number of queries).	
The second line contains $n$ space-separated integers where element $i$ corresponds to array element $a_i$ $(0 \leq i \lt n)$.		
Each line $i$ of the $q$ subsequent lines contains $3$ space-separated integers, $x_i$, $y_i$ and $k_i$ respectively, describing query $q_i$ $(0 \leq i < q)$.


## Output Format

Print $q$ lines where line $i$ contains the answer to query $q_i$ (i.e., the maximum value of $g(x_i, y_i)$ if no more than $k_i$ bits are changed).


## Constraints

- $1 \leq n, q\leq 5 \times 10^5$
- $0 \le a_i \le 1$
- $0 \le x_i \leq y_i \lt n$
- $0 \le k_i \le n$

**Subtask**

* $1 \leq n, q\leq 5000$ and $0\leq k_i \leq 1$ for $\text{40%}$ of the maximum score
* $n=5\times 10^5$, $m=5\times 10^5$ and $k_i=0$ for $\text{20%}$ of the maximum score


## Sample Input

3 2
0 0 1
0 2 1
0 1 0

## Sample Output

0

## Explanation

Given , we perform the following  queries:

- If we change  to , then we get  and .

- In this query, .
