# Kevin and Expected Value 

- **Domain:** algorithms
- **Difficulty:** Medium
- **Max Score:** 40
- **Success Ratio:** 0.43270622286541244
- **Total Submissions:** 691
- **Solved Count:** 299
- **URL:** https://www.hackerrank.com/challenges/kevin-and-expected-value

## Problem Statement

Kevinsogo is a professor of mathematics, One day he gave an assignment to his students which was hard for them. The students want you to help them in solving the problem.<br>

Given the value of $N$,  
$$ x = \text{rand}() \bmod N $$  
$$ Y = \sqrt{x + { \sqrt{x + { \sqrt {x + \sqrt {x+ \cdots }}}} }}$$

Note that $\text{rand}()$ returns an integer between $0$ and $10^{100}$ (inclusive) uniformly at random.

Find out the expected value of $Y$.

**Input Format**  
The first line contains an integer $T$ i.e. the number of test cases.<br>
The next $T$ lines will each contain an integer $N$.<br>

**Output Format**  
Print the output corresponding to each test case in a separate line. The answer will be considered correct if its absolute error doesn't exceed $10^{-3}$ or $0.001$.  

**Constraints**  
*Task 1: 30 points*  
$ 1\le T \le 10000$  
$ 1\le N \le 5 \times 10^6$  

*Task 2: 10 additional points*  
$ 1\le T \le 1000$  
$ 1\le N \le 10^{16}$  


**Sample Input**

    3
    1
    5
    10


**Sample Output**

	0.0
    1.69647248786
    2.43798952788


## Input Format

The first line contains an integer  i.e. the number of test cases.

The next  lines will each contain an integer .

## Output Format

Print the output corresponding to each test case in a separate line. The answer will be considered correct if its absolute error doesn't exceed  or .

## Constraints

Task 1: 30 points

Task 2: 10 additional points

## Sample Input

1
5
10

## Sample Output

0.0
1.69647248786
2.43798952788
