# Consecutive Subsequences

- **Domain:** ai
- **Difficulty:** Medium
- **Max Score:** 50
- **Success Ratio:** 0.7691067397613673
- **Total Submissions:** 3101
- **Solved Count:** 2385
- **URL:** https://www.hackerrank.com/challenges/consecutive-subsequences

## Problem Statement

Jigar got a sequence of __n__ positive integers as his birthday present! He likes consecutive subsequences whose sum is divisible by __k__. He asks you to write a program to count them for him.

__Input Format__ <br>
The first line contains **T**, the number of testcases.  
__T__ testcases follow. Each testcase consists of 2 lines.  
The first line contains **n** and **k** separated by a single space.  
And the second line contains __n__ space separated integers.

__Output Format__ <br>
For each test case, output the number of consecutive subsequenences whose sum is divisible by __k__ in a newline.

__Constraints__ <br>
1 ≤ T ≤ 20 <br>
1 ≤ n ≤ 10<sup>6</sup> <br>
1 ≤ k ≤ 100 <br>
1 ≤ a[i] ≤ 10<sup>4</sup> <br>

__Sample Input__
<pre>
2
5 3
1 2 3 4 1
6 2
1 2 1 2 1 2
</pre>

__Sample Output__
<pre>
4
9
</pre>

__Explanation__

For 

    1 2 3 4 1

there exists, 4 subsequences whose sum is divisible by 3, they are   

    3
    1 2
    1 2 3
    2 3 4

For 

    1 2 1 2 1 2

there exists, 9 subsequences whose sum is divisible by 2, they are  

    2
    2
    2
    1 2 1
    1 2 1
    1 2 1 2
    2 1 2 1
    1 2 1 2
    2 1 2 1 2

## Input Format

The first line contains T, the number of testcases.

T testcases follow. Each testcase consists of 2 lines.

The first line contains n and k separated by a single space.

And the second line contains n space separated integers.

## Output Format

For each test case, output the number of consecutive subsequenences whose sum is divisible by k in a newline.

## Constraints

1 ≤ T ≤ 20

1 ≤ n ≤ 106

1 ≤ k ≤ 100

1 ≤ a[i] ≤ 104

## Sample Input

5 3
1 2 3 4 1
6 2
1 2 1 2 1 2

## Sample Output

9

## Explanation

For

1 2 3 4 1

there exists, 4 subsequences whose sum is divisible by 3, they are

3
1 2
1 2 3
2 3 4

For

1 2 1 2 1 2

there exists, 9 subsequences whose sum is divisible by 2, they are

2
2
2
1 2 1
1 2 1
1 2 1 2
2 1 2 1
1 2 1 2
2 1 2 1 2
