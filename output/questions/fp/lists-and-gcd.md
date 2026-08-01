# Lists and GCD

- **Domain:** fp
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.9525155455059355
- **Total Submissions:** 1769
- **Solved Count:** 1685
- **URL:** https://www.hackerrank.com/challenges/lists-and-gcd

## Problem Statement

We call an integer $p > 1$ a _prime number_ (or simply a _prime_) if its only positive divisors are $1$ and $p$.  
<br>
_Fundamental theorem of arithmetic states:_ Every positive integer $n$ can be uniquely expressed as a product of power of primes, i.e.,

$N = p_1^{n_1} \times p_2^{n_2} \times p_3^{n_3} \times \ldots$

where, 

- $p_i$ is the $i^{th}$ prime, i.e., $p_1 = 2, p_2 = 3, p_3 = 5, \ldots$
- $\forall i. n_i \ge 0$

---
**Greatest common divisor of two positive integers**  
<br>
For two positive integers, $A$ and $B$, whose _prime factorization_ is represented as  
<br>
$A = p_1^{a_1} \times p_2^{a_2} \times p_3^{a_3} \times \ldots$   
<br>
$B = p_1^{b_1} \times p_2^{b_2} \times p_3^{b_3} \times \ldots$  

We calculate the _greatest common divisor_, $gcd(A, B)$, as  

$gcd(A, B) = p_1^{min(a_1, b_1)} \times p_2^{min(a_2, b_2)} \times p_3^{min(a_3, b_3)} \times \ldots$  

---
**Greater common divisor of a list of numbers**  
<br>
_Greatest common factor_ of a  list of positive integers, $lst = \{l_1, l_2,\ldots l_q\}$, is represented as  

$gcd(lst) = gcd(l_1, gcd(l_2, gcd(l_3, \ldots ,(gcd(l_{q-1}, l_q))\ldots)))$  

---
**Finite representation of prime factorization**  
<br>
Since primes are infinite, it is not possible to store factors in the form provided above. To that end, we will only consider those prime factors ($p_i$) whose power is greater than zero ($n_i>0$). That is:  


$N = p_{i_1}^{n_{i_1}} \times p_{i_2}^{n_{i_2}} \times p_{i_3}^{n_{i_3}} \times \ldots$  

, where

- $p_{i_j} < p_{i_{j+1}}$
- $0 < n_{i_j},\ \ j \in [1, 2, \ldots]$; for rest $n_i = 0$

And we will represent them as following:

$N = p_{i_1}\ {n_{i_1}}\ p_{i_2}\ {n_{i_2}}\ p_{i_3}\ {n_{i_3}}\ \ldots$  


*For example:*  

- $49 = 7^2 = 7\ 2$
- $28 = 2^2 \times 7^1 = 2\ 2\ 7\ 1$

---
**Challenge**   
<br>
You are given the elements of list, $lst$, in the representation provided above. Find its greatest common divisor, i.e., $gcd(lst)$.  

## Input Format

First line contains an integer, $q$, which is the size of list, $lst$.  
Then follows $q$ lines, where $i^{th}$ line represents the factors of $i^{th}$ element of $lst$, $l_i$  


## Output Format

Print one line representing the greatest common divisor of $lst$  ($gcd(lst)$) in the above representation.  


**Constraints**  

- $2 \le q \le 1000$
- All other integers lie in $[1, 10^5]$
- $1 \le $ Total number of prime factors of an element $\le 100$  

**Notes**  

- Test cases are designed such that $gcd(lst)$ will always be greater than $1$.

**Sample Input #00**  

	2
	7 2
	2 2 7 1


**Sample Output #00**

	7 1
    
**Sample Input #01**  

	4
	2 2 3 2 5 3
	3 2 5 3 11 1
	2 2 3 3 5 4 7 6 19 18
	3 10 5 15

**Sample Output #01**  

	3 2 5 3

## Constraints

-

- All other integers lie in

-  Total number of prime factors of an element

Notes

- Test cases are designed such that  will always be greater than .

Sample Input #00

2
7 2
2 2 7 1

Sample Output #00

7 1

Sample Input #01

4
2 2 3 2 5 3
3 2 5 3 11 1
2 2 3 3 5 4 7 6 19 18
3 10 5 15

Sample Output #01

3 2 5 3

## Explanation

Test case #00: . Therefore .

Test case #01: .
