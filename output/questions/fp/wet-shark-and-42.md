# Wet Shark and 42

- **Domain:** fp
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.5403543307086615
- **Total Submissions:** 2032
- **Solved Count:** 1098
- **URL:** https://www.hackerrank.com/challenges/wet-shark-and-42

## Problem Statement

As punishment for attacking Sunland, Wet Shark is now forced to walk on a line of numbered squares, starting from $1$ and going to infinity. Wet Shark initially has a strength of $S$. To make the experience harder for Wet Shark, each square that has a label divisible by $4$ and/or $2$ but not divisible by $42$ contains a black glob of jelly, stepping on which his strength decreases by $1$. 

Wet Shark does not know that this line of squares is infinitely long, and he is determined to continue walking until his strength reaches $0$. Wet Shark walks from square to square, so he starts at square $1$, goes to square $2$, then $3$, then $4$, etc. 

Wet Shark’s punisher needs your help, and wants to compute where Wet Shark will stop in order to meet him there and punish him. Given Wet Shark’s initial strength $S$, find the square on which Wet Shark’s strength will reach $0$. Wet Shark can go far if defenses are not strong enough, so please output the answer modulo $10^9+7$. Wet Shark is curious, so he wants to know that given $S$ strength initially, how far he will go for different values $S$. Help him figure out how long he can go without doom for each $S$.


## Input Format

The first line of the input contains an integer $T$, the number of queries. The following lines describe the queries.

Each query consists of a line containing a single integer, which is the value of $S$.


## Output Format

Print $T$ lines, each line containing the answer for each query, i.e. the last square Wet Shark will reach before he runs out of strength, starting with a strength of $S$, modulo $10^9+7$.

**Constraints**  

$1 \le T \le 100$  
$1 \le S \le 10^{18}$  

## Sample Input

3
4

## Sample Output

8

## Explanation

Square 1: 3 strength

Square 2: 2 strength

Square 3: 2 strength

Square 4: 1 strength

Square 5: 1 strength

Square 6: 0 strength

Thus the answer is 6.
