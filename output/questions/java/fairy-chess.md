# Fairy Chess

- **Domain:** java
- **Difficulty:** Advanced
- **Max Score:** 80
- **Success Ratio:** 0.7446700507614213
- **Total Submissions:** 1970
- **Solved Count:** 1467
- **URL:** https://www.hackerrank.com/challenges/fairy-chess

## Problem Statement

Let's play *Fairy Chess*!

You have an $n \times n$ chessboard. An $s$-leaper is a chess piece which can move from some square $(x_0, y_0)$ to some square $(x_1, y_1)$ if $abs(x_0 - x_1) + abs(y_0 - y_1) \le s$; however, its movements are restricted to *up* ($\uparrow$), *down* ($\downarrow$), *left* ($\leftarrow$), and *right* ($\rightarrow$) within the confines of the chessboard, meaning that diagonal moves are not allowed. In addition, the leaper cannot leap to any square that is occupied by a *pawn*.

Given the layout of the chessboard, can you determine the number of ways a leaper can move $m$ times within the chessboard?
 
**Note:** $abs(x)$ refers to the absolute value of some integer, $x$.

## Input Format

The first line contains an integer, $q$, denoting the number of queries. Each query is described as follows:

1. The first line contains three space-separated integers denoting $n$, $m$, and $s$, respectively.
2. Each line $i$ of the $n$ subsequent lines contains $n$ characters. The $j^{th}$ character in the $i^{th}$ line describes the contents of square $(i,j)$ according to the following key:
	- `.` indicates the location is *empty*.
    - `P` indicates the location is occupied by a *pawn*.
    - `L` indicates the location of the *leaper*.

## Output Format

For each query, print the number of ways the leaper can make $m$ moves on a new line. Because this value can be quite large, your answer must be modulo $10^9 + 7$.

## Constraints

- $1 \le q \le 10$
- $1 \le m \le 200$
- There will be exactly one `L` character on the chessboard.
- The $s$-leaper can move *up* ($\uparrow$), *down* ($\downarrow$), *left* ($\leftarrow$), and *right* ($\rightarrow$) within the confines of the chessboard. It *cannot* move diagonally.

## Sample Input

3
4 1 1
....
.L..
.P..
....
3 2 1
...
...
..L
4 3 2
....
...L
..P.
P...

## Sample Output

4
11
385

## Explanation

You must perform two queries, outlined below. The green cells denote a cell that was leaped to by the leaper, and coordinates are defined as .

- The leaper can leap to the following locations:

Observe that the leaper cannot leap to the square directly underneath it because it's occupied by a pawn. Thus, there are  ways to make  move and we print  on a new line.

- The leaper can leap to the following locations:

Thus, we print  on a new line.

Note: Don't forget that your answer must be modulo .
