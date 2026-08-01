# Teleporters

- **Domain:** databases
- **Difficulty:** Expert
- **Max Score:** 150
- **Success Ratio:** 0.7246963562753036
- **Total Submissions:** 247
- **Solved Count:** 179
- **URL:** https://www.hackerrank.com/challenges/teleporters

## Problem Statement

ByteLand is a large country with a tree-like road system. It has $N$ cities and $(N-1)$ unidirected roads. The capital of ByteLand is a city, numbered $1$, and all the roads go away from the capital. So people use these roads to reach any city from the capital. But it is impossible to reach the capital from a city by roads. 

To solve this problem, there is a system of teleporters. Each city has a teleporter in it. Each teleporter has a value of *strength*. Let's say, the $i$-th one has the value of *strength* equal to $A_i$. This means that by using the teleporter, you'll become $A_i$ cities close to the capital (the same as going $A_i$ roads in the capital direction). If the distance to the capital is less than $A_i$, you'll simply move to the capital instead.

The road system of ByteLand and the initial teleports' strengths will be given to you. You'll also be given $M$ queries about the teleport network in ByteLand. These queries will have one of the following forms:

- $1$ $X$ $Y$ : The strength of the teleport in the city with the number $X$ becomes equal to $Y$;

- $2$ $X$ : Please output the minimal number of teleports that needs to be used to get from the city with the number $X$ to the capital. We can use only teleports in this query, but not the roads!

## Input Format

The first line of input will contain two space-separated integers $N$ and $M$.

The second line will contain $N$ space separated integers $A_1, A_2, ..., A_N$ - the initial strengths of the teleports.

The following $(N-1)$ lines will contain pairs of space separated positive integers $X$ and $Y$ with the meaning that there is a road between the cities with the numbers $X$ and $Y$.

Each of following $M$ lines will contain a query in one of the formats, described above.

**Constraints**  


1 <= N <= 100000  
1 <= M <= 100000  
1 <= A<sub>i</sub> <= 10000

## Output Format

For each query of the second type, output an answer on a separate line.	

## Constraints

1 <= N <= 100000

1 <= M <= 100000

1 <= Ai <= 10000

## Sample Input

5 2
1 2 1 2 1
1 2
2 3
3 4
4 5
2 4
2 5

## Sample Output

3

## Explanation

In the first query, we jump two cities up and appear in the second city, then we jump once more and move to the capital.

In the second query, we jump one city up and appear in the city . From that city we need  more teleportations to get to the capital (this is yet the first query).
