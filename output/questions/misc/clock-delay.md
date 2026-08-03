# Clock Delay

---

| Field | Value |
|---|---|
| **Slug** | `clock-delay` |
| **Contest** | hourrank-28 |
| **Difficulty** | Easy |
| **Score** | 15 |
| **URL** | https://www.hackerrank.com/challenges/clock-delay |

---

## Problem Statement

Vernon is a working man. He needs to attend a conference, and so he has to leave his home at exactly $h_1:m_1$, denoting the time in hours and minutes in a 24-hour clock. The moment he leaves, his home clock displays the correct time, $h_1:m_1$. 

![image](https://s3.amazonaws.com/hr-assets/0/1527929894-2244939652-clocks.png)

He returns home after *exactly* $k$ hours. It is guaranteed that he returns on the same day, hence $h_1 + k < 24$. However, the home clock shows $h_2:m_2$, which may or may not be the correct time. He suspects that the home clock is lagging, and he wishes to know the duration of time in minutes by which his home clock has been lagging.  

It is guaranteed that the actual time is either the same as, or after the time displayed by the clock.  

Complete the function `lagDuration` which takes in five integers $h_1, m_1, h_2, m_2, k$ and returns an integer denoting the duration of time in minutes by which the clock has been lagging.

## Input Format

The first line contains $q$, the number of queries.  

Each query is described by two lines. The first line contains four space-separated integers $h_1, m_1, h_2, m_2$. The second line contains a single integer $k$.

## Output Format

For each query, print a single line containing a single integer indicating the duration of time in minutes by which the clock has been lagging.

## Constraints

- $1 \le q \le 1000$  
- $0 \le h_1 < 23$  
- $0 \le h_2 < 24$  
- $0 \le m_1, m_2 < 60$  
- $1 \le k$  
- $h_1 + k < 24$  
- It is guaranteed that $h_1:m_1$ is strictly before $h_2:m_2$
