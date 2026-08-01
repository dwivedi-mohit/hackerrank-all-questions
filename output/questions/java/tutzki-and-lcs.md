# LCS Returns

- **Domain:** java
- **Difficulty:** Medium
- **Max Score:** 50
- **Success Ratio:** 0.6023872679045092
- **Total Submissions:** 3770
- **Solved Count:** 2271
- **URL:** https://www.hackerrank.com/challenges/tutzki-and-lcs

## Problem Statement

Given two strings, $a$ and $b$, find and print the total number of ways to insert a character at any position in string $a$ such that the length of the [Longest Common Subsequence](https://en.wikipedia.org/wiki/Longest_common_subsequence_problem?oldformat=true) of characters in the two strings increases by one.

## Input Format

The first line contains a single string denoting $a$. 		
The second line contains a single string denoting $b$.

## Output Format

Print a single integer denoting the total number of ways to insert a character into string $a$ in such a way that the length of the longest common subsequence of $a$ and $b$ increases by one.

## Constraints

**Scoring**		

* $1 \le |a|, |b| \le 5000$
* Strings $a$ and $b$ are alphanumeric (i.e., consisting of arabic digits and/or upper and lower case English letters).
* The new character being inserted must also be alphanumeric (i.e., a digit or upper/lower case English letter).

**Subtask**		

* $1 \le |a|, |b| \le 1000$ for $\text{66.67%}$ of the maximum score.  

## Sample Input

aa
baaa

## Explanation

The longest common subsequence shared by  and  is aa, which has a length of . There are two ways that the length of the longest common subsequence can be increased to  by adding a single character to :

- There are  different positions in string  where we could insert an additional a to create longest common subsequence aaa (i.e., at the beginning, middle, and end of the string).

- We can insert a b at the beginning of the string for a new longest common subsequence of baa.

As we have  ways to insert an alphanumeric character into  and increase the length of the longest common subsequence by one, we print  on a new line.
