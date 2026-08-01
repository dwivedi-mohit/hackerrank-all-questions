# Summing the K-N-R Series 

- **Domain:** data-structures
- **Difficulty:** Advanced
- **Max Score:** 80
- **Success Ratio:** 0.41324921135646686
- **Total Submissions:** 317
- **Solved Count:** 131
- **URL:** https://www.hackerrank.com/challenges/summing-the-k-n-r-series

## Problem Statement

You are given a sequence whose $n^{\text{th}}$ term is  
$$T_n = n^K \times R^n$$
You have to evaluate the series
$$S_n = T_1 + T_2 + T_3 + \cdots + T_n$$
Find $S_n \bmod (10^9+7)$.

**Input Format**  

The first line of input contains $T$, the number of test cases.  
Each test case consists of three lines, each containing $K$, $n$ and $R$ respectively.  

**Output Format** 

For each test case, print the required answer in a line.  

**Constraints**  

$1 \le T \le 10$  
$1 \le K \le 10^{3}$  
$1 \le n \le 10^{16}$  
$2 \le R \le 10^{16}$  
$R\bmod (10^9 + 7) \not= 1$  

**Sample Input**  

	2
    2
    5
    2
    3
    4
    3
    
**Sample Output**  

	1146
    5988

**Explanation**  

Case 1: $1146 =  1^2\times 2^1   +   2^2\times 2^2   +   3^2\times 2^3   +   4^2\times 2^4   +   5^2\times 2^5$  
Case 2: $5988 = 1^3\times 3^1   +   2^3\times 3^2   +   3^3\times 3^3   +   4^3\times 3^4$  


## Input Format

The first line of input contains , the number of test cases.

Each test case consists of three lines, each containing ,  and  respectively.

## Output Format

  

## Sample Input

2
5
2
3
4
3

## Sample Output

5988

## Explanation

Case 1:

Case 2:
