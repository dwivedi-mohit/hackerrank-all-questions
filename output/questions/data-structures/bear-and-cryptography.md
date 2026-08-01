# Bear And Cryptography

- **Domain:** data-structures
- **Difficulty:** Advanced
- **Max Score:** 100
- **Success Ratio:** 0.5308310991957105
- **Total Submissions:** 373
- **Solved Count:** 198
- **URL:** https://www.hackerrank.com/challenges/bear-and-cryptography

## Problem Statement

Limak is a little bear who loves school. Today was his first lesson in cryptography, and the teacher assigned some difficult homework&mdash;to find any number with exactly $K$ divisors. Limak wants to go the extra mile and find the biggest possible number; however, his teacher explained that there are arbitrarily large numbers with this property. 

To give this little bear a more achievable challenge, the teacher advised him to consider only numbers not greater than $N$. 

Given $N$ and $K$, what is the largest number Limak can find?

## Input Format

The first line contains an integer, $T$ (the number of test cases).  
The $T$ subsequent lines of test cases each contain two space-separated integers, $N$ and $K$, respectively.




## Output Format

For each test case, print the biggest number Limak can find on a new line. Print $-1$ if no such number exists.

## Constraints

* $1 \le T \le 50$  
* $1 \le N \le 10^{12}$  
* $1 \le K \le 40$

## Sample Input

15 3
15 4
15 5

## Sample Output

15
-1

## Explanation

As each test case uses , here are the numbers ranging from  to  and their divisors:

 is evenly divisible by  numbers (, , , and ).

 is evenly divisible by  numbers (, , , and ).

 is evenly divisible by  numbers ( and ).

 is evenly divisible by  numbers (, , , , , and ).

 is evenly divisible by  numbers ( and ).

 is evenly divisible by  numbers (, , , and ).

 is evenly divisible by  numbers (, , and ).

 is evenly divisible by  numbers (, , , and ).

 is evenly divisible by  numbers ( and ).

 is evenly divisible by  numbers (, , and ).

 is evenly divisible by  numbers ( and ).

 is evenly divisible by  numbers (, , and ).

 is evenly divisible by  numbers ( and ).

 is evenly divisible by  numbers ( and ).

 is only evenly divisible by  number ().

Test Case 0:

We must find the largest number  having exactly  divisors. Because  is the largest number  having exactly  divisors, we print  on a new line.

Test Case 1:

We must find the largest number  having exactly  divisors. Because  is the largest number in the list above having exactly  divisors, we print  on a new line.

Test Case 2:

There is no number between  and  having exactly  divisors, so we print  on a new line.
