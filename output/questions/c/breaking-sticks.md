# Breaking Sticks

- **Domain:** c
- **Difficulty:** Medium
- **Max Score:** 40
- **Success Ratio:** 0.7359649122807017
- **Total Submissions:** 1140
- **Solved Count:** 839
- **URL:** https://www.hackerrank.com/challenges/breaking-sticks

## Problem Statement

You recently received a bag of chocolate sticks for Halloween. To prevent you from compulsively eating all the chocolate sticks in one go, your dietician devises the following fun game.

In each move, you choose one of the sticks from your bag. Then, you either eat it, or  break it into some number of equally-sized parts and save the pieces for later. The lengths of all sticks must always be integers, so breaking a stick into $d$ parts is possible only if $d$ is a divisor of the stick's length, and $d > 1$.

Note that this means that a stick of length $1$ cannot be broken anymore, and can only be eaten.

For example, a chocolate stick of length $4$ will be dealt with as shown below. 

![image](https://s3.amazonaws.com/hr-assets/0/1512379963-3180b66375-choc.png)

Given the chocolate sticks you received, determine the length of the longest sequence of moves you can perform.

Complete the function `longestSequence` which takes an integer array $a$, denoting the lengths of the chocolate sticks, as input. Return the maximum number of moves you can perform to consume the chocolate sticks according the game. 



## Input Format

The first line contains one integer $n$ which is the number of chocolate sticks.

The second line contains $n$ space-separated integers $a_1, a_2, \ldots, a_n$, the lengths of the chocolate sticks.

## Output Format

Print a single integer which is the maximum number of moves you can perform.

## Constraints

- $1 \leq n \leq 100$
- $1 \leq a_i \leq 10^{12}$

**Subtasks**  

- For $20\%$ of the total score, $a_i \leq 10^6$

## Sample Input

1
6

## Sample Output

10

## Explanation

You break a chocolate stick into three equal parts (1 move), then break each of them in half (3 moves), and then eat all six sticks (6 moves). This gives you 10 moves.
