# Day 7: Regular Expressions I

- **Domain:** mathematics
- **Difficulty:** Easy
- **Max Score:** 15
- **Success Ratio:** 0.9774597959536573
- **Total Submissions:** 115660
- **Solved Count:** 113053
- **URL:** https://www.hackerrank.com/challenges/js10-regexp-1

## Problem Statement

**Objective**

In this challenge, we use a *Regular Expression* to evaluate a string. Check out the attached tutorial for more details.

**Task**

Complete the function in the editor below by returning a *RegExp* object, $re$, that matches any string $s$ that *begins* and *ends* with the same *vowel*. Recall that the English vowels are `a`, `e`, `i`, `o`, and `u`.


## Output Format

The function must return a *RegExp* object that matches any string $s$ beginning with and ending in the same vowel.

## Constraints

- The length of string $s$ is $\ge$ $3$.
- String $s$ consists of lowercase letters  only (i.e., `[a-z]`).

## Sample Input

bcd

## Sample Output

false

## Explanation

This string starts with (and ends in) a consonant, so it cannot start and end with the same vowel.
