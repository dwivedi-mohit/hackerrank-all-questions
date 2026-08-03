# Recording Episodes

---

| Field | Value |
|---|---|
| **Slug** | `episode-recording` |
| **Domain** | algorithms |
| **Difficulty** | Hard |
| **Score** | 70 |
| **URL** | https://www.hackerrank.com/challenges/episode-recording |

---

## Preview

Given schedules for each season of Dave's favorite show, find the maximum number of consecutive episodes he can record from each season.

## Problem Statement

Dave is a die-hard fan of a show called "HackerRank", in which a young programmer uses her problem-solving abilities to solve crimes. He splurged on a Digital Video Recorder (DVR) so that he can record HackerRank episodes and watch them later. Luckily, Dave managed to get his hands on schedules for all the episodes in each upcoming season.

Each season has $n$ episodes numbered from $1$ to $n$. Each episode airs twice; the first time it's called "live", and the second time it's called "repeat". So, for each episode, we have $4$ integers, $(s_{live}$ and $e_{live})$ for the live airing and $(s_{repeat}$ and $e_{repeat})$ for the repeat airing, where $s$ is episode's start time and and $e$ is its end time. All times are given as integers representing the number of minutes passed since the start of the season.

Episodes broadcast on multiple channels, so some of the air times overlap and the episodes may not broadcast sequentially. It's possible that both the live and repeat broadcasts of some episode $i$ are held before episode $j$, even though $i > j$. In addition, live and repeat broadcasts of the same episode may differ in length due to the number of advertisements during the broadcast. 

Dave only has one TV with a DVR attached to it, and the DVR is capable of recording one episode at a time. For each episode in a season, Dave first decides whether or not he will record it. If he decides to record it, he will either record it during $(s_{live}, e_{live})$ or $(s_{repeat}, e_{repeat})$. Dave will only ever record one of the two airings of an episode, and he always records *full* episodes. This means that once he starts recording an episode, he will always record it until the end (i.e., he never records partial episodes). 

Dave realizes that it might not be possible for him to record all episodes successfully, so instead of focusing on recording all episodes of HackerRank (which may be impossible), he decides to record all consecutively airing episodes whose episode number occurs in some inclusive $[L,R]$ interval such that $R-L$ (i.e., the number of consecutive episodes recorded) is as large as possible. 	

Given the programming schedule for each season, find $L$ and $R$ episode numbers for largest range of consecutive episodes Dave can record during that season and print these respective values as two space-separated integers on a new line. If two or more such intervals exist, choose the one having the smallest $L$ value.

## Input Format

The first line contains a single positive integer, $q$, denoting number of seasons of HackerRank.			
The subsequent lines describe each of the $q$ seasons in the following format:

1. The first line contains an integer, $n$, denoting the number of episodes in the season.
2. Each line $i$ of the $n$ subsequent line contains four space-separated integers describing the respective values of $s_{live}$, $e_{live}$, $s_{repeat}$, and $e_{repeat}$.

## Output Format

On a new line for each season, print two space-separated integers denoting the respective $L$ and $R$ (inclusive) values for the maximum possible range of consecutive episodes Dave can record such that $R-L$ is as large as possible. If more than one such interval exists, choose the interval having the smallest $L$.

## Constraints

* $1 \le q \le 100$
* $1 \le n \le 100$
* $1 \le s_l, e_l, s_r, e_r \leq 10^4$
* $s_{live} \le e_{live}$
- $s_{repeat} \le e_{repeat}$
- $s_{live} \le s_{repeat}$

## Sample Tests

### Test 1

```
3
3
10 20 30 40
20 35 21 35
14 30 35 50
1
10 20 30 40
3
11 19 31 39
12 38 13 37
10 20 30 40
```

### Test 2

```
1 2
1 1
1 1
```
