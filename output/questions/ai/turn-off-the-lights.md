# Turn Off the Lights

- **Domain:** ai
- **Difficulty:** Hard
- **Max Score:** 70
- **Success Ratio:** 0.716796875
- **Total Submissions:** 2560
- **Solved Count:** 1835
- **URL:** https://www.hackerrank.com/challenges/turn-off-the-lights

## Problem Statement

There are $n$ bulbs in a straight line, numbered from $0$ to $n - 1$. 
Each bulb $i$ has a button associated with it, and there is a *cost*, $c_i$, for pressing this button. When some button $i$ is pressed, all the bulbs at a distance $\le k$ from bulb $i$ will be toggled(off->on, on->off). 

Given $n$, $k$, and the costs for each button, find and print the minimum cost of turning off all $n$ bulbs if they're all on initially.

## Input Format

The first line contains two space-separated integers describing the respective values of $n$ and $k$.		
The second line contains $n$ space-separated integers describing the respective costs of each bulb (i.e., $c_0, c_1, \ldots, c_{n - 1}$).

## Output Format

Print a long integer denoting the minimum cost of turning off all $n$ bulbs.

## Constraints

* $3 \le n \le 10^4$
* $0 \le k \le 1000$
* $0 \le c_i \le 10^9$

## Sample Input

3 1
1 1 1

## Explanation

If we press the middle switch, the middle bulb and the  closest adjacent bulbs (i.e., the first and third) will turn off. Because all bulbs will be off in one button press, this cost is minimal. Thus, we print  as our answer.
