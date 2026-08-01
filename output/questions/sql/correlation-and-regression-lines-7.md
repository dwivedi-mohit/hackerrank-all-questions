# Correlation and Regression Lines - A Quick Recap #2

- **Domain:** sql
- **Difficulty:** Medium
- **Max Score:** 5
- **Success Ratio:** 0.8271905159966563
- **Total Submissions:** 13159
- **Solved Count:** 10885
- **URL:** https://www.hackerrank.com/challenges/correlation-and-regression-lines-7

## Problem Statement

Given the test scores of 10 students in Physics and History, compute the slope of the regression line obtained by treating Physics as the independent variable. The result should be rounded to three decimal places.

The scores to use:

    Physics Scores	15	12	8	8	7	7	7	6	5	3
	History	Scores	10	25	17	11	13	17	20	13	9	15

## Slope of a regression line

$\Large m = \frac{\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^{n} (x_i - \bar{x})^2}$

Where:

- $m$ is the slope of the regression line,  
- $x_i$ and $y_i$ are the data points,  
- $\bar{x}$ and $\bar{y}$ are the means of the $x$-values and $y$-values, respectively,  
- $n$ is the number of data points.  


**Output Format**  

In the text box, enter the floating point/decimal value required. Do not leave any leading or trailing spaces. Your answer may look like:
	0.255
    
This is **NOT** the actual answer - just the format in which you should provide your answer.

## Output Format

In the text box, enter the floating point/decimal value required. Do not leave any leading or trailing spaces. Your answer may look like:
    0.255

This is NOT the actual answer - just the format in which you should provide your answer.
