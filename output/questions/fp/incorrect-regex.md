# Incorrect Regex

- **Domain:** fp
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.9182655080443948
- **Total Submissions:** 116230
- **Solved Count:** 106730
- **URL:** https://www.hackerrank.com/challenges/incorrect-regex

## Problem Statement

You are given a string $S$.  
Your task is to find out whether $S$ is a valid [regex](https://en.wikipedia.org/wiki/Regular_expression) or not.

## Input Format

The first line contains integer $T$, the number of test cases.  
The next $T$ lines contains the string $S$.

__Constraints__

$0 < T < 100$

## Output Format

Print "True" or "False" for each test case without quotes.

## Sample Input

.*\+
.*+

## Sample Output

True
False

## Explanation

.*\+ : Valid regex.

.*+: Has the error multiple repeat. Hence, it is invalid.
