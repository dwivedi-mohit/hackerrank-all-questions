# Recalling Early Days GP with Trees

- **Domain:** ai
- **Difficulty:** Hard
- **Max Score:** 120
- **Success Ratio:** 0.8580146460537021
- **Total Submissions:** 2458
- **Solved Count:** 2109
- **URL:** https://www.hackerrank.com/challenges/recalling-early-days-gp-with-trees

## Problem Statement

[Chinese Version](https://hr-testcases.s3.amazonaws.com/959/959-chinese.md)<br/>
[Russian Version](https://hr-testcases.s3.amazonaws.com/959/959_rus.md)<br/>

You are given a [tree](http://en.wikipedia.org/wiki/Tree_(graph_theory)) with N nodes and each has a value associated with it. You are given Q queries, each of which is either an update or a retrieval operation. 

The **update query** is of the format

	i j X

This means you'd have to add a [GP](http://en.wikipedia.org/wiki/Geometric_progression) series to the nodes which lie in the path from node `i` to node `j` (both inclusive) with first term of the GP as `X` on node `i` and the common ratio as `R` (given in the input)

The **retrieval** query is of the format

i j

You need to return the sum of the node values (S) lying in the path from node i to node j modulo 100711433. 

**Input Format**  
The first line contains two integers (N and R respectively) separated by a space.  
In the next N-1 lines, the i<sup>th</sup> line describes the i<sup>th</sup> edge: a line with two integers a b separated by a single space denotes an edge between a, b.  
The next line contains 2 space separated integers (U and Q respectively) representing the number of Update and Query operations to follow.  
U lines follow. Each of the next U lines contains 3 space separated integers (i,j, and X respectively).  
Each of the next Q lines contains 2 space separated integers, i and j respectively. 

**Output Format**  
It contains exactly Q lines and each line containing the answer of the i<sup>th</sup> query.

**Constraints**

2 <= N <= 100000  
2 <= R <= 10<sup>9</sup>  
1 <= U <= 100000  
1 <= Q <= 100000  
1 <= X <= 10  
1 <= a, b, i, j <= N  

**Sample Input**  

	6 2
    1 2
    1 4
    2 6
    4 5
    4 3
    2 2
    1 6 3
    5 3 5
    6 4
    5 1

**Sample Output**

	31
    18

**Explanation**

The node values after the first updation becomes :  

    3 6 0 0 0 12  
    
The node values after second updation becomes :  

    3 6 20 10 5 12  
    
Answer to Query #1: 12 + 6 + 3 + 10 = 31  
Answer to Query #2: 5 + 10 +3 = 18  

## Input Format

The first line contains two integers (N and R respectively) separated by a space.

In the next N-1 lines, the ith line describes the ith edge: a line with two integers a b separated by a single space denotes an edge between a, b.

The next line contains 2 space separated integers (U and Q respectively) representing the number of Update and Query operations to follow.

U lines follow. Each of the next U lines contains 3 space separated integers (i,j, and X respectively).

Each of the next Q lines contains 2 space separated integers, i and j respectively.

## Output Format

It contains exactly Q lines and each line containing the answer of the ith query.

## Constraints

2 <= N <= 100000

2 <= R <= 109

1 <= U <= 100000

1 <= Q <= 100000

1 <= X <= 10

1 <= a, b, i, j <= N

## Sample Input

6 2
1 2
1 4
2 6
4 5
4 3
2 2
1 6 3
5 3 5
6 4
5 1

## Sample Output

18

## Explanation

The node values after the first updation becomes :

3 6 0 0 0 12

The node values after second updation becomes :

3 6 20 10 5 12

Answer to Query #1: 12 + 6 + 3 + 10 = 31

Answer to Query #2: 5 + 10 +3 = 18

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
