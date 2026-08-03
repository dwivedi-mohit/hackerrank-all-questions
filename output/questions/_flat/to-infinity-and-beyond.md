# To Infinity and Beyond

---

| Field | Value |
|---|---|
| **Slug** | `to-infinity-and-beyond` |
| **Domain** | mathematics |
| **Difficulty** | Expert |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/to-infinity-and-beyond |

---

## Preview

Help Holly Bee get to Infinity (and beyond).

## Problem Statement

Holly Bee lives at location $(0, 0, 0)$ in a *3D* Cartesian space and wants to go to Infinity, a tea shop franchise where each shop is located at some $(x_i, y_i, z_i)$. To get there, she must perform a series of *moves* in the following forms:

- *Walk*. This only applies when Holly is on the ground (i.e., when $z = 0$). If Holly is at $(x, y, 0)$, then she can go to either $(x + 1, y, 0)$ or $(x, y + 1, 0)$ in one move.

- *Fly*. If Holly is at $(x,y,z)$, then she can go to $(X,Y,Z)$ as long as $x < X$, $y < Y$, and $z < Z$.


Note that Holly Bee *must* be on a lattice point after each move.


Holly Bee has $t$ Infinity shops near her meadow. She knows that there are many paths she can take to reach each Infinity shop, but she wants to know the *exact* number of paths she can take to each shop. Given the *3D* coordinates for $t$ Infinity shops, find and print the number of ways for Holly Bee to get to each shop on a new line. Recall that Holly Bee always starts at location $(0, 0, 0)$.

## Input Format

The first line contains an integer, $t$, denoting the number of Infinity shops.  	
Each line $i$ of the $t$ subsequent lines describes the location of an Infinity tea shop in the form of three space-separated integers denoting the respective $x_i$, $y_i$, and $z_i$ values of the shop's location.

## Output Format

For each Infinity tea shop location $i$, print the number of different paths from $(0,0,0)$ to $(x_i, y_i, z_i)$ using some sequence of *walk* and *fly* moves described above. As this number can be very large, your answer must be modulo $(10^9+7)$.

## Constraints

For $\text{20%}$ of the maximum score:


- $1 \le t \le 50$

- $x_i, y_i, z_i \ge 1$

- $x_i \times y_i \le 10^{6}$

- $z_i \le 10^{12}$


For the remaining $\text{80%}$ the maximum score:


- $1 \le t \le 5$

- $x_i, y_i, z_i \ge 1$

- $x_i \times y_i \le 10^{12}$

- $z_i \le 10^{12}$

## Sample Tests

### Test 1

```
4
3 1 4
1 4 3
2 2 2
11 24 69
```

### Test 2

```
3
4
6
909000199
```
