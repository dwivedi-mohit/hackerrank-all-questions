# John and GCD list

- **Domain:** mathematics
- **Difficulty:** Easy
- **Max Score:** 50
- **Success Ratio:** 0.9402855906533968
- **Total Submissions:** 4622
- **Solved Count:** 4346
- **URL:** https://www.hackerrank.com/challenges/john-and-gcd-list

## Problem Statement

John is new to Mathematics and does not know how to calculate [GCD](https://en.wikipedia.org/wiki/Greatest_common_divisor) of numbers. So he wants you to help him in a few GCD calculations. John has a list _A_ of numbers, indexed _1_ to _N_. He wants to create another list B having _N+1_ numbers, indexed from _1_ to _N+1_, and having the following property:

GCD(B[i], B[i+1]) = A[i],  &forall; 1  &le; i  &le; N
 
As there can be many such lists, John wants to know the list _B_ in which sum of all elements is minimum. It is guaranteed that such a list will always exist.
 
**Input Format**  
The first line contains an integer _T_, i.e., the number of the test cases. _T_ testcases follow.    
The first line of each test case contains an integer _N_, i.e., the number of elements in the array.  
The second line of each test case contains _N_ space separated integers that  denote the elements of the list _A_.  

**Output Format**  
For each test case, print in a new line the list _B_ such that each element is separated by a single space. 

**Constraints**  
1 &le; _T_ &le; 10   
2 &le; _N_ &le; 10<sup>3</sup>  
1 &le; _A[i]_ &le; 10<sup>4</sup>  
1 &le; _B[i]_  

**Sample Input**  

    2
    3
    1 2 3
    3
    5 10 5
    
**Sample Output**  

    1 2 6 3
    5 10 10 5

**Explanation**  

For the first testcase, 

     GCD(1,2) = 1
     GCD(2,6) = 2
     GCD(6,3) = 3
     sum = 1+2+6+3 = 12 which is minimum among all possible list B

For the second testcase, 

    GCD(5, 10) = 5
    GCD(10, 10) = 10
    GCD(10, 5) = 5
    sum = 5 + 10 + 10 + 5 = 30 which is the minimum among all possible list B

## Input Format

The first line contains an integer T, i.e., the number of the test cases. T testcases follow.

The first line of each test case contains an integer N, i.e., the number of elements in the array.

The second line of each test case contains N space separated integers that  denote the elements of the list A.

## Output Format

For each test case, print in a new line the list B such that each element is separated by a single space.

## Constraints

1 ≤ T ≤ 10

2 ≤ N ≤ 103

1 ≤ A[i] ≤ 104

1 ≤ B[i]

## Sample Input

3
1 2 3
3
5 10 5

## Sample Output

1 2 6 3
5 10 10 5

## Explanation

For the first testcase,

 GCD(1,2) = 1
 GCD(2,6) = 2
 GCD(6,3) = 3
 sum = 1+2+6+3 = 12 which is minimum among all possible list B

For the second testcase,

GCD(5, 10) = 5
GCD(10, 10) = 10
GCD(10, 5) = 5
sum = 5 + 10 + 10 + 5 = 30 which is the minimum among all possible list B
