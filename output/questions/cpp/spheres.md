# Spheres

- **Domain:** cpp
- **Difficulty:** Medium
- **Max Score:** 30
- **Success Ratio:** 0.7271966527196653
- **Total Submissions:** 1195
- **Solved Count:** 869
- **URL:** https://www.hackerrank.com/challenges/spheres

## Problem Statement

Initially, two non-touching spheres of radii _R1_ and _R2_ are lying in space at rest. Both of them are then given accelerations _a1_ and _a2_ respectively at time=0. Find whether they will ever come in contact. Their initial positions are represented as _(x1,y1,z1)_ and _(x2,y2,z2)_ respectively. Accelerations have respective components in 3D. They are represented as _(a1<sub>i</sub>,a1<sub>j</sub>,a1<sub>k</sub>)_ and _(a2<sub>i</sub>,a2<sub>j</sub>,a2<sub>k</sub>)_ respectively.


**Input Format**  
The first line contains _T_, the number of test cases.  
Each test case consists of five lines, where the first line contains _R1_ and _R2_. The next two lines contain position and acceleration of the first sphere. The next two lines after this contain position and acceleration of the second sphere. All numbers in input are integers. 

**Output Format**  
For each test case, print `YES`, if the spheres come in contact. Otherwise, print `NO` (quotes for clarity).  

**Constraints**  
1 &le; _T_ &le; 10<sup>4</sup>    
1 &le; _R1_, _R2_ &le; 10<sup>2</sup>    
-10<sup>2</sup> &le; _x1_, _y1_, _z1_ , _x2_ , _y2_ , _z2_ &le; 10<sup>2</sup>    
-10<sup>2</sup> &le; _a1<sub>i</sub>_ , _a1<sub>j</sub>_ , _a1<sub>k</sub>_ , _a2<sub>i</sub>_ , _a2<sub>j</sub>_ , _a2<sub>k</sub>_ &le; 10<sup>2</sup>     

**Sample input**  

	2
	1 2
	0 0 0
	-1 0 0
	4 0 0
	1 0 0
    1 2
    0 0 0
    100 0 0
    4 0 0
    0 0 0

**Sample output**  

	NO
    YES
    
**Explanation**   
For first testcase, both spheres go in opposite directions, so they'll never come in contact.   
For second testcase, second sphere is not moving while first sphere is accelerating towards the second sphere. So they come in contact.

## Input Format

The first line contains T, the number of test cases.

Each test case consists of five lines, where the first line contains R1 and R2. The next two lines contain position and acceleration of the first sphere. The next two lines after this contain position and acceleration of the second sphere. All numbers in input are integers.

## Output Format

For each test case, print YES, if the spheres come in contact. Otherwise, print NO (quotes for clarity).

## Constraints

1 ≤ T ≤ 104

1 ≤ R1, R2 ≤ 102

-102 ≤ x1, y1, z1 , x2 , y2 , z2 ≤ 102

-102 ≤ a1i , a1j , a1k , a2i , a2j , a2k ≤ 102

Sample input

2
1 2
0 0 0
-1 0 0
4 0 0
1 0 0
1 2
0 0 0
100 0 0
4 0 0
0 0 0

Sample output

NO
YES

## Explanation

For first testcase, both spheres go in opposite directions, so they'll never come in contact.

For second testcase, second sphere is not moving while first sphere is accelerating towards the second sphere. So they come in contact.
