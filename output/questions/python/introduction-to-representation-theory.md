# Introduction to Representation Theory

- **Domain:** python
- **Difficulty:** Advanced
- **Max Score:** 100
- **Success Ratio:** 0.8688524590163934
- **Total Submissions:** 244
- **Solved Count:** 212
- **URL:** https://www.hackerrank.com/challenges/introduction-to-representation-theory

## Problem Statement

Welcome to Sevenkplus' perfect math class! In this class, you will learn about representation theory. And this class is in a different format than before: Learning by doing! You need to solve a problem, which can be solved elegantly using (really elementary) representation theory. (Of course you can solve this problem without representation theory. But learning more is helpful!)

Sevenkplus had an $n\times n$ complex matrix $M$. He calculated $Tr(M^0), \ldots,Tr(M^{m-1})$ and found that $M^m=I$. (For a square matrix $A$, $Tr(A)$ is the trace of $A$. $I$ is the $n\times n$ identity matrix.)
However, the dark side of the world destroyed $M$, and only $n, m, Tr(M^0), \ldots, Tr(M^{m-1})$ remained.

Sevenkplus wants to recover his beloved $M$. However, this is impossible.  
Nevertheless, doing something weaker is possible: Only recover the eigenvalues of $M$. Here the eigenvalues are defined to be the entries on the diagonal of the Jordan normal form of $M$. For a fixed $M$, they are unique up to permutation.

## Input Format

The first line contains two space separated integers, $n$ and $m$.  
Followed by $m$ lines where for each value of $k \in [0,m)$ line contains two real numbers $a_k, b_k$, which means that $Tr(M^k) = a_k + i \cdot b_k$, where $i$ is the imaginary unit.  

**Constraints**  
$1\leqslant n \leqslant 10000$  
$1 \leqslant m \leqslant 2000$  
$|a_k|, |b_k| \leqslant 10000$  
It is guaranteed that there is an $M$ that satisfies the relations.  

## Output Format

Print $n$ lines where for each value of $k \in [0,m)$ line contains two real numbers $c_k, d_k$.  
The multi-set of $c_k+i\cdot d_k$ should be the multi-set of eigenvalues of $M$.  

You can output the eigenvalues in any order.  
In case of multiple answers output any of them, your answer is considered correct if your answer satisfies the input, within absolute error $10^{-6}$.  

## Constraints

It is guaranteed that there is an  that satisfies the relations.

## Sample Input

2 4
2 0
0 0
2 0
0 0

## Sample Output

1 0
-1 0

## Explanation

Two possible 's are  and . Note that there may be other 's that satisfies the relations.
