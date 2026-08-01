# Definite Random Walks

- **Domain:** mathematics
- **Difficulty:** Expert
- **Max Score:** 100
- **Success Ratio:** 0.8455284552845529
- **Total Submissions:** 1722
- **Solved Count:** 1456
- **URL:** https://www.hackerrank.com/challenges/definite-random-walks

## Problem Statement

Alex has a board game consisting of:

- A *chip* for marking his current location on the board.
- $n$ *fields* numbered from $1$ to $n$. Each position $i$ has a value, $f_i$, denoting the *next* position for the chip to jump to from that field.
- A *die* with $m$ faces numbered from $0$ to $m-1$. Each face $j$ has a probability, $p_j$, of being rolled.

Alex then performs the following actions:

- Begins the game by placing the chip at a position in a field randomly and with equiprobability. 
- Takes $k$ turns; during each turn he:
	- Rolls the die. We'll denote the number rolled during a turn as $d$.
    - Jumps the chip $d$ times. Recall that each field contains a value denoting the *next* field number to jump to.
- After completing $k$ turns, the game ends and he must calculate the respective probabilities for each field as to whether the game ended with the chip in that field.

Given $n$, $m$, $k$, the game board, and the probabilities for each *die* face, print $n$ lines where each line $i$ contains the probability that the chip is on field $i$ at the end of the game.

**Note:** All the probabilities in this task are rational numbers modulo $M = 998244353$. That is, if the probability can be expressed as the irreducible fraction $\frac{p}{q}$ where $q \bmod M \ne 0$, then it corresponds to the number $(p \times q^{-1}) \bmod M$ (or, alternatively, $p \times q^{-1} ≡ x (\bmod M)$). [Click here](https://en.wikipedia.org/wiki/Modular_multiplicative_inverse) to learn about *Modular Multiplicative Inverse*.

## Input Format

The first line contains three space-separated integers describing the respective values of $n$ (the number of positions), $m$ (the number of die faces), and $k$ (the number of turns).			
The second line contains $n$ space-separated integers describing the respective values of each $f_i$ (i.e., the index of the field that field $i$ can transition to).		
The third line contains $m$ space-separated integers describing the respective values of each $p_j$ (where $0 \le p_j < M$) describing the probabilities of the faces of the $m$-sided die.  

## Output Format

Print $n$ lines of output in which each line $i$ contains a single integer, $x_i$ (where $0 \le x_i < M$), denoting the probability that the chip will be on field $i$ after $k$ turns.

## Constraints

+ $1 \le n \le 6\times 10^4$  
+ $4 \le m \le 10^5$  
+ $1 \le k \le 1000$  
- $1 \le i, f_i \le n$
- $0 \le p_j \lt M$
+ The sum of $p_j \bmod M$ is $1$  

**Note:** The time limit for this challenge is doubled for *all* languages. Read more about standard time limits at our [environment](https://www.hackerrank.com/environment) page.

## Sample Input

4 5 1
2 3 2 4
332748118 332748118 332748118 0 0

## Sample Output

582309206
332748118
332748118
748683265

## Explanation

The diagram below depicts the respective probabilities of each die face being rolled:

The diagram below depicts each field with an arrow pointing to the next field:

There are four equiprobable initial fields, so each field has a  probability of being the chip's initial location. Next, we calculate the probability that the chip will end up in each field after  turn:

- The only way the chip ends up in this field is if it never jumps from the field, which only happens if Alex rolls a . So, this field's probability is . We then calculate and print the result of  on a new line.

- The chip can end up in field  after one turn in the following scenarios:

- Start in field  and roll a , the probability for which is .

- Start in field  and roll a  or a , the probability for which is .

- Start in field  and roll a , the probability for which is .

After summing these probabilities, we get a total probability of  for the field. We then calculate and print the result of  on a new line.

- The chip can end up in field  after one turn in the following scenarios:

- Start in field  and roll a , the probability for which is .

- Start in field  and roll a , the probability for which is .

- Start in field  and roll a  or a , the probability for which is .

After summing these probabilities, we get a total probability of  for the field. We then calculate and print the result of  on a new line.

- If the chip is initially placed in field , it will always end up in field  regardless of how many turns are taken (because this field loops back onto itself). Thus, this field's probability is . We then calculate and print the result of  on a new line.
