# Picking Cards

- **Domain:** algorithms
- **Difficulty:** Easy
- **Max Score:** 50
- **Success Ratio:** 0.8038747346072187
- **Total Submissions:** 3768
- **Solved Count:** 3029
- **URL:** https://www.hackerrank.com/challenges/picking-cards

## Problem Statement

There are N cards on the table and each has a number between 0 and N. Let us denote the number on the i<sup>th</sup> card by c<sub>i</sub>. You want to pick up all the cards. The i<sup>th</sup> card can be picked up only if at least c<sub>i</sub> cards have been picked up before it. (As an example, if a card has a value of 3 on it, you can't pick that card up unless you've already picked up 3 cards previously) In how many ways can all the cards be picked up?

**Input Format**  
The first line contains the number of test cases T. T test cases follow. Each case contains an integer N on the first line, followed by integers c<sub>1</sub>,..c<sub>i</sub>,...,c<sub>N</sub> on the second line.

**Output Format**  
Output T lines one corresponding to each test case containing the required answer for the corresponding test case. As the answers can be very big, output them modulo 1000000007.


**Constraints:**  
1 <= T <= 10  
1 <= N <= 50000  
0 <= c<sub>i</sub> <= N

**Sample Input:**  

	3  
    3  
    0 0 0  
    3  
    0 0 1  
    3  
    0 3 3

**Sample Output:**  

	6  
    4  
    0

**Sample Explanations:**

For the first case, the cards can be picked in any order, so there are 3! = 6 ways.  
For the second case, the cards can be picked in 4 ways: {1,2,3}, {2,1,3}, {1,3,2}, {2,3,1}.   
For the third case, no cards can be picked up after the first one, so there are 0 ways to pick up all cards.


## Input Format

The first line contains the number of test cases T. T test cases follow. Each case contains an integer N on the first line, followed by integers c1,..ci,...,cN on the second line.

## Output Format

Output T lines one corresponding to each test case containing the required answer for the corresponding test case. As the answers can be very big, output them modulo 1000000007.

## Constraints

1 <= T <= 10

1 <= N <= 50000

0 <= ci <= N

## Sample Input

3
3
0 0 0
3
0 0 1
3
0 3 3

## Sample Output

6
4
0

Sample Explanations:

For the first case, the cards can be picked in any order, so there are 3! = 6 ways.

For the second case, the cards can be picked in 4 ways: {1,2,3}, {2,1,3}, {1,3,2}, {2,3,1}. 

For the third case, no cards can be picked up after the first one, so there are 0 ways to pick up all cards.
