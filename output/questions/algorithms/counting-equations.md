# Counting Equations

- **Domain:** algorithms
- **Difficulty:** Expert
- **Max Score:** 100
- **Success Ratio:** 0.8680555555555556
- **Total Submissions:** 144
- **Solved Count:** 125
- **URL:** https://www.hackerrank.com/challenges/counting-equations

## Problem Statement

[Sevenkplus](http://sevenkplus.com/) was interested in contributing a challenge to hackerrank and he came up with this problem. 

You are given a linear congruence system with `n` variables and `m` equations:   
a<sub>11</sub> x<sub>1</sub> + a<sub>12</sub> x<sub>2</sub> + ... + a<sub>1n</sub> x<sub>n</sub> = b<sub>1</sub> (mod p)   
a<sub>21</sub> x<sub>1</sub> + a<sub>22</sub> x<sub>2</sub> + ... + a<sub>2n</sub> x<sub>n</sub> = b<sub>2</sub> (mod p)   
...  
a<sub>m1</sub> x<sub>1</sub> + a<sub>m2</sub> x<sub>2</sub> + ... + a<sub>mn</sub> x<sub>n</sub> = b<sub>m</sub> (mod p)   


where, 

p is a prime number  
0 <= a<sub>ij</sub> < p  
0 <= x<sub>i</sub> < p  
0 <= b<sub>i</sub> < p  

Given integers `n`, `m`, `p`, `a`, `b`, count the number of solutions to this equation. Since the output can be large, please output your answer modulo `10^9+7`.


He writes the standard solution and a test data generator without difficulty, and generates some test data. 
However, when he attempts to remove hidden folders from the problem folder before uploading, he accidentally deletes the input file. 
Luckily, the output file remains and he still remembers some features of the input. He remembers `n`, `m`, `p` and that `w` entries of `a` are zero. However, he cannot recall more about the input. 

He wants to count how many possible inputs are there that will result in the desired output `S` (number of solutions to the equation system) output modulo `10^9+7`. Can you help Sevenkplus?

**Input Format**  
The first line contains an integer T. T testcases follow. 
For each test case, the first line contains five numbers, `m`, `n`, `p`, `S`, `w`. separated by a single space.   
`w` lines follow. Each line contains two numbers `x`, `y`, which indicates that a<sub>xy</sub>=0.

**Output Format**  
For each test case, output one line in the format `Case #t: ans`, where `t` is the case number (starting from 1), and `ans` is the answer. 

**Constraints**  
1 ≤ T ≤ 33  
1 <= m, n <= 1000  
p <= 10^9, p is a prime number  
0 <= S < 10^9+7  
w <= 17  
1 <= x <= m  
1 <= y <= n  
In any test case, one pair (x, y) will not occur more than once.

**Sample Input**

    6
    2 2 2 0 1
	1 1
	2 2 2 1 1
	1 1
	2 2 2 2 1
	1 1
	2 2 2 3 1
	1 1
	2 2 2 4 1
	1 1
	488 629 183156769 422223791 10
	350 205
	236 164
	355 8
	3 467
	355 164
	350 467
	3 479
	72 600
	17 525
	223 370

**Sample Output**

	Case #1: 13
	Case #2: 8
	Case #3: 10
	Case #4: 0
	Case #5: 1
	Case #6: 225166925

**Explanation**  

For test case 1, the 13 possible equations are:

	a11	a12	b1	a21	a22	b2
	0	0	0	0	0	1
	0	0	1	0	0	0
	0	0	1	0	0	1
	0	0	1	0	1	0
	0	0	1	0	1	1
	0	0	1	1	0	0
	0	0	1	1	0	1
	0	0	1	1	1	0
	0	0	1	1	1	1
	0	1	0	0	0	1
	0	1	0	0	1	1
	0	1	1	0	0	1
	0	1	1	0	1	0

**Timelimits**  
Timelimits for this challenge is given [here](https://www.hackerrank.com/environment)

## Input Format

The first line contains an integer T. T testcases follow.
For each test case, the first line contains five numbers, m, n, p, S, w. separated by a single space.

w lines follow. Each line contains two numbers x, y, which indicates that axy=0.

## Output Format

For each test case, output one line in the format Case #t: ans, where t is the case number (starting from 1), and ans is the answer.

## Constraints

1 ≤ T ≤ 33

1 <= m, n <= 1000

p <= 10^9, p is a prime number

0 <= S < 10^9+7

w <= 17

1 <= x <= m

1 <= y <= n

In any test case, one pair (x, y) will not occur more than once.

## Sample Input

2 2 2 0 1
1 1
2 2 2 1 1
1 1
2 2 2 2 1
1 1
2 2 2 3 1
1 1
2 2 2 4 1
1 1
488 629 183156769 422223791 10
350 205
236 164
355 8
3 467
355 164
350 467
3 479
72 600
17 525
223 370

## Sample Output

Case #1: 13
Case #2: 8
Case #3: 10
Case #4: 0
Case #5: 1
Case #6: 225166925

## Explanation

For test case 1, the 13 possible equations are:

a11 a12 b1  a21 a22 b2
0   0   0   0   0   1
0   0   1   0   0   0
0   0   1   0   0   1
0   0   1   0   1   0
0   0   1   0   1   1
0   0   1   1   0   0
0   0   1   1   0   1
0   0   1   1   1   0
0   0   1   1   1   1
0   1   0   0   0   1
0   1   0   0   1   1
0   1   1   0   0   1
0   1   1   0   1   0

Timelimits

Timelimits for this challenge is given here
