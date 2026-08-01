# Queues: A Tale of Two Stacks

- **Domain:** algorithms
- **Difficulty:** Medium
- **Max Score:** 30
- **Success Ratio:** 0.9022502763810135
- **Total Submissions:** 84123
- **Solved Count:** 75900
- **URL:** https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks

## Problem Statement

A [queue](https://en.wikipedia.org/wiki/Queue_(abstract_data_type)) is an abstract data type that maintains the order in which elements were added to it, allowing the oldest elements to be removed from the front and new elements to be added to the rear. This is called a *First-In-First-Out* (FIFO) data structure because the first element added to the queue (i.e., the one that has been waiting the longest) is always the first one to be removed.

A basic queue has the following operations:

- *Enqueue*: add a new element to the end of the queue.
- *Dequeue*: remove the element from the front of the queue and return it.

In this challenge, you must first implement a queue using *two stacks*. Then process $q$ queries, where each query is one of the following $3$ types: 

1. `1 x`: Enqueue element $x$ into the end of the queue.
2. `2`: Dequeue the element at the front of the queue.
3. `3`: Print the element at the front of the queue.

For example, a series of queries might be as follows:  


![image](https://s3.amazonaws.com/hr-assets/0/1529528638-d7f1fca7bc-twostacks.png)

**Function Description**

Complete the *put*, *pop*, and *peek* methods in the editor below.  They must perform the actions as described above.

## Input Format

The first line contains a single integer, $q$, the number of queries.   	

Each of the next $q$ lines contains a single query in the form described in the problem statement above. All queries start with an integer denoting the query $type$, but only query $1$ is followed by an additional space-separated value, $x$, denoting the value to be enqueued.

## Output Format

For each query of type $3$, return the value of the element at the front of the fifo queue on a new line. 

## Constraints

- $1 \le q \le 10^5$  
- $1 \le type \le 3$  
- $1 \le |x| \le 10^9$  
- It is guaranteed that a valid answer always exists for each query of types $2$ and $3$.


## Sample Input

1 42
2
1 14
3
1 28
3
1 60
1 78
2
2

## Sample Output

14
