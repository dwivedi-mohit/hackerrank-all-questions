# Random Number Generator

- **Domain:** mathematics
- **Difficulty:** Hard
- **Max Score:** 80
- **Success Ratio:** 0.5590062111801242
- **Total Submissions:** 161
- **Solved Count:** 90
- **URL:** https://www.hackerrank.com/challenges/random-number-generator-1

## Problem Statement

Sabya is writing code to output a random number between $1$ and $N$ inclusive. The code can output different integers in the interval with different probabilities so that the sum of the probabilities is equal to $1$.
<br>

For evaluation, the code is run twice. If the output in both cases are different, his score is equal to the *sum* of the outputs. Otherwise, his score is equal to $0$.
<br>

Sabya is very intelligent, and he writes code that maximizes his expected score. Find the expected score. Output the ratio of the expected score to the maximum possible score. The maximum possible score is $2\times N - 1$.
<br>




## Input Format

The first line contains $T$: the number of test cases.  
The next $T$ lines each contain a single integer, $N$.

## Output Format

Output $T$ lines: the ratio $\frac{\text{expected score}}{\text{maximum score}}$ in each case.    
The answer is considered correct if the absolute error is less than $10^{-8}$.  

**Constraints**  
$1 \leqslant T \leqslant 10^5$  
$1 \leqslant N \leqslant 10^6$

## Sample Input

1
2
3

## Sample Output

0.00000000000
0.50000000000
0.54545454545

## Explanation

In the first case, the output is always  both times.

In the second case,  and  are generated with the probability of  and

In the third case, ,  and  are generated with the probability of ,  and , respectively.
