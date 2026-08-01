# Find The Operations

- **Domain:** mathematics
- **Difficulty:** Hard
- **Max Score:** 80
- **Success Ratio:** 0.8658892128279884
- **Total Submissions:** 343
- **Solved Count:** 297
- **URL:** https://www.hackerrank.com/challenges/flip

## Problem Statement

You are given a square grid of size N, with rows numbered from 0 to N - 1 starting from the top and columns numbered from 0 to N - 1 starting from the left.   

A cell (u, v) refers to the cell that is on the u<sup>th</sup> row and the v<sup>th</sup> column. Each cell contains an integer - 0 or 1. You can pick any cell and flip the number in all the cells (including the picked cell) within the Manhattan distance D from the picked cell. A flip here means changing the number from 0 to 1 and vice-versa. The manhattan distance from the cell (u, v) to the cell (x, y) is equal to $|u - x| + |v - y|$ where $|i|$ is the absolute value of i.   

Your mission is to change all values in the grid to zero without using more than N×N flips.

**Input Format**  
The first line of the input contains two integers N and D  separated by a single space.  
Each line in the next N lines contains N integers separated by a single space which are either 0 or 1. the i<sub>th</sub> number on the j<sub>th</sub> line is the number on the cell (i - 1, j - 1) of the grid.

**Constraints**  
1 ≤  N ≤  20  
 0 ≤ D ≤ 40

**Output Format**  
If there is no solution, your output should contain exactly a single string "Impossible" (without quotes). If a solution exists, print out the string "Possible" (without quotes) in the first line of your output. In the second line, print out an integer M which represent the number of operations that you need. Each line in the next M lines should contain a pair of integers separated by a single space representing the cell that you picked for the corresponding operation. Note that if there is more than one solution you can pick any one of them.

**Sample Input:#00**

    3 1
    0 1 0
    1 1 1
    0 1 0

**Sample Output:#00**

    Possible
    1
    1 1

**Sample Input:#01**

    3 2
    1 0 1 
    1 1 0 
    0 0 0 

**Sample Output:#01**

    Impossible

**Explanation**

In the first testcase, we can perform the first operation in the center cell, this will flip all the elements to 0 within 1 manhattan distance.  
In the second testcase, we cannot make it an all 0 matrix under 9 moves. Hence, Impossible. 


## Input Format

The first line of the input contains two integers N and D  separated by a single space.

Each line in the next N lines contains N integers separated by a single space which are either 0 or 1. the ith number on the jth line is the number on the cell (i - 1, j - 1) of the grid.

## Output Format

If there is no solution, your output should contain exactly a single string "Impossible" (without quotes). If a solution exists, print out the string "Possible" (without quotes) in the first line of your output. In the second line, print out an integer M which represent the number of operations that you need. Each line in the next M lines should contain a pair of integers separated by a single space representing the cell that you picked for the corresponding operation. Note that if there is more than one solution you can pick any one of them.

Sample Input:#00

3 1
0 1 0
1 1 1
0 1 0

Sample Output:#00

Possible
1
1 1

Sample Input:#01

3 2
1 0 1
1 1 0
0 0 0

Sample Output:#01

Impossible

## Constraints

1 ≤  N ≤  20

 0 ≤ D ≤ 40

## Explanation

In the first testcase, we can perform the first operation in the center cell, this will flip all the elements to 0 within 1 manhattan distance.

In the second testcase, we cannot make it an all 0 matrix under 9 moves. Hence, Impossible.
