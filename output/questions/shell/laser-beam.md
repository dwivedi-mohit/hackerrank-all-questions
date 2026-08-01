# Laser Beam

- **Domain:** shell
- **Difficulty:** Expert
- **Max Score:** 120
- **Success Ratio:** 0.9207920792079208
- **Total Submissions:** 303
- **Solved Count:** 279
- **URL:** https://www.hackerrank.com/challenges/laser-beam

## Problem Statement

You are standing at position $(0,0,0)$. One enemy is positioned at $(x,y,z)$ for every $(x,y,z)$ such that $|x| \le N$, $|y| \le N$, $|z| \le N$ and $|x| + |y| + |z| > 0$.

You have a single laser beam which you can use to shoot enemies. You can aim it in any direction, and all enemies in that direction will be eliminated. You win if the number of enemies you eliminate is at least $M$ and is divisible by $D$.

How many directions can you aim the laser so that you win? As the answer can get very large, output the answer modulo $1000000007$ ($= 10^9 + 7$).

**Input Format**  
The first line contains a single integer, $T$, which is the number of test cases.
The next $T$ lines each contain three integers separated by single spaces, $N$, $M$ and $D$.

**Output Format**  
For each test case, output a single line containing the number of directions you can aim the laser, modulo $1000000007$.

**Constraints**  
$1 \le T \le 3$  
$1 \le N \le 3\cdot 10^9$  
$1 \le M \le 1000$  
$1 \le D \le 1000$  

**Sample Input**  

    2
    3 2 1
    100 3 2

**Sample Output**  

    26
    70946

**Explanation**  
For the first test case, here are the 26 directions you can point the laser beam to:  
$(-1,-1,-1)$, $(-1,-1,0)$, $(-1,-1,1)$, $(-1,0,-1)$, $(-1,0,0)$, $(-1,0,1)$  
$(-1,1,-1)$, $(-1,1,0)$, $(-1,1,1)$, $(0,-1,-1)$, $(0,-1,0)$, $(0,-1,1)$  
$(0,0,-1)$, $(0,0,1)$, $(0,1,-1)$, $(0,1,0)$, $(0,1,1)$, $(1,-1,-1)$  
$(1,-1,0)$, $(1,-1,1)$, $(1,0,-1)$, $(1,0,0)$, $(1,0,1)$, $(1,1,-1)$  
$(1,1,0)$, $(1,1,1)$



## Input Format

The first line contains a single integer, , which is the number of test cases.
The next  lines each contain three integers separated by single spaces, ,  and .

## Output Format

For each test case, output a single line containing the number of directions you can aim the laser, modulo .

## Sample Input

3 2 1
100 3 2

## Sample Output

70946

## Explanation

For the first test case, here are the 26 directions you can point the laser beam to:

, , , , ,

, , , , ,

, , , , ,

, , , , ,

,
