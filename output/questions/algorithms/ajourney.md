# Journey to Mars

- **Domain:** algorithms
- **Difficulty:** Medium
- **Max Score:** 50
- **Success Ratio:** 0.6783310901749664
- **Total Submissions:** 743
- **Solved Count:** 504
- **URL:** https://www.hackerrank.com/challenges/ajourney

## Problem Statement

Elon Musk has succesfully built an automated staircase from Earth to Mars. Many people want to go to Mars, but that's not possible due to limited capacity of the staircase and logistics involved. Hence, Elon asks interested candidates to solve a tough challenge. If they solve it, they get a chance to visit Mars, otherwise not. Sam is highly interested in going to Mars. Can you help him solve the challenge? <br><br>
The staircase has N steps. One can either go step by step, or at each step, can take a jump of at most N steps. 

Elon is interested to know the number of ways in which you can go to Mars. Since the number of steps in stairs can be insanely large, Elon is only interested in the first and the last K digits of number of ways from which he can compute the actual answer with his algorithm.
<br><br>
**Input Format**<br>
   First line is an integer T that denotes the number of test cases.<br>
   Next T lines contain 2 integers each, N and K.
   
**Output Format**<br>
  T lines. Each line corresponds to one of the test cases and contains the sum of numbers which are formed by first K digit and last K digits of number of ways.
  
**Constraints**

	1<=T<=1000
    1<=N<=10^9
    1<=K<=9
  
If S is the number of ways in which one can climb the staircase, then 
the number of digits in S is greater or equal to the K.
  
**Sample Input**

	2
	10 2 
	12 1


**Sample Output**

	63
	10

If there are 10 steps, let's call the number of ways in which one can go is 
S

let S be of the form wxyz. 

So, summing wx + yz gives 63.

## Input Format

First line is an integer T that denotes the number of test cases.

   Next T lines contain 2 integers each, N and K.

## Output Format

T lines. Each line corresponds to one of the test cases and contains the sum of numbers which are formed by first K digit and last K digits of number of ways.

## Constraints

1<=T<=1000
1<=N<=10^9
1<=K<=9

If S is the number of ways in which one can climb the staircase, then
the number of digits in S is greater or equal to the K.

## Sample Input

10 2
12 1

## Sample Output

10

If there are 10 steps, let's call the number of ways in which one can go is
S

let S be of the form wxyz.

So, summing wx + yz gives 63.
