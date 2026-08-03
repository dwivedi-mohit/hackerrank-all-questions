# Puzzle and PC

---

| Field | Value |
|---|---|
| **Slug** | `puzzle-and-pc` |
| **Domain** | fp |
| **Difficulty** | Hard |
| **Score** | 80 |
| **URL** | https://www.hackerrank.com/challenges/puzzle-and-pc |

---

## Preview

Help little Johnny with the puzzle.

## Problem Statement

Mom has to go to work and she doesn't want little Johnny to get bored. So she gives him a simple puzzle to solve. She also tells him that he can play a PC game only if he solves this problem. Johnny loves PC games and wants to solve this puzzle quickly. So he asks you for help.


You are given a square _NxN_ board divided into single cells, where _N_ is always a power of 2. You are also given an infinite number of L-shaped trominoes:


![tromino](http://hr-challenge-images.s3.amazonaws.com/4022/tromino.png)

Note that each tromino can covers three cells.

The board has one special cell _S_ on which you are not allowed to place any tromino. Your task is to cover the whole board with trominoes in such a way that any two trominoes don't overlap, and every cell (except cell _S_) is covered by some tromino.


Indexing starts from 1, and top-left cell is indexed (1, 1).


**Input**

In the first line, there is an integer $M$. $N = 2^M$ denotes the size of the board.

In the second line, there are two integers, _r c_, denoting the row and the column of cell _S_.

**Output**

For every tromino placed, print one line containing 6 space separated numbers, denoting the coordinates (in row major form) of 3 cells covered by this block.

**Constraints**

- $1 \le M \le 9$
- $1 \le r, c \le 2^M$

**Note**


- You are also allowed to rotate the trominoes.
- There may be multiple solution for a case. All valid solutions will be considered correct.

**Sample Input #00**

    1
    2 2

**Sample Output #00**

	1 1 1 2 2 1

**Sample Input #01**


    2
    1 1

**Sample Output #01**


    2 3 3 2 3 3
    1 2 2 1 2 2
    1 3 1 4 2 4
    3 1 4 1 4 2
    3 4 4 3 4 4

**Explanation #00**

*Sample Case #00:* Since you are not allowed to cover bottom-right cell, you will cover points (1,1), (1,2) & (2,1) with a single tromino.

	    1   2
	1 | 1 | 1 |
	2 | 1 | x |


*Sample Case #01:* Since $N = 2^2 = 4$, board is of size $4x4$ and you are not allowed cover top-left cell. You will need 5 trominoes to cover whole board, except cell (1, 1).

1. `2 3 3 2 3 3`: This tromino will cover points (2, 3), (3, 2), (3, 3).
2. `1 2 2 1 2 2`: This tromino will cover points (1, 2), (2, 1), (2, 2).
3. `1 3 1 4 2 4`: This tromino will cover points (1, 3), (1, 4), (2, 4).
4. `3 1 4 1 4 2`: This tromino will cover points (3, 1), (4, 1), (4, 2).
5. `3 4 4 3 4 4`: This tromino will cover ponits (3, 4), (4, 3), (4, 4).

.

	    1   2   3   4
	1 | x | 2 | 3 | 3 |
	2 | 2 | 2 | 1 | 3 |
	3 | 4 | 1 | 1 | 5 |
	4 | 4 | 4 | 5 | 5 |

Note that there can be multiple configurations to this input, and all will be considered correct

---
**Tested by** [Wanbo](/wanbo)

## Sample Tests

### Test 1

```
1
2 2
```

### Test 2

```
1 1 1 2 2 1
```

### Test 3

```
2
1 1
```

### Test 4

```
2 3 3 2 3 3
1 2 2 1 2 2
1 3 1 4 2 4
3 1 4 1 4 2
3 4 4 3 4 4
```

### Test 5

```
1 2
1 | 1 | 1 |
2 | 1 | x |
```

### Test 6

```
1 2 3 4
1 | x | 2 | 3 | 3 |
2 | 2 | 2 | 1 | 3 |
3 | 4 | 1 | 1 | 5 |
4 | 4 | 4 | 5 | 5 |
```
