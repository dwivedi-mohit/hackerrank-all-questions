# Finding the percentage

- **Domain:** databases
- **Difficulty:** Easy
- **Max Score:** 10
- **Success Ratio:** 0.974878327427096
- **Total Submissions:** 979473
- **Solved Count:** 954867
- **URL:** https://www.hackerrank.com/challenges/finding-the-percentage

## Problem Statement

The provided code stub will read in a dictionary containing key/value pairs of name:\[marks\] for a list of students.  Print the average of the marks array for the student name provided, showing 2 places after the decimal.  

**Example**  
$\text{marks key:value pairs are}$  
$\text{'alpha': [20, 30, 40]}$  
$\text{'beta': [30, 50, 70]}$  
$\text{query_name = 'beta'}$  

The **query_name** is 'beta'.  beta's average score is $(30+50+70)/3 = 50.0$.

## Input Format

The first line contains the integer $n$, the number of students' records. The next $n$ lines contain the names and marks obtained by a student, each value separated by a space. The final line contains **query_name**, the name of a student to query.

## Output Format

Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

## Constraints

+ $2 \le n \le 10$  
+ $0 \le marks[i] \le 100$  
+ $\text{length of marks arrays} = 3$  

## Sample Input

3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

## Sample Output

56.00

## Explanation

Marks for Malika are  whose average is
