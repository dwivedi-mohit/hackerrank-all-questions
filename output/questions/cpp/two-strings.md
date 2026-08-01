# Two Strings

- **Domain:** cpp
- **Difficulty:** Easy
- **Max Score:** 25
- **Success Ratio:** 0.9083367052301561
- **Total Submissions:** 363297
- **Solved Count:** 329996
- **URL:** https://www.hackerrank.com/challenges/two-strings

## Problem Statement

Given two strings, determine if they share a common substring.  A substring may be as small as one character.  

**Example**   
$s1 = \text{'and'}$  
$s2 = \text{'art'}$  

These share the common substring $a$.  

$s1 = \text{'be'}$  
$s2 = \text{'cat'}$  

These do not share a substring.  

**Function Description**

Complete the function *twoStrings* in the editor below.    

twoStrings has the following parameter(s):  

- *string s1:*  a string
- *string s2:*  another string    

**Returns**  

- *string:* either `YES` or `NO`

## Input Format

The first line contains a single integer $p$, the number of test cases.		

The following $p$ pairs of lines are as follows:

- The first line contains string $s1$.
- The second line contains string $s2$.

## Output Format

For each pair of strings, return `YES` or `NO`.

## Constraints

- $s1$ and $s2$ consist of characters in the range ascii[a-z].
- $1 \le p \le 10$
- $1 \le |s1|, |s2| \le 10^5$

## Sample Input

hello
world
hi
world

## Sample Output

YES
NO

## Explanation

We have  pairs to check:

- , . The substrings  and  are common to both strings.

- , .  and  share no common substrings.
