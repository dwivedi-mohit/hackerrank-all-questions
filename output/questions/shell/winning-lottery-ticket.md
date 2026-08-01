# Winning Lottery Ticket

- **Domain:** shell
- **Difficulty:** Medium
- **Max Score:** 40
- **Success Ratio:** 0.32765691249044276
- **Total Submissions:** 14387
- **Solved Count:** 4714
- **URL:** https://www.hackerrank.com/challenges/winning-lottery-ticket

## Problem Statement

The SuperBowl Lottery is about to commence, and there are several lottery tickets being sold, and each ticket is identified with a ticket ID. In one of the many winning scenarios in the Superbowl lottery, a winning pair of tickets is:

- Concatenation of the two ticket IDs in the pair, in any order, contains each digit from $0$ to $9$ at least once.

For example, if there are $2$ distinct tickets with ticket ID $129300455$ and $56789$, $(129300455, 56789)$ is a winning pair. 

NOTE: The ticket IDs can be concantenated in any order. Digits in the ticket ID can occur in any order. 

Your task is to find the number of winning pairs of distinct tickets, such that concatenation of their ticket IDs (in any order) makes for a winning scenario. Complete the function `winningLotteryTicket` which takes a string array of ticket IDs as input, and return the number of winning pairs. 



## Input Format

The first line contains $n$ denoting the total number of lottery tickets in the super bowl.  
Each of the next $n$ lines contains a string, where string on a $i^{th}$ line denotes the ticket id of the $i^{th}$ ticket.

## Output Format

Print the number of pairs in a new line.

## Constraints

- $1 \leq n \leq 10^{6}$
- $1 \leq$ length of $\text{ticket_i}$ $\leq 10^{6}$
- sum of lengths of all $\text{ticket_i} \leq 10^{6}$
- Each ticket id consists of digits from $[0 , 9]$

## Sample Input

5
129300455
5559948277
012334556
56789
123456879

## Sample Output

5

## Explanation

Pairs of distinct tickets that make for a winning scenario are :

  Ticket ID 1
  Ticket ID 2
  Winning Pair

Notice that each winning pair has digits from  to  atleast once, and the digits in the ticket ID can be of any order. Thus, the number of winning pairs is .
