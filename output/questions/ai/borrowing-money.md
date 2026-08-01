# Demanding Money

- **Domain:** ai
- **Difficulty:** Hard
- **Max Score:** 50
- **Success Ratio:** 0.6907988587731811
- **Total Submissions:** 2804
- **Solved Count:** 1937
- **URL:** https://www.hackerrank.com/challenges/borrowing-money

## Problem Statement

Killgrave wants to use his mind control powers to get money from the Justice League superheroes living in $N$ houses in Happy Harbor that are numbered sequentially from $1$ to $N$. There are $M$ roads, and each road $j$ connects two different houses, $A_j$ and $B_j$. Each superhero house $i$ (where $1 \le i \le N$) has $C_i$ dollars stashed away for a rainy day.

As long as a superhero is home at house $i$, Killgrave knows they will hand over all of their saved money, $C_i$. Once he gets money from them, he moves on to the next house. However, the superheroes are cunning; when Killgrave comes to house $X$, every neighbor immediately connected to house $X$ by a single road skips town for a couple of days (making it impossible for Killgrave to get money from them). In other words, after Killgrave visits all the superheroes he wants, there will be no road in which he was able to get money from both houses on either end of the road.

What is the maximum amount of money Killgrave can collect from the superheroes, and how many *different* ways can Killgrave get that amount of money? Two ways are considered to be different if the sets of visited houses are different.

**Note:** Killgrave can start at an arbitrary house and doesn't have to only use the roads.

## Input Format

The first line contains two space-separated integers, $N$ (the number of houses) and $M$ (the number of roads), respectively.		
The second line contains $N$ space-separated integers, where each integer $i$ describes the amount of money, $C_i$, at house $i$.		
Each line $j$ of the $M$ subsequent lines contains two space-separated integers defining a road connecting houses $A_j$ and $B_j$. Every road connects a different pair of houses.

## Output Format

Print two space-separated integers:

1. The first integer must denote the maximum amount of money Killgrave can get out of the Justice League.
2. The second integer must denote the number of different ways he can collect that amount of money.

## Constraints

- $1 \le N \le 34$
- $0 \le M \le N \cdot \frac{(N - 1)}{2}$
- $0 \le C_i \le 100$
- $1 \leq A_j, B_j \leq N$, where $A_j \neq B_j$
- No unordered pair $(A_j, B_j)$ will appear more than once.

## Sample Input

3 2
6 8 2
1 2
3 2

## Sample Output

8 2

## Explanation

Killgrave has two possible courses of action:

- Visit house  and get  dollars.

- Visit houses  and  and get  dollars.

Both of these options result in  dollars, so we know that this is maximal. Thus, we print the maximum amount of money () followed by the number of ways he can get that amount of money () as two space-separated values on a single line.
