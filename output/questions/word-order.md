# Word Order

- **Domain:** ai
- **Difficulty:** Medium
- **Max Score:** 50
- **Success Ratio:** 0.921919360026852
- **Total Submissions:** 214509
- **Solved Count:** 197760
- **URL:** https://www.hackerrank.com/challenges/word-order

## Problem Statement

You are given $n$ words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification. 

**Note:** Each input line ends with a **"\n"** character.

**Constraints:**  
$1\le n\le 10^5$  
The sum of the lengths of all the words do not exceed $10^6$  
All the words are composed of lowercase English letters only.

## Input Format

The first line contains the integer, $n$.  
The next $n$ lines each contain a word. 

## Output Format

Output $2$ lines.  
On the first line, output the number of distinct words from the input.  
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

## Constraints

The sum of the lengths of all the words do not exceed

All the words are composed of lowercase English letters only.

## Sample Input

bcdef
abcdefg
bcde
bcdef

## Sample Output

2 1 1

## Explanation

There are  distinct words. Here, "bcdef" appears twice in the input at the first and last positions. The other words appear once each. The order of the first appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the output.

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
