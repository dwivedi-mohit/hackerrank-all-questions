# The Matchstick Experiment

- **Domain:** algorithms
- **Difficulty:** Medium
- **Max Score:** 40
- **Success Ratio:** 0.5240384615384616
- **Total Submissions:** 208
- **Solved Count:** 109
- **URL:** https://www.hackerrank.com/challenges/matchstick-experiment

## Problem Statement

In an $n \times m$ grid, $2 \cdot n \cdot m - n - m$ matchsticks are placed at the boundaries between cells. For example, if $n = 5$ and $m = 9$, the $2 \cdot 5 \cdot 9 - 5 - 9 = 76$ matchsticks are placed in the following way:


![image](https://s3.amazonaws.com/hr-challenge-images/0/1483127672-02c43b13b2-Matchstickexperiment1.png)

<!-- https://s3.amazonaws.com/hr-challenge-images/0/1482774196-8139dcea71-Matchstickexperiment1.png -->

**The Experiment**

<!-- 1. Remove each matchstick $i$ that has a certain probability of removal, $p$, from the $2 \cdot n \cdot m - n - m$ matchsticks. -->

1. For each of the $2\cdot n\cdot m - n - m$ matchsticks, remove it with probability $p$.  

2. We define a *connected component* to be a maximal set of cells not isolated from one another by matchsticks. We calculate our $score$ as the number of connected components in the grid with $\le 3$ cells, divided by $n \cdot m$. 

For example, suppose our grid looks like this after performing the first step:


![image](https://s3.amazonaws.com/hr-challenge-images/0/1483127799-da90208aa9-Matchstickexperiment2.png)

<!-- https://s3.amazonaws.com/hr-challenge-images/0/1482774211-8d7fdda32a-Matchstickexperiment2.png -->

To calculate our $score$, we need to first find the number of connected components having $\le 3$ cells. The diagram below counts all such components consisting of $\le 3$ connected cells:


![image](https://s3.amazonaws.com/hr-challenge-images/0/1483128069-3c0037e1f7-Matchstickexperiment3.png)
<!-- https://s3.amazonaws.com/hr-challenge-images/0/1482774276-e1f1c57162-Matchstickexperiment3.png -->

As you can see, there are $16$ connected components of size $\le 3$. From this, we perform the following calculation:
$$score = \frac{(\text{connected components with size } \le 3)}{n \cdot m} = \frac{16}{45} \approx 0.35555555$$

----

You are given $q$ queries where each query consists of $n$, $m$, and $p$. For each query, find and print the *expected* value of $score$ on a new line.

**Need Help?** Check out [this learning aid](http://www.cs.princeton.edu/courses/archive/fall06/cos341/handouts/variance-notes.pdf) explaining some important properties of *expected values*.

## Input Format

The first line contains an integer, $q$, denoting the number of queries. 	
Each of the $q$ subsequent lines contains three space-separated integers describing the respective values of integer $n$, integer $m$, and real number $p$.

## Output Format

For each query, print a single real number on a new line denoting the answer to the query. Any answer having an absolute error within $10^{-9}$ of the true answer is acceptable.  

## Constraints

+ $0 \le p \le 1$ 
+ $1 \le q, n, m \le 10^5$  
+ $p$ is a real number scaled to two decimal places (e.g., $1.23$).

**Subtask**  

+ For $\text{40%}$ of the total score, $q, n, m \le 300$  

## Sample Input

2
2 2 0.50
2 3 0.75

## Sample Output

0.4375000000
0.0810546875000

## Explanation

We can verify our answer by performing several brute-force simulations of the experiment and then averaging the scores.
