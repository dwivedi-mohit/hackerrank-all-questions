# Basketball tournament

---

| Field | Value |
|---|---|
| **Slug** | `basketball-tournament-1` |
| **Contest** | hourrank-31 |
| **Difficulty** | Advanced |
| **Score** | 75 |
| **URL** | https://www.hackerrank.com/challenges/basketball-tournament-1 |

---

## Problem Statement

Barry is the coach of a basketball club. There are $n$ players in the team, and player $i$ has a height of $h_i$ cm. 

- Function $f(i, j)$ is the measure of the teamwork between player $i$ and $j$. Then $f(i, j) = h_i + h_j$. 
- Function $P(S)$ is the power of set $S$, consisting some players. Then $P(S) = \sum f(i, j)$, for all $i$ and $j$, where $i$ and $j$ are players in set $S$. 

For example, there are 2 players in set, with $h_i = \{2, 3\}$, and indexes $1, 2$ respectively. Then power of this set is equal to $f(1, 1) + f(1, 2) + f(2, 1) + f(2, 2) = 4+5+5+6$.

The team is going to take part in a tournament. There are $m$ rounds in the tournament, each of them having some conditions. 

For round $i$, the requirments: 

There are three positive integers $l_i, r_i, x_i$. To participate in round $i$, Barry needs to find minimal $K$ such that there's at least one consecutive subsequence of players between $l$ and $r$, where height of each player in this subsequence is at most $K$, and $\textbf{power}$ of this subsequence is not less than $x_i$. If there exists such $K$, Barry's team is able to participate in round $i$. Otherwise, the team is not eligible. 

You need to help him determine for every round, is it possible to participate in that round. If it is possible, print minimal $K$ for round $i$, otherwise print $-1$.

## Input Format

The first line contains two integers $n$ and $m$ - the number of players and rounds respectively.

The second line contains array of $n$ postive integers $h_i$.

The next $m$ lines contains three positve integers: $l_i, r_i, x_i$.

## Output Format

For every round print minimal $K$ if it's possible, otherwise print $-1$.

## Constraints

- $1 \le n, m \le 3 \cdot 10^5$  
- $1 \le h_i \le 10^7$
- $1 \le l_i \le r_i \le n$
- $1 \le x_i \le 10^{18}$


At least for $25\%$ of the total score, $1\le n,m \le 5000$.

At least for $75\%$ of the total score, $1\le n,m \le 50000$.
