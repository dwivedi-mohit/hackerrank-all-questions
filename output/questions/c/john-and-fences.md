# John and Fences

- **Domain:** c
- **Difficulty:** Medium
- **Max Score:** 50
- **Success Ratio:** 0.8111239860950173
- **Total Submissions:** 863
- **Solved Count:** 700
- **URL:** https://www.hackerrank.com/challenges/john-and-fences

## Problem Statement

John's house has bizarre fencing. There are _N_ fences. Though the contiguous fences have the constant width of 1 unit but their height varies. Height of these fences is represented by array _H = [h<sub>1</sub>, h<sub>2</sub>... h<sub>N</sub>]_.  
<br>
John loves his fences but has to finally bow down to his wife's repeated requests of replacing them with the regular fences. Before taking them down, John wants to keep some part of the fences as souvenir. He decides to carve out the largest rectangular area possible where the largest rectangle can be made of a number of contiguous fence. Note that sides of the rectangle should be parallel to _X_ and _Y_ axis.

Let's say there are 6 fences, and their height is, _H_ = _[2, 5, 7, 4, 1, 8]_. Then they can be represented as

                       __
	8         __      |  |
    7        |  |     |  |
    6      __|  |     |  |
    5     |  |  |__   |  |
    4     |  |  |  |  |  |
    3   __|  |  |  |  |  |
    2  |  |  |  |  |__|  |
    1  |__|__|__|__|__|__|
	    h1 h2 h3 h4 h5 h6

Some possible carvings are as follow: 

* If we carve rectangle from _h1, h2 and h3_ then we can get the max area of 2x3 = 6 units.
* If we carve rectangle from _h3, h4, h5 and h6_, then max area is 4x1 = 4 units.
* If we carve rectangle from _h2, h3 and h4_, then max area is 4x3 = 12, which is also the most optimal solution for this case.

**Input**  
First line will contain an integer _N_ denoting the number of fences. It will be followed by a line containing _N_ space separated integers, _h<sub>1</sub> h<sub>2</sub> ... h<sub>N</sub>_, which represents the height of each fence.

**Output**  
Print the maximum area of rectangle which can be carved out.  

**Note**  


**Constraints**  
1 &le; _N_ &le; 10<sup>5</sup>  
1 &le; _h<sub>i</sub>_ &le; 10<sup>4</sup>  

**Sample Input**  

	6
	2 5 7 4 1 8

**Sample Output**  

	12

**Explanation**  
John can carve a rectangle of height 4 from fence #2, #3 and #4, whose respective heights are 5, 7 and 4. So this will lead to a rectangle of area 3x4 = 12 units.  

---

**Tested by:** [Lalit Kundu](/darkshadows)


## Constraints

1 ≤ N ≤ 105

1 ≤ hi ≤ 104

## Sample Input

2 5 7 4 1 8

## Explanation

John can carve a rectangle of height 4 from fence #2, #3 and #4, whose respective heights are 5, 7 and 4. So this will lead to a rectangle of area 3x4 = 12 units.

Tested by: Lalit Kundu
