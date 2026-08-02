# DP: Coin Change

- **Domain:** ai
- **Difficulty:** Hard
- **Max Score:** 60
- **Success Ratio:** 0.8466828857490409
- **Total Submissions:** 21374
- **Solved Count:** 18097
- **URL:** https://www.hackerrank.com/challenges/ctci-coin-change

## Problem Statement

Given a number of dollars and an array of denominations of coins, determine how many ways you can make change.  For example, making change for $n = 12$ dollars from coin denominations $coins = [1,2,5,10]$, there are $15$ ways to make change:  

```
1 1 1 1 1 1 1 1 1 1 1 	1 1 5 5			1 1 1 1 1 1 1 5
1 1 1 1 1 1 1 1 1 1 2	2 5 5
1 1 1 1 1 1 1 1 2 2	1 1 10
1 1 1 1 1 1 2 2 2	2 10
1 1 1 1 2 2 2 2		2 2 2 1 5
1 1 2 2 2 2 2       	2 2 1 1 1 5
2 2 2 2 2 2          	2 1 1 1 1 1 5
```
**Hints:**		

- You can solve this problem recursively, but you must optimize your solution to eliminate [overlapping subproblems](http://en.wikipedia.org/wiki/Overlapping_subproblem) using [Dynamic Programming](http://en.wikipedia.org/wiki/Dynamic_programming) if you wish to pass all test cases. More specifically, think of ways to store the checked solutions and use the stored values to avoid repeatedly calculating the same values.
* Think about the degenerate cases:  
   - How many ways can you make change for $0$ dollars? 
   - How many ways can you make change for less than $0$ dollars if you have no coins?
* If you are having trouble defining the storage for your precomputed values, then think about it in terms of the base case $(n = 0)$.

**Function Description**

Complete the function *makeChange* in the editor below.  It should return the integer representing the number of ways change can be made.

makeChange has the following parameter(s):

- *n*: an integer, the amount to change  
- *coins*: an array of integers representing coin denominations  

## Input Format

The first line contains two space-separated integers, $n$ and $m$, the amount to make change for and the number of denominations of coin.		
The second line contains $m$ space-separated integers describing the denominations of each $coins[i]$.

## Output Format

Print a single integer denoting the number of ways we can make change for $n$ dollars using an infinite supply of our $m$ types of coins.

**Sample Input 0**		

	4 3
	1 2 3 
    
**Sample Output 0**		

 	4
    
**Explanation 0**		
For $n = 4$ and $coins = \{1,2,3\}$ there are four solutions: 

1. $\{1,1,1,1\}$
2. $\{1,1,2\}$ 
3. $\{2,2\}$ 
4. $\{1,3\}$ 

Thus, we print $4$ on a new line.
    
**Sample Input 1**

    10 4
    2 5 3 6

**Sample Output 1**

	5
    
**Explanation 1**		
For $n = 10$ and $coins = \{2, 5, 3, 6\}$ there are five solutions: 

1. $\{2,2,2,2,2\}$
2. $\{2,2,3,3\}$
3. $\{2,2,6\}$
4. $\{2,3,5\}$
5. $\{5,5\}$

Thus, we print $5$ on a new line.

## Constraints

- $1 \le coins[i] \le 50$
- $1 \le n \le 250$
- $1 \le m \le 50$
- The list of coins contains $m$ distinct integers where each integer denotes the dollar value of a coin available in an infinite quantity.

## Sample Input

4 3
1 2 3

## Sample Output

4

## Explanation

For  and  there are four solutions:

-

-

-

-

Thus, we print  on a new line.

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
