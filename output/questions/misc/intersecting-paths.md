# Intersecting Paths

---

| Field | Value |
|---|---|
| **Slug** | `intersecting-paths` |
| **Domain** | misc |
| **Difficulty** | Hard |
| **Score** | 100 |
| **Contest** | 101hack33 |
| **URL** | https://www.hackerrank.com/challenges/intersecting-paths |

---

## Preview

Find if 2 paths intersect.

## Problem Statement

There are $N$ buildings in a line. They are indexed from $1$ to $N$ from left to right with the leftmost being $1$ and the rightmost being $N$. The $i^{th}$ building has a height $A_i$.	
A person starts walking following this crazy procedure:	

- Step 1: The walk starts from some building $x$.	
- Step 2: He moves to the next building (to the right) of a height smaller than the current building's height. If there is no such building, he stops the walk and goes to step $4$.	
- Step 3: He moves to the next building (to the right) of a height larger than the current building's height. If there is no such building, he stops the walk and goes to step $4$. 
- Step 4: If the walk has been stopped in step $2$ or step $3$, then stop completely.  Otherwise, go back to step $2$.
  

Formally:	
In step $2$, if the person is at building $i$, he moves to building $j$, where $j$ is the least index, such that $j > i$ and $A_i > A_j$. He stops if there is no such $j$.	

In step $3$, if the person is at building $i$, he moves to building $j$, where $j$ is the least index, such that $j > i$ and $A_i < A_j$. He stops if there is no such $j$.	

The person wants to know if there is, at least, $1$ common building between the walk starting from building $i$ and the walk starting from building $j$. 	
He has $Q$ questions.	 
Please help him answer all the questions.

## Input Format

The first line contains $N$, the number of buildings.	
The next line contains $N$ integers representing the array $A$.			
The next line contains $Q$, the number of queries.		
The next $Q$ lines each contain $2$ integers, $x$ and $y$ $(x < y)$ representing the $2$ starting points.

***Constraints***	
$ 1 \le N \le 5 * 10^5 $	
$ 1 \le A_i \le 10^9 $	
$ 1 \le Q \le 5 * 10^5$		
For each query, $ 1 \le x < y \le N$

## Output Format

For each query, output a single line containing $1$ if the paths intersect. Otherwise, output $0$.

## Sample Tests

### Test 1

```
5 
10 30 20 50 40 
3 
1 3 
2 3 
2 5
```

### Test 2

```
0 
1 
1
```
