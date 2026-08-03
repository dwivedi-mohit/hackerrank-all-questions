# Bead Ornaments

---

| Field | Value |
|---|---|
| **Slug** | `beadornaments` |
| **Domain** | algorithms |
| **Difficulty** | Advanced |
| **Score** | 70 |
| **URL** | https://www.hackerrank.com/challenges/beadornaments |

---

## Preview

Find out how many different ornaments can be created with the given algorithm?

## Problem Statement

There are $N$ colors of beads. You have $b_i$ beads of the $i^{th}$ color. You want to make an ornament by joining all the beads together. You create the ornament by using the following algorithm:

* Step #$1$ Arrange all the beads in any order such that beads of the same color are placed together.

* Step #$2$ The ornament initially consists of only the first bead from the arrangement.

* Step #$3$ For each subsequent bead in order, join it to a bead of the same color in the ornament. If there is no bead of the same color, it can be joined to any bead in the ornament.

All beads are distinct, even if they have the same color. Two ornaments are considered different if two beads are joined by a thread in one configuration, but not in the other.  How many different ornaments can be formed using this algorithm? Return the answer modulo $(10^9 + 7)$.


**Update/clarification**

Think of the bead formation as a tree and not as a straight line. Any number of beads can be connected to a bead.

**Example** 

$b = [2]$ 


There are two beads of color $a$: $a1$ and $a2$.  These can occur as $a1, a2$ or $a2, a1$.  In both cases, the same two beads are joined, so the arrangements are not different.  There is $1$ way to join these beads. 


$b = [2, 2]$


There are two beads of two colors, $a1, a2, b1, b2$.  They can be arranged as $a1, a2$, $a2, a1$, $b1, b2$ and $b2, b1$.  Call these groups $A1$, $A2$, $B1$ and $B2$.  The 8 possible arranements of groups are shown below.


<pre>
1 A1, B1 = a1, a2, b1, b2
2 A2, B1 = a2, a1, b1, b2
3 A1, B2 = a1, a2, b2, b1
4 A2, B2 = a2, a1, b2, b1
5 B1, A1 = b1, b2, a1, a2
6 B2, A1 = b2, b1, a1, a2 
7 B1, A2 = b1, b2, a2, a1
8 B2, A2 = b2, b1, a2, a1
</pre>

Note that in line 1, $(a1, a2)$, $(a2, b1)$ and $(b1, b2)$ are the connections.  This also occurs on line 8, so these two lines are not different.  In fact, line 8 is just line 1 reversed, like flipping the string of beads end for end.  Using the same logic, the other similar lines are $(2, 6), (3, 7), (4, 5)$.  There are only 4 different arrangements.


**Function Description** 


Complete the *beadOrnaments* function in the editor below. 


*beadOrnaments* has the following parameters: 


- *int b[n]:* the number of beads of each color 


**Returns** 


- *int:* the number of arrangements modulo $(10^9 + 7)$

## Input Format

The first line contains the number of test cases $T$. 

Each of the following $T$ pairs of lines contain: 

- An integer, $n$, the number of elements in array $b$ 

- $n$ space-separated integers that comprise $b$

## Constraints

* $1 <= T <= 20$
* $1 <= n <= 10$
* $1 <= b[i] <= 30$

## Sample Tests

### Test 1

```
1 A1, B1 = a1, a2, b1, b2
2 A2, B1 = a2, a1, b1, b2
3 A1, B2 = a1, a2, b2, b1
4 A2, B2 = a2, a1, b2, b1
5 B1, A1 = b1, b2, a1, a2
6 B2, A1 = b2, b1, a1, a2 
7 B1, A2 = b1, b2, a2, a1
8 B2, A2 = b2, b1, a2, a1
```

### Test 2

```
STDIN Function
----- --------
5 T = 5 
2 b[] size n = 2
2 1 b = [2, 1]
2 n = 2
2 2 b = [2, 2]
1 n = 1
4 b = [4]
2 n = 2
3 1 b = [3, 1]
5 n = 5
1 1 1 1 1 b = [1, 1, 1, 1, 1]
```

### Test 3

```
2
4
16
9
125
```
