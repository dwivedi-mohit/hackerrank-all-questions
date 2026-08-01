# Day 4: Class vs. Instance

- **Domain:** python
- **Difficulty:** Easy
- **Max Score:** 30
- **Success Ratio:** 0.9654043597946581
- **Total Submissions:** 537640
- **Solved Count:** 519040
- **URL:** https://www.hackerrank.com/challenges/30-class-vs-instance

## Problem Statement

**Objective**	
In this challenge, we're going to learn about the difference between a *class* and an *instance*; because this is an *Object Oriented* concept, it's only enabled in certain languages. Check out the [Tutorial](/challenges/30-class-vs-instance/tutorial) tab for learning materials and an instructional video!	

**Task**	
Write a *Person* class with an instance variable, $age$, and a constructor that takes an integer, $initialAge$, as a parameter. The constructor must assign $initialAge$ to $age$ after confirming the argument passed as $initialAge$ is not negative; if a negative argument is passed as $initialAge$, the constructor should set $age$ to $0$ and print `Age is not valid, setting age to 0.`. In addition, you must write the following instance methods:

1. *yearPasses()* should increase the $age$ instance variable by $1$. 	
2. *amIOld()* should perform the following conditional actions:
- If $age \lt 13$, print `You are young.`.		
- If $age \geq 13$ and $age \lt 18$, print `You are a teenager.`.	
- Otherwise, print `You are old.`.

To help you learn by example and complete this challenge, much of the code is provided for you, but you'll be writing everything in the future. The code that creates each instance of your *Person* class is in the *main* method. Don't worry if you don't understand it all quite yet!

**Note:** Do not remove or alter the stub code in the editor.

## Input Format

Input is handled for you by the stub code in the editor. 

The first line contains an integer, $T$ (the number of test cases), and the $T$ subsequent lines each contain an integer denoting the $age$ of a Person instance.

## Output Format

Complete the method definitions provided in the editor so they meet the specifications outlined above; the code to test your work is already in the editor. If your methods are implemented correctly, each test case will print $2$ or $3$ lines (depending on whether or not a valid $initialAge$ was passed to the constructor).

## Constraints

- $1 \le T \le 4$  
- $-5 \le age \le 30$

## Sample Input

-1
10
16
18

## Sample Output

Age is not valid, setting age to 0.
You are young.
You are young.

You are young.
You are a teenager.

You are a teenager.
You are old.

You are old.
You are old.

## Explanation

Test Case 0:

Because , our code must set  to  and print the "Age is not valid..." message followed by the young message. Three years pass and , so we print the young message again.

Test Case 1:

Because , our code should print that the person is young. Three years pass and , so we print that the person is now a teenager.

Test Case 2:

Because , our code should print that the person is a teenager. Three years pass and , so we print that the person is old.

Test Case 3:

Because , our code should print that the person is old. Three years pass and the person is still old at , so we print the old message again.

The extra line at the end of the output is supposed to be there and is trimmed before being compared against the test case's expected output. If you're failing this challenge, check your logic and review your print statements for spelling errors.
