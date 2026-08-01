# Period

- **Domain:** shell
- **Difficulty:** Hard
- **Max Score:** 100
- **Success Ratio:** 0.8125
- **Total Submissions:** 416
- **Solved Count:** 338
- **URL:** https://www.hackerrank.com/challenges/period

## Problem Statement

You are given 2 integers **a** and **b**. Let a number be defined as 
![image1](https://s3.amazonaws.com/hr-assets/0/1526567764-7f13ff1150-period1.png). As we know ![image1](https://s3.amazonaws.com/hr-assets/0/1526567764-7f13ff1150-period1.png) will be an irrational number when b is non-zero. In this problem, we call it the AC number. We define 

![Image2](https://s3.amazonaws.com/hr-assets/0/1526567811-db0dd614fb-period2.png) (where x an integer)<br /><br /> and the operation ![Image3](https://s3.amazonaws.com/hr-assets/0/1526567834-0366f2bad1-perioda.png) on AC number as:

![Image4](https://s3.amazonaws.com/hr-assets/0/1526567862-8b1090f7e1-period4.png)

This problem is to find the smallest positive integer **n**, such that:

![Image5](https://s3.amazonaws.com/hr-assets/0/1526567879-29dc56cbe4-period5.png)

We call the integer **n** as period. You are given **a**, **b** and **m**. Can you figure out the period?

**Input Format**  
The first line of the input contains a single integer T denoting the number of test-cases.   
T lines follow, each containing 3 integers - a, b and m separated by a single space. 

**Output Format**  
Output the Period if it exists, otherwise output "-1" (quotes only for reference)

**Constraints**  
1 ≤ T ≤ 300  
5 ≤ m ≤ 10<sup>7</sup>  
0 ≤ a, b < m


**Sample Input #00**

    4
    0 0 13
    1 0 7
    3 0 10007
    1 1 19

**Sample Output #00**

    -1
    1
    5003
    18
    
**Explanation #00**   

For the 1st test-case, no amount of operation ⊗ on a = 0, b = 0 gives 1 on the RHS. Hence the answer is -1.   
When a = 1, b = 0, we have 1 for n = 1.  
On repeated operations, the third and the fourth testcases sum to 1 for n = 5003 and n = 18 respectively. 


## Input Format

The first line of the input contains a single integer T denoting the number of test-cases.

T lines follow, each containing 3 integers - a, b and m separated by a single space.

## Output Format

Output the Period if it exists, otherwise output "-1" (quotes only for reference)

## Constraints

1 ≤ T ≤ 300

5 ≤ m ≤ 107

0 ≤ a, b < m

Sample Input #00

4
0 0 13
1 0 7
3 0 10007
1 1 19

Sample Output #00

-1
1
5003
18

Explanation #00

For the 1st test-case, no amount of operation ⊗ on a = 0, b = 0 gives 1 on the RHS. Hence the answer is -1.

When a = 1, b = 0, we have 1 for n = 1.

On repeated operations, the third and the fourth testcases sum to 1 for n = 5003 and n = 18 respectively.
