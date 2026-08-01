# Girlfriend & Necklace

- **Domain:** cpp
- **Difficulty:** Hard
- **Max Score:** 80
- **Success Ratio:** 0.698170731707317
- **Total Submissions:** 328
- **Solved Count:** 229
- **URL:** https://www.hackerrank.com/challenges/gneck

## Problem Statement

Mr. X wants to buy a necklace for his girlfriend.
The available necklaces are bi-colored (red and blue beads).

Mr. X desperately wants to impress his girlfriend and knows that she will like the necklace only if **every prime length continuous sub-sequence of beads in the necklace** has more or equal number of red beads than blue beads.

Given the number of beads in the necklace N, Mr. X wants to know the number of all possible such necklaces.

_Note: - It is given that the necklace is a single string and not a loop._


**Input Format**  
The first line of the input contains an integer *T*, the number of testcases.  
*T* lines follow, each line containing *N*, the number of beads in the necklace.  

**Constraints**  
1 &le; T &le; 10<sup>4</sup>  
2 &le; N &le; 10<sup>18</sup>  

**Output Format**  
For each testcase, print in a newline, the number of such necklaces that are possible.  If the answer is greater than or equal to 10<sup>9</sup>+7, print the answer modulo ( % ) 10<sup>9</sup>+7.

**Sample Input**

    2
    2
    3

**Sample Output**

    3
    4

**Explanation**

For the first testcase, valid arrangement of beads are 

    BR RB RR

For the second testcase, valid arrangement of beads are

    BRR RBR RRR RRB

## Input Format

The first line of the input contains an integer T, the number of testcases.

T lines follow, each line containing N, the number of beads in the necklace.

## Output Format

For each testcase, print in a newline, the number of such necklaces that are possible.  If the answer is greater than or equal to 109+7, print the answer modulo ( % ) 109+7.

## Constraints

1 ≤ T ≤ 104

2 ≤ N ≤ 1018

## Sample Input

2
3

## Sample Output

4

## Explanation

For the first testcase, valid arrangement of beads are

BR RB RR

For the second testcase, valid arrangement of beads are

BRR RBR RRR RRB
