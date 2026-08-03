# Sherlock and Physics

---

| Field | Value |
|---|---|
| **Slug** | `sherlock-and-physics` |
| **Domain** | misc |
| **Difficulty** | Hard |
| **Score** | 40 |
| **Contest** | 101hack26 |
| **URL** | https://www.hackerrank.com/challenges/sherlock-and-physics |

---

## Problem Statement

_It is a capital mistake to theorize before one has data. Insensibly one begins to twist facts to suit theories, instead of theories to suit facts._

Watson is going to give Sherlock the following hypothetical physics problem.

A point (say $A$) is revolving continuously with uniform speed on the circumference of a circle with centre at origin and radius $R$. At $\textrm{time}=0$, the point $A$ starts from the coordinates $(R,0)$, moves counterclockwise, and completes one revolution in time $S$ units (i.e. it reaches coordinates $(R,0)$ again at $\textrm{time}=S$). 


You have another point (say $B$) at origin, which you can project (hit) in any direction at $\textrm{time} \ge 0$ in top-right quadrant, i.e. point $B$ goes along positive $x$ on the line $y=m*x$ where ($m \ge 0$), starting from origin. This point $B$ moves with unit speed.

You need to report the minimum possible time at which $A$ and $B$ can collide. For such a hit (collision), you also need to report the angle at which you will project (hit) the point $A$. If the angle made with $x$-axis is $2*\pi*k$ (in radians), you need to output $k$ as an [irreducible fraction][123].

Assume all values are in standard units.

For more clarity, in the following image you can strike off point $B$ in any direction in the red marked area.
<img src="https://s3.amazonaws.com/hr-challenge-images/0/1433762855-560fa6b703-unnamed.jpg" title="unnamed.jpg" />
[123]: https://en.wikipedia.org/wiki/Irreducible_fraction

## Input Format

The first line contains $T$, the number of test cases. 

Each test case consists of integers $R$ and $S$ in one line.

## Output Format

For each test case output format is as follows: 


The first integer denotes the minimum possible time where a collision between $A$ and $B$ occurs. Also, if the angle of such a hit is $2*\pi*k$, output $k$ as an irreducible fraction in form $x/y$, where $x$ is numerator and $y$ is denominator.

Note: If $k$ is $0$, the irreducible fraction is $0/1$.

**Constraints**

$1 \le T \le 50$

$1 \le R, S \le 10^9$

## Sample Tests

### Test 1

```
2
1 1
2 8
```

### Test 2

```
1 0/1
2 1/4
```
