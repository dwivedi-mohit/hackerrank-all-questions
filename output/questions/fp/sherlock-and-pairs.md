# Sherlock and Pairs

- **Domain:** fp
- **Difficulty:** Medium
- **Max Score:** 30
- **Success Ratio:** 0.7206615001383891
- **Total Submissions:** 14452
- **Solved Count:** 10415
- **URL:** https://www.hackerrank.com/challenges/sherlock-and-pairs

## Problem Statement

Sherlock is given an array of $N$ integers ($A$<sub>$0$</sub>, $A$<sub>$1$</sub> ... $A$<sub>$N-1$</sub> by Watson. Now Watson asks Sherlock how many different pairs of indices $i$ and $j$ exist such that $i$ is not equal to $j$ but $A$<sub>$i$</sub> is equal to $A$<sub>$j$</sub>.     

That is, Sherlock has to count the total number of pairs of indices $(i, j)$ where  $A$<sub>$i$</sub> $= A$<sub>$j$</sub> AND $i ≠ j$.

**Input Format**   
The first line contains $T$, the number of test cases. $T$ test cases follow.   
Each test case consists of two lines; the first line contains an integer $N$, the size of array, while the next line contains $N$ space separated integers.

**Output Format**   
For each test case, print the required answer on a different line. 

**Constraints**   
$1 \le T \le 10$   
$1 \le N \le 10$<sup>$5$</sup>    
$1 \le A[i] \le 10$<sup>$6$</sup>  

**Sample input**

    2
    3
    1 2 3
    3
    1 1 2
    
**Sample output**   

    0
    2
    
**Explanation**   
In the first test case, no two pair of indices exist which satisfy the given condition.   
In the second test case as _A[0] = A[1] = 1_, the pairs of indices _(0,1)_ and _(1,0)_ satisfy the given condition.

## Input Format

The first line contains , the number of test cases.  test cases follow.

Each test case consists of two lines; the first line contains an integer , the size of array, while the next line contains  space separated integers.

## Output Format

For each test case, print the required answer on a different line.

## Constraints

Sample input

2
3
1 2 3
3
1 1 2

Sample output

0
2

## Explanation

In the first test case, no two pair of indices exist which satisfy the given condition.

In the second test case as A[0] = A[1] = 1, the pairs of indices (0,1) and (1,0) satisfy the given condition.
