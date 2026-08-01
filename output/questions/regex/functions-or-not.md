# Functions or Not?

- **Domain:** regex
- **Difficulty:** Easy
- **Max Score:** 5
- **Success Ratio:** 0.9523421588594705
- **Total Submissions:** 4910
- **Solved Count:** 4676
- **URL:** https://www.hackerrank.com/challenges/functions-or-not

## Problem Statement

**Objective**	
In this problem, we touch upon a basic concept that is fundamental to Functional Programming: identifying a relation which represents a valid function.  

**Task**	
You are given a set of unique $(x,y)$ ordered pairs constituting a relation. The $x$-values form the domain, and the $y$-values form the range to which they map. For each of these relations, identify whether they may possibly represent a valid *function* or not.  

**Note:** You do not have to find the *actual* function, you just need to determine that the relation may be representative of some valid function.

## Input Format

The first line contains an integer, $T$, denoting the number of test cases. The subsequent lines describe $T$ test cases, and the input for each test case is as follows:

1. The first line contains an integer, $N$, the number of $(x,y)$ pairs in the test case. 
2. The $N$ subsequent lines each contain two space-separated integers describing the respective $x$ and $y$ values for each ordered pair.  



## Output Format

On a new line for each test case, print $\scriptsize{\texttt{YES}}$ if the set of ordered pairs represent a valid function, or $\scriptsize{\texttt{NO}}$ if they do not.  

## Constraints

- $1 \le T \le 5$
- $2 \le $N$ \le 100$  
- $0 \le x,y \le 500$    
- $x \text{ and } y \text{ are both integers.}$

## Sample Input

3
1 1
2 2
3 3
4
1 2
2 4
3 6
4 8

## Sample Output

YES
YES

## Explanation

Test Case 0:

, Ordered Pairs:
The set of ordered pairs represents a relation, which could represent a function such as , . Thus, we print  on a new line.

Test Case 1:

, Ordered Pairs:

The set of ordered pairs represents a relation, which could represent a function such as ,  . Thus, we print  on a new line.
