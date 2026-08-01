# Chandrima and XOR

- **Domain:** shell
- **Difficulty:** Hard
- **Max Score:** 60
- **Success Ratio:** 0.8755274261603375
- **Total Submissions:** 474
- **Solved Count:** 415
- **URL:** https://www.hackerrank.com/challenges/chandrima-and-xor

## Problem Statement

Chandrima likes the XOR operation very much and keeps finding and solving related problems. One day she comes across a problem and gets stuck on it, which makes her sad. You being her friend decide to help her out by writing a code for the same. 

Consider a list of all natural numbers. Now you remove all numbers whose binary representation has at least two consecutive $1$ bits, from the list, hence generating a new list having elements $1,2,4,5,8,...$ and so on. Now you are given $N$ numbers from this newly generated list. You have to find the XOR of these numbers.

**Input Format**  
The first line has an integer $N$, denoting the number of integers in list $A$.  
The next line contains $N$ space-separated integers. $A_i$ represents the $A_i^{\text{th}}$ number of the generated list. Since the answer can be very large, print the answer modulo $(10^9+7)$.

**Output Format**  
Just print one line containing the final answer.  


**Constraints**  
$1 \le N \le 5\cdot 10^5$  
$1 \le A_i \le 10^{18}$

**Sample Input 1**  

    3
    1 2 3

**Sample Output 1**  

    7

**Sample Input 2**  

    3
    1 3 4

**Sample Output 2**  

    0

**Explanation**  

*Sample 1:*  
The values to be considered are $1,2,4$, and the answer is $1\oplus2\oplus4 = 7$.

*Sample 2:*  
The values to be considered are $1,4,5$, and the answer is $1\oplus4\oplus5 = 0$.


## Input Format

The first line has an integer , denoting the number of integers in list .

The next line contains  space-separated integers.  represents the  number of the generated list. Since the answer can be very large, print the answer modulo .

## Output Format

Just print one line containing the final answer.

## Sample Input

3
1 2 3

## Sample Output

7

## Explanation

Sample 1:

The values to be considered are , and the answer is .

Sample 2:

The values to be considered are , and the answer is .
