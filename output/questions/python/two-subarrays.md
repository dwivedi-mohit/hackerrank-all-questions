# Two Subarrays

- **Domain:** python
- **Difficulty:** Expert
- **Max Score:** 70
- **Success Ratio:** 0.7037492317148125
- **Total Submissions:** 1627
- **Solved Count:** 1145
- **URL:** https://www.hackerrank.com/challenges/two-subarrays

## Problem Statement

Consider an array, $A=a_0, a_1, \ldots, a_{n-1}$, of $n$ integers. We define the following terms:

- **Subsequence**		
    A subsequence of $A$ is an array that's derived by removing zero or more elements from $A$ without changing the order of the remaining elements. Note that a subsequence may have zero elements, and this is called *the empty subsequence*.
    
- **Strictly Increasing Subsequence**		
    A non-empty subsequence is *strictly increasing* if every element of the subsequence is larger than the previous element. 

- **Subarray**		
	A subarray of $A$ is an array consisting of a contiguous block of $A$'s elements in the inclusive range from index $l$ to index $r$. Any subarray of $A$ can be denoted by $A[l,r]= a_l, a_{l+1}, \ldots, a_{r}$.


The diagram below shows all possible subsequences and subarrays of $A=[2,1,3]$:	


![image](https://s3.amazonaws.com/hr-challenge-images/0/1485242068-78c480cd00-subarray6.png)

We define the following functions:

* $sum(l,r)= a_l + a_{l+1} + \ldots + a_r$
* $inc(l,r)$ = the maximum sum of some *strictly increasing subsequence* in subarray $A[l,r]$
* $f(l, r)=sum(l,r) - inc(l,r)$


We define the *goodness*, $g$, of array $A$ to be:

$$g = max\ f(l,r)\ \text{for}\ 0 \leq l \leq r < n  $$

In other words, $g$ is the maximum possible value of $f(l,r)$ for all possible subarrays of array $A$. 

Let $m$ be the length of the smallest subarray such that $f(l,r)=g$. Given $A$, find the value of $g$ as well as the number of subarrays such that $r-l+1=m$ and $f(l,r)=g$, then print these respective answers as space-separated integers on a single line.




## Input Format

The first line contains an integer, $n$, denoting number of elements in array $A$.	
The second line contains $n$ space-separated integers describing the respective values of $a_0, a_1, \ldots, a_{n-1}$.

## Output Format

Print two space-seperated integers describing the respective values of $g$ and the number of subarrays satisfying $r-l+1=m$ and $f(l,r)=g$.

## Constraints

* $1\leq n \leq 2 \cdot 10^5 $
* $ -40 \leq a_i \leq 40 $

**Subtasks** 

For the $20 \%$ of the maximum score:

* $1\leq n \leq 2000 $

* $-10 \leq a_i \leq 10 $

For the $60 \%$ of the maximum score:

* $1\leq n \leq 10^5 $

* $-12\leq a_i \leq 12 $

## Sample Input

3
2 3 1

## Sample Output

1 1

## Explanation

The figure below shows how to calculate :

 is the length of the smallest subarray satisfying . From the table, we can see that . There is only one subarray of length  such that .
