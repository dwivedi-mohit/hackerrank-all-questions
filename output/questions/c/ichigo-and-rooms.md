# Ichigo and Rooms

- **Domain:** c
- **Difficulty:** Medium
- **Max Score:** 80
- **Success Ratio:** 0.5956678700361011
- **Total Submissions:** 277
- **Solved Count:** 165
- **URL:** https://www.hackerrank.com/challenges/ichigo-and-rooms

## Problem Statement





Ichigo is on his way to save Rukia. Unfortunately, when Ichigo was busy fighting Renji, Kenpachi Zaraki had gone to the Dangai(the same place where Ichigo got his final Getsuga Tenshou) to train. Now, he has a Bankai called Tensa Quantum Computer and he used it against Ichigo!

Tensa Quantum Computer consists of 2N rooms arranged in a circle. Kenpachi imprisoned Rukia in one of these rooms. The rooms have the numbers 1, 2, ..., N-1, N, -N, -(N-1), ..., -1 written on them in that order clockwise. Each room has a one-way door to another unique room. Kenpachi knows that if a room has number X, then it leads to another room which is at distance abs(X) from this room. More precisely, if X is positive, it means that this room leads to the X-th room in the clockwise direction from the current room. And if X is negative, then that means that this room leads to the (-X)-th room in the anticlockwise direction from the current room.

Kenpachi knows that Ichigo starts at the room with the number A. Being a determined guy, Ichigo doesn't sit still until he finds Rukia. Instead he keeps running to the next room for as long as he can. But Kenpachi's funny and crafty lieutenant Yachiru Kusajishi suggested that if Kenpachi keeps Rukia in one of the rooms that Ichigo will never visit, then Ichigo will keep running forever and die from exhaustion.

Now, Kenpachi wants to know the number of rooms that he can keep Rukia in, so that poor Ichigo never finds her and hence, keeps running.

_Note: abs(X) is the absolute value of X._

**Input Format**

Line 1: **T**  
T - Number of test cases.  
Lines 2 to T+1: **N A**  
N - Half the total number of rooms.  
A - The number of the room where Ichigo starts his pursuit of Rukia.  

**Output Format**

For each test case, print a single integer in a new line that is the number of rooms where Kenpachi can imprison Rukia so that Ichigo never finds her.

**Constraints**

1 <= T <= 1000  
1 <= N <= 10<sup>9</sup>  
1 <= abs(A) <= N



**Sample Input**

	4
    1 1
    4 1
    4 -3
    1729 -786

**Sample Output**

	0
    2
    6
	3170

**Explanation**

In the first test case, the rooms that Ichigo visits have numbers 1, -1, 1, -1, ... in that order. So, there are no unvisited rooms. 

In the second test case, the rooms that Ichigo visits have numbers 1, 2, 4, -1, -2, -4, 1, 2, ... in that order. So, there are two unvisited rooms namely the ones numbered 3 and -3. 

In the third test case, the rooms that Ichigo visits have numbers -3, 3, -3, 3, ... in that order. So, there are six unvisited rooms namely the ones numbered 1, 2, 4, -4, -2, -1.

## Input Format

Line 1: T

T - Number of test cases.

Lines 2 to T+1: N A

N - Half the total number of rooms.

A - The number of the room where Ichigo starts his pursuit of Rukia.

## Output Format

For each test case, print a single integer in a new line that is the number of rooms where Kenpachi can imprison Rukia so that Ichigo never finds her.

## Constraints

1 <= T <= 1000

1 <= N <= 109

1 <= abs(A) <= N

## Sample Input

1 1
4 1
4 -3
1729 -786

## Sample Output

2
6
3170

## Explanation

In the first test case, the rooms that Ichigo visits have numbers 1, -1, 1, -1, ... in that order. So, there are no unvisited rooms.

In the second test case, the rooms that Ichigo visits have numbers 1, 2, 4, -1, -2, -4, 1, 2, ... in that order. So, there are two unvisited rooms namely the ones numbered 3 and -3.

In the third test case, the rooms that Ichigo visits have numbers -3, 3, -3, 3, ... in that order. So, there are six unvisited rooms namely the ones numbered 1, 2, 4, -4, -2, -1.
