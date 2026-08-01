# Similar Strings

- **Domain:** c
- **Difficulty:** Advanced
- **Max Score:** 85
- **Success Ratio:** 0.5948422124194096
- **Total Submissions:** 5894
- **Solved Count:** 3506
- **URL:** https://www.hackerrank.com/challenges/similar-strings

## Problem Statement

Jimmy loves playing with strings. He thinks string $A$ is *similar* to string $B$ if the following conditions are satisfied:

* Both strings have the same length (i.e., $A = a_0 a_1 \ldots a_{n - 1}$ and $B = b_0 b_1 \ldots b_{n - 1}$). 
* For each valid pair of indices, $(i,j)$, in the strings, $[a_i = a_j$ and $b_i = b_j]$ or $[a_i \ne a_j$ and $b_i \ne b_j]$.  

For example, string $a = \texttt{"adba"}$ and $b = \texttt{"bcgb"}$ are similar as for $i = 0, j = 3$, $a[0] == a[3]$ and $b[0] == b[3]$ and for all other $i,j$ pairs $a[i] \ne a[j]$ as well as $b[i] \ne b[j]$.  
 
He has a string, $S$, of size $n$ and gives you $q$ queries to answer where each query is in the form of a pair of integers $(l_i, r_i)$. For each substring $S[l_i, r_i]$, find the number of substrings $S[x,y]$ where substring $S[l_i, r_i]$ is *similar* to substring $S[x,y]$ and print this number on a new line.

**Note:** Substring $S[x,y]$ is the contiguous sequence of characters from index $x$ to index $y$. For example, if $S = $ `abcdefgh`, then $S[3, 6] = $ `cdef`. 

## Input Format

The first line contains two space-separated integers describing the respective values of $n$ and $q$. 		
The second line contains string $S$.		
Each line $i$ of the $q$ subsequent lines contains two space-separated integers describing the respective values of $l_{i}$ and $r_{i}$ for query $i$.


## Output Format

For each query, print the number of similar substrings on a new line.

## Constraints

* $1 \le n, q \le 5 \times 10^4$
* $1 \le L_i \le R_i \le n$
* $s_i ∈ \{a, b, c, d, e, f, g, h, i, j\}$

## Sample Input

8 4
giggabaj
1 1
1 2
1 3
2 4

## Sample Output

6
2
1

## Explanation

We perform the following sequence of queries:

- Strings with length  are all similar, so our answer is .

- gi, ig, ga, ab, ba, and aj are similar, so our answer is .

- gig and aba are similar, so our answer is .

- igg has no similar string, so our answer is .
