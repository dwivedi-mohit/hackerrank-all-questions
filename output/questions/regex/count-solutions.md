# Count Solutions

- **Domain:** regex
- **Difficulty:** Medium
- **Max Score:** 40
- **Success Ratio:** 0.33661971830985915
- **Total Submissions:** 710
- **Solved Count:** 239
- **URL:** https://www.hackerrank.com/challenges/count-solutions

## Problem Statement

Eric has four integers $a$, $b$, $c$, and $d$. 

Instantly, he wondered how many pairs of _integers_, $(x, y)$, satisfy the following equation:

$$x^2 + y^2 = (x \times a) + (y \times b)$$

where $1 \le x \le c$ and $1 \le y \le d$. 

Find and print the number of pairs that satisfy the above equation.  

## Input Format

The first line contains an integer $q$, the number of queries.  
$q$ lines follow, each containing four integers, $a$, $b$, $c$, and $d$, in that order.  

## Output Format

For each test case, print one line, the number of pairs $(x,y)$ that are valid solutions to Eric's equation.   

## Constraints

+ $1 \le q \le 10$  
+ $1 \le a,b,c,d \le 10^5$

## Sample Input

1
1 1 1 1

## Sample Output

1

## Explanation

The solution to , where  and  is , .
