# Day 6: Let's Review

---

| Field | Value |
|---|---|
| **Slug** | `30-review-loop` |
| **Domain** | tutorials |
| **Difficulty** | Easy |
| **Score** | 30 |
| **URL** | https://www.hackerrank.com/challenges/30-review-loop |

---

## Preview

Characters and Strings

## Problem Statement

**Objective**	
Today we will expand our knowledge of strings, combining it with what we have already learned about loops. Check out the [Tutorial](/challenges/30-review-loop/tutorial) tab for learning materials and an instructional video.	

**Task**	
Given a string, $S$, of length $N$ that is indexed from $0$ to $N-1$, print its *even-indexed* and *odd-indexed* characters as $2$ space-separated strings on a single line (see the *Sample* below for more detail). 

**Note:** $0$ is considered to be an *even* index. 

**Example**


$s = \text{adbecf}$


Print ```abc def```

## Input Format

The first line contains an integer, $T$ (the number of test cases). 	
Each line $i$ of the $T$ subsequent lines contain a string, $S$.

## Output Format

For each String $S_j$ (where $0 \le j \le T-1$), print $S_j$'s *even-indexed* characters, followed by a space, followed by $S_j$'s *odd-indexed* characters.

## Constraints

- $1 \leq T \leq 10$  	
- $2 \leq \text{length of }S \leq 10000$

## Sample Tests

### Test 1

```
2
Hacker
Rank
```

### Test 2

```
Hce akr
Rn ak
```
