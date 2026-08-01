# Academy Surveillance

- **Domain:** regex
- **Difficulty:** Advanced
- **Max Score:** 80
- **Success Ratio:** 0.84
- **Total Submissions:** 125
- **Solved Count:** 105
- **URL:** https://www.hackerrank.com/challenges/surveillance

## Problem Statement

The Academy is a school where each common area is laid out on an $m \times n$ grid and each cell in the grid is $1$ meter by $1$ meter. Danielle is their new head of security, and she wants to place a surveillance camera along every square meter of each common area. Because the school doesn't have enough money in their security budget to do this, she decides to further restrict camera placement according to the following rules:

- Each cell can contain *at most* $1$ camera.
- Every $3 \times 3$ subgrid of a common area *must* have exactly $2$ cameras.

Given the values of $m$ and $n$ for $c$ common areas, determine the number of ways Danielle can install cameras in each common area according to the rules above. Then, for each common area, print the number of ways she can install these cameras on a new line. As these values may be quite large, your answer must be modulo $10^9 + 7$.

## Input Format

The first line contains an integer, $c$, denoting the number of common areas to install cameras in. 	 
Each line $i$ of the $c$ subsequent lines contains two space-separated integers describing the respective values of $m$ and $n$ for a common area's grid.  

## Output Format

For each common area, print an integer denoting the number of ways Danielle can install the cameras according to the given rules, modulo $10^9 + 7$, on a new line.  

## Constraints

For $\text{20%}$ of the maximum score:   

+ $1 \le c \le 10$  
+ $3 \le m, n \le 15$  

For $\text{50%}$ of the maximum score:   

+ $1 \le c \le 100$  
+ $3 \le m, n \le 50$  

For $\text{100%}$ of the maximum score:   

+ $1 \le c \le 10^5$  
+ $3 \le m, n \le 1000$  



## Sample Input

2
3 3
3 4

## Sample Output

36
78

## Explanation

The diagram below depicts the number of ways to place cameras in a  grid:

As there are  ways to place cameras in this common area, we print the result of  on a new line.
