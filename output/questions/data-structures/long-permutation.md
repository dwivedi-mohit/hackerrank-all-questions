# Long Permutation

- **Domain:** data-structures
- **Difficulty:** Hard
- **Max Score:** 50
- **Success Ratio:** 0.6626984126984127
- **Total Submissions:** 252
- **Solved Count:** 167
- **URL:** https://www.hackerrank.com/challenges/long-permutation

## Problem Statement

Consider an inifite array, $a$, of positive numbers, $a_1, a_2, \dots$, where each $a_i = i$. You can apply a permutation, $p$, of size $n$ (i.e., $n$ different numbers $1 \le p_1, \ldots, p_{n} \le n$) to the $n$-element subset of your array from $a_1$ through $a_{n}$ in the following way:  

$$ (a_1, \dots, a_{n}) \rightarrow (a_{p_{1}}, \dots, a_{p_{n}}).$$ 
   
To get infinite array $b$, you must apply permutation $p$ to the first $n$ elements ($a_1$ to $a_{n}$), then to elements $a_2$ through $a_{n+1}$, then to elements $a_3$ through $a_{n+2}$, and so on, infinitely many times. 

Given the values of $n$, $m$, and $p$, find and print the value of $b_m$. See the *Explanation* section below for more detail. 

**Note:** This challenge uses $1$-based array indexing.

## Input Format

The first line contains $2$ space-separated integers, $n$ and $m$, respectively.  
The second line contains $n$ space-separated integers describing the respective values of $p_1, p_2, \dots, p_{n}$.

## Output Format

Print a single integer denoting the value of $b_m$.

**Sample Input 0**

    2 10
    2 1
    
**Sample Output 0**

	11

**Sample Input 1**

	3 1
	2 3 1
    
**Sample Output 1**

	2
    
**Sample Input 2**

	3 10
    2 3 1
    
**Sample Output 2**

	10 

## Constraints

- $1 \le n \le 10^5$
- $1 \le m \le 10^{18}$  
- $1 \le p_1, p_2, \dots, p_{n} \le n$, and each $p_i$ is unique.  

## Sample Input

2 10
2 1

## Sample Output

11

## Explanation

Sample Case 0 has the following sequence of array transformations:

As you can see, each . Thus, we know that .

Sample Case 1 and Sample Case 2 have the following sequence of array transformations:

As you can see,  and .
