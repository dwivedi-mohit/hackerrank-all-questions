# Sherlock and Queries

- **Domain:** ai
- **Difficulty:** Advanced
- **Max Score:** 30
- **Success Ratio:** 0.3549165120593692
- **Total Submissions:** 5390
- **Solved Count:** 1913
- **URL:** https://www.hackerrank.com/challenges/sherlock-and-queries

## Problem Statement

Watson gives Sherlock an array $A$ of $N$ elements and two arrays $B$ and $C$, of $M$ elements each. Then he asks Sherlock to perform the following program:

    for i = 1 to M do
        for j = 1 to N do
            if j % B[i] == 0 then
                A[j] = A[j] * C[i]
            endif
        end do
    end do

This code needs to be optimized. Can you help Sherlock and tell him the resulting array $A$? You should print all the array elements modulo $(10^9 + 7)$.
          
**Input Format**     
The first line contains two integer, $N$ and $M$. The next line contains $N$ integers, the elements of array $A$. The last two lines contain $M$ integers each, the elements of array $B$ and $C$, respectively.

**Output Format**     
Print $N$ space-separated integers, the elements of array $A$ after performing the program modulo $(10^9 + 7)$.

**Constraints**  
$1 \le N, M \le 10^5$   
$1 \le B[i] \le N$   
$1 \le A[i], C[i] \le 10^5$

**Sample Input**

	4 3
	1 2 3 4
	1 2 3
	13 29 71
    
**Sample Output**

	13 754 2769 1508

## Input Format

The first line contains two integer,  and . The next line contains  integers, the elements of array . The last two lines contain  integers each, the elements of array  and , respectively.

## Output Format

Print  space-separated integers, the elements of array  after performing the program modulo .

## Sample Input

4 3
1 2 3 4
1 2 3
13 29 71

## Sample Output

13 754 2769 1508

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
