# Smart Number

- **Domain:** python
- **Difficulty:** Easy
- **Max Score:** 25
- **Success Ratio:** 0.8495780954021009
- **Total Submissions:** 34842
- **Solved Count:** 29601
- **URL:** https://www.hackerrank.com/challenges/smart-number

## Problem Statement

In this challenge, the task is to debug the existing code to successfully execute all provided test files.
_________________________________________________________________________________

A number is called a *smart* number if it has an odd number of factors. Given some numbers, find whether they are smart numbers or not.
 
Debug the given function `is_smart_number` to correctly check if a given number is a smart number. 
 
**Note:** You can modify only *one* line in the given code and you cannot add or remove any new lines.

*To restore the original code, click on the icon to the right of the language selector.*

## Input Format

The first line of the input contains $t$, the number of test cases.  
The next $t$ lines contain one integer each.


## Output Format

The output should consist of $t$ lines. In the $i^{th}$ line print *YES* if the $i^{th}$ integer has an odd number of factors, else print *NO*.

## Constraints

- $1 \le t \le 10^3$   
- $1 \le n_i \le 10^4$, where $n_i$ is the $i^{th}$ integer.  

## Sample Input

1
2
7
169

## Sample Output

YES
NO
NO
YES

## Explanation

The factors of 1 are just 1 itself.So the answer is YES.
 The factors of 2 are 1 and 2.It has even number of factors.The answer is NO.
 The factors of 7 are 1 and 7.It has even number of factors.The answer is NO.
 The factors of 169 are 1,13 and 169.It has odd number of factors.The answer is YES.
