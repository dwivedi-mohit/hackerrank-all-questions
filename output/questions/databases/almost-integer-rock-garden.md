# Almost Integer Rock Garden

- **Domain:** databases
- **Difficulty:** Expert
- **Max Score:** 80
- **Success Ratio:** 0.8263520678685048
- **Total Submissions:** 3772
- **Solved Count:** 3117
- **URL:** https://www.hackerrank.com/challenges/almost-integer-rock-garden

## Problem Statement

Victor is building a [Japanese rock garden](https://en.wikipedia.org/wiki/Japanese_rock_garden) in his $24 \times 24$ square courtyard. He overlaid the courtyard with a [Cartesian coordinate system](https://en.wikipedia.org/wiki/Cartesian_coordinate_system) so that any point $(x, y)$ in the courtyard has coordinates $x \in [-12, 12]$ and $y \in [-12, 12]$. Victor wants to place $12$ stones in the garden according to the following rules:

- The center of each stone is located at some point $(x, y)$, where $x$ and $y$ are integers $ \in [-12, 12]$. 
- The coordinates of all twelve stones are pairwise distinct. 
- The [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance#Two_dimensions) from the center of any stone to the [origin](https://en.wikipedia.org/wiki/Origin_(mathematics)#Cartesian_coordinates) is *not an integer*. 
- The sum of Euclidean distances between all twelve points and the origin is an [almost integer](https://en.wikipedia.org/wiki/Almost_integer), meaning the absolute difference between this sum and an integer must be $\le 10^{-12}$.

Given the values of $x$ and $y$ for the first stone Victor placed in the garden, place the remaining $11$ stones according to the requirements above. For each stone you place, print two space-separated integers on a new line describing the respective $x$ and $y$ coordinates of the stone's location.

## Input Format

Two space-separated integers describing the respective values of $x$ and $y$ for the first stone's location.

## Output Format

Print $11$ lines, where each line contains two space-separated integers describing the respective values of $x$ and $y$ for a stone's location.

## Constraints

- $-12 \le x, y \le 12$

## Sample Input

7 11

## Sample Output

11 1
-2 12
5 4
12 -3
10 3
9 6
-12 -7
1 11
-6 -6
12 -4
4 12

## Explanation

The diagram below depicts the placement of each stone and maps its distance to the origin (note that red denotes the first stone placed by Victor and blue denotes the eleven remaining stones we placed):

Now, let's determine if the sum of these distances is an almost integer. First, we find the distance from the origin to the stone Victor placed at , which is . Next, we calculate the distances for the remaining stones we placed in the graph above:

-

-

-

-

-

-

-

-

-

-

-

When we sum these eleven distances with the distance for the stone Victor placed, we get . The nearest integer to this number is , and the distance between this sum and the nearest integer is  (meaning it's an almost integer). Because this configuration satisfies all of Victor's rules for his rock garden, we print eleven lines of x y coordinates describing the locations of the stones we placed.
