# Day 7: Regular Expressions III

- **Domain:** sql
- **Difficulty:** Easy
- **Max Score:** 15
- **Success Ratio:** 0.9966464594350574
- **Total Submissions:** 46518
- **Solved Count:** 46362
- **URL:** https://www.hackerrank.com/challenges/js10-regexp-3

## Problem Statement

**Task**

Complete the function in the editor below by returning a *RegExp* object, $re$, that matches *every integer* in some string $s$.

## Output Format

The function must return a *RegExp* object that matches *every integer* in some string $s$.

## Constraints

- The length of string $s$ is $\ge$ $3$.
- It's guaranteed that string $s$ contains *at least* one integer.

## Sample Input

102, 1948948 and 1.3 and 4.5

## Sample Output

102
1948948
1
3
4
5

## Explanation

When we call match on string  and pass the correct RegExp as our argument, it returns the following array of results: [ '102', '1948948', '1', '3', '4', '5' ].
