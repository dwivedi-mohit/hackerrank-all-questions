# Day 3: Throw

- **Domain:** ai
- **Difficulty:** Easy
- **Max Score:** 15
- **Success Ratio:** 0.9947568795084157
- **Total Submissions:** 119776
- **Solved Count:** 119148
- **URL:** https://www.hackerrank.com/challenges/js10-throw

## Problem Statement

**Objective**

In this challenge, we practice using *throw* and *catch* statements to work with custom error messages. 

**Task**

Complete the *isPositive* function below. It has one integer parameter, $a$. If the value of $a$ is positive, it must return the string `YES`. Otherwise, it must *throw* an *Error* according to the following rules:

- If $a$ is $0$, *throw* an *Error* with $message = $ `Zero Error`.
- If $a$ is negative, *throw* an *Error* with $message = $ `Negative Error`.

## Input Format

Locked stub code in the editor reads the following input from stdin and passes each value of $a$ to the function as an argument:		
The first line is an integer, $n$, denoting the number of times the function will be called with some $a$.		
Each line $i$ of the $n$ subsequent lines contains an integer denoting some $a$.

## Output Format

If the value of $a$ is positive, the function must return the string `YES`. Otherwise, it must *throw* an *Error* according to the following rules:

- If $a$ is $0$, *throw* an *Error* with $message = $ `Zero Error`.
- If $a$ is negative, *throw* an *Error* with $message = $ `Negative Error`.

## Constraints

- $1 \le n \le 5$
- $-100 \le a \le 100$

## Sample Input

3
1
2
3

## Sample Output

YES
YES
YES

## Explanation

Each of the given values is positive, so we return YES each time. The value returned during each function call is printed on a new line by locked stub code in the editor.

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
