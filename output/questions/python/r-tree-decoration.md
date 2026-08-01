# Robanukkah Tree

- **Domain:** python
- **Difficulty:** Hard
- **Max Score:** 90
- **Success Ratio:** 0.8918918918918919
- **Total Submissions:** 74
- **Solved Count:** 66
- **URL:** https://www.hackerrank.com/challenges/r-tree-decoration

## Problem Statement

Robot Bender is celebrating Robanukkah, the most important holiday for robots.

He <s>stole</s> bought a Robanukkah tree, which is actually a common tree (i.e., a connected acyclic graph with $N$ vertices). He wants to decorate it with regular [polyhedrons](https://en.wikipedia.org/wiki/Polyhedron) by placing one regular polyhedron in each vertex.

A regular polyhedron is a convex polyhedron whose faces are identical regular polygons. There are five types of regular polyhedrons:

<img src="https://s3.amazonaws.com/hr-challenge-images/15554/1469365303-23972b13c3-hedron.jpg" title="hedron.jpg" />

Bender has $F$ types of polyhedrons. All polyhedrons of the same type are indistinguishable by their shape. Bender has at least $N$ polyhedrons of each available type.

In addition, Bender has $K$ colors. He paints each face of each polyhedron in *one* of these colors.

Bender considers two polyhedrons to be _similar_ if one of the following is true:

* They are of the same type.
* Some face of the first polyhedron and some face of the second polyhedron are painted with the same color.

Bender considers the decorated tree to be _beautiful_ if any two adjacent vertices don't contain similar polyhedrons. In particular, any decoration of a one-vertex tree is beautiful.

Two polyhedrons are equally painted if it is possible to rotate and move one of them so that it coincides with the other *and* the coincided faces are painted in the same color.

Two decorations of the tree are the same if each vertex in both decorations has equally painted polyhedrons.

Can you help Bender find the number of ways he can decorate his tree beautifully? Find and print it modulo $10^9+9$.

## Input Format

The first line contains three space-separated integers denoting the respective values of $N$ (the number of vertices in the tree), $K$ (the number of available colors), and $F$ (the number of types of polyhedrons).		
The second line contains $F$ different space-separated numbers describing $f_1, \dots, f_F$, where $f_i$ is the number of faces of polyhedrons of the $i^{th}$ type. $f_i \in \{4,6,8,12,20\}$.			
The third line contains $N-1$ space-separated numbers describing $p_2, \dots, p_N$, where $p_i$ is index of parent of $i^{th}$ vertex. The root of the tree has index $1$.	

**Note:** If the tree consists of only one vertex, the third line will be empty.

## Output Format

Print a single integer denoting the number of ways to decorate the tree modulo $10^9+9$.

## Constraints

* $1 \le N \le 5 \times 10^4$
* $1 \le K \le 10^5$
* $1 \le F \le 5$

## Sample Input

3 3 2
4 6
1 1

## Explanation

Let's consider all ways to decorate the given Robanukkah tree:

- Cube in the root, tetrahedrons in the leaves.

- All faces of the cube are painted in the same color (which can be chosen in  ways). Each tetrahedron can then be independently painted using one or two of the remaining colors, and there are  ways to do this. In total, there are  ways.

- Faces of the cube are painted in exactly two colors (the pair of colors can be chosen in  ways). There are  ways to paint a cube using exactly two colors. The painting of tetrahedrons will be clearly defined: all faces of both of them should be painted in the leftover color. In total,  ways.

- Tetrahedron in the root, cubes in the leaves.
- All faces of the tetrahedron are painted in the same color (which can be chosen in  ways). Each cube can then be independently painted using one or two of the remaining colors, and there are  ways to do that. In total,  ways.

- Faces of the tetrahedron are painted in exactly two colors (which can be chosen in  ways). There are  ways to paint the tetrahedron in exactly two colors. The painting of each cube will be clearly defined in that all faces of both of them should be painted in the leftover color. In total,  ways.

In total, .

Note: Your output must be modulo .
