# Sam's Puzzle (Approximate)

- **Domain:** python
- **Difficulty:** Advanced
- **Max Score:** 85
- **Success Ratio:** 0.6252439817826936
- **Total Submissions:** 1537
- **Solved Count:** 961
- **URL:** https://www.hackerrank.com/challenges/sams-puzzle

## Problem Statement

Sam invented a new puzzle game played on an $n \times n$ matrix named $puzzle$, where each cell contains a unique integer in the inclusive range between $1$ and $n^2$. The coordinate of the top-left cell is $(1, 1)$.

**The Moves**

A move consists of two steps:

1. Choose a sub-square of $puzzle$.
2. Rotate the sub-square in the *clockwise* direction.

For example: 

![image](https://s3.amazonaws.com/hr-challenge-images/0/1481461326-391b5e70d0-sam31.png)

We describe a move as the clockwise rotation of a $k \times k$ sub-square whose top-left corner is located at coordinate $(i, j)$. In the example above, $i = 1$, $j = 1$, and $k = 2$.

**Good Pairs of Cells**

A pair of cell is *good* if one of the following is true:

* They're located in the same row and the number in the left cell is less than the number in the right cell. 
* They're located in the same column and the number in the upper cell is less than the number in the lower cell.

The diagram below depicts all the *good* pairs of cells located in the same row:

![image](https://s3.amazonaws.com/hr-challenge-images/0/1481437201-9ff1620127-sams3.png)

The diagram below depicts all the *good* pairs of cells located in the same column:

![image](https://s3.amazonaws.com/hr-challenge-images/0/1481460380-071db1a562-sams2.png)

**Goodness of a Square**

We define the *goodness* of a sub-square to be the total number of good pairs of cells in the sub-square.

**The Goal**

Given the initial value of $puzzle$, maximize its goodness as much as is possible by performing a sequence of *at most* $500$ moves. Then print the necessary moves according to the *Output Format* specified below.

## Input Format

The first line contains an integer denoting $n$.
Each of the $n$ subsequent lines contains $n$ space-separated integers. The $j^{th}$ integer in the $i^{th}$ line denotes the cell located in coordinate $(i,j)$.


## Output Format

Print the following lines of output:

- On the first line, print an integer, $m$, denoting the number of moves necessary to maximize the goodness of $puzzle$. Recall that this number must be $\le 500$.
- For each move, print three space-separated integers describing its respective $i$, $j$, and $k$ values on a new line. Recall that a move is described as the clockwise rotation of a $k \times k$ sub-square whose top-left corner is located at coordinate $(i, j)$. 


## Constraints

* $1 \le n \le 30$
* Each cell contains a unique number in the inclusive range between $1$ and $n^2$.

**Scoring**

- We define $g_b$ as the goodness in the beginning, $g_a$ as the goodness after your moves, and $g_{max}$ as the maximum possible goodness.
- A valid answer earns $max(0, \large \frac{g_a - g_b}{g_{max} - g_b} \normalsize )  \times \text{100%}$ of a test case's available points (it's guaranteed that $g_{max}>g_{b}$). The total score will be rounded up to the next $\text{1%}$.

**Test Case Generation**

* Consider all the cells in $puzzle$ to be initially empty. Sam sorts the $n^2$ numbers in ascending order and then picks them one by one and places them in some random cell which has no empty cell to its left and no empty cell above it. This generates a square with goodness $n^2 \times (n-1)$.
* After generating $puzzle$, Sam makes some random rotations. During each step, he chooses three random numbers, $i$, $j$, and $k$, and rotates a $k \times k$ sub-square with the top-left corner at coordinate $(i, j)$ in the *counterclockwise* direction. Here $1 \le i, j, k \le n$ and $max(i,j)+k \le n+1$. 
* Sam makes *at most* $100$ such random counterclockwise rotations. This means that it's possible to achieve maximum goodness in as little as $100$ moves.

## Sample Input

3
8 6 9
7 2 5
1 4 3

## Sample Output

3
1 1 2
2 2 2
1 1 3

## Explanation

- After the first move:

- After the second move:

- After the third move:

The goodness after this sequence of moves is , and the maximum possible goodness is .

Because the initial goodness was , this solution will get  of the test case's available points.
