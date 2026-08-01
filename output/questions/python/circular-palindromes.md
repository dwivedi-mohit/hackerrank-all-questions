# Circular Palindromes

- **Domain:** python
- **Difficulty:** Advanced
- **Max Score:** 120
- **Success Ratio:** 0.6651959317977865
- **Total Submissions:** 13372
- **Solved Count:** 8895
- **URL:** https://www.hackerrank.com/challenges/circular-palindromes

## Problem Statement

A *palindrome* is a string that reads the same from left to right as it does from right to left.

Given a string, $S$, of $N$ lowercase English letters, we define a *$k$-length rotation* as cutting the first $k$ characters from the beginning of $S$ and appending them to the end of $S$. For each $S$, there are $N$ possible $k$-length rotations (where $0 \le k \lt N$). See the *Explanation* section for examples.

Given $N$ and $S$, find all $N$ $k$-length rotations of $S$; for each rotated string, $S_k$, print the maximum possible length of any palindromic substring of $S_k$ on a new line.

## Input Format

The first line contains an integer, $N$ (the length of $S$).	
The second line contains a single string, $S$.

## Output Format

There should be $N$ lines of output, where each line $k$ contains an integer denoting the maximum length of any palindromic substring of rotation $S_k$.

**Sample Input 0**

    13
    aaaaabbbbaaaa
    
**Sample Output 0**

    12
    12
    10
    8
    8
    9
    11
    13
    11
    9
    8
    8
    10

**Sample Input 1**

    7
    cacbbba
    
**Sample Output 1**

    3
    3
    3
    3
    3
    3
    3


**Sample Input 2**

    12
    eededdeedede

**Sample Output 2**

    5
    7
    7
    7
    7
    9
    9
    9
    9
    7
    5
    4

## Constraints

- $1 \le N \le 5 \times 10^5$
- $0 \le k \lt N$
- $\textit{S is comprised of lowercase English letters.}$

## Sample Input

13
aaaaabbbbaaaa

## Sample Output

12
12
10
8
8
9
11
13
11
9
8
8
10

## Explanation

Consider Sample Case 1, where .

The possible rotations, , for string  are:

.

The longest palindromic substrings for each  are:

 and , so we print their length () on a new line.

, so we print its length () on a new line.

 and , so we print their length () on a new line.

 and , so we print their length () on a new line.

 and , so we print their length () on a new line.

 and , so we print their length () on a new line.

 and , so we print their length () on a new line.
