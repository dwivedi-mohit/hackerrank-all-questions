# Sherlock and Permutations

- **Domain:** java
- **Difficulty:** Hard
- **Max Score:** 20
- **Success Ratio:** 0.6337620578778135
- **Total Submissions:** 18660
- **Solved Count:** 11826
- **URL:** https://www.hackerrank.com/challenges/sherlock-and-permutations

## Problem Statement

Watson asks Sherlock:  
Given a string _S_ of _N_ `0's` and _M_ `1's`, how many unique permutations of this string start with `1`?   

Help Sherlock by printing the answer modulo (_10<sup>9</sup>+7_).   

**Input Format**   
First line contains _T_, the number of test cases.  
Each test case consists of _N_ and _M_ separated by a space.

**Output Format**   
For each test case, print the answer modulo (_10<sup>9</sup>+7_).

**Constraints**  
1 &le; T &le; 200  
1 &le; N,M &le; 1000  

**Sample Input**   

	2
	1 1
	2 3
    
**Sample Output**      
	
    1
    6

**Explanation**  
Test1: Out of all unique permutations ie. `01` and `10`, only second permutation satisfies. Hence, output is 1.  
Test2: Out of all unique permutations ie. `00111 01011 01101 01110 10011 10101 10110 11001 11010 11100`, only `10011 10101 10110 11001 11010 11100` satisfy. Hence, output is 6.

## Input Format

First line contains T, the number of test cases.

Each test case consists of N and M separated by a space.

## Output Format

For each test case, print the answer modulo (109+7).

## Constraints

1 ≤ T ≤ 200

1 ≤ N,M ≤ 1000

## Sample Input

1 1
2 3

## Sample Output

6

## Explanation

Test1: Out of all unique permutations ie. 01 and 10, only second permutation satisfies. Hence, output is 1.

Test2: Out of all unique permutations ie. 00111 01011 01101 01110 10011 10101 10110 11001 11010 11100, only 10011 10101 10110 11001 11010 11100 satisfy. Hence, output is 6.
