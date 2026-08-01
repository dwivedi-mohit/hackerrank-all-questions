# A stones game

- **Domain:** sql
- **Difficulty:** Medium
- **Max Score:** 90
- **Success Ratio:** 0.7668566001899335
- **Total Submissions:** 2106
- **Solved Count:** 1615
- **URL:** https://www.hackerrank.com/challenges/half

## Problem Statement

Koga and Ryuho, new generation Athena's saints, are training to improve their control over the cosmos. According to the ancient Masters, a saint's power to control the cosmos strengthens, when one allows the energy of the universe to flow within the body and then concentrates it. This energy can even be used to explode the objects. 

Today's training is based on a game, and the goal is to use as little cosmos as possible to win. Two saints play as follows: 

Initially there are $N$ piles of stones; pile $1$ has $1$ stone, pile $2$ has $2$ stones, and so on. Thus, the $i^{th}$ pile has $i$ stones. The saints take turns and in each turn, a saint must select a non-empty pile and destroy *at least half of the stones in it*. The winner is the saint who destroys the last available stone . 

For example, from a pile of $7$ stones, a saint must destroy at least $4$ stones, leaving a single (and possibly empty) pile at most 3 stones. With such game, saints learn how to use the appropriate amount of cosmos in a single strike: too much will destroy more stones than desired, too little won't be enough. They also improve their battle thinking and strategy skills.

Ryuho suspects that such game is not as random as it appears to be at first glance. He strongly believes that with the correct single blow, you're assured to win from the very first turn, if you play optimally, no matter how good the other saint plays. Moreover, he is particularly interested in knowing the minimum number of stones he needs to destroy at that first move. Can you help him?  


## Input Format

First line of the input consists of an integer $T$, $T$ testcases follow, each in a new line. Each line will contain a single integer $N$, which describes the number of initial piles as explained above.


## Output Format

For each line in the input, output the minimum number of stones Ryuho needs to destroy in his first turn, assuming he starts playing and that both he and Koga play always as well as possible. If this is not possible, just print $0$.


## Constraints

* $1 <= T <= 10^6$  
* $1 <= N <= 10^9$


## Sample Input

5
1
10
6
8
123456

## Sample Output

1
7
2
7
32768

## Explanation

For the first testcase, we can see that the saint can destroy the first stone and win the game.
