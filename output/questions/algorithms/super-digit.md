# Super Digit

- **Domain:** algorithms
- **Difficulty:** Medium
- **Max Score:** 20
- **Success Ratio:** 0.7711111111111111
- **Total Submissions:** 4050
- **Solved Count:** 3123
- **URL:** https://www.hackerrank.com/challenges/super-digit

## Problem Statement

We define super digit of an integer $x$ using the following rules:  

- If $x$ has only $1$ digit, then its super digit is $x$.   
- Otherwise, the super digit of $x$ is equal to the super digit of the digit-sum of $x$. Here, digit-sum of a number is defined as the sum of its digits.  

For example, super digit of $9875$ will be calculated as:

	super_digit(9875) = super_digit(9+8+7+5) 
	                  = super_digit(29) 
	                  = super_digit(2+9)
	                  = super_digit(11)
	                  = super_digit(1+1)
	                  = super_digit(2)
	                  = 2.

You are given two numbers $n$ and $k$. You have to calculate the super digit of $P$. 

$P$ is created when number $n$ is concatenated $k$ times. That is, if $n = 123$ and $k = 3$, then $P = 123123123$.  


## Input Format

The first line contains two space separated integers, $n$ and $k$.  

## Output Format

 Output the super digit of $P$, where $P$ is created as described above.

## Constraints

- $1 \le n < 10^{100000}$
- $1 \le k \le 10^5$

## Sample Input

148 3

## Sample Output

3

## Explanation

Here   and , so .

super_digit(P) = super_digit(148148148)
               = super_digit(1+4+8+1+4+8+1+4+8)
               = super_digit(39)
               = super_digit(3+9)
               = super_digit(12)
               = super_digit(1+2)
               = super_digit(3)
               = 3.
