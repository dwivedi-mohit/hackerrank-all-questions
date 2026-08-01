# Sherlock's Array Merging Algorithm

- **Domain:** java
- **Difficulty:** Hard
- **Max Score:** 60
- **Success Ratio:** 0.7658428390367554
- **Total Submissions:** 3156
- **Solved Count:** 2417
- **URL:** https://www.hackerrank.com/challenges/sherlocks-array-merging-algorithm

## Problem Statement

Watson gave Sherlock a collection of arrays $V$. Here each $V_i$ is an array of variable length. It is guaranteed that if you merge the arrays into one single array, you'll get an array, $M$, of $n$ distinct integers in the range $[1,n]$. 

Watson asks Sherlock to merge $V$ into a sorted array. Sherlock is new to coding, but he accepts the challenge and writes the following algorithm:

* $M \gets \textrm{[ ]}$ (an empty array).

* $k \gets $ number of arrays in the collection $V$.

* While there is at least one non-empty array in $V$:
	* $T \gets \textrm{[ ]}$ (an empty array) and $i \gets 1$.
    * While $i \le k$:
        * If $V_i$ is not empty:
    	    * Remove the first element of $V_i$ and push it to $T$.
        * $i \gets i + 1$.
        
    * While $T$ is not empty:
    	* Remove the minimum element of $T$ and push it to $M$.

* Return $M$ as the *output*.

Let's see an example. Let V be $\{[3,5], [1], [2,4]\}$.


![image](https://s3.amazonaws.com/hr-assets/0/1487236255-0a10b84d71-sherlock4.png)

The image below demonstrates how Sherlock will do the merging according to the algorithm:


![image](https://s3.amazonaws.com/hr-assets/0/1487236775-99cec837ef-sherlock7.png)



Sherlock isn't sure if his algorithm is correct or not. He ran Watson's *input*, $V$, through his pseudocode algorithm to produce an *output*, $M$, that contains an array of $n$ integers. However, Watson forgot the contents of $V$ and only has Sherlock's $M$ with him! Can you help Watson reverse-engineer $M$ to get the original contents of $V$?

Given $m$, find the number of different ways to create collection $V$ such that it produces $m$ when given to Sherlock's algorithm as *input*. As this number can be quite large, print it modulo $10^9+7$.

**Notes:**

* Two collections of arrays are *different* if one of the following is *true*:
	* Their sizes are different.
    * Their sizes are the same but at least one array is present in one collection but not in the other.
   
* Two arrays, $A$ and $B$, are different if one of the following is *true*:
	* Their sizes are different.
    * Their sizes are the same, but there exists an index $i$ such that $a_i \neq b_i$.

## Input Format

The first line contains an integer, $n$, denoting the size of array $M$.		
The second line contains $n$ space-separated integers describing the respective values of $m_0, m_1, \ldots, m_{n-1}$.

## Output Format

Print the number of different ways to create collection $V$, modulo $10^9+7$.

## Constraints

* $1 \le n \le 1200$    
* $1 \le m_i \le n$    

## Sample Input

3
1 2 3

## Sample Output

4

## Explanation

There are four distinct possible collections:

-

-

-

- .

Thus, we print the result of  as our answer.
