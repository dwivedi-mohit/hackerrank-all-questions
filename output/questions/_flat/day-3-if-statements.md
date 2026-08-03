# Day 3: If-Else Statements!

---

| Field | Value |
|---|---|
| **Slug** | `day-3-if-statements` |
| **Contest** | 30-days-of-code |
| **Difficulty** | Easy |
| **Score** | 30 |
| **URL** | https://www.hackerrank.com/challenges/day-3-if-statements |

---

## Problem Statement

Welcome to Day 3! Check out [a review of if-else statements here](https://youtu.be/07Yum5sXxT8), or just jump right into the problem. 

Using "if-else" you can perform decision making in your code. See the flowchart below (taken from wikipedia):

<img src="https://s3.amazonaws.com/hr-challenge-images/13689/1446563087-4ec019a919-332px-If-Then-Else-diagram.svg.png" title="332px-If-Then-Else-diagram.svg.png" />

This problem will test your knowledge on "if-else" statements.

Given an integer $N$ as input, check the following:

* If $N$ is odd, print *"Weird"*.
* If $N$ is even and, in between the range of 2 and 5(inclusive), print *"Not Weird"*.
* If $N$ is even and, in between the range of 6 and 20(inclusive), print *"Weird"*.
* If $N$ is even and $N> 20$, print *"Not Weird"*.

We have given you partially completed code in the editor, complete it to solve the problem.

## Input Format

There is a single line of input: integer $N$.

**Constraints**  
$ 1 \le N \le 100$

## Output Format

Print *"Weird"* if the number is weird. Otherwise, print *"Not Weird"*. Do not print the quotation marks.

**Sample Input 1**
	
    3
**Sample Output 1**
	
    Weird
<br/>
**Explanation**  
*N*=3, is odd hence the its a Weird Number.

**Sample Input 2**
	
    24
**Sample Output 2**
	
    Not Weird
<br/>
**Explanation**  
*N*=24, is >20 hence its not a Weird Number.
