# TBS Problem

---

| Field | Value |
|---|---|
| **Slug** | `tbsp` |
| **Domain** | algorithms |
| **Difficulty** | Expert |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/tbsp |

---

## Preview

The traveling salesman has started selling blimps! Their prices are declining though, so he'll need to get moving! Help him plot the route.

## Problem Statement

Quality Blimps Inc. is looking to expand their sales to other cities ($N$), so they hired you as a salesman to fly to other cities to sell blimps. Blimps can be expensive to travel with, so you will need to determine how many blimps to take along with you on each trip and when to return to headquarters to get more. Quality Blimps has an unlimited supply of blimps. 

You will be able to sell only one blimp in each city you visit, but you do not need to visit every city, since some have expensive travel costs. Each city has an initial price that blimps sell for, but this goes down by a certain percentage as more blimps are sold (and the novelty wears off). Find a good route that will maximize profits. 

**Details**

*Blimp Decline*  - The blimps will decline ($D$) in price every time you visit $10\%$ of the cities (the number of cities will always be a multiple of $10$). For example, if $D$ is $.95$ and there are $10$ cities, then for every city you visit (except headquarters), the price of blimps will be multiplied by $.95$. So after $5$ visits, every city's blimp price will be about $77\%$ of the initial value ($.95^5$).

Note that if the price declines after you visit some city, then it will only happen *after* you made the sale on that city, so your sale on that city will not be affected. In particular, each blimp you sell in the first $10\%$ of the cities will always be sold at their corresponding city's initial price.

## Input Format

The first line of input for each test case will contain three parameters:

- number of cities ($N$) 
- blimp cost per mile ($C$) 
- blimp factor of decline ($D$) 

This will be followed by $N$ lines, which will each contain three integers $x_i, y_i, p_i$, the city location (x and y coordinates the grid, in miles) and the initial blimp sales price, respectively.

## Output Format

On each line, output the x and y coordinates of the next city you are visiting. When leaving the headquarters, also output the number of blimps you are taking with you for that part of the trip. You do not need to return to headquarters when you finish your sales. 

You can only visit each city at most once.

## Constraints

+ $10 \le N \le 10^5$
+ $0.2 \le C \le 4$
+ $0.5 \le D \le 0.99$
+ $-10^3 \le x_i \le 10^3$
+ $-10^3 \le y_i \le 10^3$

+ $p_i < 10^5$

+ The city locations will be distinct

<!-- I didn't check that last one, but I'm guessing it's true since the checker looks like it assumes it. -->

## Sample Tests

### Test 1

```
10 3 0.95
1 1 30
2 2 35
0 8 50
7 2 20
7 3 25
10 7 90
9 8 35
5 15 10
8 18 15
1 9 60
```

### Test 2

```
1 1 2
2 2
0 0
10 7 2
9 8
0 0
0 8 2
1 9
```
