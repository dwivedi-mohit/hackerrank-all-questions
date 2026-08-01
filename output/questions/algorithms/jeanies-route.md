# Jeanie's Route

- **Domain:** algorithms
- **Difficulty:** Medium
- **Max Score:** 80
- **Success Ratio:** 0.795556552962298
- **Total Submissions:** 4456
- **Solved Count:** 3545
- **URL:** https://www.hackerrank.com/challenges/jeanies-route

## Problem Statement

Byteland has $N$ cities (numbered from $1$ to $N$) and $N-1$ bidirectional roads. It is guaranteed that there is a route from any city to any other city. 

Jeanie is a postal worker who must deliver $K$ letters to various cities in Byteland. She can start and end her delivery route in any city. Given the destination cities for $K$ letters and the definition of each road in Byteland, find and print the minimum distance Jeanie must travel to deliver all $K$ letters.

**Note:** The letters can be delivered in any order.



## Input Format

The first line contains two space-separated integers, $N$ (the number of cities) and $K$ (the number of letters), respectively.		
The second line contains $K$ space-separated integers describing the delivery city for each letter.		
Each line $i$ of the $N-1$ subsequent lines contains $3$ space-separated integers describing a road as $u_{i} \ v_{i} \ d_{i}$, where $d_i$ is the distance (length) of the bidirectional road between cities $u_i$ and $v_i$.

## Output Format

Print the minimum distance Jeanie must travel to deliver all $K$ letters.

## Constraints

- $2 \le K \le N \le 10^5$
- $1 \le d_{i}\le 10^3$
- $\textit{Byteland is a weighted undirected acyclic graph.}$

## Sample Input

5 3
1 3 4
1 2 1
2 3 2
2 4 2
3 5 3

## Sample Output

6

## Explanation

Jeanie has  letters she must deliver to cities , , and  in the following map of Byteland:

One of Jeanie's optimal routes is , for a total distanced traveled of . Thus, we print  on a new line.
