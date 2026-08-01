# Inheritance

- **Domain:** c
- **Difficulty:** Easy
- **Max Score:** 30
- **Success Ratio:** 0.9060297572435395
- **Total Submissions:** 1277
- **Solved Count:** 1157
- **URL:** https://www.hackerrank.com/challenges/inheritance

## Problem Statement

**Objective**	
Today, we're delving into Inheritance. Check out the [Tutorial](/challenges/30-inheritance/tutorial) tab for learning materials and an instructional video!

**Task**	
You are given two classes, *Person* and *Student*, where *Person* is the base class and *Student* is the derived class. Completed code for *Person* and a declaration for *Student* are provided for you in the editor. Observe that *Student* inherits all the properties of *Person*.

Complete the *Student* class by writing the following:

- A *Student* class constructor, which has $4$ parameters: 
	1. A string, $firstName$.
    2. A string, $lastName$.
    3. An integer, $id$.
    4. An integer array (or vector) of test scores, $scores$.
- A *char  calculate()* method that calculates a Student object's average and returns the grade character representative of their calculated average:

<img src="https://s3.amazonaws.com/hr-challenge-images/17165/1458142706-3073bc9143-Grading.png" title="Grading.png" />

## Input Format

The locked stub code in your editor calls your *Student* class constructor and passes it the necessary arguments. It also calls the *calculate* method (which takes no arguments).

*You are not responsible for reading the following input from stdin:*		
The first line contains $firstName$, $lastName$, and $id$, respectively. The second line contains the number of test scores. The third line of space-separated integers describes $scores$.

## Output Format

*This is handled by the locked stub code in your editor.* Your output will be correct if your *Student* class constructor and *calculate()* method are properly implemented.

## Constraints

- $ 4 \le | firstName |, | lastName | \le 10$    
- $ |id| \equiv 7$  
- $0 \le score, average \le 100$

## Sample Input

Heraldo Memelli 8135627
2
100 80

## Sample Output

Name: Memelli, Heraldo
 ID: 8135627
 Grade: O

## Explanation

This student had  scores to average:  and . The student's average grade is . An average grade of  corresponds to the letter grade , so our calculate() method should return the character'O'.
