# Gretchen and the Play

---

| Field | Value |
|---|---|
| **Slug** | `goty-and-the-play` |
| **Domain** | misc |
| **Difficulty** | Medium |
| **Score** | 50 |
| **Contest** | indeed-prime-codesprint |
| **URL** | https://www.hackerrank.com/challenges/goty-and-the-play |

---

## Preview

Given a list of actions, reassign actors between scenes and count the number of scenes having less than P actors.

## Problem Statement

Gretchen is directing a new play with $M$ scenes performed by $N$ actors, where each actor only appears in exactly one scene. To ensure that the distribution is perfect, she performs the following *actions*:

1. Assign actor $N_i$ to scene $M_i$.		
2. Count the number of scenes having less than $P$ actors assigned to them.
 
Given a list of *actions*, determine the distribution of actors in Gretchen's play.

## Input Format

The first line contains three space-separated integers, $M$, $N$, and $Q$, respectively; $M$ is the number of scenes, $N$ is the number of actors, and $Q$ is the number of *actions* Gretchen plans to perform. *$N$ and $M$ use zero-based indexing.*

The second line contains $N$ space-separated integers; the $i^{th}$ integer represents the scene, $M_{i}$, that actor $N_{i}$ is initially assigned to.

The $Q$ subsequent lines describe Gretchen's actions; each of these lines starts with an integer, $A$, which corresponds to *Action 1* or *Action 2* (as detailed in the *Problem Statement*). 	

When $A = 1$ (*Action 1*), it will be followed by two space-separated integers, $N_i$ and $M_i$, respectively; this action says to assign actor $N_i$ to scene $M_i$.	

When $A = 2$ (*Action 2*), it will be followed by a single integer, $P$; this action says to count the number of segments having $\lt P$ actors assigned to them.

**Note:** All *Action 1* actions are permanent, so each *Action 1* affects all future actions.

**Constraints:**

$1\leq M, N, Q\leq 10^5$

$0\leq M_i\leq M-1$

$0\leq N_i\leq N-1$

$1\leq P\leq N$

## Output Format

For each *Action 2*, print the number of scenes having $\lt P$ actors on a new line.

## Sample Tests

### Test 1

```
5 5 6
0 1 2 3 4
2 2
1 0 2
2 2
2 1
1 3 1
2 2
```

### Test 2

```
5
4
1
3
```

### Test 3

```
------------------------------------------------------
| Scene (M) | 0 | 1 | 2 | 3 | 4 |
------------------------------------------------------
| Number of actors | 1 | 1 | 1 | 1 | 1 |
------------------------------------------------------
```

### Test 4

```
------------------------------------------------------
| Scene (M) | 0 | 1 | 2 | 3 | 4 |
------------------------------------------------------
| Number of actors | 0 | 1 | 2 | 1 | 1 |
------------------------------------------------------
```

### Test 5

```
-----------------------------------------------------
| Scene (M) | 0 | 1 | 2 | 3 | 4 |
------------------------------------------------------
| Number of actors | 0 | 2 | 2 | 0 | 1 |
------------------------------------------------------
```
