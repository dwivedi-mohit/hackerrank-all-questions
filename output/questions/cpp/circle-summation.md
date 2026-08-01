# Circle Summation

- **Domain:** cpp
- **Difficulty:** Advanced
- **Max Score:** 80
- **Success Ratio:** 0.4372262773722628
- **Total Submissions:** 1370
- **Solved Count:** 599
- **URL:** https://www.hackerrank.com/challenges/circle-summation

## Problem Statement

There are $n$ children, numbered $1,2,\ldots,n$, sitting around a circle in a clockwise manner. The $i$th child has a piece of paper with the number $a_i$ written on it. They play the following game:

- In the $1$st round, the child numbered $i$ increases his number by the sum of the numbers of his neighbors.  
- In the $2$nd round, the child next in clockwise order increases his number by the sum of the numbers of his neighbors.
- In the $3$rd round, the child next in clockwise order increases his number by the sum of the numbers of his neighbors.
- And so on.  

The game ends after $m$ rounds have been played.  

For every $i$, find the numbers that the children end up with if the game starts with child $i$ playing the first round. Since the numbers can be large, output them [modulo](https://en.wikipedia.org/wiki/Modulo_operation) $10^9 + 7$.  

## Input Format

The first line contains $t$, the number of test cases. $t$ cases follow.  

The first line of each test case contains two space-separated integers $n$ and $m$. The next line contains $n$ integers, the $i$th of which is $a_i$.  

## Output Format

For each test case, print $n$ lines, each having $n$ integers. The $j$th integer on the $i$th line contains the number that the $j$th child ends up with if the game starts with child $i$ playing the first round.  

Print a blank line after each test case *except the last one*.  

Since the numbers can be large, output them [modulo](https://en.wikipedia.org/wiki/Modulo_operation) $10^9 + 7$.  

## Constraints

- $1 \le t \le 15$  
- $3 \le n \le 50$  
- $1 \le m \le 10^9$  
- $1 \le a_i \le 10^9$  


## Sample Input

2
5 1
10 20 30 40 50
3 4
1 2 1

## Sample Output

80 20 30 40 50
10 60 30 40 50
10 20 90 40 50
10 20 30 120 50
10 20 30 40 100

23 7 12
11 21 6
7 13 24
