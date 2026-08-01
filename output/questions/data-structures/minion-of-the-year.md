# Minion of the Year

- **Domain:** data-structures
- **Difficulty:** Expert
- **Max Score:** 120
- **Success Ratio:** 0.6801346801346801
- **Total Submissions:** 297
- **Solved Count:** 202
- **URL:** https://www.hackerrank.com/challenges/minion-of-the-year

## Problem Statement

Gru wanted to upgrade the quality of his minions' despicableness through his new base, The Volcano. Dave, desperately wanting the *Minion of the Year* award, rushed to The Volcano only to find out that he needs to solve a series of questions before he can unlock the gate and enter.

Dave is given a prime $P$, and $N$ questions.

In each question/query, Dave is given four integers $(A, B, C, D)$, and Dave needs to find the minimum possible value of $Ax + By$ among all positive integer pairs $(x,y)$ such that $P$ divides $\left|C^x - D^y\right|$.

Unfortunately, the gate has a strict time limit, and if Dave is unable to answer all questions quickly and correctly, then a hidden freeze ray will zap him and he won't be able to move. Please help Dave answer all the questions so he can enter The Volcano and win the Minion of the Year award!

**Input Format**  
The first line of input consists of an integer, $T$, which is the number of test cases.

The first line of each test case consists of two integers separated by a space, $P$ and $N$. The following $N$ lines contain the queries, each in a line. Each question consists of four integers separated by single spaces: $A$, $B$, $C$ and $D$.

**Output Format**  
For each query, output a single line containing the minimum value of $Ax + By$, or output `wala` if no such pairs $(x,y)$ exist.

**Constraints**  
$1 \le T \le 3$  
$1 \le N \le 6000$  
$2 \le P \le 10^8$  
$0 \le A, B, C, D \le 10^8$  
$P$ is prime  

**Sample Input**  

    2
    7 2
    1 1 1 5
    7 8 8 7
    11 5
    1 1 1 1
    0 1 2 3
    3 2 1 0
    9 8 7 6
    0 0 1 1

**Sample Output**  

    7
    wala
    2
    1
    wala
    33
    0

**Explanation**  
For the first query, $P = 7$, $(A, B, C, D) = (1, 1, 1, 5)$, the minimum $1x + 1y$ is $7$, which occurs at $(x,y) = (1,6)$ ($7$ divides $\left|1^1 - 5^6\right| = 15624 = 7\cdot 2232$).

For the second query, no matter what $(x,y)$ you choose, $\left|8^x - 7^y\right|$ will not by divisible by $7$, so the answer is `wala`.

## Input Format

The first line of input consists of an integer, , which is the number of test cases.

The first line of each test case consists of two integers separated by a space,  and . The following  lines contain the queries, each in a line. Each question consists of four integers separated by single spaces: , ,  and .

## Output Format

For each query, output a single line containing the minimum value of , or output wala if no such pairs  exist.

## Constraints

is prime

## Sample Input

7 2
1 1 1 5
7 8 8 7
11 5
1 1 1 1
0 1 2 3
3 2 1 0
9 8 7 6
0 0 1 1

## Sample Output

wala
2
1
wala
33
0

## Explanation

For the first query, , , the minimum  is , which occurs at  ( divides ).

For the second query, no matter what  you choose,  will not by divisible by , so the answer is wala.
