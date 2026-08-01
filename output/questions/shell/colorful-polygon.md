# Colorful Polygon

- **Domain:** shell
- **Difficulty:** Medium
- **Max Score:** 120
- **Success Ratio:** 0.5818181818181818
- **Total Submissions:** 165
- **Solved Count:** 96
- **URL:** https://www.hackerrank.com/challenges/colorful-polygon

## Problem Statement

You are given regular $n$-gon. Each vertex of the $n$-gon was randomly colored with one of $n$ colors. Your task is to find the number of special subsets of polygon vertices. Each special subset must meet all the requirements:

- The subset must contain at least two vertices.
- If vertices belonging to the subset are erased from the polygon (note, that the adjacent edges of those vertices will also get erased), the remaining vertices and edges form some continuous paths. None of those paths should contain two vertices of the same color.

Please, calculate the number of described special subsets and print it modulo $10^{9}+7$.

**Input Format**

The first line contains an integer $n$ $(3 \le n \le 10^5)$. The next line contains $n$ space-separated integers $a_1, a_2, \dots, a_n$ $(1 \le a_i \le n)$. Integer $a_i$ denotes the color of the $i$-th polygon vertex. All the vertices of the polygon are numbered from $1$ to $n$ in clockwise order.

You may assume that each $a_i$ was generated randomly, uniformly and independently from other values. For example, you may assume that $a_{i} = random(1, n)$ for each $i$. Where function $random(1, n)$ returns uniform integer from $1$ to $n$.

**Output Format**

Print a single integer $-$ the answer to the problem modulo $10^9+7$.

**Sample Input #1**

    4
    1 1 1 1

**Sample Output #1**

    7

**Sample Input #2**

    4
    4 2 3 1

**Sample Output #2**

    11
    



## Input Format

The first line contains an integer  . The next line contains  space-separated integers  . Integer  denotes the color of the -th polygon vertex. All the vertices of the polygon are numbered from  to  in clockwise order.

You may assume that each  was generated randomly, uniformly and independently from other values. For example, you may assume that  for each . Where function  returns uniform integer from  to .

## Output Format

Print a single integer  the answer to the problem modulo .

Sample Input #1

4
1 1 1 1

Sample Output #1

7

Sample Input #2

4
4 2 3 1

Sample Output #2

11
