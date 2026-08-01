# Employee Salaries

- **Domain:** c
- **Difficulty:** Easy
- **Max Score:** 10
- **Success Ratio:** 0.9962839829935455
- **Total Submissions:** 1387238
- **Solved Count:** 1382083
- **URL:** https://www.hackerrank.com/challenges/salary-of-employees

## Problem Statement

Write a query that prints a list of employee names (i.e.: the *name* attribute) for employees in **Employee** having a salary greater than $\$2000$ per month who have been employees for less than $10$ months. Sort your result by ascending _employee\_id_.

## Input Format

The **Employee** table containing employee data for a company is described as follows: 

<img src="https://s3.amazonaws.com/hr-challenge-images/19629/1458557872-4396838885-ScreenShot2016-03-21at4.27.13PM.png"/>

where _employee\_id_ is an employee's ID number, _name_ is their name, _months_ is the total number of months they've been working for the company, and _salary_ is the their monthly salary.

## Sample Output

Angela
Michael
Todd
Joe

## Explanation

Angela has been an employee for  month and earns  per month.

Michael has been an employee for  months and earns  per month.

Todd has been an employee for  months and earns  per month.

Joe has been an employee for  months and earns  per month.

We order our output by ascending employee_id.
