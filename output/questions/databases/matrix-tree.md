# Matrix Tree

- **Domain:** databases
- **Difficulty:** Medium
- **Max Score:** 100
- **Success Ratio:** 0.8098290598290598
- **Total Submissions:** 468
- **Solved Count:** 379
- **URL:** https://www.hackerrank.com/challenges/matrix-tree

## Problem Statement

[Sevenkplus](http://sevenkplus.com/) has a rooted tree with $N$ vertices. The vertices are labeled from $1$ to $N$. $1$ is the root of the tree. Each vertex $v$ has a weight $W_v$.  
He forms a $N \times N$ matrix $M$ from the tree. $M$ is defined by  
$$M(x,y)=W_{lca(x,y)}$$  
where $lca(x,y)$ is the lowest common ancestor of vertex $x$ and vertex $y$.  
He wants to calculate the determinant of $M$.  

**Input Format**  
First line contains the number of vertices, $N$.  
Second line contains $N$ numbers, $W_1 ~ W_2 ~ \cdots ~ W_N$ separated by a space.   
This is followed by $N-1$ lines. Each line contains two numbers $x$, $y$, denoting that there is an edge between $x$  and $y$.  

**Output Format**  
Output one line, the determinant of $M$ modulo $(10^9 + 7)$.

**Constraints**  
$1 \le N \le 10^5$   
$\forall i, 0 \le W_i \le 10^9$. 

**Sample Input**

	3
	1 2 3
	1 2
    1 3

**Sample Output**

	2

**Explanation**

$$
M =  \left[ {\begin{array}{ccc}
   1 & 1 & 1\\\
   1 & 2 & 1\\\
   1 & 1 & 3
  \end{array} } \right ]
$$

Then, $$|M| = 1\times \left[ {\begin{array}{cc}
   2 & 1\\\
   1 & 3
  \end{array} } \right ] - 1 \times \left[ {\begin{array}{cc}
   1 & 1\\\
   1 & 3
  \end{array} } \right ] + 1 \times \left[ {\begin{array}{cc}
   1 & 2\\\
   1 & 1
  \end{array} } \right ]$$. 

Hence $|M| = (1 \times 5) - (1\times 2) + (1 \times -1) = 2$

**Timelimits**  
Timelimits for this challenge is given [here](https://www.hackerrank.com/environment)

## Input Format

First line contains the number of vertices, .

Second line contains  numbers,  separated by a space.

This is followed by  lines. Each line contains two numbers , , denoting that there is an edge between   and .

## Output Format

Output one line, the determinant of  modulo .

## Constraints

.

## Sample Input

1 2 3
1 2
1 3

## Explanation

Then,
.

Hence

Timelimits

Timelimits for this challenge is given here
