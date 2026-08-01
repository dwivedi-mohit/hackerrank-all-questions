# Day 17: More Exceptions

- **Domain:** sql
- **Difficulty:** Easy
- **Max Score:** 30
- **Success Ratio:** 0.9928226639404735
- **Total Submissions:** 189764
- **Solved Count:** 188402
- **URL:** https://www.hackerrank.com/challenges/30-more-exceptions

## Problem Statement

**Objective**	
Yesterday's challenge taught you to manage exceptional situations by using *try* and *catch* blocks. In today's challenge, you will practice throwing and propagating an exception. Check out the [Tutorial](/challenges/30-more-exceptions/tutorial) tab for learning materials and an instructional video.

**Task**	
Write a *Calculator* class with a single method: *int power(int,int)*. The *power* method takes two integers, $n$ and $p$, as parameters and returns the integer result of $n^p$. If either $n$ or $p$ is negative, then the method must throw an exception with the message: `n and p should be non-negative`. 

**Note:** Do not use an access modifier (e.g.: public) in the declaration for your *Calculator* class.

## Input Format

Input from stdin is handled for you by the locked stub code in your editor. The first line contains an integer, $T$, the number of test cases. Each of the $T$ subsequent lines describes a test case in $2$ space-separated integers that denote $n$ and $p$, respectively.

## Output Format

Output to stdout is handled for you by the locked stub code in your editor. There are $T$ lines of output, where each line contains the result of $n^p$ as calculated by your *Calculator* class' *power* method.

## Constraints

- No Test Case will result in overflow for correctly written code.

## Sample Input

3 5
2 4
-1 -2
-1 3

## Sample Output

16
n and p should be non-negative
n and p should be non-negative

## Explanation

:  and  are positive, so power returns the result of , which is .

:  and  are positive, so power returns the result of =, which is .

: Both inputs ( and ) are negative, so power throws an exception and   is printed.

: One of the inputs () is negative, so power throws an exception and   is printed.
