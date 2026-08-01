# New Year Game

- **Domain:** python
- **Difficulty:** Medium
- **Max Score:** 60
- **Success Ratio:** 0.6699395770392749
- **Total Submissions:** 2648
- **Solved Count:** 1774
- **URL:** https://www.hackerrank.com/challenges/newyear-game

## Problem Statement

It's New Year's Day, and Balsa and Koca are stuck inside watching the rain. They decide to invent a game, the rules for which are described below.

Given array $a$ containing $n$ integers, they take turns making a single move. *Balsa always moves first, and both players are moving optimally (playing to win and making no mistakes)*.

During each move, the current player chooses one element from $a$, adds it to their own score, and deletes the element from $a$; because the size of $a$ decreases by $1$ after each move, $a$'s size will be $0$ after $n$ moves and the game ends (as all elements were deleted from $a$). We refer to Balsa's score as $S_b$ and Koca's score as $S_k$. Koca wins the game if |$S_b$-$S_k$| is divisible by $3$; otherwise Balsa wins. 

Given $a$, determine the winner.

**Note:** $S_b + S_k = a_0 + a_1 + ... + a_{n-2} + a_{n-1}$.

## Input Format

The first line contains an integer, $T$, denoting the number of test cases.		
Each test case is comprised of two lines; the first line has an integer $n$, and the second line has $n$ space-separated integers $a_0, a_1, \ldots, a_{n-2}, a_{n-1}$ describing array $a$.

**Constraints**<br>


$1 \leq T \leq 100 $<br>
$1 \leq a_i \leq 2000 $<br>
$1 \leq n \leq 2000 $

**Subtasks**

For $50\%$ score: $1 \leq n \leq 200 $<br>
For $100\%$ score: $1 \leq n \leq 2000 $<br>

## Output Format

For each test case, print the winner's name on a single line; if Balsa wins print **Balsa**, otherwise print **Koca**.

## Constraints

Subtasks

For  score:

For  score:

## Sample Input

3
7 6 18
1
3

## Sample Output

Balsa
Koca

## Explanation

Test Case 1

Array . The possible play scenarios are:

- , , , and .

- , , , and .

- , , -, and .

In this case, it doesn't matter what Balsa chooses because the difference between their scores isn't divisible by . Thus, Balsa wins.

Test Case 2

Array . Balsa must choose that element, the first move ends the game.

, , , and . Thus, Koca wins.
