# Who Gets the Catch?

---

| Field | Value |
|---|---|
| **Slug** | `who-gets-the-catch` |
| **Contest** | hourrank-21 |
| **Difficulty** | Easy |
| **Score** | 20 |
| **URL** | https://www.hackerrank.com/challenges/who-gets-the-catch |

---

## Problem Statement

<!-- Allusion to Pokemon Go... -->
A wild venotoise has spawned in the middle of the street, and $n$ *catchers* are nearby! Venotoises are quite rare and disappear quickly, so the $n$ catchers begin racing towards it. Your task is to find who will catch the venotoise.

![image](https://s3.amazonaws.com/hr-assets/0/1496393115-16abb33138-WhoGetstheCatchsample.png)

We represent the street as a long, straight line. The $i^\text{th}$ catcher is located at position $x_i$ along this line, and the venotoise is located at position $x$. The venotoise is stationary, and the $i^\text{th}$ catcher is moving towards the venotoise at a speed of $v_i$ units per second. A catcher moving at a speed of $v$ units per second can travel a distance of $d$ units in exactly $\frac{d}{v}$ seconds.  

The first catcher that makes it to the location of the venotoise catches it. If there isn't a unique "first catcher", that is, if there are two or more catchers that initially reach the venotoise at the exact same time, then the venotoise disappears, and no one gets the catch.

## Input Format

The first line contains two space-separated integers, $n$, the number of catchers, and $x$, the venotoise's location.
The second line contains $n$ space-separated integers, $x_0, x_1, \ldots, x_{n-1}$, denoting the locations of the catchers.  
The third line contains $n$ space-separated integers, $v_0, v_1, \ldots, v_{n-1}$, denoting the speeds of the catchers.

## Output Format

Print one line containing a single integer denoting the index of the catcher that catches the venotoise, or $-1$ if no one gets the catch.

## Constraints

- $1 \le n \le 1000$  
- $1 \le x, x_i \le 3000$  
- $1 \le v_i \le 60$  
- Each catcher can reach the venotoise's location in an integer number of seconds.
