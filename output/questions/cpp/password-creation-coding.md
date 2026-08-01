# Password Creation (Coding)

- **Domain:** cpp
- **Difficulty:** Easy
- **Max Score:** 100
- **Success Ratio:** 0.9035087719298246
- **Total Submissions:** 114
- **Solved Count:** 103
- **URL:** https://www.hackerrank.com/challenges/password-creation-coding

## Problem Statement



Given 2 strings, merge them into a single string.

A password manager wants to create new passwords using two strings given by the user, then combined to create a harder-to-guess combination. Given two strings, interleave the characters of the strings to create a new string. Beginning with an empty string, alternately append a character from string _a_ and from string _b._ If one of the strings is exhausted before the other, append the remaining letters from the other string all at once. The result is the new password.

 

Example

If _a = 'hackerrank'_ and _b = 'mountain'_, the result is _hmaocuknetrariannk._

 

    

Function Description

Complete the function _newPassword_ in the editor below.

 

_newPassword_ has the following parameter(s):

    _string a:_  the first string

    _string b:_  the second string

 

Returns:

    _string: _the merged string

 

Constraints

- 1 ≤ lengths of_ a, b _ ≤ 25000
- All characters in _a_ and _b_ are lowercase letters in the range ascii['a'-'z']

 

  Input Format For Custom Testing

Input from stdin will be processed as follows and passed to the function:

 

The first line contains the string _a._

The second line contains the string _b._

  Sample Case 0

Sample Input

STDIN Function ----- ----- abc → a = 'abc' def → b = 'def'

 

Sample Output

adbecf

 

Explanation

 

Alternately taking characters from each string, the merged string is '_adbecf'._

Sample Case 1

 

Sample Input

STDIN Function ----- ----- cat → a = 'cat' rabbit → b = 'rabbit'

 

Sample Output

craatbbit

 

Explanation

 

Alternately taking characters from each string, the merged string is '_craatbbit'_. After _a_ is exhausted, the remainder of _b_ is concatenated to get '_craatbbit'_.



## Constraints

- 1 ≤ lengths of_ a, b _ ≤ 25000

- All characters in a and b are lowercase letters in the range ascii['a'-'z']

Input Format For Custom Testing

Input from stdin will be processed as follows and passed to the function:

The first line contains the string a.

The second line contains the string b.

Sample Case 0

## Sample Input

STDIN Function ----- ----- abc → a = 'abc' def → b = 'def'

## Sample Output

adbecf

## Explanation

Alternately taking characters from each string, the merged string is 'adbecf'.

Sample Case 1
