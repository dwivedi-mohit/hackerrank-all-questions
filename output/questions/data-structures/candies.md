# Candies

- **Domain:** data-structures
- **Difficulty:** Medium
- **Max Score:** 50
- **Success Ratio:** 0.7056890494648644
- **Total Submissions:** 110159
- **Solved Count:** 77738
- **URL:** https://www.hackerrank.com/challenges/candies

## Problem Statement

Alice is a kindergarten teacher. She wants to give some candies to the children in her class.  All the children sit in a line and each of them has a rating score according to his or her performance in the class.  Alice wants to give at least 1 candy to each child. If two children sit next to each other, then the one with the higher rating must get more candies. Alice wants to minimize the total number of candies she must buy.

**Example**  

$arr = [4, 6, 4, 5, 6, 2]$    

She gives the students candy in the following minimal amounts: $[1, 2, 1, 2, 3, 1]$.  She must buy a minimum of _10_ candies.  

**Function Description**

Complete the *candies* function in the editor below.  

candies has the following parameter(s):  

- *int n:* the number of children in the class  
- *int arr[n]:* the ratings of each student  

**Returns**  

- *int:* the minimum number of candies Alice must buy  


## Input Format

The first line contains an integer, $n$, the size of $arr$.   
Each of the next $n$ lines contains an integer $arr[i]$ indicating the rating of the student at position $i$.




## Constraints

* $1 \le n \le 10^5$  
* $1 \le arr[i] \le 10^5$ 

## Sample Input

3
1
2
2

## Sample Output

4

## Explanation

Here 1, 2, 2 is the rating. Note that when two children have equal rating, they are allowed to have different number of candies. Hence optimal distribution will be 1, 2, 1.
