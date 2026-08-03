# The Cowardly Sage

---

| Field | Value |
|---|---|
| **Slug** | `the-cowardly-sage` |
| **Contest** | hourrank-3 |
| **Difficulty** | Hard |
| **Score** | 70 |
| **URL** | https://www.hackerrank.com/challenges/the-cowardly-sage |

---

## Problem Statement

Karas is a legendary gambler, famous for understanding which games can be won. He is often referred to as "The Cowardly Sage" due to his guiding principle, "Never play a game you are sure you cannot win."
<hr>

At the *Firework Ground*, two players stand in the ground's center at $(0,0)$, surrounded by $N$ fireworks. Each firework, $i$, is $r_i$ units away from the center. A straight line drawn from the center to firework $i$ will have a gradient, or slope, of $\frac{a_i}{b_i}$.

The two players move in turns, and the game only allows these two moves:

1. **Circular:** Choose a radius, $r$, and activate all fireworks exactly $r$ units from the center.
2. **Linear:** Choose a gradient, $\frac{a}{b}$. Activate all fireworks that lie on the line $l$ passing through the ground's center with that gradient. An equation for $l$ would be $y=\frac{a}{b}x$. 

Once a firework is activated, it's ignited in the sky and is no longer part of the field.

For each turn, a player makes one of the two allowed moves. A player must activate at least one firework per turn. *If a player fails to activate a firework, they lose.*

**Note:** Each location in the field can have $0$, $1$, or $2$ fireworks. For safety reasons, no move will ever activate more than two fireworks.

Given the details for the *Firework Ground*, determine whether or not Karas will play the game (keeping in mind that he never plays a game if there is a possibility he will lose). Karas moves first.

## Input Format

The first line contains a single integer, $T$, the number of test cases.

The first line of each test case contains a single integer, $N$, the number of fireworks. This is followed by $N$ lines, each of which describes a firework. 

For each firework, there will be three positive integers, $r_{i}$, $a_{i}$ and $b_{i}$. 	
$r_{i}$ is the distance between the $i^{th}$ firework and the center.	
$\frac{a_{i}}{b_{i}}$ is the gradient of a straight line, $l$, drawn from the $i^{th}$ firework to the center. 

**Constraints**

$1 \leq T \leq 5$<br>
$1 \leq N \leq 1000$ <br>
$ 1 \leq r_{i}, a_{i}, b_{i} \leq 10^{9}$

## Output Format

For each test case, print either **Sage** (if Karas decides to play), or **Coward** (if he does not).
