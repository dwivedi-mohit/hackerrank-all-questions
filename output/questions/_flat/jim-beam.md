# Jim Beam

---

| Field | Value |
|---|---|
| **Slug** | `jim-beam` |
| **Domain** | mathematics |
| **Difficulty** | Hard |
| **Score** | 40 |
| **URL** | https://www.hackerrank.com/challenges/jim-beam |

---

## Preview

Help Jim determine if he can play with laser beam.

## Problem Statement

Jim likes to play with laser beams.

Jim stays at point $(0,0)$.

There is a mirror at point $(X_m, Y_m)$ and a wall between points $(X_1, Y_1)$ and $(X_2, Y_2)$.

Jim wants to find out if he can point the laser beam on the mirror.

**Input Format**

First line contains the number of test cases, $T$.

Each subsequent line contains one test case: space separated integers that denote endpoints of the wall $X_1, Y_1$, $X_2, Y_2$ and position of the mirror $X_m, Y_m$.


**Output Format**

The answer for each test case: Display `YES` if Jim can point the laser beam to the mirror, otherwise display `NO` .


**Constraints**

$1 \le T \le 100$

$0 \le |X_1|,|Y_1|,|X_2|,|Y_2|,|X_m|,|Y_m| \le 10^6$

Mirror doesn't have common points with wall.

Wall doesn't pass through the point $(0,0)$.


**Sample Input**

	5
	1 2 2 1 2 2
	-1 1 1 1 1 -1
	1 1 2 2 3 3
	2 2 3 3 1 1
    0 1 1 1 0 2

**Sample Output**
	
    NO
	YES
	NO
	YES
    NO

## Sample Tests

### Test 1

```
5
1 2 2 1 2 2
-1 1 1 1 1 -1
1 1 2 2 3 3
2 2 3 3 1 1
0 1 1 1 0 2
```

### Test 2

```
NO
YES
NO
YES
NO
```
