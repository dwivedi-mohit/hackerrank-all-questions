# Random Integers Random Bits

- **Domain:** ai
- **Difficulty:** Hard
- **Max Score:** 60
- **Success Ratio:** 0.5653846153846154
- **Total Submissions:** 260
- **Solved Count:** 147
- **URL:** https://www.hackerrank.com/challenges/rirb

## Problem Statement

Given an integer range [A,B],  

1. What’s the probability to get a 1-bit if we first randomly choose a number x in the range and then randomly choose a bit from x?  
2. What’s the expected number of bit 1s if we randomly choose a number x in the range?  

**Input Format**  
The first line of input is the number of test cases $T$  
Each test cases is a line contains 2 integers $A$ and $B$ separated by a space. 

**Output Format**  
For each test case output a line containing 2 float numbers separated by a space. The first one is the probability and the second one is the expected number. You should output the number accurate to 5 fractional digits. 


**Constraints**  
$1 \le T \le 200$  
$1 \le A \le B \le 10^{10}$  

**Sample Input**

	1
	2 4

**Sample Output**
	
    0.61111 1.33333

**Explanation**  
(10)  (11)  (100)  
(1) So we got a one in $\frac{1}{3} \times \frac{1}{2} + \frac{1}{3} \times \frac{1}{1} + \frac{1}{3} \times \frac{1}{3} = \frac{11}{18}$  
(2) The expected 1 we have is : $1 \times \frac{1}{3} + 2 \times \frac{1}{3} + 1 \times \frac{1}{3} = \frac{4}{3}$  




## Input Format

The first line of input is the number of test cases

Each test cases is a line contains 2 integers  and  separated by a space.

## Output Format

For each test case output a line containing 2 float numbers separated by a space. The first one is the probability and the second one is the expected number. You should output the number accurate to 5 fractional digits.

## Sample Input

2 4

## Sample Output

0.61111 1.33333

## Explanation

(10)  (11)  (100)

(1) So we got a one in

(2) The expected 1 we have is :
