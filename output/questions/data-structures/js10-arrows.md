# Day 5: Arrow Functions

- **Domain:** data-structures
- **Difficulty:** Easy
- **Max Score:** 15
- **Success Ratio:** 0.9944461669115565
- **Total Submissions:** 74183
- **Solved Count:** 73771
- **URL:** https://www.hackerrank.com/challenges/js10-arrows

## Problem Statement

**Objective**

In this challenge, we practice using *arrow functions*. Check the attached tutorial for more details.

**Task**

Complete the function in the editor. It has one parameter: an array, $nums$. It must iterate through the array performing one of the following actions on each element:

- If the element is even, multiply the element by $2$.
- If the element is odd, multiply the element by $3$.

The function must then return the modified array.

## Input Format

The first line contains an integer, $n$, denoting the size of $nums$.	
The second line contains $n$ space-separated integers describing the respective elements of $nums$.

## Output Format

Return the modified array where every even element is doubled and every odd element is tripled.

## Constraints

- $1 \le n \le 10$
- $1 \le nums_{i} \le 100$, where $nums_{i}$ is the $i^{th}$ element of $nums$.

## Sample Input

5
1 2 3 4 5

## Sample Output

3 4 9 8 15

## Explanation

Given , we modify each element so that all even elements are multiplied by  and all odd elements are multipled by . In other words, . We then return the modified array as our answer.
