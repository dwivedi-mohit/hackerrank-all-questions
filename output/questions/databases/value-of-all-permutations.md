# Value of all Permutations

- **Domain:** databases
- **Difficulty:** Hard
- **Max Score:** 80
- **Success Ratio:** 0.728
- **Total Submissions:** 125
- **Solved Count:** 91
- **URL:** https://www.hackerrank.com/challenges/value-of-all-permutations

## Problem Statement

You are given an array $A$ of size $N$. You are asked to answer $Q$ queries.  

Each query contains a number $M$.  

For each *distinct* permutation of the array $A$, you need to print the sum of the values returned by the `find` function.

As the sum can be too large, output it modulo $P$, which is a prime and given in input.  

	find(int permutation_A[], int M)
	{
        x = Length(permutation_A)
        sum = 0
        for(i = 0; i < x; i++) {
        	if (permutation_A[i] <= M)
            	sum = sum + permutation_A[i]
            else
            	break
		}
		return sum
    }


**Input Format**  
The first line of input contains $P$.  
The second line of input contains $N$. The next line contains $N$ numbers $A[0] \ldots A[N-1]$ separated by single spaces.  
The next line contains $Q$, the number of queries to follow. Each subsequent line contains one positive integer $M$.  

**Output Format**  
For each query, output as asked above.  

**Constraints**  
$1000000 \le P \le 2000003$  
$1 \le N \le 10^5$  
$1 \le Q \le 10^5$  
$1 \le A[i], M \le 10^9$

**Sample Input**

	2000003
	5
	4 2 3 1 4
	2
	1
	2

**Sample Output**

	12
    45
    
**Explanation**

*Query 1*:  
Consider all permutations. if the first number is greater than 1, then the loop will break in the beginning itself. There are a total of 60 distinct permutations out of which 48 will give 0. The remaining 12 will fetch 1 each from the function. Thus the answer is 12.  


## Input Format

The first line of input contains .

The second line of input contains . The next line contains  numbers  separated by single spaces.

The next line contains , the number of queries to follow. Each subsequent line contains one positive integer .

## Output Format

For each query, output as asked above.

## Sample Input

5
4 2 3 1 4
2
1
2

## Sample Output

45

## Explanation

Query 1:

Consider all permutations. if the first number is greater than 1, then the loop will break in the beginning itself. There are a total of 60 distinct permutations out of which 48 will give 0. The remaining 12 will fetch 1 each from the function. Thus the answer is 12.
