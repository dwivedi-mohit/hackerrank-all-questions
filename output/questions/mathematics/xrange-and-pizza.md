# Xrange's Pancakes

- **Domain:** mathematics
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.8523809523809524
- **Total Submissions:** 630
- **Solved Count:** 537
- **URL:** https://www.hackerrank.com/challenges/xrange-and-pizza

## Problem Statement

Xrange makes the best *polygonal pancakes* in PancakeLand. To grow the business, they hired $m$ line cooks to be pancake *rotators* and *flippers*.

A regular [n-gon](https://en.wikipedia.org/wiki/Polygon) has $n$ vertices, $n$ flipping axes, and $n$ rotation points. We define the following:

- Flipping Axes		
	- If $n$ is odd, each flipping axis passes through a single vertex and the midpoint of the opposite side (resulting in $n$ total flipping axes).
    - If $n$ is even, $\frac{n}{2}$ flipping axes pass through every pair of opposing vertices and $\frac{n}{2}$ flipping axes pass through every pair of opposing sides.
    - The angle between consecutive axes is $\frac{360}{2n}$  degrees.
    - A $k$-flipper flips the pancake at axis number $k$.
- Rotation Points		
    - There are $n$ types of rotators.
    - A $k$-rotator rotates the the pancake clockwise by $\frac{(360 \times k)}{n}$ degrees. The types of rotators are $0$-rotator, $1$-rotator, &hellip;, $(n - 1)$-rotator.
    
![rsz_1hackerrankprob1.png](https://s3.amazonaws.com/hr-challenge-images/0/1443458064-e8a628fb83-rsz_1hackerrankprob1.png)

Each pancake passes through a long line of rotators and flippers who change the polygonal pancake's orientation during cooking. Xrange wants to hire one more rotator or flipper to restore the pancake to its initial orientation for plating.

Given $n$ and the sequence of rotators and flippers that the pancake passes through, determine which type of rotator or flipper must be added to the end of the line to restore the pancake to its initial orientation.

## Input Format

The first line contains two space-separated integers denoting the respective values of $n$ (the number of vertices in the polygonal pancake) and $m$ (the number of line cooks performing the transformations).		  
Each line $i$ of the $m$ subsequent lines describes a line cook in the form of two space-separated integers, $type$ and $k$ (respectively). If $type = 1$, line cook $i$ is a rotator; if $type = 2$, line cook $i$ is a flipper. The second value, $k$, is the integer by which they flip or rotate the pancake; flippers flip the pancake along axis number $k$, and rotators rotate the pancake by $\frac{360 \times k}{n}$ degrees.

## Output Format

Print a single line with two space-separated integers denoting the respective values of $type$ and $k$ for the rotator or flipper needed at the end of the line in order to restore the pancake to its initial orientation. 

**Sample Input 0**  

    5 5
    1 1
    1 3
    2 2
    2 2
    1 4
    
**Sample Output 0**  

    1 2
    
**Explanation 0**  

The diagram below demonstrates the sequence of flips and rotations performed on the polygonal pancake as it makes its way down the line:

<img src="https://s3.amazonaws.com/hr-challenge-images/12799/1472865179-0c6f50e10e-pancake1.png" title="pancake1.png" />


Once the pancake reaches the end of the line, it needs to be rotated (which is $type = 1$) by $k = 2$ to be restored to its original orientation. Thus, we print `1 2` on a new line. 

**Sample Input 1**  

    6 5
    1 2
    1 4
    2 3
    2 2
    2 4
    
**Sample Output 1**  

    2 5

## Constraints

- $3 \leq n \le 10^6$  
- $1 \le m \le 10^6$  
- $0 \le k \lt n$   

## Sample Input

5 5
1 1
1 3
2 2
2 2
1 4

## Sample Output

1 2

## Explanation

The diagram below demonstrates the sequence of flips and rotations performed on the polygonal pancake as it makes its way down the line:

Once the pancake reaches the end of the line, it needs to be rotated (which is ) by  to be restored to its original orientation. Thus, we print 1 2 on a new line.
