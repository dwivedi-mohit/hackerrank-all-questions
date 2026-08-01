# GCD Matrix

- **Domain:** python
- **Difficulty:** Hard
- **Max Score:** 60
- **Success Ratio:** 0.6671932596103213
- **Total Submissions:** 1899
- **Solved Count:** 1267
- **URL:** https://www.hackerrank.com/challenges/gcd-matrix

## Problem Statement

Alex has two arrays defined as $A = [a_0, a_1, \ldots, a_{n-1}]$ and $B = [b_0, b_1, \ldots, b_{m-1}]$. He created an $n \times m$ matrix, $M$, where $M_{i,j} = \gcd(a_i, b_j)$ for each $i,j$ in $M$. Recall that $\gcd(a, b)$ is the [greatest common divisor](https://en.wikipedia.org/wiki/Greatest_common_divisor) of $a$ and $b$. 

For example, if $A = [2, 3]$ and $B = [5, 6]$, he builds $M = [[1, 2], [1, 3]]$ like so:

| $(i,j)$ | $0$ | $1$ |
| -- | -- | -- |
| $0$ | $\gcd(2,5) = 1$ | $\gcd(2,6) = 2$ |
| $1$ | $\gcd(3,5) = 1$ | $\gcd(3,6) = 3$ |

Alex's friend Kiara loves matrices, so he gives her $q$ questions about matrix $M$ where each question is in the form of some submatrix of $M$ with its upper-left corner at $M_{r_1, c_1}$ and its bottom-right corner at $M_{r_2, c_2}$. For each question, find and print the number of *distinct* integers in the given submatrix on a new line.

## Input Format

The first line contains three space-separated integers describing the respective values of $n$ (the size of array $A$), $m$ (the size of array $B$), and $q$ (Alex's number of questions).		
The second line contains $n$ space-separated integers describing $a_0, a_1, \ldots, a_{n-1}$.		
The third line contains $m$ space-separated integers describing $b_0, b_1, \ldots, b_{m-1}$.		
Each line $i$ of the $q$ subsequent lines contains four space-separated integers describing the respective values of $r_1$, $c_1$, $r_2$, and $c_2$ for the $i^{th}$ question (i.e., defining a submatrix with upper-left corner $(r_1, c_1)$ and bottom-right corner $(r_2, c_2)$).

## Output Format

For each of Alex's questions, print the number of *distinct* integers in the given submatrix on a new line.

## Constraints

* $1 \le n, m \le 10^5$  
* $1 \le a_i, b_i \le 10^5$  
* $1 \le q \le 10$  
* $0 \le r_1, r_2 \lt n$  
* $0 \le c_1, c_2 \lt m$  

**Scoring**  

* $1 \le n, m \le 1000$ for $25\%$ of score.  
* $1 \le n, m \le 10^5$ for $100\%$ of score.  

## Sample Input

3 3 3
1 2 3
2 4 6
0 0 1 1
0 0 2 2
1 1 2 2

## Sample Output

2
3
3

## Explanation

Given  and , we build the following :

The diagram below depicts the submatrices for each of the  questions in green:

- For the submatrix between  and , the set of integers is . The number of distinct integers is .

- For the submatrix between  and , the set of integers is . The number of distinct integers is .

- For the submatrix between  and , the set of integers is . The number of distinct integers is .
