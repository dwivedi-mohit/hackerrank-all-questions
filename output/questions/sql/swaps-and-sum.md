# Swaps and Sum

- **Domain:** sql
- **Difficulty:** Advanced
- **Max Score:** 120
- **Success Ratio:** 0.641218872870249
- **Total Submissions:** 3052
- **Solved Count:** 1957
- **URL:** https://www.hackerrank.com/challenges/swaps-and-sum

## Problem Statement

You are given a sequence $a_1, a_2, \dots, a_n$. The task is to perform the following queries on it:

**Type 1.** Given two integers $l$ and $r$ $(1 \le l < r \le n;~r-l+1~is~even)$. Reorder the elements of the sequence in such a way (changed part of the sequence is in brackets):
$$a_1, a_2, ..., a_n \to a_1, a_2, ..., a_{l-2}, a_{l-1}, [a_{l+1}, a_{l}, a_{l + 3}, a_{l+2}, ..., a_{r}, a_{r-1}], a_{r+1}, a_{r+2}, ..., a_n$$
That is swap the first two elements of segment $[l, r]$, the second two elements, and so on.

**Type 2.** Given two integers $l$ and $r$, print the value of sum $\sum\limits_{i=l}^{r} a_i$.

**Input Format**  

The first line contains two integers $n$ and $q$. The second line contains $n$ integers $a_1, a_2, \dots, a_n$, denoting initial sequence.

Each of the next $q$ lines contains three integers $tp_i, l_i, r_i$, where $tp_i$ denotes the type of the query, and $l_i, r_i$ are parameters of the query. It's guaranteed that for a first-type query $(r - l + 1)$ will be even.  

**Constraints**  
$2 \le n \le 2 \times 10^5$  
$1 \le q \le 2 \times 10^5$  
$1 \le a_i \le 10^6$  
$1 \le tp_i \le 2$  
$1 \le l_i \le r_i \le n$


**Output Format**

For each query of the second type print the required sum.

**Sample Input**

    6 4
    1 2 3 4 5 6
    1 2 5
    2 2 3
    2 3 4
    2 4 5
   
**Example Output**

    5
    7
    9
    
**Explanation**

After the first query the sequence becomes [1, 3, 2, 5, 4, 6]. 

## Input Format

The first line contains two integers  and . The second line contains  integers , denoting initial sequence.

Each of the next  lines contains three integers , where  denotes the type of the query, and  are parameters of the query. It's guaranteed that for a first-type query  will be even.

## Output Format

For each query of the second type print the required sum.

## Sample Input

6 4
1 2 3 4 5 6
1 2 5
2 2 3
2 3 4
2 4 5

Example Output

5
7
9

## Explanation

After the first query the sequence becomes [1, 3, 2, 5, 4, 6].
