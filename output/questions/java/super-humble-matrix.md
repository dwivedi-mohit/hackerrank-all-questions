# Super Humble Matrix

- **Domain:** java
- **Difficulty:** Medium
- **Max Score:** 40
- **Success Ratio:** 0.7894736842105263
- **Total Submissions:** 437
- **Solved Count:** 345
- **URL:** https://www.hackerrank.com/challenges/super-humble-matrix

## Problem Statement

Sherry likes matrices a lot, but her favorite ones are *humble matrices*. An $N \times M$ matrix (we'll call it $A$) is *humble* if:

- It contains all the elements in range $[1 , N \times M ]$ exactly once.
- For any $2$ elements $(i_1, j_1)$ and $(i_2, j_2)$ in matrix $A$:<br>
	If $i_1 + j_1 \lt i_2 + j_2$ , then $A_{i_1, j_1} \lt A_{i_2, j_2}$ should hold. 
    
Given $N$ and $M$, find and print the total number of possible humble matrices; as this number can be quite large, print your answer modulo $10^9+7$.

## Input Format

Two space-separated integers, $N$ and $M$, respectively.

## Output Format

Print the total number of humble matrices possible, modulo $10^9+7$.

**Sample Input 0**

    2 2
    
    
**Sample Output 0**

	2

**Sample Input 1**

    3 2
    
    
**Sample Output 1**

	4


    
    
    

## Constraints

- $1 \le N,M \le 10^6$

**Scoring**

* $1 \le N,M \le 10^3$ for $30\%$ of the test data.  
* $1 \le N,M \le 10^6$ for $100\%$ of the test data.

## Sample Input

2 2

## Sample Output

2

## Explanation

There are  possible  humble matrices:

- [ 1, 2 ]

[ 3, 4 ]

- [ 1, 3 ]

[ 2, 4 ]

Thus, we print the result of , which is .
