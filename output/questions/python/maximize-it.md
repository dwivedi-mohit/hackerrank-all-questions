# Maximize It!

- **Domain:** python
- **Difficulty:** Hard
- **Max Score:** 50
- **Success Ratio:** 0.8460715154463634
- **Total Submissions:** 184995
- **Solved Count:** 156519
- **URL:** https://www.hackerrank.com/challenges/maximize-it

## Problem Statement

You are given a function $f(X) = X^{2}$. You are also given $K$ lists. The $i^{th}$ list consists of $N_i$ elements.

You have to pick one element from each list so that the value from the equation below is *maximized*: <br>

$S = (f(X_1) \; + f(X_2) \;+\;... \;+\; f(X_k))$%$M$

$X_i$ denotes the element picked from the $i^{th}$ list . Find the maximized value $S_{max}$  obtained. 

$\%$ denotes the modulo operator. 

Note that you need to take exactly one element from each list, not necessarily the largest element. You add the squares of the chosen elements and perform the modulo operation. The maximum value that you can obtain, will be the answer to the problem. 




## Input Format

The first line contains $2$ space separated integers $K$ and $M$.  
The next $K$ lines each contains an integer $N_i$, denoting the number of elements in the $i^{th}$ list, followed by $N_i$ space separated integers denoting the elements in the list. 

## Output Format

Output a single integer denoting the value $S_{max}$. 

## Constraints

$1 \le K \le 7$  
$1 \le M \le 1000$  
$1 \le N_i \le 7$  
$1 \le Magnitude \; of \; elements\;in\;list\; \le 10^{9}$  

## Sample Input

3 1000
2 5 4
3 7 8 9
5 5 7 8 9 10

## Explanation

Picking  from the st list,  from the nd list and  from the rd list gives the maximum  value equal to % = .
