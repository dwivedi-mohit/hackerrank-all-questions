# Ema's Supercomputer

- **Domain:** java
- **Difficulty:** Medium
- **Max Score:** 40
- **Success Ratio:** 0.7226089538451387
- **Total Submissions:** 30311
- **Solved Count:** 21903
- **URL:** https://www.hackerrank.com/challenges/two-pluses

## Problem Statement

Ema built a quantum computer! Help her test its capabilities by solving the problem below.

------

Given a grid of size $n \times m$, each cell in the grid is either $good$ or $bad$.

A *valid* plus is defined here as the crossing of two segments (horizontal and vertical) of equal lengths. These lengths must be odd, and the middle cell of its horizontal segment must cross the middle cell of its vertical segment.	

In the diagram below, the blue pluses are *valid* and the orange ones are *not valid*.
<img src="https://s3.amazonaws.com/hr-challenge-images/13512/1445015866-5e338e8b70-pluseses.png" title="pluseses.png" /><br>

Find the two largest *valid* pluses that can be drawn on $good$ cells in the grid, and return an integer denoting the maximum product of their areas.  In the above diagrams, our largest pluses have areas of $5$ and $9$.  The product of their areas is $5 \times 9 = 45$.

**Note:** The two pluses *cannot* overlap, and the product of their areas should be maximal.

**Function Description**  

Complete the *twoPluses* function in the editor below.  It should return an integer that represents the area of the two largest pluses.

twoPluses has the following parameter(s):  

- *grid*: an array of strings where each string represents a row and each character of the string represents a column of that row  

## Input Format

The first line contains two space-separated integers, $n$ and $m$.  
Each of the next $n$ lines contains a string of $m$ characters where each character is either **G** ($good$) or **B** ($bad$). These strings represent the rows of the grid.  If the $y^{th}$ character in the $x^{th}$ line is **G**, then $(x,y)$ is a $good$ cell.  Otherwise it's a $bad$ cell.




## Output Format

Find $2$ pluses that can be drawn on $good$ cells of the grid, and return an integer denoting the maximum product of their areas.

**Sample Input 0**

    5 6
    GGGGGG
    GBBBGB
    GGGGGG
    GGBBGB
    GGGGGG
    
**Sample Output 0**

	5

**Sample Input 1**
    
    6 6
    BGBBGB
    GGGGGG
    BGBBGB
    GGGGGG
    BGBBGB
    BGBBGB

**Sample Output 1**

	25

## Constraints

* $2 \le n \le 15$<br>
* $2 \le m \le 15$<br>

## Sample Input

5 6
GGGGGG
GBBBGB
GGGGGG
GGBBGB
GGGGGG

## Sample Output

5

## Explanation

Here are two possible solutions for Sample 0 (left) and Sample 1 (right):

Explanation Key:

- Green:  cell

- Red:  cell

- Blue: possible .

For the explanation below, we will refer to a plus of length  as .

Sample 0

There is enough good space to color one  plus and one  plus. , and . The product of their areas is .

Sample 1

There is enough good space to color two  pluses. . The product of the areas of our two  pluses is .
