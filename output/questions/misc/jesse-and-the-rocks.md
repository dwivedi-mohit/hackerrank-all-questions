# Jesse and the Rocks

---

| Field | Value |
|---|---|
| **Slug** | `jesse-and-the-rocks` |
| **Contest** | codeagon-2016 |
| **Difficulty** | Easy |
| **Score** | 20 |
| **URL** | https://www.hackerrank.com/challenges/jesse-and-the-rocks |

---

## Problem Statement

Jesse is standing at the head of a straight line of $N$ rocks of varying *strengths*, and can break a rock, $i$, if his strength ($strengthJesse$) is *greater than or equal to* $strengthRock_i$. Jesse can skip a single rock in the line without breaking it (but no more rocks can be skipped after that) and must stop after reaching a rock that cannot be either broken or skipped. Starting at the first rock and going through the line in order, help Jesse find the maximum number of rocks ($maxRocks$) that can be broken.

**Note:** A skipped rock is *not* broken.

## Input Format

The first line contains $2$ space-separated integers, $N$ (the number of rocks) and $strengthJesse$, respectively. 	
The second line contains a list of $N$ space-separated integers ($strengthRock_0$ through $strengthRock_{N-1}$) describing the strength of each rock.

**Constraints**   
$1\le N\le 10^5$  
$1 \le strengthJesse \le 10^9$  
$1 \le strengthRock_i \le 10^9$, where $0 \le i \le N-1$

## Output Format

Print $maxRocks$ as a single integer.
