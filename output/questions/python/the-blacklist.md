# The Blacklist

- **Domain:** python
- **Difficulty:** Advanced
- **Max Score:** 100
- **Success Ratio:** 0.7119148936170213
- **Total Submissions:** 2350
- **Solved Count:** 1673
- **URL:** https://www.hackerrank.com/challenges/the-blacklist

## Problem Statement

A new gangster is trying to take control of the city. He makes a list of his $N$ adversaries (e.g. _gangster_ $1$, _gangster_ $2$, ... _gangster_ $N-1$, _gangster_ $N$) and plans to get rid of them.

$K$ mercenaries are willing to do the job. The gangster can use any number of these mercenaries. But he has to honor one condition set by them: they have to be assigned in such a way that they eliminate a consecutive group of gangsters in the list, e.g. _gangster_ $i$, _gangster_ $i+1$, ..., _gangster_ $j-1$, _gangster_ $j$, where the following is true: $1 \le i \le j \le N$.

While our new gangster wants to kill all of them, he also wants to pay the least amount of money. All mercenaries charge a different amount to kill different people. So he asks you to help him minimize his expenses.  


## Input Format

The first line contains two space-separated integers, $N$  and $K$. Then $K$ lines follow, each containing $N$ integers as follows:<br>
The $j$<sup>th</sup> number on the $i$<sup>th</sup> line is the amount charged by the $i$<sup>th</sup> mercenary for killing the $j$<sup>th</sup> gangster on the list.



## Output Format

Just one line, the minimum cost for killing the $N$ gangsters on the list.

## Constraints

+ $1 \le N \le 20$
+ $1 \le K \le 10$
+ $0 \le amount$ $charged \le 10000$

## Sample Input

3 2
1 4 1
2 2 2

## Explanation

The new gangster can assign mercenary 1 to kill gangster 1, and mercenary 2 to kill gangster 2 and gangster 3.
