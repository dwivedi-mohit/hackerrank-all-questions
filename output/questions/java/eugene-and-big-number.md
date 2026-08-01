# Eugene and Big Number

- **Domain:** java
- **Difficulty:** Medium
- **Max Score:** 100
- **Success Ratio:** 0.56797583081571
- **Total Submissions:** 993
- **Solved Count:** 564
- **URL:** https://www.hackerrank.com/challenges/eugene-and-big-number

## Problem Statement

Eugene must do his homework, but he is struggling.   
He has three integer numbers: *A*, *N*, *M*. He writes number *A* on the board *N* times **in a row**. Let's call the resulting big number *X*.
Help Eugene find *X* [modulo](https://en.wikipedia.org/wiki/Modulo_operation) *M*. 

## Input Format

First line contains *T*, the number of testcases.  
Each testcase contains three numbers: *A*, *N*, *M* separated by a single space.   


## Output Format

Print the required answer for each testcase in a new line.

## Constraints

+ $1 \le T \le 200$  
+ $0 \le A \le 10^3$  
+ $0 < N < 10^{12}$    
+ $1 < M < 10^9$    



## Sample Input

12 2 17
523 3 11

## Sample Output

6

## Explanation

First testcase:

A = 12

N = 2

X = 1212

1212 modulo 17 = 5

Second testcase:

A = 523

N = 3

X = 523523523

523523523 modulo 11 = 6
