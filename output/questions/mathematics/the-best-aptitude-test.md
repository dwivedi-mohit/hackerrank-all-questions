# The Best Aptitude Test

- **Domain:** mathematics
- **Difficulty:** Medium
- **Max Score:** 15
- **Success Ratio:** 0.7166060606060606
- **Total Submissions:** 4125
- **Solved Count:** 2956
- **URL:** https://www.hackerrank.com/challenges/the-best-aptitude-test

## Problem Statement

A college admits students on the basis of their scores in a series of 5 aptitude tests. The academic performance of the admitted students is then tracked, and when they complete the first year of their academic program in college, their Grade Point Average (GPA) is recorded. A student's GPA is an indicator of his/her academic performance. Higher the GPA, the better. This exercise is conducted on one batch of students. Absolute GPA is used for this problem.

The next year, the college realizes that it does not have the necessary resources to conduct all 5 aptitude tests, it decides to conduct only 1 of the 5 tests. Which of the aptitude tests would you recommend them to conduct for the next round of admissions?
 
You are given the recorded data. Identify the aptitude test which has clearly the best predictive value in determining the relative academic standing of the students after they enter the college.

**Input Format**  

The 1<sup>st</sup> line in the file is an integer T, T testcases follow.  
Each testcase has 7 lines.  

The 1<sup>st</sup> line of every testcase contains the number of admitted students, N.  
The 2<sup>nd</sup> line of every testcase has N decimal numbers (upto 2 decimal places) separated by a single space which are the Grade Point Averages (GPAs) of the admitted students at the end of the 1<sup>st</sup> academic year. The i<sup>th</sup> score, is the GPA of the i<sup>th</sup> student at the end of the 1<sup>st</sup> year.  
This next 5 lines of every testcase has N decimal numbers ( upto 2 decimal places) separated by a single space in each line, which is the performance of the students in the 5 aptitude tests conducted for the entrance exam. The i<sup>th</sup>  integer in each line, is what the i<sup>th</sup> student scored in that aptitude test.  

**Constraints**

1 <= T <= 10  
4 <= N <= 100  
0.0 <= k <= 10.0, where k is the GPA of every student.  
0.0 <= s <= 100.0, where s is the score of every student in any of the 5 aptitude tests.  

**Output Format**

T integers, each on a new line.  
For each test case, output the Aptitude Test (1-5) which appears to be the best predictor of the relative academic standing of the students after they enter the college.

**Sample Input**

    1
    5
    7.5 7.7 7.9 8.1 8.3
    10 30 20 40 50
    11 9 5 19 29
    21 9 15 19 39
    91 9 75 19 89
    81 99 55 59 89
    
**Example Output**

    1

**Explanation**

In the given example, we can see that the ranks of the students, on the basis of their 1<sup>st</sup> year GPA; "matches quite well" with their relative standings in the first aptitude test (in which their scores were 10,30,20,40 50). You need to identify how you can quantify how well the relative standings in an aptitude test *match* with the relative standings of the GPA.

Assume that for each test case provided, there is one aptitude test, the scores in which, appear to be be good predictors of the academic performance of the students in college (measured by GPA). The other aptitude tests do not seem to have much predictive value, and can be done away with.

**Scoring**  

Score for a test case = 10 * C/T  
Where T = Number of Tests
And   C = Correct Answers  

*Please note, that there is no perfect solution to this open-ended problem.  Any solution scoring 80% or above, of the maximum score, is a commendable achievement.*

## Input Format

The 1st line in the file is an integer T, T testcases follow.

Each testcase has 7 lines.

The 1st line of every testcase contains the number of admitted students, N.

The 2nd line of every testcase has N decimal numbers (upto 2 decimal places) separated by a single space which are the Grade Point Averages (GPAs) of the admitted students at the end of the 1st academic year. The ith score, is the GPA of the ith student at the end of the 1st year.

This next 5 lines of every testcase has N decimal numbers ( upto 2 decimal places) separated by a single space in each line, which is the performance of the students in the 5 aptitude tests conducted for the entrance exam. The ith  integer in each line, is what the ith student scored in that aptitude test.

## Output Format

T integers, each on a new line.

For each test case, output the Aptitude Test (1-5) which appears to be the best predictor of the relative academic standing of the students after they enter the college.

## Constraints

1 <= T <= 10

4 <= N <= 100

0.0 <= k <= 10.0, where k is the GPA of every student.

0.0 <= s <= 100.0, where s is the score of every student in any of the 5 aptitude tests.

## Sample Input

5
7.5 7.7 7.9 8.1 8.3
10 30 20 40 50
11 9 5 19 29
21 9 15 19 39
91 9 75 19 89
81 99 55 59 89

Example Output

1

## Explanation

In the given example, we can see that the ranks of the students, on the basis of their 1st year GPA; "matches quite well" with their relative standings in the first aptitude test (in which their scores were 10,30,20,40 50). You need to identify how you can quantify how well the relative standings in an aptitude test match with the relative standings of the GPA.

Assume that for each test case provided, there is one aptitude test, the scores in which, appear to be be good predictors of the academic performance of the students in college (measured by GPA). The other aptitude tests do not seem to have much predictive value, and can be done away with.

Scoring

Score for a test case = 10 * C/T

Where T = Number of Tests
And   C = Correct Answers

Please note, that there is no perfect solution to this open-ended problem.  Any solution scoring 80% or above, of the maximum score, is a commendable achievement.
