# Lexicographic paths

- **Domain:** data-structures
- **Difficulty:** Medium
- **Max Score:** 50
- **Success Ratio:** 0.6761978361669243
- **Total Submissions:** 1294
- **Solved Count:** 875
- **URL:** https://www.hackerrank.com/challenges/lexicographic-steps

## Problem Statement

Krishnakant is standing at $(0,0)$ in the [Cartesian plane](http://en.wikipedia.org/wiki/Cartesian_coordinate_system). He wants to go to the point $(x,y)$ in the same plane using only horizontal and vertical moves of $1$ unit. There are many ways of doing this, and he is writing down all such ways. Each way comprises of few $H$ moves and few $V$ moves. i.e. moves in horizontal and vertical direction respectively. For example, if Krishnakant wants to go to point $(2,2)$ from point $(0,0)$, $HVHV$ is one of the possible ways.   

Given the value of $K$, he wants to know lexicographically $K^{th}$ smallest way of going to $(x,y)$ from $(0,0)$.   

**Input Format**  
The first line contains an integer $T$ , i.e., number of test cases.  
Next $T$ lines will contain integers $x$,$y$ and $K$.  

**Output Format**  
For each test case, print lexicographically $K^{th}$ smallest path.  

**Constraints**  
$1 \le T \le 100000$  
$1 \le x \le 10$  
$1 \le y \le 10$  
$0 \le K < \text{number of paths}$ 

**Sample Input**  

    2
	2 2 2
	2 2 3


**Sample Output**  

    HVVH
	VHHV


**Explanation**

All the paths of going to $(2,2)$ from $(0,0)$ in lexicographically increasing order:<br><br>

$0.  HHVV$<br>
$1.  HVHV$<br>
$2.  HVVH$<br>
$3.  VHHV$<br>
$4.  VHVH$<br>
$5.  VVHH$<br>

## Input Format

The first line contains an integer  , i.e., number of test cases.

Next  lines will contain integers , and .

## Output Format

For each test case, print lexicographically  smallest path.

## Sample Input

2 2 2
2 2 3

## Sample Output

HVVH
VHHV

## Explanation

All the paths of going to  from  in lexicographically increasing order:
