# Fibonacci GCD

- **Domain:** data-structures
- **Difficulty:** Hard
- **Max Score:** 80
- **Success Ratio:** 0.6195348837209302
- **Total Submissions:** 1075
- **Solved Count:** 666
- **URL:** https://www.hackerrank.com/challenges/fibonacci-gcd

## Problem Statement

Fibonacci numbers have the following form:  
$$F_1 = 1 \\\
F_2 = 1 \\\
F_3 = 2 \\\
\vdots \\\
F_n = F_{n-2}+F_{n-1}$$  

We have an array $a_1, a_2, \ldots, a_N$ which contains $N$ elements.   

We want to find $\gcd(F_{a_1},F_{a_2},F_{a_3}, \cdots ,F_{a_N} )$.  

**Input Format**  
The first line contains $N$, where $N$ denotes size of the array.  
Each of the next $N$ lines contains a number: the $i^{\text{th}}$ line contains $a_i$.

**Output Format**  
Print a single integer — the remainder of the division of the resulting number by $10^9+7$.  

**Constraints**  
$1 \le N \le 2 \times 10^5$   
$1 \le a_i \le 10^{12}$  


**Sample Input 1**

    3
    2
    3
    5

**Sample Output 1**

    1

**Explanation 1**  
$F_2 = 1$  
$F_3 = 2$  
$F_5 = 5$   
$\gcd(1,2,5)=1$  


**Sample Input 2**

    2
    3
    6

**Sample Output 2**

    2

**Explanation 2**  
$F_3 = 2$  
$F_6 = 8$  
$\gcd(2,8)=2$  





## Input Format

The first line contains , where  denotes size of the array.

Each of the next  lines contains a number: the  line contains .

## Output Format

Print a single integer — the remainder of the division of the resulting number by .

## Sample Input

3
2
3
5

## Sample Output

1
