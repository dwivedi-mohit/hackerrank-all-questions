# Lazy Mayor and Lasers

---

| Field | Value |
|---|---|
| **Slug** | `lazy-mayor-and-lasers` |
| **Domain** | misc |
| **Difficulty** | Medium |
| **Score** | 30 |
| **Contest** | 101hack40 |
| **URL** | https://www.hackerrank.com/challenges/lazy-mayor-and-lasers |

---

## Preview

Help the Mayor in demolish buildings.

## Problem Statement

The Mayor of Byteland wants to shorten some buildings that are obstructing Byteland's skyline.

There are $n$ vertical buildings having heights $h_1, h_2, \ldots, h_n$. Each building can be assumed to be of infinitesimally small width. The base of building $i$ is located at position $i$ on the $x$-axis. This means the first building is at position $1$, the second is at position $2$, and so on.

The Mayor decides to use lasers to reduce the height of the buildings using a laser with an infinite beam which can be placed at a position on $x$-axis. However, this laser can be fired only at a $45 ^{\circ}$ angle with the negative $x$-axis. When the laser passes through an existing building, the part of the building above the laser is destroyed. Note that the laser doesn't affect the building at the position from which the laser was fired.

For example, the image below shows two lasers fired from positions $3$ and $5$ in blue. Portions of buildings destroyed by these lasers are shown in red (i.e., above the laser line) and portions of buildings left intact are shown in purple (i.e., below the laser line).

![rsz_1figure_1.png](https://s3.amazonaws.com/hr-challenge-images/22870/1468401757-fc0b317ae4-rsz_1figure_1.png)

The Mayor orders that $m$ lasers be fired from positions $x_{m_1}, x_{m_2}, \ldots, x_{m_m}$, one by one. Help the Mayor by finding and printing the remaining heights of each building after all $m$ lasers are fired.

## Input Format

The first line contains a single integer, $n$, denoting the number of buildings.  

The second line contains $n$ space-separated integers denoting the respective initial heights of the buildings (i.e., $h_1, h_2, \ldots, h_n$. 

The third line contains a single integer, $m$, denoting the number of lasers that will fire.	
The fourth line contains $m$ space-separated integers describing the respective positions from which the lasers will be fired (i.e., $x_{m_1}, x_{m_2}, \ldots, x_{m_m}$).

## Output Format

Print a single integer denoting the *sum* of the remaining building heights after all the lasers are fired.

## Constraints

- $1 \le h_i \le 10^9$ 

- $1 \le x_i \le n$ 

- $1 \le n, m \le 10^5$ 


**Subtasks**   	

- For $\text{40%}$ of the maximum score, $1 \le n, m \le 10^3$

## Sample Tests

### Test 1

```
5
3 1 4 5 1
2
3 5
```

### Test 2

```
7
```
