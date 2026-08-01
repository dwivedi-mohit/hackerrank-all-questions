# Count Palindromes

- **Domain:** fp
- **Difficulty:** Hard
- **Max Score:** 140
- **Success Ratio:** 0.2952029520295203
- **Total Submissions:** 542
- **Solved Count:** 160
- **URL:** https://www.hackerrank.com/challenges/count-palindromes

## Problem Statement

A string is made of only lowercase latin letters (a,b,c,d,.....,z). Can you find the length of the lexicographically smallest string such that it has exactly $K$ sub-strings, each of which are palindromes? 

## Input Format

The first line of input contains single integer $T$ - the number of testcases.  
T lines follow, each containing the integer $K$.


## Output Format

Output exactly $T$ lines. Each line should contain single integer - the length of the lexicographically smallest string.


## Constraints

* $1 \leq T \leq 100$  
* $1 \leq K \leq 10^{12}$  

## Sample Input

10
17

## Sample Output

7

## Explanation

for , one of the smallest possible strings that satisfies the property is aaaa.
All  palindromes are

- a,a,a,a

- aa, aa, aa

- aaa, aaa

- aaaa

Note

Two sub-strings with different indices are both counted.
