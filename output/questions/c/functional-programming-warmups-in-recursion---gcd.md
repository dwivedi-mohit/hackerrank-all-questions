# Computing the GCD

- **Domain:** c
- **Difficulty:** Easy
- **Max Score:** 2
- **Success Ratio:** 0.9535647861128332
- **Total Submissions:** 16130
- **Solved Count:** 15381
- **URL:** https://www.hackerrank.com/challenges/functional-programming-warmups-in-recursion---gcd

## Problem Statement

**Objective** <Br>
In this challenge, we learn how to compute GCD using the Euclidean algorithm.

**Resources** <br>
Here's a helpful video on the topic:   
[(iframe youtube JUzYl1TYMcU 600 350)] 
 

Given two integers, $x$ and $y$, a recursive technique to find their GCD is the [Euclidean Algorithm](http://people.cis.ksu.edu/~schmidt/301s12/Exercises/euclid_alg.html). 

The algorithm states that, for computing the GCD of two positive integers $x$ and $y$, if $x$ and $y$ are equal, $GCD(x,y) = x$. Otherwise $GCD(x,y) = GCD(x-y,y)$ if $x > y$. There are a few optimizations that can be made to the above logic to arrive at a more efficient implementation.

**Task** <br>
Given the starter code, you need to complete a function body that returns the GCD of two given integers $x$ and $y$. <br>
The task of reading in input and printing the output will be handled by us.  
 
**Programming Language Support**  
At this point of time, we have a template for Scala. This means that we provide the code required to accept the input and display the output.  


## Input Format

One line of input containing $2$ space separated integers.  

## Output Format

Output one integer, the GCD of the two given numbers.  

## Constraints

$1 \le a,b \le 10^6$   

## Sample Input

1 5

## Explanation

Sample Return Values:

GCD(1,5) = 1
GCD(10,100) = 10
GCD(22,131) = 1
