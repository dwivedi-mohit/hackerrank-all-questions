# Computer Virus

- **Domain:** java
- **Difficulty:** Advanced
- **Max Score:** 100
- **Success Ratio:** 0.47635135135135137
- **Total Submissions:** 296
- **Solved Count:** 141
- **URL:** https://www.hackerrank.com/challenges/demidenko-computer-virus

## Problem Statement

Suppose we have an *n-dimensional* supercomputer with an infinite number of processors. Every processor has a vector of $n$ integers as its (*n-dimensional*) coordinates and can be thought of as a point in the $n$-dimensional space. Furthermore, at every $n$-dimensional lattice point, there is a processor. Two processors are called _neighbors_ if their coordinate vectors are different in only one position, and the absolute difference of the numbers in that position is equal to $1$. For example $(0,0,0)$ and $(1,0,0)$ are neighbors, and so are $(-1,2,3,4)$ and $(-1,2,3,3)$. But $(0,0,0)$ and $(1,0,1)$, and $(1,2,3,4)$ and $(1,2,3,2)$, are not neighbors.

Some processors of this computer are infected by a virus. At time $0$, only one processor is infected. After every second, all uninfected processors that are neighbors with infected ones become infected too. Given $n$ and $t$, calculate the number of processors that are infected after $t$ seconds, modulo $(10^9+7)$.

## Input Format

The first line contains an integer $Q$, the number of test cases.  
Each of the next $Q$ lines contains two integers $n$ and $t$, separated by a space.

## Output Format

For every test case, write the answer in a single line.  

**Constraints**  

$1 \leq Q \leq 10^{5}$  
$1\leq n\leq 5 \times 10^{6}$  
$0\leq t\leq 10^{18}$  
The sum of all $n$'s in one file does not exceed $5 \times 10^{6}$


## Constraints

The sum of all 's in one file does not exceed

## Sample Input

2 0
2 1
2 2
3 1
1 10

## Sample Output

5
13
7
21
