# Mr. X and His Shots

---

| Field | Value |
|---|---|
| **Slug** | `x-and-his-shots` |
| **Domain** | data-structures |
| **Difficulty** | Medium |
| **Score** | 50 |
| **URL** | https://www.hackerrank.com/challenges/x-and-his-shots |

---

## Preview

Find the number of shots that you can stop in the given range.

## Problem Statement

A cricket match is going to be held. The field is represented by a 1D plane. A cricketer, Mr. X has $N$ favorite shots. Each shot has a particular range.
The range of the  $i^{th}$ shot is from $A$<sub>i</sub> to $B$<sub>i</sub>. That means his favorite shot can be anywhere in this range. Each player on the opposite team 
can field only in a particular range. Player $i$ can field from $C$<sub>i</sub> to $D$<sub>i</sub>. You are given the $N$ favorite shots of Mr. X and the range of $M$ players.<br><br> 
$\ Si \ $ represents the strength of each player i.e. the number of shots player $i$ can stop. <br>
Your task is to find:

$\left(\sum_{i=1}^m Si \right )$.

**Game Rules**: A player can stop the $i^{th}$ shot if the range overlaps with the player's fielding range.<br><br>
For more clarity about overlapping, study the following figure:


<img src="https://s3.amazonaws.com/hr-challenge-images/8943/1441719277-9d9c50f731-L.png" title="L.png" />

## Input Format

The first line consists of two space separated integers, $N$ and $M$.<br/>
Each of the next $N$ lines contains two space separated integers. The $i^{th}$ line contains $A_i$ and $B_i$.<br/>
Each of the next $M$ lines contains two integers. The $i^{th}$ line contains integers $C_i$ and $D_i$.

## Output Format

You need to print the sum of the strengths of all the players: $\left(\sum_{i=1}^m Si \right )$.<br>
 

   **Constraints**:<br>
 

 $1 ≤ N, M ≤ 10^5$

 $1 \le  A_i , B_i , C_i, D_i \le 10^8$

## Sample Tests

### Test 1

```
4 4 
1 2 
2 3
4 5
6 7
1 5
2 3
4 7
5 7
```

### Test 2

```
9
```
