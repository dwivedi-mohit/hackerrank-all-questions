# Super Kth LIS

- **Domain:** c
- **Difficulty:** Advanced
- **Max Score:** 90
- **Success Ratio:** 0.7586685159500693
- **Total Submissions:** 1442
- **Solved Count:** 1094
- **URL:** https://www.hackerrank.com/challenges/super-kth-lis

## Problem Statement

Given an array of $N$ integers ($a_0, a_1, \ldots, a_{N-1}$), find all possible increasing subsequences of maximum length, $L$. Then print the lexicographically $K^{th}$ longest increasing subsequence as a single line of space-separated integers; if there are less than $K$ subsequences of length $L$, print $\texttt{-1}$.

Two subsequences $[a_{p_0}, a_{p_1}, \ldots, a_{p_{L-2}}, a_{p_{L-1}}]$ and $[a_{q_0}, a_{q_1}, a_{q_2}, \ldots, a_{q_{L-2}}, a_{q_{L-1}}]$ are considered to be *different* if there exists at least one $i$ such that $p_i \ne q_i$.

## Input Format

The first line contains $2$ space-separated integers, $N$ and $K$, respectively.	
The second line consists of $N$ space-separated integers denoting $a_0, a_1, \ldots, a_{N-1}$ respectively.

## Output Format

Print a single line of $L$ space-separated integers denoting the lexicographically $K^{th}$ longest increasing subsequence; if there are less than $K$ subsequences of length $L$, print $\texttt{-1}$.

**Note:** $L$ is the length of longest increasing subsequence in the array.

**Sample Input 0**

    5 3
    1 3 1 2 5
    
**Sample Output 0**

    1 3 5
    
**Sample Input 1**

    5 2
    1 3 2 4 5
    
**Sample Output 1**

    1 3 4 5    

## Constraints

- $1 \le N \le 10^{5}$   
- $1 \le K \le 10^{18}$  
- $1 \le a_i \le N$

**Scoring**

* $1 \le N \le 10^3$ for $30\%$ of the test data.  
* $1 \le N \le 10^5$ for $100\%$ of the test data.

## Sample Input

5 3
1 3 1 2 5

## Sample Output

1 3 5

## Explanation

Sample Case 0:

The longest possible increasing subsequences in lexicographical order are:

-

-

-

Notice that the first and second subsequences appear the same; they are actually both different because the  in the first subsequence comes from array element , and the  in the second subsequence comes from array element . Because , we print the  one () as a single line of space-separated integers.

Sample Case 1:

The longest possible increasing subsequences in lexicographical order are:

-

-

Because , we print the  one () as a single line of space-separated integers.
