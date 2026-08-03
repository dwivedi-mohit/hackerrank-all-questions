# Bags of Apples

---

| Field | Value |
|---|---|
| **Slug** | `bags-of-apples` |
| **Domain** | misc |
| **Difficulty** | Easy |
| **Score** | 30 |
| **Contest** | 101hack28 |
| **URL** | https://www.hackerrank.com/challenges/bags-of-apples |

---

## Preview

Choose some numbers from a given array so that their sum is divisible by three. If there are multiple such sums, find the greatest among them.

## Problem Statement

Mika is a very rich guy. He has $n$ bags of apples. Each bag contains a positive integer number of apples, the bag with number $i$ containing $a_i$ apples. Mika decided that the time has come to sell some of his bags. When selling a bag, Mika is automatically selling each apple inside the bag, but he can't take an apple out of the bag and sell it separately. To make this more interesting, Mika added yet another extra condition: he wants the total number of sold apples to be divisible by $3$. 

So Mika is wondering what is the maximum number of apples that can be sold? Help him calculate that number.

**Input Format**<br>

The first line contains integer $n$ ($1 \leq n \leq 1000$), the number of Mika's bags of apples. 

The second line contains $n$ numbers $a_1, a_2, \ldots, a_n$ ($1 \leq a_i \leq 1000$), where $a_i$ is the number of apples in the $i$<sup>$th$</sup> bag ($1 \leq i \leq n$).

**Output Format**<br>

In a single line, print the largest total number of apples which can be sold.

**Sample Input 1**<br>

	4
    2 2 1 2

**Sample Output 1**<br>

	6

**Sample Input 2**<br>

    5
    3 6 9 9 3


**Sample Output 2**<br>

	30

## Sample Tests

### Test 1

```
4
2 2 1 2
```

### Test 2

```
6
```

### Test 3

```
5
3 6 9 9 3
```

### Test 4

```
30
```
