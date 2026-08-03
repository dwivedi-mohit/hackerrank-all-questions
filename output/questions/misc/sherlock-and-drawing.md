# Sherlock and Drawing

---

| Field | Value |
|---|---|
| **Slug** | `sherlock-and-drawing` |
| **Domain** | misc |
| **Difficulty** | Expert |
| **Score** | 100 |
| **Contest** | 101hack40 |
| **URL** | https://www.hackerrank.com/challenges/sherlock-and-drawing |

---

## Preview

Help Watson draw a binary tree in a grid!

## Problem Statement

Watson has always wanted to draw full binary trees in grids. Each non-leaf node in a full binary tree has two children. In a grid, each row number $r$ is indexed in increasing order from top to bottom, and each column number $c$ is indexed in increasing order from left to right. A cell's location is represented as $(r, c)$, where $r$ is its row number and $c$ is its column number. Assuming that Watson has a grid of infinite size, he first draws a complete binary tree, $T_1$, of height $1$ in the grid, as shown below:

![Selection_019](https://s3.amazonaws.com/hr-challenge-images/0/1457644044-931b946619-Selection_019.png)

Here, the character `E` denotes an edge and the character `N` denotes a node.

To create a full binary tree of height $2$ named $T_2$, Watson creates a copy of $T_1$ and aligns it with $T_1$ such that both the roots have the same row number and a single empty column separates the *rightmost child* of $T_1$ from the *leftmost child* of $\text{copy}(T_1)$. The result of this operation looks like this:

![Selection_021](https://s3.amazonaws.com/hr-challenge-images/0/1457644283-7490977f64-Selection_021.png)

Next, he adds diagonal edges and parent nodes to the respective roots of $T_1$ and $\text{copy}(T_1)$ until the trees' ancestral nodes converge into the root node of $T_2$ (depicted below):

![Selection_020](https://s3.amazonaws.com/hr-challenge-images/0/1457644498-fcf7a6c8a6-Selection_020.png)

In this way, we can represent a full binary tree of any height in a grid. Watson's algorithm is summarized as follows:

```
//draws full binary tree of height H in the grid

function drawTree( H ):
    if H == 1:
        Print T1(as defined in statement) in grid
        return

    T = drawTree( H - 1 )
    T’ = copy( T )

    Put T’ to right of T and align so that the row numbers of both the roots are the same.
    Leave one column between rightmost child of T and leftmost child of T’.

    Let (r, c) be coordinates of root of T
    Let (r, c’) be coordinates of root of T’
    // c’ will be greater than c.

    do:
        r -= 1
        c += 1
        c’ -= 1
        put character ’E’ at cells (r, c) and (r, c’)
    while c != c’

    //Now, c == c’.
    //(r, c) is the coordinates of the root of tree of height H.
    put character ’N’ at cell (r, c)
```

---- 

Sherlock wants to put Watson's algorithm to the test by coming up with a *query*. He gives Watson an integer, $h$, and cell coordinates $(r_{root}, c_{root})$, telling him to draw a full binary tree of height $h$ such that the root of this tree lies at coordinates $(r_{root}, c_{root})$.

Next, Sherlock gives Watson $q$ queries in the following form:

- $r_1, c_1, r_2, c_2$: Print two space-separated integers denoting the respective numbers of `N` and `E` characters enclosed in the rectangular grid defined by top-left and bottom-right corner coordinates $(r_1, c_1)$ and $(r_2, c_2)$, respectively. 		

	Note that the cells $(r_1, c_1)$ and $(r_2, c_2)$ are both included in the query rectangle, meaning the boundaries are within the confines of the grid.
 
**Warning:** Use fast IO methods as the input files can be very large.

## Input Format

The first line contains four space-separated integers describing the respective values of:

1. $h$, the height of the binary tree.
2. $r_{root}$, the row where the root is located.
3. $c_{root}$, the column where the root is located.
4. $q$, the number of queries.

Each of the $q$ subsequent lines contains four space-separated integers describing the respective values of:

1. $r_1$, the row at the inclusive upper boundary of the query rectangle.
2. $c_1$, the column at the inclusive left-hand boundary of the query rectangle.
3. $r_2$, the row at the inclusive lower boundary of the query rectangle.
4. $c_2$, the column at the inclusive right-hand boundary of the query rectangle.

## Output Format

For each query, print two space-separated integers describing the respective numbers of nodes and edges in the rectangular query area.

## Constraints

- $1 \le h \le 50$ 

- $1 \le q \le 12 \times 10^4$ 

- $-10^{18} \le r_{root}, c_{root}, r_1, c_1, r_2, c_2 \le 10^{18}$ 

- $r_1 \le r_2$ 

- $c_1 \le c_2$   


**Subtasks** 


- For $\text{10%}$ of the maximum score, $1 \le h \le 10$ and $1 \le q \le 10$. 

- For additional $\text{15%}$ of the maximum score, $1 \le h \le 10$ and $1 \le q \le 12 \times 10^4$.

## Sample Tests

### Test 1

```
//draws full binary tree of height H in the grid
function
drawTree
(
H
)
:
if
H
==
1
:
Print
T1
(
as
defined
in
statement
)
in
grid
return
T
=
drawTree
(
H
-
1
)
T
’
=
copy
(
T
)
Put
T
’
to
right
of
T
and
align
so
that
the
row
numbers
of
both
the
roots
are
the
same
.
Leave
one
column
between
rightmost
child
of
T
and
leftmost
child
of
T
’
.
Let
(
r
,
c
)
be
coordinates
of
root
of
T
Let
(
r
,
c
’
)
be
coordinates
of
root
of
T
’
// c’ will be greater than c.
do:
r
-=
1
c
+=
1
c
’
-=
1
put
character
’
E
’
at
cells
(
r
,
c
)
and
(
r
,
c
’
)
while
c
!=
c
’
//Now, c == c’.
//(r, c) is the coordinates of the root of tree of height H.
put
character
’
N
’
at
cell
(
r
,
c
)
```

### Test 2

```
2 0 5 3
0 0 0 7
0 5 5 10
3 0 5 4
```

### Test 3

```
1 0
4 4
3 2
```
