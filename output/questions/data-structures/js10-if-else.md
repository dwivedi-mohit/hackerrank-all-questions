# Day 2: Conditional Statements: If-Else

- **Domain:** data-structures
- **Difficulty:** Easy
- **Max Score:** 10
- **Success Ratio:** 0.9897238068416261
- **Total Submissions:** 152683
- **Solved Count:** 151114
- **URL:** https://www.hackerrank.com/challenges/js10-if-else

## Problem Statement

**Objective**

In this challenge, we learn about *if-else* statements. Check out the attached tutorial for more details.

**Task**

Complete the `getGrade(score)` function in the editor. It has one parameter: an integer, $score$, denoting the number of points Julia earned on an exam. It must return the letter corresponding to her $grade$ according to the following rules:

- If $25 \lt score \le 30$, then $grade = A$.
- If $20 \lt score \le 25$, then $grade = B$.
- If $15 \lt score \le 20$, then $grade = C$.
- If $10 \lt score \le 15$, then $grade = D$.
- If $5 \lt score \le 10$, then $grade = E$.
- If $0 \le score \le 5$, then $grade = F$.

## Input Format

Stub code in the editor reads a single integer denoting $score$ from stdin and passes it to the function.

## Output Format

The function must return the value of $grade$ (i.e., the letter grade) that Julia earned on the exam.

## Constraints

- $0 \le score \le 30$

## Sample Input

11

## Sample Output

D

## Explanation

Because , it satisfies the condition  (which corresponds to D). Thus, we return D as our answer.
