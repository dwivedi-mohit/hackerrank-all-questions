# Shashank and NIM

---

| Field | Value |
|---|---|
| **Slug** | `shashank-and-nim` |
| **Domain** | misc |
| **Difficulty** | Hard |
| **Score** | 60 |
| **Contest** | adobe-hackathon |
| **URL** | https://www.hackerrank.com/challenges/shashank-and-nim |

---

## Preview

Help Shashank win the NIM Game.

## Problem Statement

Shashank is playing the NIM game with Sara. The NIM game rules are described below:

There are $N$ buckets. Each bucket contains $1$ or more ball(s). During each turn, a player selects a bucket and takes out $1$ or more ball(s). The last player to take out the last ball(s) wins the game.

Shashank makes a modification to the game because he is bored. For the first 50 moves, the game is played in the following manner: 


1. Shashank adds a bucket containing a non-zero number of balls.
2. Sara adds a bucket containing a non-zero number of balls. 
3. Shashank selects a bucket and takes out $1$ or more balls.
4. Sara selects a bucket and takes out $1$ or more balls.

After the first 50 moves, the usual rules of the NIM game are followed, and the addition of buckets does not take place. Shashank plays first. Shashank wants to know the minimum number of balls the **first additional** bucket should contain (which he is adding in the first turn of the game). If no such bucket exists, print −1.

Your task: Find the minimum number of balls Shashank should add to win the game.

**Input Format**

The first line contains an integer $T$, denoting the number of test cases.<br>
The first line of each test case contains an integer $N$, denoting the number of buckets.<br>
The next line contains $N$ integers. The $i^{th}$ integer denotes the number of balls in the $i^{th}$ bucket.


**Output Format**

Print the answer corresponding to each test case on separate lines. 

**Constraints**


$ 1\le T \le 10$  <br>
$ 1\le N \le 10^4$ <br>
$ 1\le A_i \le 10^{18}$ , where $A_i$ is the $i^{th}$ integer.


**Sample Input**

	1
    1
    10


**Sample Output**

	10

## Sample Tests

### Test 1

```
1
1
10
```

### Test 2

```
10
```
