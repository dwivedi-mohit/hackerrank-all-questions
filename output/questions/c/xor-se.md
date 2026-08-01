# Xor-sequence

- **Domain:** c
- **Difficulty:** Medium
- **Max Score:** 40
- **Success Ratio:** 0.5527360243202162
- **Total Submissions:** 23684
- **Solved Count:** 13091
- **URL:** https://www.hackerrank.com/challenges/xor-se

## Problem Statement

An array, $A$, is defined as follows: 

* $A_0=0$
* $A_x=A_{x-1} ⊕ x$ for $x>0$, where $⊕$ is the symbol for [XOR](https://en.wikipedia.org/wiki/Exclusive_or)

You will be given a left and right index $l \ r$.  You must determine the XOR sum of the segment of $A$ as $A[l]⊕A[l+1]⊕...⊕A[r-1]⊕A[r]$. 

For example, $A=[0,1,3,0,4,1,7,0,8]$.  The segment from $l=1$ to $r=4$ sums to $1 \oplus 3 \oplus 0 \oplus 4 =6$. 

Print the answer to each question.

**Function Description**  

Complete the *xorSequence* function in the editor below.  It should return the integer value calculated.  

xorSequence has the following parameter(s):  

- *l*: the lower index of the range to sum  
- *r*: the higher index of the range to sum  

## Input Format

The first line contains an integer $q$, the number of questions.  
Each of the next $q$ lines contains two space-separated integers, $l[i]$ and $r[i]$, the inclusive left and right indexes of the segment to query.



## Output Format

On a new line for each test case, print the *XOR-Sum* of $A$'s elements in the inclusive range between indices $l[i]$ and $r[i]$.

## Constraints

 $1 \le q \le 10^5$  
 $1 \le l[i] \le r[i] \le 10^{15}$  

## Sample Input

3
2 4
2 8
5 9

## Sample Output

7
9
15

## Explanation

The beginning of our array looks like this:

Test Case 0:

Test Case 1:

Test Case 2:
