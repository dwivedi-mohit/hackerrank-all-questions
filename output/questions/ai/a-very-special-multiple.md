# A Very Special Multiple

- **Domain:** ai
- **Difficulty:** Hard
- **Max Score:** 80
- **Success Ratio:** 0.4957698815566836
- **Total Submissions:** 591
- **Solved Count:** 293
- **URL:** https://www.hackerrank.com/challenges/a-very-special-multiple

## Problem Statement

Charlie and Johnny play a game. For every integer $X$ Charlie gives, Johnny has to find the smallest positive integer $Y$ such that $X \times Y$ ($X$ multiplied by $Y$) contains only 4s and 0s and starts with one or more 4s followed by zero or more 0s. For example, 404 is an invalid number but 4400, 440, and 444 are valid numbers. 

If $a$ is the number of 4s and $b$ is the number of 0s, can you print the value of $(2\times a) + b$?  

**Input Format**  

The first line of input contains a single integer $T$, the number of test cases.  

$T$ lines follow, each line containing the integer $X$ as stated above.

**Output Format**  

For every $X$, print the output $(2\times a) + b$ in a newline as stated in the problem statement.  

**Constraints**  

$1 \le T \le 100$  
$1 \le X \le 10^{10}$  

**Sample Input**  
 
    3
    4
    5
    80

**Sample Output**  
 
    2
    3
    4

**Explanation**  

For the 1<sup>st</sup> test case, the smallest such multiple of $4$ is 4 itself. Hence the value of $a$ will be $1$ and and the value of $b$ will be $0$, and the answer is $(2\times a) + b = 2$.  

For the 2<sup>nd</sup> test case, $Y = 8$ and 40 is the minimum such multiple of $5$. Hence the values of $a$, $b$ and $(2 \times a) + b$ will be $1$, $1$ and $3$ respectively.


## Input Format

The first line of input contains a single integer , the number of test cases.

 lines follow, each line containing the integer  as stated above.

## Output Format

For every , print the output  in a newline as stated in the problem statement.

## Sample Input

4
5
80

## Sample Output

3
4

## Explanation

For the 1st test case, the smallest such multiple of  is 4 itself. Hence the value of  will be  and and the value of  will be , and the answer is .

For the 2nd test case,  and 40 is the minimum such multiple of . Hence the values of ,  and  will be ,  and  respectively.
