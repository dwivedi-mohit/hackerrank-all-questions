# Dorsey Thief

- **Domain:** c
- **Difficulty:** Advanced
- **Max Score:** 85
- **Success Ratio:** 0.6138939670932358
- **Total Submissions:** 2735
- **Solved Count:** 1679
- **URL:** https://www.hackerrank.com/challenges/dorsey-thief

## Problem Statement

Mr. Dorsey Dawson recently stole $X$ grams of gold from ACME Jewellers. He is now on a train back home. To avoid getting caught by the police, he has to convert all the gold he has into paper money. He turns into a salesman and starts selling the gold in the train.  

There are $N$ passengers who have shown interest in buying the gold. The $i^{th}$ passenger agrees to buy $a_i$ grams of gold by paying $v_i$ dollars. Dawson wants to escape from the police and also maximize the profit. Can you help him maximize the profit?

**Note**: The $i^{th}$ passenger would buy **exactly** $a_i$ grams if the transaction is successful.



## Input Format

The first line contains two space separated integers, $N$ and $X$,  where $N$ is the number of passengers who agreed to buy and $X$ is the stolen amount of gold (in grams).  
$N$ lines follow. Each line contains two space separated integers - $v_i$ and $a_i$, where $v_i$ is the the value which the $i^{th}$ passenger has agreed to pay in exchange for $a_i$ grams of gold.  



## Output Format

If it's possible for Dorsey to escape, print the maximum profit he can enjoy, otherwise print `Got caught!`.  



## Constraints

+ $1 \le X \le 5000$  
+ $1 \le N \le 10^6$  
+ all $v_i$'s and $a_i$'s are less than or equal to $10^6$ and greater than $0$.  

## Sample Input

4 10
460 4
590 6
550 5
590 5

## Sample Output

1140

## Explanation

Selling it to passengers buying 4 grams and 6 grams would lead to 1050 dollars whereas selling it to passengers buying 5 grams gold would lead to 1140 dollars. Hence the answer.
