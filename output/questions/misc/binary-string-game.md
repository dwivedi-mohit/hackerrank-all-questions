# Binary String Game

---

| Field | Value |
|---|---|
| **Slug** | `binary-string-game` |
| **Domain** | misc |
| **Difficulty** | Hard |
| **Score** | 100 |
| **Contest** | 101hack32 |
| **URL** | https://www.hackerrank.com/challenges/binary-string-game |

---

## Preview

Given a binary string and some 'k', each player must flip 'k' continuous 1's in a move. The first one to not make a move loses; who will be the winner?

## Problem Statement

Alice and Bob decide to play a game, described below. Both players are clever and will always choose the best possible strategy. Alice is older and will always play first.

Given a *binary string*, $S$, and some number, $k$, each player must find $k$ consecutive $1$'s in the string and flip them to $0$'s. If no such sequence of $k$ consecutive $1$'s can be found, the player loses the game. Who will win the game?

## Input Format

The first line contains one integer $n$, indicating the number of games Alice and Bob will play.

Then, the following $2n$ lines describe $n$ games separately. For $i(1 \le i \le n)$-th game, we will give $k_i$, the number of consecutive $1$'s each player must flip per turn in $2i$-th line and give the binary string, $S_i$ in $2i+1$-th line. 

**Constraints**		
For 25% test cases: $1 \le k \le |S|$ $\le 10$  

For 75% test cases: $1 \le k \le |S|$ $\le 1000$

For *the other* 25% test cases: $k = 2$; $1 \le |S| \le 10^6$.		
For 100% test cases: $1 \le n \le 5$.

String S can only contains '0' and '1'

## Output Format

For each $S$, print the name of the winner (i.e.: **Alice** or **Bob**) on a new line.

## Sample Tests

### Test 1

```
3
4
111111
2
111111
4
110111
```

### Test 2

```
Alice
Alice 
Bob
```
