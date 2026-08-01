# Clues on a Binary Path

- **Domain:** regex
- **Difficulty:** Hard
- **Max Score:** 60
- **Success Ratio:** 0.47537993920972643
- **Total Submissions:** 1645
- **Solved Count:** 782
- **URL:** https://www.hackerrank.com/challenges/clues-on-a-binary-path

## Problem Statement

Logan and Veronica live in Neptune, which has $n$ houses and $m$ bidirectional roads connecting them. Each road has an assigned value, $c_i$, where $c_i \in \{0, 1\}$, and each house is numbered with a distinct integer from $1$ to $n$.

Logan and Veronica are looking for clues and need to find the number of different paths of length $d$ from house number $1$. Each path is characterized by a binary sequence of length $d$, where each integer $j$ in the path is the value of $c_j$ for the $j^{th}$ edge in the path. Two paths are different if the binary sequences characterizing these paths are distinct. Note that they may need to visit the same house several times or use the same road several times to find all possible paths.

Given a map of Neptune, help Logan and Veronica find and print the number of different paths of length $d$ from house number $1$ to the other houses in Neptune.

## Input Format

The first line contains three space-separated integers describing the respective values of $n$ (the number of houses), $m$ (the number of bidirectional roads), and $d$ (the distance they want to travel).		
Each of the $m$ subsequent lines contains three space-separated integers describing the respective values of $u$, $v$, and $c$ that define a bidirectional road between houses $u$ and $v$ having assigned value $c$.


## Output Format

Print an integer denoting the total number of paths.

## Constraints

- $1 \le n \le 90$
- $0 \le m \le n \cdot (n - 1)$
- $1 \le d \le 20$
- $c \in \{0,1\}$
- There may be roads connecting house to itself.
- There may be more than one road between two houses.

## Sample Input

3 2 3
1 2 0
1 3 1

## Explanation

There are four possible paths:

-

-

-

-

Thus, we print  as our answer.
