# Two Characters

- **Domain:** ai
- **Difficulty:** Easy
- **Max Score:** 100
- **Success Ratio:** 0.9498680738786279
- **Total Submissions:** 2653
- **Solved Count:** 2520
- **URL:** https://www.hackerrank.com/challenges/three-month-preparation-kit-two-characters

## Problem Statement

Given a string, remove characters until the string is made up of any two alternating characters.  When you choose a character to remove, all instances of that character must be removed.  Determine the longest string possible that contains just two alternating letters.

**Example**    

$s = \text{'abaacdabd'}$   

Delete `a`, to leave `bcdbd`.  Now, remove the character `c` to leave the valid string `bdbd` with a length of 4. Removing either `b` or `d` at any point would not result in a valid string.  Return $4$.   

Given a string $s$, convert it to the longest possible string $t$ made up only of alternating characters.  Return the length of string $t$.  If no string $t$ can be formed, return $0$.

**Function Description**

Complete the *alternate* function in the editor below.  

alternate has the following parameter(s):  

- *string s:* a string   

**Returns**. 

- *int:* the length of the longest valid string, or $0$ if there are none   

## Input Format

The first line contains a single integer that denotes the length of $s$. 	
The second line contains string $s$.


## Constraints

* $ 1 \le \text{ length of s }\le 1000 $
* $s[i] \in \text{ascii[a-z]}$ 

## Sample Input

STDIN       Function
-----       --------
10          length of s = 10
beabeefeab  s = 'beabeefeab'

## Explanation

The characters present in  are a, b, e, and f. This means that  must consist of two of those characters and we must delete two others.  Our choices for characters to leave are [a,b], [a,e], [a, f], [b, e], [b, f] and [e, f].

If we delete e and f, the resulting string is babab. This is a valid  as there are only two distinct characters (a and b), and they are alternating within the string.

If we delete a and f, the resulting string is bebeeeb. This is not a valid string  because there are consecutive e's present.  Removing them would leave consecutive b's, so this fails to produce a valid string .

Other cases are solved similarly.

babab is the longest string we can create.

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
