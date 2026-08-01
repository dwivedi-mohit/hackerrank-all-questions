# Buying Everything

- **Domain:** databases
- **Difficulty:** Medium
- **Max Score:** 100
- **Success Ratio:** 0.20270270270270271
- **Total Submissions:** 74
- **Solved Count:** 15
- **URL:** https://www.hackerrank.com/challenges/buying-everything

## Problem Statement

Jesse is going on a shopping spree in HackerLand. He wants to buy $m$ items. In HackerLand, all shops are specialized in selling only one type of item. Therefore, Jesse can purchase only one item for every distinct shop that he visits. 

HackerLand shops are located on a number line with $n$ buildings, $b_0, b_1, \ldots, b_{n-1}$, where each building $b_i$ is located at coordinate $i$. The value at each index indicates whether the shop at $b_i$ sells an item or not. $b_i = 1$ means building $i$ sells the item that Jesse needs, and $b_i = 0$ means it does not.

The distance between two buildings, $b_i$ and $b_j$, is $|j - i|$. 

Jesse always starts from his house at building $b_0$. As he buys more items, he has to carry heavy bags so his speed reduces by a *travel constant*, $k$. The travel time between $b_i$ and $b_j$, is calculated as follows:

* If he has not purchased any items, his travel time is $1 \cdot (|j - i|)$ minutes.
* If he has already purchased $c$ items, his travel time is $(|j - i|) \cdot (c \cdot k)$ minutes.

Given $n$, $m$, $k$, and a map of HackerLand, find and print the *minimum* time (in minutes) needed to purchase $m$ items from $m$ distinct shops. If he cannot buy all items, print `-1` instead.

**Note:** Building $b_0$ will not sell the items that Jesse needs. There are not always exactly $m$ shops and Jesse cannot travel backwards. 

## Input Format

The first line contains three space-separated integers describing the respective values of $n$ (the number of shops), $m$ (the number of items to purchase), and $k$ (the travel constant).		
The second line contains $n$ space-separated binary integers  $b_0, b_1, \ldots, b_{n-1}$ describing whether the respective building sells the items or not.

## Output Format

Print the minimum number of minutes taken by Jesse to purchase $m$ items from $m$ distinct shops. If it's not possible, print `-1` instead.

## Constraints

* $1 \le m \le n \le 2 \cdot 10^5$  
* $1 \le k \le 10^4$  
- $b_i \in \{0, 1\}$
* $b_0 = 0$


## Sample Input

7 1 3
0 0 0 1 0 0 0

## Sample Output

3

## Explanation

The city has  buildings, Jesse wants to buy  item, and the travel constant is . The only building that sells the needed items is , so Jesse must travel to that building to buy his first (and only) item. Because he always starts out with  items, it only takes him one minute to travel from building to building; this means that it takes him a total of  minutes to travel from  to  and purchase the item. Thus, we print  as our answer.
