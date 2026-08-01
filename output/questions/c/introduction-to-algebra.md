# Introduction to Algebra

- **Domain:** c
- **Difficulty:** Medium
- **Max Score:** 100
- **Success Ratio:** 0.6723404255319149
- **Total Submissions:** 235
- **Solved Count:** 158
- **URL:** https://www.hackerrank.com/challenges/introduction-to-algebra

## Problem Statement

Welcome to Sevenkplus' perfect math class! In this class we will study an algebraic structure called magma. 

A **magma** is a nonempty set $M$ equipped with a binary operation $\bigodot : M\times M\to M$. We write $x\bigodot y$ for the application of the operator on the two elements $x,y\in M$.
Note that there are no restrictions on the binary operation. For example, we cannot assume that $(x\bigodot y)\bigodot z=x\bigodot (y\bigodot z)$ always holds.

There are many different types of magmas. Some are interesting, others are even more interesting. Studying specific types of magmas is an important part of mathematics.
Below we introduce the following types of magmas.

A **quasigroup** is a magma such that for all $x,y\in M$, there exists a unique $z\in M$ such that $x\bigodot z=y$ and a unique $w\in M$ such that $w\bigodot x=y$.

A **loop** is a quasigroup such that there is a unique element $e\in M$ such that for all $x\in M$, $e\bigodot x=x\bigodot e=x$.

A **semigroup** is a magma such that for all $x,y,z\in M$, we have $(x\bigodot y)\bigodot z=x\bigodot(y\bigodot z)$.

A **monoid** is a semigroup such that there is a uniqe element $e\in M$ such that for all $x\in M$, $e\bigodot x=x\bigodot e=x$.

A **group** is a monoid such that for all $x\in M$, there exists $y\in M$ such that $x\bigodot y=y\bigodot x=e$.

An **abelian group** is a group such that for all $x,y\in M$, we have $x\bigodot y=y\bigodot x$.

A **rack** is a magma such that (1) for all $x,y,z\in M$, we have $x\bigodot (y\bigodot z)=(x\bigodot y)\bigodot(x\bigodot z)$ and (2) for all $x,y\in M$, there exists a unique $z\in M$ such that $x\bigodot z=y$.

A **quandle** is a rack such that for all $x\in M$, we have $x\bigodot x=x$.

In this problem, you are given several magmas. You have to tell us what types they are.

## Input Format

The first line is a integer $T$, the number of magmas given to you.
Following are $T$ magmas.

For each magma, the first line is an integer $n$, the size of the set $M$. (Yes, you only need to consider finite algebraic structures here, which greatly simplifies the problem.)
Without loss of generality, we assume that $M=\{0,1,\ldots,n-1\}$.

Following are $n$ lines. Each line contains $n$ space-separated integers. The $j$-th number on the $i$-th line is $(i-1)\bigodot (j-1)$ where $\bigodot$ is the binary operation of the magma.

**Constraints**  

$1 \le T\le 60$  
$1\le n\le 110$. 

## Output Format

For each magma, output one line, which is the **magic number**  of the magma (denoted by $S$ henceforth).

The magic number $S$ of a magma is defined as:

* Initially, let $S=0$.
* If the magma is a quasigroup, add $1$ to $S$.
* If the magma is a loop, add $2$ to $S$.
* If the magma is a semigroup, add $4$ to $S$.
* If the magma is a monoid, add $8$ to $S$.
* If the magma is a group, add $16$ to $S$.
* If the magma is an abelian group, add $32$ to $S$.
* If the magma is a rack, add $64$ to $S$.
* If the magma is a quandle, add $128$ to $S$.
* Then $S$ is the magic number of the magma.

## Constraints

.

## Sample Input

1
0
2
1 1
1 0

## Sample Output

0

## Explanation

The first magma satisfies all rules while the second one satisfies none.
