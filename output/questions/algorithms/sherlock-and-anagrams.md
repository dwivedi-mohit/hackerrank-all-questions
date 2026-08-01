# Sherlock and Anagrams

- **Domain:** algorithms
- **Difficulty:** Medium
- **Max Score:** 50
- **Success Ratio:** 0.8985791990700671
- **Total Submissions:** 158291
- **Solved Count:** 142237
- **URL:** https://www.hackerrank.com/challenges/sherlock-and-anagrams

## Problem Statement

Two strings are [*anagrams*][123] of each other if the letters of one string can be rearranged to form the other string. Given a string, find the number of pairs of substrings of the string that are anagrams of each other.  

**Example**  
$s = mom$  

The list of all anagrammatic pairs is $[m, m], [mo, om]$ at positions $[[0], [2]], [[0, 1], [1, 2]]$ respectively.

[123]: http://en.wikipedia.org/wiki/Anagram  

**Function Description**

Complete the function *sherlockAndAnagrams* in the editor below.  

sherlockAndAnagrams has the following parameter(s):

-  *string s:* a string  

**Returns**  

- *int:* the number of unordered anagrammatic pairs of substrings in $s$

## Input Format

The first line contains an integer $q$, the number of queries.   
Each of the next $q$ lines contains a string $s$ to analyze. 

## Constraints

$1 \le q \le 10$   
$2 \le \text{ length of }s \le 100$  
$s$ contains only lowercase letters in the range ascii[a-z]. 

## Sample Input

2
abba
abcd

## Sample Output

4
0

## Explanation

The list of all anagrammatic pairs is  and  at positions  and  respectively.

No anagrammatic pairs exist in the second query as no character repeats.
