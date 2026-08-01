# Number of zero-xor subsets

- **Domain:** shell
- **Difficulty:** Medium
- **Max Score:** 40
- **Success Ratio:** 0.6925704526046115
- **Total Submissions:** 1171
- **Solved Count:** 811
- **URL:** https://www.hackerrank.com/challenges/number-of-subsets

## Problem Statement

You are given an integer $N$. Consider set $S = \{0,\ 1,\ldots ,\ 2 ^ N - 1\} $. How many subsets $A\subset S$ with $ \bigoplus_{x \in A}x = 0$ ($ \oplus $ denotes xor operation) are there?  
Print your answer modulo $(10^9 + 7)$.  
Note that the  xorsum of an empty set is zero!  

**Input Format**  
The first line contains one integer $T$, the number of testcases.  
The next $T$ lines contain one integer $N$ each.

**Output Format**  
Output $T$ lines. Each line is one number, answer to the problem modulo $10^9 + 7$.

**Constraints**  
$ 1 \le T \le 10000 $  
$ 1 \le N \le 10 ^ {18} $

**Sample Input**  

	2
    1
    2
    
**Sample Output**  

	2
    4
    
**Explanation**  
For $N = 1$ there are $2$ sets - $\varnothing$ and $\{0\}$.  
For $N = 2$ there are $4$ sets - $\varnothing$, $\{0\}$, $\{1,\ 2,\ 3\}$, $\{0,\ 1,\ 2,\ 3\}$.


## Input Format

The first line contains one integer , the number of testcases.

The next  lines contain one integer  each.

## Output Format

Output  lines. Each line is one number, answer to the problem modulo .

## Sample Input

1
2

## Sample Output

4

## Explanation

For  there are  sets -  and .

For  there are  sets - , , , .
