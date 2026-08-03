# Paint The Tiles

---

| Field | Value |
|---|---|
| **Slug** | `tile-painting` |
| **Contest** | hourrank-7 |
| **Difficulty** | Easy |
| **Score** | 25 |
| **URL** | https://www.hackerrank.com/challenges/tile-painting |

---

## Problem Statement

Nikita has a line of $N$ tiles indexed from $0$ to $N-1$. She wants to paint them to match a color configuration, $C$, which is comprised of $2$ colors: $\text{Red(R)}$ and $\text{Blue(B)}$.

In one stroke, Nikita can paint $1$ or more adjacent tiles a single color. After she finishes painting, each tile $i$ should be painted color $C_{i}$. 

It should be noted that it is not allowed to apply more than $1$ stroke on a tile.

Given the required color configuration, find and print the *minimum* number of strokes required for Nikita to paint all $N$ tiles.

**Note:** In a line of tiles, $2$ tiles with the indices $i$ and $j$ are considered adjacent only if $|j-i|=1$.

## Input Format

The first line contains a single integer, $N$, denoting the number of tiles to be painted. 	
The second line contains a string, $C$, denoting the desired color configuration.

For each character $C_i$ in $C$:

- If $C_{i} = \text{"R"}$, it means the $i^{th}$ tile must be painted *red*.	
- If $C_{i} = \text{"B"}$, it means the $i^{th}$ tile must be painted *blue*.

## Output Format

Print the minimum number of strokes required to paint all $N$ tiles in the desired color configuration.

**Sample Input 0**  
    
    5  
    RRRRR

**Sample Output 0**  
   
   	1

**Sample Input 1**  
    
    5  
    RRBRR

**Sample Output 1**  
    
    3

**Sample Input 2**  
    
    5  
    BRBRB

**Sample Output 2**  
    
    5

## Constraints

* $1 \le N \le 1000$
* $C_i \in \text{\{"R", "B"\}}$
