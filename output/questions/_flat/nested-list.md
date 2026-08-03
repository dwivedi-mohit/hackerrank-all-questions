# Nested Lists

---

| Field | Value |
|---|---|
| **Slug** | `nested-list` |
| **Domain** | python |
| **Difficulty** | Easy |
| **Score** | 10 |
| **URL** | https://www.hackerrank.com/challenges/nested-list |

---

## Preview

In a classroom of N students, find the student with the second lowest grade.

## Problem Statement

Given the names and grades for each student in a class of $N$ students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

**Note:** If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

**Example**

$records = [[\text{"chi"}, 20.0], [\text{"beta"}, 50.0], [\text{"alpha"}, 50.0]]$

The ordered list of scores is $[20.0, 50.0]$, so the second lowest score is $50.0$.  There are two students with that score: $[\text{"beta", "alpha"}]$.  Ordered alphabetically, the names are printed as:
<pre>
alpha
beta
</pre>

## Input Format

The first line contains an integer, $N$, the number of students. 	
The $2N$ subsequent lines describe each student over $2$ lines.

- The first line contains a student's name.

- The second line contains their grade.

## Output Format

Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

## Constraints

- $2 \le N \le 5$

- There will always be one or more students having the second lowest grade.

## Sample Tests

### Test 1

```
alpha
beta
```

### Test 2

```
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
```

### Test 3

```
Berry
Harry
```
