# Sherlock and the Maze

- **Domain:** c
- **Difficulty:** Medium
- **Max Score:** 50
- **Success Ratio:** 0.8395604395604396
- **Total Submissions:** 455
- **Solved Count:** 382
- **URL:** https://www.hackerrank.com/challenges/sherlock-and-the-maze

## Problem Statement

Watson gives a 2-D grid to Sherlock. Rows are numbered _1_ to _N_ from top to bottom and columns are numbered _1_ to _M_ from left to right. Sherlock is at position _(1,1)_ right now and he is free to face any direction before he starts to move. He needs to reach _(N,M)_. In one step, he can either move downwards or rightwards. Also, he cannot make more than _K_ turns during his whole journey.   

There are two possible scenarios when a turn can occur at point _(i, j)_:  

    Turns Right: (i-1, j)  ->  (i, j)  ->  (i, j+1)
                          Down        Right
            
    Turns Down:  (i, j-1)  ->  (i, j)  ->  (i+1, j)
                         Right        Dowm

Given _N_, _M_ and _K_, help him by printing the number of ways to reach _(N,M)_ with at most _K_ turns. As this value can be very large, print the answer modulo (10<sup>9</sup> + 7).   
    
**Input**     
First line contains _T_, the number of testcases. Then _T_ lines follow, where each line represents a test case. Each testcase consists of three space separated integers, _N M K_, where _(N, M)_ is the final location and _K_ is the maximum number of allowed turns.  

**Output**   
For each testcase, print the required answer in one line.    

**Constraints**    
1 &le; _T_ &le; 10    
1 &le; _N, M_ &le; 100  
0 &le; _K_ &le; 100  

**Note**  

1. He can take **at most** _K_ turns.
2. He is free to face any direction before starting from _(1, 1)_.

**Sample Input**   

	3
    2 2 3
    2 3 1
    4 4 4
    
**Sample Output**   

	2
    2
    18

**Sample explanation**   
*Test Case #00:* There is no way to reach _(2, 2)_ with 0, 2 or 3 turns. He will always reach _(2, 2)_ with 1 turn only. There are two ways shown below:  

1. He starts from _(1, 1)_ facing right and moves to _(1, 2)_. Then he faces down and moves to _(2, 2)_.
2. He starts from _(1, 1)_ facing down and moves to _(2, 1)_. Then he turns right and moves to _(2, 2)_.

*Test Case #01:* He can't reach _(2, 3)_ with 0 turns. There are only two ways to reach _(2, 3)_ with exactly 1 turn.

1. He starts from _(1, 1)_ facing down and moves to _(2, 1)_. Then he turns right and takes two steps forward to reach _(2, 3)_.
2. He starts from _(1, 1)_ facing right and moves two steps forward to reach _(1, 3)_. Then he turns down and proceeds one step to _(2, 3)_.

*Test Case #02:* There are 0 ways with 0 turn, 2 ways with 1 turn, 4 ways with 2 turns, 8 ways with 3 turns and 4 ways with 4 turns to reach _(4, 4)_.

---
**Tested by:** [Ashutosh Singla](/ashu1461), [Abhiranjan](/abhiranjan)

## Constraints

1 ≤ T ≤ 10

1 ≤ N, M ≤ 100

0 ≤ K ≤ 100

Note

- He can take at most K turns.

- He is free to face any direction before starting from (1, 1).

## Sample Input

2 2 3
2 3 1
4 4 4

## Sample Output

2
18

Sample explanation

Test Case #00: There is no way to reach (2, 2) with 0, 2 or 3 turns. He will always reach (2, 2) with 1 turn only. There are two ways shown below:

- He starts from (1, 1) facing right and moves to (1, 2). Then he faces down and moves to (2, 2).

- He starts from (1, 1) facing down and moves to (2, 1). Then he turns right and moves to (2, 2).

Test Case #01: He can't reach (2, 3) with 0 turns. There are only two ways to reach (2, 3) with exactly 1 turn.

- He starts from (1, 1) facing down and moves to (2, 1). Then he turns right and takes two steps forward to reach (2, 3).

- He starts from (1, 1) facing right and moves two steps forward to reach (1, 3). Then he turns down and proceeds one step to (2, 3).

Test Case #02: There are 0 ways with 0 turn, 2 ways with 1 turn, 4 ways with 2 turns, 8 ways with 3 turns and 4 ways with 4 turns to reach (4, 4).

Tested by: Ashutosh Singla, Abhiranjan
