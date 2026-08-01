# Emma and sum of products

- **Domain:** ai
- **Difficulty:** Hard
- **Max Score:** 80
- **Success Ratio:** 0.5695876288659794
- **Total Submissions:** 388
- **Solved Count:** 221
- **URL:** https://www.hackerrank.com/challenges/emma-and-sum-of-products

## Problem Statement

Emma is really fond of integers and loves playing with them. Her friends were jealous, and to test her, one of them gave her a problem.  
Emma is given a list $A$ of $N$ integers and is asked a set of $Q$ queries. Each query is denoted by an integer $K$, for which you have to return the sum of product of all possible sublists having exactly $K$ elements.  
Emma has got stuck in this problem and you being her best friend have decided to help her write a code to solve it. Since the answers can be very large, print the answers modulo $100003$.

**Input Format**  
First line has an integer $N$, denoting the number of integers in list $A$. Next line contains $N$ space separated integers. The third line contains integer $Q$, and next $Q$ lines have a single integer $K$.

**Output Format**  
For each of the queries, print the corresponding answer in a new line.  

**NOTE** Sublist here refers to selecting $K$ elements from a list of $N$ elements. There will be $N \choose K$ ways to do that, it doesn't matter if two elements are same.

**Constraints**  
$1 \le N \le 3\times10^4$  
$1 \le A_i \le 10^5$  
$1 \le Q \le N$  
$1 \le K \le N$  

**Sample Input #00**  

    3
    1 2 3
    2
    1
    2

**Sample Output #00**  

    6
    11

**Sample Input #01**  

    3
    1 2 2
    1
    2

**Sample Output #01**  

    8

**Explanation**  

Sample #00:  
For $K=1$ possible sublists are $\{1\},\{2\},\{3\}$ so answer is $1+2+3 = 6$.  
For $K=2$ possible sublists are $\{1,2\},\{2,3\},\{3,1\}$ so answer is $(1\times2) + (2\times3) + (3\times1) = 2+6+3 = 11$.

Sample #01:  
For $K=2$ possible sublists are $\{1,2\},\{2,2\},\{2,1\}$ so answer is $(1\times 2) + (2\times2) + (2\times 1) = 2+4+2 = 8$.

## Input Format

First line has an integer , denoting the number of integers in list . Next line contains  space separated integers. The third line contains integer , and next  lines have a single integer .

## Output Format

For each of the queries, print the corresponding answer in a new line.

NOTE Sublist here refers to selecting  elements from a list of  elements. There will be  ways to do that, it doesn't matter if two elements are same.

## Constraints

Sample Input #00

3
1 2 3
2
1
2

Sample Output #00

6
11

Sample Input #01

3
1 2 2
1
2

Sample Output #01

8

## Explanation

Sample #00:

For  possible sublists are  so answer is .

For  possible sublists are  so answer is .

Sample #01:

For  possible sublists are  so answer is .
