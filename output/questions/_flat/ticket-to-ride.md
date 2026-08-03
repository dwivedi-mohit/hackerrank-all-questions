# Ticket to Ride

---

| Field | Value |
|---|---|
| **Slug** | `ticket-to-ride` |
| **Domain** | data-structures |
| **Difficulty** | Expert |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/ticket-to-ride |

---

## Preview

Find the best path on the tree.

## Problem Statement

Simon received the board game [Ticket to Ride](http://www.daysofwonder.com/tickettoride) as a birthday present. After playing it with his friends, he decides to come up with a strategy for the game.

There are $n$ cities on the map and $n - 1$ road plans. Each road plan consists of the following: 

* Two cities which can be directly connected by a road.
* The length of the proposed road. 

The entire road plan is designed in such a way that if one builds all the roads, it will be possible to travel between any pair of cities. 

A ticket enables you to travel between two different cities. There are $m$ tickets, and each ticket has a cost associated with it. A ticket is considered to be *useful* if there is a path between those cities.

Simon wants to choose two cities, $u$ and $v$, and build a *minimal* number of roads so that they form a simple path between them. Let $s_{t}$ be the sum of costs of all *useful* tickets and $s_{r}$ be the sum of lengths of all the roads Simon builds. The profit for pair $(u, v)$ is defined as $s_{t} - s_{r}$. Note that $u$ and $v$ are not necessarily unique and may be the same cities.

Given $n$ road plans and $m$ ticket prices, help Simon by printing the value of his maximum possible profit on a new line.

## Input Format

The first line contains single positive integer, $n$, denoting the number of cities. 	
Each of the $n - 1$ subsequent lines contains three space-separated integers describing the respective values of $u$, $v$, and $l$ for a road plan, where $1 \le u$, $v \le n$, and $u \neq v$. Here, $u$ and $v$ are two cities that the road plan proposes to connect and $l$ is the length of the proposed road.			
The next line contains a single positive integer, $m$, denoting the number of tickets. 	
Each of the $m$ subsequent lines contains three space-separated integers describing the respective values of $u$, $v$, and $c$ for a ticket from city $u$ to city $v$ (where $c$ is the cost of the ticket).

## Output Format

Print a single integer denoting the the maximum profit Simon can make.

**Time Limits**			

* $6$ seconds for Java and C#.
* Please refer to our [Environment](https://www.hackerrank.com/environment) page to see time limits for other languages.

## Constraints

* $1 \le n \le 2 \times 10^5$
* $1 \le m \le 10^5$
* $1 \le l, c \le 10^9$

## Sample Tests

### Test 1

```
7
1 2 1
1 3 1
1 4 4
4 5 1
4 6 1
4 7 1
5
5 7 3
3 6 2
3 4 10
2 7 15
1 6 7
```

### Test 2

```
13
```
