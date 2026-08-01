# Print Pretty

- **Domain:** databases
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.9212942842322197
- **Total Submissions:** 71329
- **Solved Count:** 65715
- **URL:** https://www.hackerrank.com/challenges/prettyprint

## Problem Statement

Given a text file with many lines of numbers to format and print, for each row of $3$ space-separated doubles, format and print the numbers using the specifications in the *Output Format* section below.

## Input Format

The first line contains an integer, $T$, the number of test cases.  
Each of the $T$ subsequent lines describes a test case as $3$ space-separated floating-point numbers: $A$, $B$, and $C$, respectively.

## Output Format

For each test case, print $3$ lines containing the formatted $A$, $B$, and $C$, respectively. Each $A$, $B$, and $C$ must be formatted as follows:

1. $A$: Strip its decimal (i.e., truncate it) and print its hexadecimal representation (including the $\texttt{0x}$ prefix) in lower case letters.
2. $B$: Print it to a scale of $2$ decimal places, preceded by a $+$ or $-$ sign (indicating if it's positive or negative), right justified, and left-padded with underscores so that the printed result is exactly $15$ characters wide.
3. $C$: Print it to a scale of exactly nine decimal places, expressed in scientific notation using upper case.

## Constraints

- $1 \le T \le 1000$  
- Each number will fit into a double.

## Sample Input

100.345 2006.008 2331.41592653498

## Sample Output

0x64
_______+2006.01
2.331415927E+03

## Explanation

For the first line of output,  (in reverse, ).

The second and third lines of output are formatted as described in the Output Format section.
