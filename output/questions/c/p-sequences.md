# P-sequences

- **Domain:** c
- **Difficulty:** Hard
- **Max Score:** 100
- **Success Ratio:** 0.65
- **Total Submissions:** 2640
- **Solved Count:** 1716
- **URL:** https://www.hackerrank.com/challenges/p-sequences

## Problem Statement

We call a sequence of `N` natural numbers (*a*<sub>1</sub>, *a*<sub>2</sub>, ..., *a*<sub>N</sub>) a *P-sequence*, if the product of any two adjacent numbers in it is not greater than *P*. In other words, if a sequence (*a*<sub>1</sub>, *a*<sub>2</sub>, ..., *a*<sub>N</sub>) is a *P-sequence*, then *a*<sub>i</sub> * *a*<sub>i+1</sub> &le; `P` &forall; 1 &le; i &lt; N

You are given `N` and `P`. Your task is to find the number of such *P-sequences* of `N` integers modulo 10<sup>9</sup>+7.


## Input Format

The first line of input consists of `N`  
The second line of the input consists of `P`. 


## Output Format

Output the number of *P-sequences* of `N` integers modulo 10<sup>9</sup>+7.


## Constraints

2 &le; N &le; 10<sup>3</sup>  
1 &le; P &le; 10<sup>9</sup>  
1 &le; a<sub>i</sub>  


## Sample Input

2
2

## Sample Output

3

## Explanation

3 such sequences are {1,1},{1,2} and {2,1}
