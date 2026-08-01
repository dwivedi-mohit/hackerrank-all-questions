# The Great XOR

- **Domain:** mathematics
- **Difficulty:** Medium
- **Max Score:** 25
- **Success Ratio:** 0.7185369449051041
- **Total Submissions:** 21708
- **Solved Count:** 15598
- **URL:** https://www.hackerrank.com/challenges/the-great-xor

## Problem Statement

Given a long integer $x$, count the number of values of $a$ satisfying the following conditions:  

* $a \oplus x > x$
* $0 < a < x$

where $a$ and $x$ are long integers and $\oplus$ is the [bitwise XOR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR) operator.  

You are given $q$ queries, and each query is in the form of a long integer denoting $x$. For each query, print the total number of values of $a$ satisfying the conditions above on a new line.

For example, you are given the value $x=5$.  Condition $2$ requires that $a < x$.  The following tests are run:  

$1 \oplus 5 = 4$  
$2 \oplus 5 = 7$  
$3 \oplus 5 = 6$  
$4 \oplus 5 = 1$   
  
We find that there are $2$ values meeting the first condition: $2$ and $3$.  

**Function Description**  

Complete the *theGreatXor* function in the editor below.  It should return an integer that represents the number of values satisfying the constraints.  

theGreatXor has the following parameter(s):

- *x*: an integer  

## Input Format

The first line contains an integer $q$, the number of queries. 	
Each of the next $q$ lines contains a long integer describing the value of $x$ for a query.  


## Output Format

For each query, print the number of values of $a$ satisfying the given conditions on a new line.

## Constraints

* $1 \le q \le 10^{5}$
* $1 \le x \le 10^{10}$

**Subtasks**

For $50\%$ of the maximum score:

* $1 \le q \le 10^{3}$
* $1 \le x \le 10^{4}$


## Sample Input

2
2
10

## Sample Output

1
5

## Explanation

We perform the following  queries:

- For  the only value of  satisfying  is . This also satisfies our other condition, as  and . Because we have one valid  and there are no more values to check, we print  on a new line.

- For , the following values of  satisfy our conditions:

There are five valid values of .
