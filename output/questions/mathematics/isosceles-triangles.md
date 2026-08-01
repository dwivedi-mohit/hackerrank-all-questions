# Isosceles Triangles

- **Domain:** mathematics
- **Difficulty:** Hard
- **Max Score:** 250
- **Success Ratio:** 0.46756756756756757
- **Total Submissions:** 370
- **Solved Count:** 173
- **URL:** https://www.hackerrank.com/challenges/isosceles-triangles

## Problem Statement

[Sevenkplus](http://sevenkplus.com/) has a regular polygon. Each vertex of the polygon has a color, either white or black. Sevenkplus wants to count the number of isosceles triangles whose vertices are vertices of the regular polygon and have the same color.  

**Input Format**   
The first line contains an integer T. T testcases follow.   
For each test case, there is only one line, which consists of a 01-string with length >= 3. Number of vertices `n` of the regular polygon equals length of the string. The string represents color of vertices in clockwise order. `0` represents white and `1` represents black. 

**Output Format**  
For each test case, output one line in the format `Case #t: ans`, where `t` is the case number (starting from 1), and `ans` is the answer. 

**Constraints**  
Sum of all n in the input <= 10^6.  

**Sample Input**

	5
	001
	0001
	10001
	111010
	1101010

**Sample Output**

	Case 1: 0
	Case 2: 1
	Case 3: 1
	Case 4: 2
	Case 5: 3

**Explanation**

In case 5, indices of vertices of the three monochromatic isosceles triangles are (0,3,5), (1,3,5) and (2,4,6) (assuming indices start from 0). 

**Timelimits**  
Timelimits for this challenge is given [here](https://www.hackerrank.com/environment)

## Input Format

The first line contains an integer T. T testcases follow.

For each test case, there is only one line, which consists of a 01-string with length >= 3. Number of vertices n of the regular polygon equals length of the string. The string represents color of vertices in clockwise order. 0 represents white and 1 represents black.

## Output Format

For each test case, output one line in the format Case #t: ans, where t is the case number (starting from 1), and ans is the answer.

## Constraints

Sum of all n in the input <= 10^6.

## Sample Input

001
0001
10001
111010
1101010

## Sample Output

Case 1: 0
Case 2: 1
Case 3: 1
Case 4: 2
Case 5: 3

## Explanation

In case 5, indices of vertices of the three monochromatic isosceles triangles are (0,3,5), (1,3,5) and (2,4,6) (assuming indices start from 0).

Timelimits

Timelimits for this challenge is given here
