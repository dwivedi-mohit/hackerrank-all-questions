# Summing the K-N series 

- **Domain:** java
- **Difficulty:** Advanced
- **Max Score:** 40
- **Success Ratio:** 0.2828507795100223
- **Total Submissions:** 898
- **Solved Count:** 254
- **URL:** https://www.hackerrank.com/challenges/summing-the-k-n-series

## Problem Statement

You are given a sequence whose $n^{\text{th}}$ term is  
$$T_n = n^K$$
You have to evaluate the series
$$S_n = T_1 + T_2 + T_3 + \cdots + T_n$$
Find $S_n \bmod (10^9+7)$.

**Input Format**  

The first line of input contains $T$, the number of test cases.  

Each test case consists of one line containing two space-separated integers $n$ and $K$.  

**Output Format**  

For each test case, print the required answer in a line.  

**Constraints**  

$1 \le T \le 10$  
$0 \le K \le 10^3$  
$1 \le n \le 10^{16}$  

**Sample Input**

    3
    5 3
    4 2
    4 1
    
**Sample Output**  

    225
    30
    10
    
**Explanation**  

Case 1: We have $225 = 1^3 + 2^3 + 3^3 + 4^3 + 5^3$  
Case 2: We have $30  = 1^2 + 2^2 + 3^2 + 4^2$  
Case 3: We have $10  = 1^1 + 2^1 + 3^1 + 4^1$  


## Input Format

The first line of input contains , the number of test cases.

Each test case consists of one line containing two space-separated integers  and .

## Output Format

For each test case, print the required answer in a line.

## Sample Input

5 3
4 2
4 1

## Sample Output

30
10

## Explanation

Case 1: We have

Case 2: We have

Case 3: We have
