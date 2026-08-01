# Grid Lines

- **Domain:** regex
- **Difficulty:** Hard
- **Max Score:** 80
- **Success Ratio:** 0.4595744680851064
- **Total Submissions:** 235
- **Solved Count:** 108
- **URL:** https://www.hackerrank.com/challenges/grid-lines

## Problem Statement

In an NxM grid with each cell's dimension being 1x1, there will be (N+1) x (M+1) cross points. 
You task is to count the number of ways (*S*) of choosing *K* different points from these cross points such that all of them lie on a straight line and at least one of the cross points lies on the border.

**Input Format**  

A single line containing 3 integers N, M & K separated by a single space. 

**Output Format**  

A single integer denoting the number of ways (S) [modulo](https://en.wikipedia.org/wiki/Modulo_operation) 1000000007

**Constraints**
  
0 < N, M <= 3000  
2 <= K <= max(N, M) + 1

**Sample Input**  

    2 2 3

**Sample Output**  

    8

**Explanation**  

If you imagine a grid of the first quadrant of the co-ordinate system. Then, we have, 8 such *3* points of which at least 1 point on the borders. 

(0,0), (0,1), (0,2)  
(1,0), (1,1), (1,2)  
(2,0), (2,1), (2,2)  
(0,0), (1,0), (2,0)  
(0,1), (1,1), (2,1)  
(0,2), (1,2), (2,2)  
(0,0), (1,1), (2,2) and   
(0,2), (1,1), (2,0)



## Input Format

A single line containing 3 integers N, M & K separated by a single space.

## Output Format

A single integer denoting the number of ways (S) modulo 1000000007

## Constraints

0 < N, M <= 3000

2 <= K <= max(N, M) + 1

## Sample Input

2 2 3

## Explanation

If you imagine a grid of the first quadrant of the co-ordinate system. Then, we have, 8 such 3 points of which at least 1 point on the borders.

(0,0), (0,1), (0,2)

(1,0), (1,1), (1,2)

(2,0), (2,1), (2,2)

(0,0), (1,0), (2,0)

(0,1), (1,1), (2,1)

(0,2), (1,2), (2,2)

(0,0), (1,1), (2,2) and

(0,2), (1,1), (2,0)
