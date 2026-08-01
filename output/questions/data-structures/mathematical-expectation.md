# Mathematical Expectation

- **Domain:** data-structures
- **Difficulty:** Hard
- **Max Score:** 100
- **Success Ratio:** 0.4126984126984127
- **Total Submissions:** 252
- **Solved Count:** 104
- **URL:** https://www.hackerrank.com/challenges/mathematical-expectation

## Problem Statement

Let's consider a random permutation p<sub>1</sub>, p<sub>2</sub>, ..., p<sub>N</sub> of numbers 1, 2, ..., N and calculate the value F=(X<sub>2</sub>+...+X<sub>N-1</sub>)<sup>K</sup>, where X<sub>i</sub> equals 1 if one of the following two conditions holds: p<sub>i-1</sub> < p<sub>i</sub> > p<sub>i+1</sub> or p<sub>i-1</sub> > p<sub>i</sub> < p<sub>i+1</sub> and X<sub>i</sub> equals 0 otherwise. What is the expected value of F?

**Input Format:**  
The first line contains two integers K and N.

**Output Format:**  
Print the expected value of F as an irreducible fraction p / q. Follow sample input for more clarification.


**Constraints:**  
1000 <= N <= 10<sup>9</sup>  
1 <= K <= 5

**Sample input**  

    1 1000

**Sample Output**  

    1996 / 3


## Input Format

The first line contains two integers K and N.

## Output Format

Print the expected value of F as an irreducible fraction p / q. Follow sample input for more clarification.

## Constraints

1000 <= N <= 109

1 <= K <= 5

Sample input

1 1000

## Sample Output

1996 / 3
