# Mehta and the Typical Supermarket

---

| Field | Value |
|---|---|
| **Slug** | `mehta-and-the-typical-supermarket` |
| **Domain** | mathematics |
| **Difficulty** | Hard |
| **Score** | 40 |
| **URL** | https://www.hackerrank.com/challenges/mehta-and-the-typical-supermarket |

---

## Preview

Help Mehta in shopping

## Problem Statement

Mehta is a very rich guy. He has $N$ types of coins, and each type of coin is available in an unlimited supply.


So Mehta goes to a supermarket to buy monthly groceries. There he sees that every item has a unique price, that is, no two items have the same price.


Now, the supermarket owner tells Mehta that they are selling items in the price range $[L, R]$ only on that particular day. He also tells Mehta that for every price, there is an item in the shop.


The supermarket has recently adopted a weird new tradition: Mehta may only use a single type of coin for each item he purchases. For example, he could pay for an item of price 4 with two 2-coins, but not with a 3-coin and a 1-coin.


As you know Mehta is very weak at calculations, so he wants you to do these calculations for him and tell how many different types of items he can buy.


**Input Format**

The first line of input contains $N$, the number of types of coins Mehta has.

Then the next $N$ lines contain an integer each: the *i<sup>th</sup>* line contains $A[i]$, the value of Mehta's *i<sup>th</sup>* type of coin.


Then the next line contains a number $D$, the number of days Mehta goes shopping.

Then each of the next $D$ lines contains numbers $L$ and $R$, denoting that they are selling items in price range $[L, R]$ on that particular day.



**Output format**

There will be $D$ lines, each containing the number of distinct items that can be bought at that particular day.


**Constraints**

$1 \le N \le 17$

$1 \le A[i] \le 51$

$1 \le D \le 101$

$1 \le L \le R \le 10^{18}$


**Sample Input**

 

    4
    2
    3
    4
    5
    3
    1 10
    2 20
    3 7
  

**Sample output**

    8
    14
    4
  

**Explanation**

For $L = 1$ and $R = 10$ you can buy items of price $\{2,3,4,5,6,8,9,10\}$.

For $L = 2$ and $R = 20$ you can buy items of price $\{2,3,4,5,6,8,9,10,12,14,15,16,18,20\}$.

For $L = 3$ and $R = 7$ you can buy items of price $\{3,4,5,6\}$.

## Sample Tests

### Test 1

```
4
2
3
4
5
3
1 10
2 20
3 7
```

### Test 2

```
8
14
4
```
