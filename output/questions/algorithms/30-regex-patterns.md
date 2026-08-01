# Day 28: RegEx, Patterns, and Intro to Databases

- **Domain:** algorithms
- **Difficulty:** Medium
- **Max Score:** 30
- **Success Ratio:** 0.9852252527762381
- **Total Submissions:** 104638
- **Solved Count:** 103092
- **URL:** https://www.hackerrank.com/challenges/30-regex-patterns

## Problem Statement

**Objective**	
Today, we're working with regular expressions. Check out the [Tutorial](/challenges/30-regex-patterns/tutorial) tab for learning materials and an instructional video!

**Task**	
Consider a database table, _Emails_, which has the attributes _First Name_ and _Email ID_. Given $N$ rows of data simulating the *Emails* table, print an alphabetically-ordered list of people whose email address ends in $\textit{@gmail.com}$.

## Input Format

The first line contains an integer, $N$, total number of rows in the table. 	
Each of the $N$ subsequent lines contains $2$ space-separated strings denoting a person's first name and email ID, respectively.

## Output Format

Print an alphabetically-ordered list of first names for every user with a gmail account. Each name must be printed on a new line.

## Constraints

- $2 \le N \le 30$
- Each of the first names consists of lower case letters $[a-z]$ only.
- Each of the email IDs consists of lower case letters $[a-z]$, $@$ and $.$ only.
- The length of the first name is no longer than 20.
- The length of the email ID is no longer than 50.

## Sample Input

riya riya@gmail.com
julia julia@julia.me
julia sjulia@gmail.com
julia julia@gmail.com
samantha samantha@gmail.com
tanya tanya@gmail.com

## Sample Output

julia
julia
riya
samantha
tanya
