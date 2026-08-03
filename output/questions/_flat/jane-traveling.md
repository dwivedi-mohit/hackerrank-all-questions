# Jane is Traveling

---

| Field | Value |
|---|---|
| **Slug** | `jane-traveling` |
| **Contest** | hourrank-2 |
| **Difficulty** | Medium |
| **Score** | 60 |
| **URL** | https://www.hackerrank.com/challenges/jane-traveling |

---

## Problem Statement

Jane lives in Byteland. There are only $5$ cities in Byteland. She has to start from the first city and travel precisely $N$ kilometers. There are exactly $10$ directed ways between the cities, two from each city. Distance from city $x$ to city $y$ is denoted by $d_{x,y}$.<br>

Can you help Jane find a way to do this? 

If there are multiple solutions, the route should consist of the smallest number of nodes. Among all the routes with smallest number of nodes, print the [lexicographically](https://en.wikipedia.org/wiki/Lexicographical_order) smallest solution.

## Input Format

The first line of input contains $N$. Each of the next $5$ lines contain two integers. 

Line $2$ contains $d_{1,2}$ and $d_{1,3}$.<br>
Line $3$ contains $d_{2,3}$ and $d_{2,4}$.<br>
Line $4$ contains $d_{3,4}$ and $d_{3,5}$.<br>
Line $5$ contains $d_{4,5}$ and $d_{4,1}$.<br>
Line $6$ contains $d_{5,1}$ and $d_{5,2}$.<br>

All distances are in kilomeeters.

**Constraint:**<br>
$ 1 \le N \le 5*10^5$<br>
$1\le d_{x,y} \le N$

## Output Format

On one line, print the route Jane has to travel (city numbers). If it's impossible, print $-1$.
