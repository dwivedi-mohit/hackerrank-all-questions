# Grid Maze

---

| Field | Value |
|---|---|
| **Slug** | `grid-maze` |
| **Domain** | misc |
| **Difficulty** | Hard |
| **Score** | 100 |
| **Contest** | 101hack28 |
| **URL** | https://www.hackerrank.com/challenges/grid-maze |

---

## Preview

You are given matrix n × m. Each cell in the matrix is either a wall or empty. Find the minimum number of walls needed to be broken that we can go from cell S to cell P and after that get out of the matrix.

## Problem Statement

Mika and Zloba love grid mazes. A grid maze is an $n \times m$ rectangle maze where each cell is either a wall or an empty cell. Let us denote the cell at the intersection of the $i$<sup>$th$</sup> line and the $j$<sup>$th$</sup> column $(i, j)$. In any moment, our friend can move from one cell to another only if both cells are empty and have a common side. So, from empty cell $(i, j)$, they can move to empty cells $(i - 1, j)$, $(i, j - 1)$, $(i, j + 1)$, and $(i + 1, j)$. But this may not be so easy. Sometimes there is a lot of walls and there is no clear way between two cells. In this case we should break some walls; if we break a wall, the cell containing the wall becomes empty.

At the beginning Mika and Zloba are located at the empty cell $S$. They must go for their supply located at the empty cell $P$ and after that get out of the maze. We consider that they got out of the maze only if they are located at a cell on the border of the maze.

We all like our heroes and we want to help them. Find the minimum number of walls needed to be broken so that Mika and Zloba can complete their journey.

**Input Format**<br>

The first line contains two integers, $n$ and $m$ ($1\leq n, m \leq 1000$), where $n$ and $m$ are the maze's height and width.

Each of the next $n$ lines contains $m$ characters. They describe the maze: the character at the intersection of the $i$<sup>$th$</sup> line and the $j$<sup>$th$</sup> column is equal to the value of cell $(i, j)$. Cells can have values ".", "#", $S$, and $P$, where "." denotes an empty cell, "#" denotes a cell containing a wall, and $S$ and $P$ are empty points, vital for our heroes as described in the statement. It is guaranteed that there will be exactly one cell with value $S$ and exactly one cell with value $P$ in the maze.


**Output Format**<br>

In the single line print one integer - the minimum number of walls needed to be broken so that Mika and Zloba can move from cell $S$ to cell $P$ and after that get out of the maze.

**Sample Input 1:**<br>

    5 6
    ##..##
    ######
    S#####
    ##P##.
    ###..#

**Sample Output 1:**<br>


    2

**Sample Input 2:**<br>

    4 4
    ...#
    #P.#
    ##.#
    .#S.
  

**Sample Output 2:**<br>    


    0

## Sample Tests

### Test 1

```
5 6
##..##
######
S#####
##P##.
###..#
```

### Test 2

```
2
```

### Test 3

```
4 4
...#
#P.#
##.#
.#S.
```

### Test 4

```
0
```
