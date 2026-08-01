# Little Gaurav and Sequence

- **Domain:** fp
- **Difficulty:** Medium
- **Max Score:** 20
- **Success Ratio:** 0.7081481481481482
- **Total Submissions:** 1350
- **Solved Count:** 956
- **URL:** https://www.hackerrank.com/challenges/little-gaurav-and-sequence

## Problem Statement

Little Gaurav is very fond of numbers and sequences. One day his teacher tells him to find a strange sequence.    

$$S = \sum_{i=0, 2^{i}\leq n}^\infty     \sum_{j=0}^n 2^{2^{i}+2j}$$

Since this sequence looks a bit difficult, the teacher tells him to find the last digit of $S$.  

Little Gaurav is confused because he cannot solve the problem and leaves this problem to the worthy programmers of the world. Help little Gaurav in finding the solution.   

**Input Format**  
The first line contains $T$, the number of test cases.  
$T$ lines follow, each line containing an integer, $N$.   

**Output Format**  
For each testcase, print the last digit of $S$ in one line.    

**Constraints**   
$1 \le T \le 1000$  
$1 \le N \le 10^{15}$  

**Sample Input**     

    3
    1
    2
    3
    
**Sample Output**   

    0
    6
    0

**Explanation**  
For n=1, only i=0 is valid. So S is $2^{2^{0}+0} + 2^{2^{0}+2} = 10$. Hence last digit of S is 0.   
For n=2, only i=0 and 1 are valid. So S is    
S1(for i=0) is $2^{2^{0}+0} + 2^{2^{0}+2} + 2^{2^{0}+4}= 42$.    
S2(for i=1) is $2^{2^{1}+0} + 2^{2^{1}+2} + 2^{2^{1}+4}= 84$.   
So last digit of S is 6. 

## Input Format

The first line contains , the number of test cases.

 lines follow, each line containing an integer, .

## Output Format

For each testcase, print the last digit of  in one line.

## Sample Input

1
2
3

## Sample Output

6
0

## Explanation

For n=1, only i=0 is valid. So S is . Hence last digit of S is 0.

For n=2, only i=0 and 1 are valid. So S is

S1(for i=0) is .

S2(for i=1) is .

So last digit of S is 6.
