# Mirko at the Construction Site

- **Domain:** algorithms
- **Difficulty:** Advanced
- **Max Score:** 100
- **Success Ratio:** 0.6753069577080492
- **Total Submissions:** 733
- **Solved Count:** 495
- **URL:** https://www.hackerrank.com/challenges/mirko-at-construction-site

## Problem Statement

Mirko is monitoring a construction site. He monitors $N$ buildings enumerated from $1$ to $N$, starting from the left. For each building, he knows the current number of floors and the number of floors built on each day. He needs to know the answer to $Q$ queries. The answer to each query is the index of the tallest building after $T$ days, as defined by the query. Your task is to help Mirko find the answers to these queries.  

## Input Format

The first line consists of the numbers $N$ and $Q$. The second line consists of $N$ integers, where the $i^{th}$ integer represents the initial height of the $i^{th}$ building. The third line consists of $N$ integers, where the $i^{th}$ integer represents the number of floors erected in one day for the $i^{th}$ building. The following $Q$ lines consist of the integer, $T$, representing the day in the query.  


## Output Format

For each query, output one number which represents the index of the tallest building after $T$ days. If there is more than one building, output the building with the *greatest* index in the input array (with indexes starting at 1).

**Constraints**  

- $ 1 \le N \le 10^5$  
- $1 \le Q \le 10^5$   
- Every other integer in the input will fit in a 32-bit signed integer. And they will be non-negative integers.

## Constraints

-

-

- Every other integer in the input will fit in a 32-bit signed integer. And they will be non-negative integers.

## Sample Input

3 6
7 5 1
1 2 3
0
1
2
3
4
5

## Sample Output

1
2
2
3
3

## Explanation

Query #1: The height at the end of the  day will be . Here, the  building is the tallest.

Query #2: The height at the end of the  day will be . Here, the  building is the tallest.

Query #3:  The height at the end of  day will be . Here, the  and  buildings are the tallest, while the  is the larger index.

Query #4:  The height at the end of  day will be . Here, the  building is the tallest.

Query #5:  The height at the end of  day will be . Here, the  and  buildings are the tallest, while the  is the larger index.

Query #6:  The height at the end of  day will be . Here, the  building is the tallest.

Tested by Ray Williams Robinson Valiente
