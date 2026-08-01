# Dynamic Summation

- **Domain:** databases
- **Difficulty:** Hard
- **Max Score:** 150
- **Success Ratio:** 0.7982017982017982
- **Total Submissions:** 2002
- **Solved Count:** 1598
- **URL:** https://www.hackerrank.com/challenges/dynamic-summation

## Problem Statement

Given a tree of _N_ nodes, where each node is uniquely numbered in between _[1, N]_. Each node also has a value which is initially 0. You need to perform following two operations in the tree.  

1. Update Operation
2. Report Operation

**Update Operation**

    U r t a b

Adds <code>a<sup>b</sup> + (a+1)<sup>b</sup> + (b+1)<sup>a</sup></code> to all nodes in the subtree rooted at `t`, considering that tree is rooted at `r` (see explanation for more details).  

**Report Operation**

    R r t m
    
Output the sum of all nodes in the subtree rooted at `t`, considering that tree is rooted at `r`. Output the sum modulo `m` (see explanation for more details).

**Input Format**

First line contains _N_, number of nodes in the tree.  
Next _N-1_ lines contain two space separated integers _x_ and _y_ which denote that there is an edge between node _x_ and node _y_.  
Next line contains _Q_, number of queries to follow.  
Next _Q_ lines follow, each line will be either a report operation or an update operation.  

**Output Format**

For each report query output the answer in a separate line.

**Constraints**

1 ≤ _N_ ≤ 100000  
1 ≤ _Q_ ≤ 100000  
1 ≤ _m_ ≤ 101  
1 ≤ _r, t, x, y_ ≤ _N_  
_x_ &ne; _y_  
1 ≤ _a, b_ ≤ 10<sup>18</sup>  

**Notes**

1. There will be at most one edge between a pair of nodes.
2. There will be no loop.
2. Tree will be completely connected. 

**Sample Input**

	4
	1 2
	2 3
	3 4
	4
	U 3 2 2 2
	U 2 3 2 2
	R 1 2 8
	R 4 3 9

**Sample Output**

	2
    3
   
**Explanation**

Initially Values in each node : [0,0,0,0]  
The first query is `U 3 2 2 2`. Here, tree is rooted at 3. It looks like 

        3(0)
       / \
      /   \
     2(0)  4(0)
     |
     |
     1(0)

For the sub tree rooted at 2 ( nodes 2 and 1 ), we add a<sup>b</sup>  + (a+1)<sup>b</sup> + (b+1)<sup>a</sup> = 2<sup>2</sup> + 3<sup>2</sup> + 3<sup>2</sup> = 22. After first update operation, nodes 1, 2, 3, and 4 will have values 22, 22, 0 and 0 respectively.  

        3(0)
       / \
      /   \
     2(22) 4(0)
     |
     |
     1(22)

The second query is `U 2 3 2 2`. Here, tree is rooted at 2. It looks like

        2(22)
       / \
      /   \
     1(22) 3(0)
           |
           |
           4(0)

For the sub tree rooted at 3 (nodes 3 and 4), we add a<sup>b</sup> + (a+1)<sup>b</sup> + (b+1)<sup>a</sup> = 2<sup>2</sup> + 3<sup>2</sup> + 3<sup>2</sup> = 22. After second update operation, nodes 1, 2, 3, and 4 each have values 22,22,22,22 respectively.  

        2(22)
       / \
      /   \
     1(22) 3(22)
           |
           |
           4(22)


The first report query is `R 1 2 8` asks for the sum modulo 8 of the subtree rooted at 2, when the tree is rooted at 1. The tree looks like 

    1(22)
     \
      \
       2*(22)
       |
       |
       3*(22)
       |
       |
       4*(22)

The sum of the values of nodes 2, 3 and 4 are 

    (22 + 22 + 22) % 8 = 2

The second report query is `R 4 3 9` asks for the sum modulo 9 of the subtree rooted at 3 when the tree is rooted at 4. The tree looks like 

    4(22)
     \
      \
       3*(22)
       |
       |
       2*(22)
       |
       |
       1*(22)

The sum of the values of nodes 3, 2 and 1 are 

    (22 + 22 + 22) % 9 = 3
    
<sub>**Time Limits:**  
C, C++: 4s | Java and other JVM based languages: 10s | Python, Python3 = 45s | Other interpreted Language: 30s | C#, Haskell: 10s | Rest: 3 times of [default](https://www.hackerrank.com/environment).  
</sub>

## Input Format

First line contains N, number of nodes in the tree.

Next N-1 lines contain two space separated integers x and y which denote that there is an edge between node x and node y.

Next line contains Q, number of queries to follow.

Next Q lines follow, each line will be either a report operation or an update operation.

## Output Format

For each report query output the answer in a separate line.

## Constraints

1 ≤ N ≤ 100000

1 ≤ Q ≤ 100000

1 ≤ m ≤ 101

1 ≤ r, t, x, y ≤ N

x ≠ y

1 ≤ a, b ≤ 1018

Notes

- There will be at most one edge between a pair of nodes.

- There will be no loop.

- Tree will be completely connected.

## Sample Input

1 2
2 3
3 4
4
U 3 2 2 2
U 2 3 2 2
R 1 2 8
R 4 3 9

## Sample Output

3

## Explanation

Initially Values in each node : [0,0,0,0]

The first query is U 3 2 2 2. Here, tree is rooted at 3. It looks like

    3(0)
   / \
  /   \
 2(0)  4(0)
 |
 |
 1(0)

For the sub tree rooted at 2 ( nodes 2 and 1 ), we add ab  + (a+1)b + (b+1)a = 22 + 32 + 32 = 22. After first update operation, nodes 1, 2, 3, and 4 will have values 22, 22, 0 and 0 respectively.

    3(0)
   / \
  /   \
 2(22) 4(0)
 |
 |
 1(22)

The second query is U 2 3 2 2. Here, tree is rooted at 2. It looks like

    2(22)
   / \
  /   \
 1(22) 3(0)
       |
       |
       4(0)

For the sub tree rooted at 3 (nodes 3 and 4), we add ab + (a+1)b + (b+1)a = 22 + 32 + 32 = 22. After second update operation, nodes 1, 2, 3, and 4 each have values 22,22,22,22 respectively.

    2(22)
   / \
  /   \
 1(22) 3(22)
       |
       |
       4(22)

The first report query is R 1 2 8 asks for the sum modulo 8 of the subtree rooted at 2, when the tree is rooted at 1. The tree looks like

1(22)
 \
  \
   2*(22)
   |
   |
   3*(22)
   |
   |
   4*(22)

The sum of the values of nodes 2, 3 and 4 are

(22 + 22 + 22) % 8 = 2

The second report query is R 4 3 9 asks for the sum modulo 9 of the subtree rooted at 3 when the tree is rooted at 4. The tree looks like

4(22)
 \
  \
   3*(22)
   |
   |
   2*(22)
   |
   |
   1*(22)

The sum of the values of nodes 3, 2 and 1 are

(22 + 22 + 22) % 9 = 3

Time Limits:

C, C++: 4s | Java and other JVM based languages: 10s | Python, Python3 = 45s | Other interpreted Language: 30s | C#, Haskell: 10s | Rest: 3 times of default.
