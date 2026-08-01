# Day 8: Least Square Regression Line

- **Domain:** java
- **Difficulty:** Easy
- **Max Score:** 30
- **Success Ratio:** 0.970358374991199
- **Total Submissions:** 14203
- **Solved Count:** 13782
- **URL:** https://www.hackerrank.com/challenges/s10-least-square-regression-line

## Problem Statement

**Objective** <br>
In this challenge, we practice using *linear regression* techniques. Check out the [Tutorial](/challenges/s10-least-square-regression-line/tutorial) tab for learning materials!

**Task** <br>
A group of five students enrolls in Statistics immediately after taking a Math aptitude test. Each student's Math aptitude test score, $x$, and Statistics course grade, $y$, can be expressed as the following list of $(x, y)$ points:	

1. $(95,85)$ 	
2. $(85,95)$ 	
3. $(80,70)$	
4. $(70,65)$  	
5. $(60,70)$  	

If a student scored an $80$ on the Math aptitude test, what grade would we expect them to achieve in Statistics? Determine the equation of the best-fit line using the least squares method, then compute and print the value of $y$ when $x = 80$.

## Input Format

There are five lines of input; each line contains two space-separated integers describing a student's respective $x$ and $y$ grades:

    95 85
    85 95
    80 70
    70 65
    60 70
    
If you do not wish to read this information from stdin, you can hard-code it into your program.

## Output Format

Print a single line denoting the answer, rounded to a scale of $3$ decimal places (i.e., $1.234$ format).
