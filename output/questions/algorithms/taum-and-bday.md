# Taum and B'day

---

| Field | Value |
|---|---|
| **Slug** | `taum-and-bday` |
| **Domain** | algorithms |
| **Difficulty** | Easy |
| **Score** | 25 |
| **URL** | https://www.hackerrank.com/challenges/taum-and-bday |

---

## Preview

Calculate the minimum cost required to buy gifts.

## Problem Statement

Taum is planning to celebrate the birthday of his friend, Diksha. There are two types of gifts that Diksha wants from Taum: one is black and the other is white. To make her happy, Taum has to buy $b$ black gifts and $w$ white gifts. 

- The cost  of each black gift is $bc$ units.

- The cost of every white gift is $wc$ units.

- The cost to convert a black gift into white gift or vice versa is $z$ units.


Determine the minimum cost of Diksha's gifts.


**Example**

$b = 3$

$w = 5$ 

$bc = 3$

$wc = 4$

$z = 1$


He can buy a black gift for $3$ and convert it to a white gift for $1$, making the total cost of each white gift $4$.  That matches the cost of a white gift, so he can do that or just buy black gifts and white gifts.  Either way, the overall cost is $3 * 3 + 5 * 4 = 29$.


**Function Description**


Complete the function *taumBday* in the editor below.  It should return the minimal cost of obtaining the desired gifts.


taumBday has the following parameter(s):


- *int b*: the number of black gifts

- *int w*: the number of white gifts

- *int bc*: the cost of a black gift

- *int wc*: the cost of a white gift

- *int z*: the cost to convert one color gift to the other color


**Returns**


- *int:* the minimum cost to purchase the gifts

## Input Format

The first line will contain an integer $t$, the number of test cases. 

The next $t$ pairs of lines are as follows:

- The first line contains the values of integers $b$ and $w$. 

- The next line contains the values of integers $bc$, $wc$, and $z$.

## Output Format

$t$ lines, each containing an integer: the minimum amount of units Taum needs to spend on gifts.

## Constraints

$1 \le t \le 10$

$0 \le b, w,bc,wc,z \le 10^9$

## Sample Tests

### Test 1

```
STDIN Function
----- --------
5 t = 5
10 10 b = 10, w = 10
1 1 1 bc = 1, wc = 1, z = 1
5 9 b = 5, w = 5
2 3 4 bc = 2, wc = 3, z = 4
3 6 b = 3, w = 6
9 1 1 bc = 9, wc = 1, z = 1
7 7 b = 7, w = 7
4 2 1 bc = 4, wc = 2, z = 1
3 3 b = 3, w = 3
1 9 2 bc = 1, wc = 9, z = 2
```

### Test 2

```
20
37
12
35
12
```
