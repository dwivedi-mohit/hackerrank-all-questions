# Lucky Numbers

- **Domain:** algorithms
- **Difficulty:** Expert
- **Max Score:** 100
- **Success Ratio:** 0.3080375356997144
- **Total Submissions:** 7353
- **Solved Count:** 2265
- **URL:** https://www.hackerrank.com/challenges/lucky-numbers

## Problem Statement

A number is called *lucky* if the sum of its digits, as well as the sum of the squares of its digits is a prime number. How many numbers between $a$ and $b$ inclusive, are lucky?

For example, $a = 20$ and $b = 25$.  Each number is tested below:  

			digit	digit	squares
	value	sum		squares	sum	
    20		2		4,0		4
    21		3		4,1		5
    22		4		4,4		8
    23		5		4,9		13
    24		6		4,16	20
    25		7		4,25	29
    
We see that two numbers, $21$, $23$ and $25$ are *lucky*.

**Note**: These lucky numbers are not to be confused with [Lucky Numbers](https://en.wikipedia.org/wiki/Lucky_number)

**Function Description**  

Complete the *luckyNumbers* function in the editor below.  It should return an integer that represents the number of lucky numbers in the given range.  

luckyNumbers has the following parameter(s):  

- *a*: an integer, the lower range bound  
- *b*: an integer, the higher range bound  

## Input Format

The first line contains the number of test cases $T$.  
Each of the next $T$ lines contains two space-separated integers, $a$ and $b$.


## Output Format

Output T lines, one for each test case in the order given.


## Constraints

+ $1 \le T \le 10^4$  
+ $1 \le a \le b \le 10^{18}$  


## Sample Input

1 20
120 130

## Sample Output

1

## Explanation

For the first case, the lucky numbers are , and .

For the second case, the only lucky number is .
