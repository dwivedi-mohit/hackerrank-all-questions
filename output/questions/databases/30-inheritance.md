# Day 12: Inheritance

- **Domain:** databases
- **Difficulty:** Easy
- **Max Score:** 30
- **Success Ratio:** 0.9793423190532344
- **Total Submissions:** 260339
- **Solved Count:** 254961
- **URL:** https://www.hackerrank.com/challenges/30-inheritance

## Problem Statement

**Objective**	
Today, we're delving into Inheritance. Check out the attached tutorial for learning materials and an instructional video.

**Task**	
You are given two classes, *Person* and *Student*, where *Person* is the base class and *Student* is the derived class. Completed code for *Person* and a declaration for *Student* are provided for you in the editor. Observe that *Student* inherits all the properties of *Person*.

Complete the *Student* class by writing the following:

- A *Student* class constructor, which has $4$ parameters: 
	1. A string, $firstName$.
    2. A string, $lastName$.
    3. An integer, $idNumber$.
    4. An integer array (or vector) of test scores, $scores$.
- A *char  calculate()* method that calculates a Student object's average and returns the grade character representative of their calculated average:

<img src="https://s3.amazonaws.com/hr-challenge-images/17165/1458142706-3073bc9143-Grading.png" title="Grading.png" />

## Input Format

The locked stub code in the editor reads the input and calls the *Student* class constructor with the necessary arguments. It also calls the *calculate* method which takes no arguments.
	
The first line contains $firstName$, $lastName$, and $idNumber$, separated by a space. The second line contains the number of test scores. The third line of space-separated integers describes $scores$.

## Output Format

*Output is handled by the locked stub code.* Your output will be correct if your *Student* class constructor and *calculate()* method are properly implemented.

## Constraints

- $ 1 \le \text{length of firstName, length of lastName} \le 10$    
- $ \text{length of idNumber} \equiv 7$  
- $0 \le score \le 100$

## Sample Input

Heraldo Memelli 8135627
2
100 80

## Sample Output

Name: Memelli, Heraldo
 ID: 8135627
 Grade: O

## Explanation

This student had  scores to average:  and . The student's average grade is . An average grade of  corresponds to the letter grade , so the calculate() method should return the character'O'.
