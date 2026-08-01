# Correlation and Regression Lines - A Quick Recap #1

- **Domain:** databases
- **Difficulty:** Medium
- **Max Score:** 5
- **Success Ratio:** 0.6749641774134426
- **Total Submissions:** 30009
- **Solved Count:** 20255
- **URL:** https://www.hackerrank.com/challenges/correlation-and-regression-lines-6

## Problem Statement

Given the test scores of 10 students in Physics and History, compute Karl Pearson’s coefficient of correlation between these scores. Round the result to three decimal places.

    Physics Scores	15	12	8	8	7	7	7	6	5	3
	History	Scores	10	25	17	11	13	17	20	13	9	15
    

##Pearson's Correlation Coefficient
$
r = \frac{\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^{n} (x_i - \bar{x})^2 \sum_{i=1}^{n} (y_i - \bar{y})^2}}
$

Where:
- $r$ is Pearson's correlation coefficient,  
- $x_i$ and $y_i$ are the individual sample points,  
- $\bar{x}$ and $bar{y}$ are the means of the $x$ and $y$ values,  
- $n$ is the number of data points.


**Output Format**  

Print the correlation coefficient as a floating-point value rounded to three decimal places, without leading or trailing spaces.

For example, if your answer is 0.255. In python you can print using   

	print("0.255")
    
This is **NOT** the actual answer - just the format in which you should provide your answer.

If you would like to test code that calculates the value, choose 'Test agains custom input' and enter anything into the input box, e.g., 'x'. The code will not run without some value in the input box. When you are satisfied with the output, press 'Submit Code'.

## Output Format

Print the correlation coefficient as a floating-point value rounded to three decimal places, without leading or trailing spaces.

For example, if your answer is 0.255. In python you can print using

print("0.255")

This is NOT the actual answer - just the format in which you should provide your answer.

If you would like to test code that calculates the value, choose 'Test agains custom input' and enter anything into the input box, e.g., 'x'. The code will not run without some value in the input box. When you are satisfied with the output, press 'Submit Code'.
