# The Prime Game 

- **Domain:** ai
- **Difficulty:** Hard
- **Max Score:** 90
- **Success Ratio:** 0.7363790186125212
- **Total Submissions:** 2955
- **Solved Count:** 2176
- **URL:** https://www.hackerrank.com/challenges/the-prime-game

## Problem Statement

Manasa loves the [nim game](http://en.wikipedia.org/wiki/Nim), in which there are $n$ buckets, each having $A_i$ balls. Two players play alternately. Each turn consists of removing some non-zero number of balls from one of the bucket. A player with lack of moves looses. But, Manasa having played it so many times, she gets bored one day. So she wants to change the rules of the game. She loves prime numbers, so she makes a new rule: any player can only remove a prime number of balls from a bucket. But there are infinite number prime numbers. So to keep the game simple, a player can only remove $x$ balls from a bucket if $x$ belongs to the set $$ S =  \{ 2,3,5,7,11,13 \}.$$

The whole game can now be described as follows:   

There are $n$ buckets, and the $k^\text{th}$ bucket contains $A_k$ balls. A player can choose a bucket and remove $x$ balls from that bucket where $x$ belongs to $S$. A player loses if there are no more available moves.

Manasa plays the first move against Sandy. Who will win if both of them play optimally?

## Input Format

The first line contains an integer $t$, the number of test cases. 

Each test case consists of two lines. The first line contains a single integer $n$. The second line contain $n$ space-separated integers $A_1, A_2, \ldots, A_n$.  

## Output Format

Print a single line containing the name of the winner: `Manasa` or `Sandy`.

## Constraints

- $ 1 \le t \le 10$  
- $ 1 \le n \le 10^4$  
- $ 1 \le A_k \le 10^{18}$  

## Sample Input

2
2
10 10
3
2 2 3

## Sample Output

Sandy
Manasa

## Explanation

For the first testcase: Since both the buckets have same number of balls, Manasa can choose any one of them for her first move. If Manasa selects to remove  or  balls to remove from first bucket. Now, Sandy  can always counter her move by removing  balls from first bucket if it's left with  balls respectively. Now, there are no valid moves left for first bucket. The same thing repeats for second bucket and Sandy wins.

For the second testcase: Manasa removes  balls from the third bucket. Now, if Sandy choose the remove  balls from second bucket Manasa will empty the first bucket and if Sandy choose the remove  balls from first bucket, Manasa will empty second one. Hence, Manasa wins.
