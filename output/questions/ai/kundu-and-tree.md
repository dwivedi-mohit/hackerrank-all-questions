# Kundu and Tree

- **Domain:** ai
- **Difficulty:** Hard
- **Max Score:** 80
- **Success Ratio:** 0.8812445223488168
- **Total Submissions:** 11410
- **Solved Count:** 10055
- **URL:** https://www.hackerrank.com/challenges/kundu-and-tree

## Problem Statement

Kundu is true tree lover. Tree is a connected graph having _N_ vertices and _N-1_  edges. Today when he got a tree, he colored each edge with one of either red(`r`) or black(`b`) color. He is interested in knowing how many triplets(a,b,c) of vertices are there , such that, there is atleast one edge having red color on all the three paths i.e. from vertex _a_ to _b_, vertex _b_ to _c_ and vertex _c_ to _a_ . Note that (a,b,c), (b,a,c) and all such permutations will be considered as the same triplet. 

If the answer is greater than 10<sup>9</sup> + 7, print the answer modulo (%) 10<sup>9</sup> + 7.

**Input Format**  
The first line contains an integer _N_, i.e., the number of vertices in tree.  
The next _N-1_ lines represent edges:  2 space separated integers denoting an edge followed by a color of the edge. A color of an edge is denoted by a small letter of English alphabet, and it can be either red(`r`) or black(`b`).  

**Output Format**  
Print a single number i.e. the number of triplets.  

**Constraints**  
1 &le; _N_ &le; 10<sup>5</sup><br> 
A node is numbered between 1 to *N*.  

**Sample Input**  

	5
    1 2 b
    2 3 r
    3 4 r
    4 5 b

    
**Sample Output**  

	4

**Explanation**

Given tree is something like this.<br>
![image](https://s3.amazonaws.com/hr-assets/0/1526563539-7ce683027b-kundu-and-trees.jpg)

(2,3,4) is one such triplet because on all paths i.e 2 to 3, 3 to 4 and 2 to 4 there is atleast one edge having red color.<br>
(2,3,5), (1,3,4) and (1,3,5) are other such triplets.  
Note that (1,2,3) is NOT a triplet, because the path from 1 to 2 does not have an edge with red color.

## Input Format

The first line contains an integer N, i.e., the number of vertices in tree.

The next N-1 lines represent edges:  2 space separated integers denoting an edge followed by a color of the edge. A color of an edge is denoted by a small letter of English alphabet, and it can be either red(r) or black(b).

## Output Format

Print a single number i.e. the number of triplets.

## Constraints

1 ≤ N ≤ 105

A node is numbered between 1 to N.

## Sample Input

1 2 b
2 3 r
3 4 r
4 5 b

## Explanation

Given tree is something like this.

(2,3,4) is one such triplet because on all paths i.e 2 to 3, 3 to 4 and 2 to 4 there is atleast one edge having red color.

(2,3,5), (1,3,4) and (1,3,5) are other such triplets.

Note that (1,2,3) is NOT a triplet, because the path from 1 to 2 does not have an edge with red color.
