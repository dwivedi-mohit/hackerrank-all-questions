# Basketball Game

---

| Field | Value |
|---|---|
| **Slug** | `basketball-game` |
| **Domain** | misc |
| **Difficulty** | Medium |
| **Score** | 45 |
| **Contest** | 101hack47 |
| **URL** | https://www.hackerrank.com/challenges/basketball-game |

---

## Preview

Help Caroline score the game-winning basket!

## Problem Statement

Caroline's basketball team made it to the finals! They've been behind for the whole game but are now only one basket away from gaining the lead and winning the championship! The basketball court is represented as a coordinate plane with $x$ and $y$ coordinates. Caroline is located at $(x_C, y_C)$, she will receive and shoot the ball at time $t = 0$, the ball will travel in a straight line across the court at a constant speed of $s_C$ (a speed of $1$ means that the ball will travel from point $(0, 0)$ to point $(1, 0)$ in $1$ second), and the basket is located at point $(x_{\text{hoop}}, y_{\text{hoop}})$.

The other team can block the shot if one of their $5$ players gets to the ball's coordinate before it reaches the basket's location. The other team will have starting positions and can move as the ball is traveling toward the basket. Determine if Caroline can make the game-winning shot without it being blocked by the other team!

## Input Format

The first line contains an integer $T$ (the number of test cases).

The first line of each test case contains two space-separated integers $x_\text{hoop}, y_\text{hoop}$ (the basket's coordinates).

The second line of each test case contains three space-separated integers $x_C$ and $y_C$ (Caroline's $x$ and $y$ coordinates), and  $s_C$ (the speed at which the ball travels).

The next five lines for each test case are for information related to the other team's players. Each line contains three integers $x_{i}$ and $y_{i}$ (for the $i^\text{th}$ player's coordinates), and $s_i$ (the constant speed at which the $i^{\text{th}}$ player can travel across the court). It is guaranteed that none of the other team's players' initial positions coincide with Caroline's position.

## Output Format

For each test case, print a single line containing either `YES` or `NO` denoting if Caroline can make the shot.

## Constraints

- $1 \le T \le 100$

- $\textrm{Absolute value of all coordinates} \le 100$ 

- $1 \le s_C, s_i \le 200$

## Sample Tests

### Test 1

```
2
5 0
0 0 1
10 0 1
11 0 1
12 0 1
13 0 1
14 0 1
7 0
0 0 1
3 3 1
10 10 1
10 10 1
10 10 1
10 10 1
```

### Test 2

```
YES
NO
```
