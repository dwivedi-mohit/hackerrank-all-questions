# Is Fibo

- **Domain:** ai
- **Difficulty:** Medium
- **Max Score:** 20
- **Success Ratio:** 0.792156862745098
- **Total Submissions:** 45135
- **Solved Count:** 35754
- **URL:** https://www.hackerrank.com/challenges/is-fibo

## Problem Statement

You are given an integer, $N$. Write a program to determine if $N$ is an element of the _Fibonacci sequence_.  

The first few elements of the Fibonacci sequence are $0,1,1,2,3,5,8,13, \cdots$. A Fibonacci sequence is one where every element is a sum of the previous two elements in the sequence. The first two elements are $0$ and $1$. 

Formally:   
$$\begin{align*}
fib_{0} &= 0 \\\  
fib_{1} &= 1 \\\  
\vdots \\\
fib_{n} &= fib_{n-1} + fib_{n-2} \forall n > 1
\end{align*}$$

**Function Description**   

Complete the *isFibo* function in the editor below.   

*isFibo* has the following parameters:   
- *int n:* the number to check   

**Returns**   
- *string:* either `IsFibo` or `IsNotFibo`

**Input Format**  
The first line contains $t$, number of test cases.   
$t$ lines follow. Each line contains an integer $n$.

**Constraints**  
$1 \le t \le 10^5$  
$1 \le n \le 10^{10}$

**Sample Input**  
<pre>
STDIN	Function
-----	--------
3		t = 3
5		n = 5
7		n = 7
8		n = 8
</pre>

**Sample Output**  

	IsFibo
    IsNotFibo
    IsFibo

**Explanation**  
$5$ is a Fibonacci number given by $\text{fib}_5  = 3 + 2$  
$7$ is not a Fibonacci number  
$8$ is a Fibonacci number given by $\text{fib}_6  = 5 + 3$  

**Time Limit**  
The time limit for this challenge is given [here](https://www.hackerrank.com/environment).   

## Input Format

  

## Output Format

  

## Constraints

  

## Sample Input

STDIN   Function
-----   --------
3       t = 3
5       n = 5
7       n = 7
8       n = 8

## Sample Output

IsFibo
IsNotFibo
IsFibo

## Explanation

is a Fibonacci number given by

 is not a Fibonacci number

 is a Fibonacci number given by

Time Limit

The time limit for this challenge is given here.
