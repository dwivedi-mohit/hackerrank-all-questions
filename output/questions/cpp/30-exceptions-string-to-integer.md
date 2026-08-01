# Day 16: Exceptions - String to Integer

- **Domain:** cpp
- **Difficulty:** Easy
- **Max Score:** 30
- **Success Ratio:** 0.9846954407062023
- **Total Submissions:** 208892
- **Solved Count:** 205695
- **URL:** https://www.hackerrank.com/challenges/30-exceptions-string-to-integer

## Problem Statement

**Objective**		
Today, we're getting started with *Exceptions* by learning how to parse an integer from a string and print a custom error message. Check out the [Tutorial](/challenges/30-exceptions-string-to-integer/tutorial) tab for learning materials and an instructional video!

**Task**	
Read a string, $S$, and print its integer value; if $S$ cannot be converted to an integer, print `Bad String`.

**Note:** You *must* use the String-to-Integer and exception handling constructs built into your submission language. If you attempt to use loops/conditional statements, you will get a $0$ score.

## Input Format

A single string, $S$.

## Output Format

Print the parsed integer value of $S$, or `Bad String` if $S$ cannot be converted to an integer.

**Sample Input 0**

	3

**Sample Output 0**

	3

**Sample Input 1**

	za

**Sample Output 1**

	Bad String

## Constraints

- $1 \le \left|S\right| \le 6$, where $\left|S\right|$ is the length of string $S$.
- $S$ is composed of *either* lowercase letters ($a-z$) *or* decimal digits ($0-9$).

## Sample Input

3

## Sample Output

3

## Explanation

Sample Case  contains an integer, so it should not raise an exception when we attempt to convert it to an integer. Thus, we print the .

Sample Case  does not contain any integers, so an attempt to convert it to an integer will raise an exception. Thus, our exception handler prints Bad String.
