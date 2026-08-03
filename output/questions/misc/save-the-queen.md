# Save the Queen!

---

| Field | Value |
|---|---|
| **Slug** | `save-the-queen` |
| **Contest** | hourrank-31 |
| **Difficulty** | Medium |
| **Score** | 40 |
| **URL** | https://www.hackerrank.com/challenges/save-the-queen |

---

## Problem Statement

The kingdom of Zokoria is under attack! The invaders wish to capture the Queen and conquer Zokoria. Aware of the danger, Heldorf , the captain of the Zokorian army must devise an exit strategy for the Queen. 

In order to do so, the invaders must be kept at bay for a period of time. There are $n$ invaders who must be engaged in fight for as long as possible. The army has $k$ soldiers, with each having the capability to fight for a total of $a$<sub>$i$</sub> seconds. The soldiers can fight against any invader at any time i.e. they can move to fight with another invader by dropping the current fight.

Heldorf wants you to find out how long does he have to help the Queen escape. You have to find the maximum possible time for which all the $n$ invaders can be kept busy?

## Input Format

The first line of input contains two numbers $n$ and $k$ -  the number of invaders and the number of soldiers respectively.

The next line contains $k$ numbers, each integer representing the time for which the respective soldier can engage in a fight.

## Output Format

Print the maximum possible time for which the $n$ invaders can be engaged in a fight. The number should be accurate up to $10^{-4}$ absolute precision.

## Constraints

- $ 1 ≤ n ≤ k ≤ 10^{4} $
- The time for which each solider can fight, $a$<sub>$i$</sub>, lies between $1$ and $10^{6}$.
