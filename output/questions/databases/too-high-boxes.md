# Boxes through a Tunnel

- **Domain:** databases
- **Difficulty:** Easy
- **Max Score:** 25
- **Success Ratio:** 0.9716317906370839
- **Total Submissions:** 206111
- **Solved Count:** 200264
- **URL:** https://www.hackerrank.com/challenges/too-high-boxes

## Problem Statement

You are transporting some boxes through a tunnel, where each box is a  [parallelepiped](https://en.wikipedia.org/wiki/Parallelepiped), and is characterized by its length, width and height.

The height of the tunnel $41$ feet and the width can be assumed to be infinite. A box can be carried through the tunnel only if its height is strictly less than the tunnel's height. Find the volume of each box that can be successfully transported to the other end of the tunnel. 
Note: Boxes cannot be rotated. 

## Input Format

The first line contains a single integer $n$, denoting the number of boxes.  
$n$ lines follow with three integers on each separated by single spaces $-$ $length_i$, $width_i$ and $height_i$ which are length, width and height in feet of the $i$-th box.

## Output Format

For every box from the input which has a height lesser than $41$ feet, print its volume in a separate line.

## Constraints

+ $1 \leq n \leq 100$
+ $1 \leq length_i,width_i,height_i \leq 100$

## Sample Input

4
5 5 5
1 2 40
10 5 41
7 2 42

## Sample Output

125
80

## Explanation

The first box is really low, only  feet tall, so it can pass through the tunnel and its volume is .

The second box is sufficiently low, its volume is .

The third box is exactly  feet tall, so it cannot pass. The same can be said about the fourth box.
