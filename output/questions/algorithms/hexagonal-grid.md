# Hexagonal Grid

- **Domain:** algorithms
- **Difficulty:** Hard
- **Max Score:** 70
- **Success Ratio:** 0.8269100743745774
- **Total Submissions:** 4437
- **Solved Count:** 3669
- **URL:** https://www.hackerrank.com/challenges/hexagonal-grid

## Problem Statement

You are given a hexagonal grid consisting of two rows, each row consisting of $n$ cells. The cells of the first row are labelled $a_1, a_2, \ldots a_n$ and the cells of the second row are labelled $b_1, b_2, \ldots, b_n$.  

For example, for $n = 6$:

![Grid Shape](https://s3.amazonaws.com/hr-assets/0/1495564532-9e16e289ea-3.png "The grid shape.")

(Note that the $b_i$ is connected with $a_{i+1}$.)

Your task is to tile this grid with $2\times 1$ *tiles* that look like the following:

![Orientations](https://s3.amazonaws.com/hr-assets/0/1495564517-f725e11e0b-1.png "Orientations of the 2x1 tile.")

As you can see above, there are three possible orientations in which a tile can be placed.

Your goal is to tile the whole grid such that every cell is covered by a tile, and no two tiles occupy the same cell. To add to the woes, certain cells of the hexagonal grid are *blackened*. No tile must occupy a blackened cell.

Is it possible to tile the grid?

Here's an example. Suppose we want to tile this grid:

![Example Blank](https://s3.amazonaws.com/hr-assets/0/1495564538-9a59a63208-4.png "Example of a grid with some blackened cells.")

Then we can do the tiling as follows:

![Example Tiled](https://s3.amazonaws.com/hr-assets/0/1495564526-f0c430b796-2.png "Example of a tiled grid.")

## Input Format

The first line contains a single integer $t$, the number of test cases.  

The first line of each test case contains a single integer $n$ denoting the length of the grid.  
The second line contains a binary string of length $n$. The $i^\text{th}$ character describes whether cell $a_i$ is blackened.  
The third line contains a binary string of length $n$. The $i^\text{th}$ character describes whether cell $b_i$ is blackened.  
A `0` corresponds to an empty cell and a `1` corresponds to blackened cell.  

## Output Format

For each test case, print `YES` if there exists at least one way to tile the grid, and `NO` otherwise.

## Constraints

- $1 \le t \le 100$  
- $1 \le n \le 10$  


## Sample Input

6
6
010000
000010
2
00
00
2
00
10
2
00
01
2
00
11
2
10
00

## Sample Output

YES
YES
NO
NO
YES
NO

## Explanation

The first test case in the sample input describes the example given in the problem statement above.

For the second test case, there are two ways to fill it: either place two diagonal tiles side-by-side or place two horizontal tiles.
