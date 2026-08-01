# Road Maintenance

- **Domain:** data-structures
- **Difficulty:** Hard
- **Max Score:** 100
- **Success Ratio:** 0.806145251396648
- **Total Submissions:** 1790
- **Solved Count:** 1443
- **URL:** https://www.hackerrank.com/challenges/road-maintenance

## Problem Statement

Byteland has $N$ cities (numbered from $1$ to $N$) and $N-1$ bidirectional roads. A *path* is comprised of $1$ or more connected roads. It is guaranteed that there is a path from any city to any other city.

Steven is a road maintenance worker in Byteland. He is required to maintain *exactly* $M$ paths on any given workday. He *cannot* work on the same road twice in one day (so no $2$ paths can contain the same $2$ roads). Steven can start his workday in any city and, once he has finished maintaining a path, teleport to his next starting city.

Given $M$, help Steven determine how many different possible $M-$path sets will allow him to perform his maintenance duties. Then print the answer modulo $10^9 + 7$.

## Input Format

The first line contains $2$ space-separated integers, $N$ (the number of cities) and $M$ (the number of roads to maintain).		
Each line $i$ of the $N−1$ subsequent lines contains $2$ space-separated integers, $A_i \ \ B_i$, describing a bidirectional road between cities $A_i$ and $B_i$.

## Output Format

Find the number of different $M-$path sets that will allow Steven to complete $M$ orders, and print the answer $\% \ (10^9 + 7)$. 

## Constraints

- $1 \le N \le 10^5$
- $1 \le M \le 5$
- $A_i \ne B_i$
- $1 \le A_i,B_i \le N$

## Sample Input

4 2
1 2
2 3
2 4

## Explanation

For the following Byteland map:

Steven can maintain  roads using any of the following  routes:

-  and

-  and

-  and

-  and

-  and

-  and

Thus, we print the result of  on a new line, which is .
