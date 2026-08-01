# String Reductions

- **Domain:** fp
- **Difficulty:** Easy
- **Max Score:** 10
- **Success Ratio:** 0.9760452961672473
- **Total Submissions:** 4592
- **Solved Count:** 4482
- **URL:** https://www.hackerrank.com/challenges/string-reductions

## Problem Statement

Given a string, $str =  s_1, s_2\ldots s_n$, consisting of $n$ lowercase English characters ($a-z$), remove all of the characters that occurred previously in the string. Formally, remove all characters, $s_i$, for:
<br>

$\exists j, s_j = s_i$ and $ j < i$

## Input Format

A single line of input containing a string $str$ of length $n$.  

## Output Format

Print the string after removing all the characters that occurred previously. 


**Sample Input #00**  

	accabb

**Sample Output #00**  

	acb

**Sample Input #01**  

	abc

**Sample Output #01**  

	abc

**Sample Input #02**

	pprrqq

**Sample Output #02**  

	prq


## Constraints

- $1 \le n \le 10^5$  
- $s_i \in \{a,\ b, \ldots,\ z\}, where\ 1 \le i \le n$

## Explanation

Test case #00: For , characters at indexes  are removed as they have already occurred.

Test case #01:  As each character occurs only once, nothing is removed.

Test case #02: For , each character occurs twice. The second of these characters is removed. Characters at positions  and  are removed.

Tested by Wanbo
