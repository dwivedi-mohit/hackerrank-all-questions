# Real Estate Broker

- **Domain:** algorithms
- **Difficulty:** Hard
- **Max Score:** 60
- **Success Ratio:** 0.7080714106110133
- **Total Submissions:** 3977
- **Solved Count:** 2816
- **URL:** https://www.hackerrank.com/challenges/real-estate-broker

## Problem Statement

You are a real estate broker in ancient Knossos. You have $m$ unsold houses, and each house $j$ has an area, $x_j$, and a minimum price, $y_j$. You also have $n$ clients, and each client $i$ wants a house with an area greater than $a_i$ and a price less than or equal to $p_i$.

Each client can buy *at most* one house, and each house can have *at most* one owner. What is the maximum number of houses you can sell?


## Input Format

The first line contains two space-separated integers describing the respective values of $n$ (the number of clients) and $m$ (the number of houses). 		
Each line $i$ of the $n$ subsequent lines contains two space-separated integers describing the respective values of $a_i$ and $p_i$ for client $i$.		
Each line $j$ of the $m$ subsequent lines contains two space-separated integers describing the respective values of $x_j$ and $y_j$ for house $j$.

## Output Format

Print a single integer denoting the maximum number of houses you can sell.

## Constraints

* $ 1 \le n,m \le 1000 $
* $ 1 \le a_i, p_i \le 10^9 $, where $0 \le i \lt n$.
* $ 1 \le x_j, y_j \le 10^9 $, where $0 \le j \lt m$.

## Sample Input

3 3
5 110
9 500
20 400
10 100
2 200
30 300

## Sample Output

2

## Explanation

Recall that each client  is only interested in some house  where  and . The diagram below depicts which clients will be interested in which houses:

- Client  will be interested in house  because it has more than  units of space and costs less than . Both of the other houses are outside of this client's price range.

- Client  will be interested in houses  and , as both these houses have more than  units of space and cost less than . They will not be interested in the remaining house because it's too small.

- Client  will be interested in house  because it has more than  units of space and costs less than . They will not be interested in the other two houses because they are too small.

All three clients are interested in the same two houses, so you can sell at most two houses in the following scenarios:

- Client  buys house  and client  buys house .

- Client  buys house  and client  buys house .

- Client  buys house  and client  buys house .

Thus, we print the maximum number of houses you can sell, , on a new line.
