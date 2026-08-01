# Elemental Orbs

- **Domain:** shell
- **Difficulty:** Medium
- **Max Score:** 100
- **Success Ratio:** 0.375
- **Total Submissions:** 8
- **Solved Count:** 3
- **URL:** https://www.hackerrank.com/challenges/elemental-orbs

## Problem Statement

You are an elemental sorcerer who owns a shop that sells magical orbs, with each orb containing the power of some distinct element (e.g., Fire, Water, Earth, etc.). The shop has a shelf with $N$ horizontal slots, where each slot has the capability of holding exactly $1$ orb.

Being a novice sorcerer, your _elemental knowledge_ is just $E$, i.e. you know only $E$ different kinds of elemental spells, where each can conjure identical orbs of a distinct element type. Before the shop opens next morning, you want to fill all the shelf with such orbs; no slot should remain unoccupied.

Now, to fill the shelf, you conjure $N$ orbs of *up to* $E$ different types (or elements) and arrange it on the shelf. However, each element $i$ has a *blasting threshold*, $B_i$, meaning that if there are more than $B_i$ contiguously-placed orbs of element type $i$ placed anywhere on the shelf, they will explode and destroy the shelf and the orbs in it. The shelf may contain less than $E$ distinct types of orbs as long as the configuration will not explode.

You want to find the number of possible configurations to arrange the shelf with these elemental orbs without any explosion.

You are given the values of $N$, $E$, and the blasting threshold $B_i$ for each element $i$. Find and print the number of distinct ways, modulo $10^9 + 7$, on a new line.

**Note**: All orbs of the same element type are identical, but each slot in a shelf is distinct. You can conjure any type of orb an infinite number of times.

## Input Format

The first line contains an integer, $t$, number of test cases. The $2 \cdot t$ subsequent lines describe each tescase over two lines:

1. The first line of each test case contains two space-separated integers describing the respective values of $N$ (the shelf's capacity) and $E$ (elemental knowledge).
2. The second line of each test case contains $E$ space-separated integers describing $B_1, B_2, \ldots, B_{E}$ (i.e., the respective blasting thresholds for all elements).

## Output Format

For each test case, print an integer on a new line describing the number of distinct ways to arrange $N$ orbs on the shelf, modulo $10^9+7$.

## Constraints

- $1 \le t \le 10$
- $1 \le N \le 2000$
- $1 \le E \le 2000$
- $1 \le B_i \le N$


## Sample Input

2
5 2
1 1
5 2
5 5

## Sample Output

2
32

## Explanation

The diagram below depicts the possible valid and invalid configurations for the first shelf, described as , , and :

Because the blasting threshold for both types of orbs is , any configuration containing more than  consecutive orb of the same type will cause the shelf to explode. As there are only two valid configurations for this shelf, we print the result of  on a new line.
