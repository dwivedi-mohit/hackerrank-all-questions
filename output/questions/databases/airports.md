# Airports

- **Domain:** databases
- **Difficulty:** Expert
- **Max Score:** 100
- **Success Ratio:** 0.8646153846153846
- **Total Submissions:** 1950
- **Solved Count:** 1686
- **URL:** https://www.hackerrank.com/challenges/airports

## Problem Statement

Airports are being built on a straight road according to a new construction plan. For convenience, imagine a number line on which at different points airports can be positioned. Because a plane can't take off and start landing immediately, there will be flight between two airports in locations $x$ and $y$ if and only if $|x - y| \geq d$, where $d$ is a constant.

Changing the position of an airport from $x$ to $y$ costs $|x - y|$. The cost to fix a certain plan is the minimum total cost of changing the positions of airports. After the changes, it should be possible to travel between any pair of airports, possibly taking flights through some intermediate airports. Note that it's possible that two airports have the same initial position, and this can be the case  after changes too.

On $i^{th}$ day, a plan to build a new airport with position $x_i$ is announced. On each day that a new airport is announced, print the smallest cost to fix the set of airports announced so far . Note that you should not change the positions of any airports, just calculate the cost to do it.


![image](https://s3.amazonaws.com/hr-assets/0/1510213617-88120a0409-nl1-23.jpg)


## Input Format

Input contains multiple queries.  
The first line consists of an integer $q$ which is the number of queries. Each query is given as follows.  
The first line of each query contains two integers $n$ and $d$, the number of days, and the minimum distance respectively.    
The second line of each test case contains $n$ space-separated integers $x_i$ denoting the position of the airport that was announced on $i^{th}$ day.

## Output Format

Print one line for each query.   
A line for a query with $n$ airports should have $n$ numbers on it where the $i^{th}$ one should be the minimum cost to fix airports in positions $x_1, x_2, \cdots, x_i$.

## Constraints

- $3 \leq n \leq 2 \times 10^5$
- $|x_i| \leq 10^8$
- $0 \leq d \leq 10^8$
- the sum of $n$ over all test cases in a file will not exceed $2 \cdot 10^5$

## Sample Input

1
3 1
0 0 0

## Sample Output

0 1 1

## Explanation

The answer for a single airport is always zero. When we have many airports in the same position, it's enough to move only one of them to satisfy the condition from the statement.
