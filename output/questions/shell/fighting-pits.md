# Fighting Pits

- **Domain:** shell
- **Difficulty:** Hard
- **Max Score:** 80
- **Success Ratio:** 0.6548208563938246
- **Total Submissions:** 3433
- **Solved Count:** 2248
- **URL:** https://www.hackerrank.com/challenges/fighting-pits

## Problem Statement

Meereen is famous for its fighting pits where fighters fight each other to the death.

Initially, there are $n$ fighters and each fighter has a strength value. The $n$ fighters are divided into $k$ teams, and each fighter belongs exactly one team. For each fight, the Great Masters of Meereen choose two teams, $x$ and $y$, that must fight each other to the death. The teams attack each other in alternating turns, with team $x$ always launching the first attack. The fight ends when all the fighters on one of the teams are dead.

Assume each team always attacks optimally. Each attack is performed as follows:

1. The attacking team chooses a fighter from their team with strength $s$.
2. The chosen fighter chooses *at most* $s$ fighters from other team and kills all of them. 
 
The Great Masters don't want to see their favorite fighters fall in battle, so they want to build their teams carefully and know who will win different team matchups. They want you to perform two type of queries:

1. `1 p x` Add a new fighter with strength $p$ to team $x$. It is guaranteed that this new fighter's strength value will not be less than any current member of team $x$.
2. `2 x y` Print the name of the team that would win a matchup between teams $x$ and $y$ in their current state (recall that team $x$ always starts first). It is guaranteed that $x \ne y$. 

Given the initial configuration of the teams and $q$ queries, perform each query so the Great Masters can plan the next fight.

**Note:** You are determining the team that *would* be the winner if the two teams fought. No fighters are actually dying in these matchups so, once added to a team, a fighter is available for all future potential matchups.

## Input Format

The first line contains three space-separated integers describing the respective values of $n$ (the number of fighters), $k$ (the number of teams), and $q$ (the number of queries).		
Each line $i$ of the $n$ subsequent lines contains two space-separated integers describing the respective values of fighter $i$'s strength, $s_i$, and team number, $t_i$. 		
Each of the $q$ subsequent lines contains a space-separated query in one of the two formats defined in the *Problem Statement* above (i.e., `1 p x` or `2 x y`).

## Output Format

After each type $2$ query, print the name of the winning team on a new line. For example, if $x=1$ and $y=2$ are matched up and $x$ wins, you would print $1$.

## Constraints

- $1 \leq n, q \leq  2\times 10^5$
- $2 \leq k \leq 2\times 10^5$
- $1 \le x, y, t_i \le k$
- $1 \le s_i, p \le 2\times 10^5$
- It is guaranteed that both teams in a query matchup will always have at least one fighter.

**Scoring**			
This challange has binary scoring. This means you will get a full score if your solution passes all test cases; otherwise, you will get $0$ points.

## Sample Input

7 2 6
1 1
2 1
1 1
1 2
1 2
1 2
2 2
2 1 2
2 2 1
1 2 1
1 2 1
2 1 2
2 2 1

## Sample Output

2
1
1

## Explanation

Team  has three fighters with the following strength levels: .

Team  has four fighters with the following strength levels: .

The first query matching up team  and  would play out as follows:

- Team  attacks  The fighter with strength  can kill one fighter with strength  and one fighter with strength . Now, , and .

- Team  attacks  The fighter with strength  can kill the fighter with strength . Now, , and .

- Team  attacks  The fighter with strength  can kill one fighter with strength . Now, , and .

- Team  attacks  The fighter with strength  can kill one fighter with strength . Now, , and .

- Team  attacks  The fighter with strength  can kill the last fighter with strength . Now, , and .

After this last attack, all of Team 's fighters would be dead. Thus, we print  as team  would win that fight.
