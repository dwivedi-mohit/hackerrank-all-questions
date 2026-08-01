# Left Rotate the Array

- **Domain:** shell
- **Difficulty:** Easy
- **Max Score:** 30
- **Success Ratio:** 0.8377642329140189
- **Total Submissions:** 7711
- **Solved Count:** 6460
- **URL:** https://www.hackerrank.com/challenges/linkedin-practice-array-left-rotation

## Problem Statement

A *left rotation* operation on an array of size $n$ shifts each of the array's elements $1$ unit to the left. For example, if $2$ left rotations are performed on array $[1, 2, 3, 4, 5]$, then the array would become $[3, 4, 5, 1, 2]$.

Given an array of $n$ integers and a number, $d$, perform $d$ left rotations on the array. Then print the updated array as a single line of space-separated integers.

## Input Format

The first line contains two space-separated integers denoting the respective values of $n$ (the number of integers) and $d$ (the number of left rotations you must perform). 	
The second line contains $n$ space-separated integers describing the respective elements of the array's initial state.

## Output Format

Print a single line of $n$ space-separated integers denoting the final state of the array after performing $d$ left rotations.

## Constraints

- $1 \le n \le 10^5$  
- $1 \le d \le n$  
- $1 \le a_i \le 10^6$

## Sample Input

5 4
1 2 3 4 5

## Sample Output

5 1 2 3 4

## Explanation

When we perform  left rotations, the array undergoes the following sequence of changes:

Thus, we print the array's final state as a single line of space-separated values, which is 5 1 2 3 4.
