# King and Four Sons

- **Domain:** java
- **Difficulty:** Expert
- **Max Score:** 100
- **Success Ratio:** 0.7938931297709924
- **Total Submissions:** 1703
- **Solved Count:** 1352
- **URL:** https://www.hackerrank.com/challenges/happy-king

## Problem Statement

The King of Byteland wants to grow his territory by conquering $K$ other countries. To prepare his $4$ heirs for the future, he decides they must work together to capture each country. 

The King has an army, $A$, of $N$ battalions; the $i^{th}$ battalion has $A_i$ soldiers. For each battle, the heirs get a detachment of soldiers to share but will fight amongst themselves and lose the battle if they don't each command the same number of soldiers (i.e.: the detachment must be divisible by $4$). If given a detachment of size $0$, the heirs will fight alone without any help.

The battalions chosen for battle must be selected in the following way:

1. A subsequence of $K$ battalions must be selected (from the $N$ battalions in army $A$). 
2. The $j^{th}$ battle will have a squad of soldiers from the $j^{th}$ selected battalion such that its size is divisible by $4$. 

The soldiers within a battalion have unique strengths. For a battalion of size $5$, the detachment of soldiers $\{0, 1, 2, 3\}$ is *different* from the detachment of soldiers $\{0, 1, 2, 4\}$

The King tasks you with finding the number of ways of selecting $K$ detachments of battalions to capture $K$ countries using the criterion above. As this number may be quite large, print the answer modulo $10^9+7$.


## Input Format

The first line contains two space-separated integers, $N$ (the number of battalions in the King's army) and $K$ (the number of countries to conquer), respectively.

The second line contains $N$ space-separated integers describing the King's army, $A$, where the $i^{th}$ integer denotes the number of soldiers in the $i^{th}$ battalion ($A_i$). 

**Constraints**

* $1 ≤ N ≤ 10^4$
* $1 ≤ K ≤ min(100, N)$
* $1 ≤ A_{i} ≤ 10^9$
* $1 ≤ A_{i} \leq 10^3$ holds for test cases worth at least $30\%$ of the problem's score.


## Output Format

Print the number of ways of selecting the $K$ detachments of battalions modulo $10^9+7$.

## Constraints

-

-

-

-  holds for test cases worth at least  of the problem's score.

## Sample Input

3 2
3 4 5

## Explanation

First, we must find the ways of selecting  of the army's  battalions; then we must find all the ways of selecting detachments for each choice of battalion.

Battalions :

 has  soldiers, so the only option is an empty detachment ().

 has  soldiers, giving us  detachment options ( and ).

So for this subset of battalions, we get  possible detachments.

Battalions :

 has  soldiers, so the only option is an empty detachment ().

 has  soldiers, giving us  detachment options (, , , , , ).
So for this subset of battalions, we get  possible detachments.

Battalions :

 has  soldiers, giving us  detachment options ( and ).

 has  soldiers, giving us  detachment options (, , , , , ).

So for this subset of battalions, we get  possible detachments.

In total, we have  ways to choose detachments, so we print , which is .
