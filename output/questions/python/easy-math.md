# Easy math

- **Domain:** python
- **Difficulty:** Medium
- **Max Score:** 50
- **Success Ratio:** 0.5771217712177121
- **Total Submissions:** 1355
- **Solved Count:** 782
- **URL:** https://www.hackerrank.com/challenges/easy-math

## Problem Statement

Charlie and Johnny play a game. For every integer *X* Charlie gives, Johnny has to find the smallest positive integer *Y*, such that X * Y contains only 4's and 0's and starts with one or more 4's followed by zero or more 0's. (i.e.), 404 is an invalid number but 400 is a valid number. 

If *a* is the number of 4's and *b* is the number of 0's, can you print the value of 2 * a + b.

**Input Format**<br>
The first line contains an integer T. T lines follow, each line containing the integer X as stated above.

**Output Format**<br>
For every X, print the output 2 * a + b in a newline as stated in the problem statement. 

**Constraints**<br>
1<=T<=10<sup>3</sup>  
1<=X<=10<sup>5</sup>

**Sample Input #00**
 
    3
    4
    5
    80

**Sample Output #00**
 
    2
    3
    4

**Explanation**  
For the 1<sup>st</sup> test-case, the smallest such multiple of 4 is **4** itself. Hence value of a will be 1 and and value of b will be 0. The required value of 2 * a+b is 2.     

For the 2<sup>nd</sup> test-case, **Y** = 8 and 40 is the minimum such multiple of 5. Hence value of a,b and 2 * a+b will be 1, 1 and 3 respectively.


## Input Format

The first line contains an integer T. T lines follow, each line containing the integer X as stated above.

## Output Format

For every X, print the output 2 * a + b in a newline as stated in the problem statement.

## Constraints

1<=T<=103

1<=X<=105

Sample Input #00

3
4
5
80

Sample Output #00

2
3
4

## Explanation

For the 1st test-case, the smallest such multiple of 4 is 4 itself. Hence value of a will be 1 and and value of b will be 0. The required value of 2 * a+b is 2.

For the 2nd test-case, Y = 8 and 40 is the minimum such multiple of 5. Hence value of a,b and 2 * a+b will be 1, 1 and 3 respectively.
