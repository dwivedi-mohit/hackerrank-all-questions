# Substring Searching

- **Domain:** ai
- **Difficulty:** Medium
- **Max Score:** 50
- **Success Ratio:** 0.5973756906077348
- **Total Submissions:** 1448
- **Solved Count:** 865
- **URL:** https://www.hackerrank.com/challenges/kmp-fp

## Problem Statement

In 1974, a very fast string searching method was proposed by the name of [KMP algorithm](http://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm) with linear run-time complexity. Your task here is to code this (or any similar) algorithm in a functional language.

Given two strings _text_ and _pat_, find whether _pat_ exists as a substring in _text_.

**Input**  
First line will contain an integer, _T_, which represents total number of test cases.
Then _T_ test cases follow. Each case will contains two lines each containing a string. First line will contain _text_ while the second line will contain _pat_.

**Output**  
For each case print `YES` if _pat_ is a substring of _text_ otherwise `NO`.

**Constraints**  
1 &le; _T_ &le; 10  
1 &le; _|pat|_ &le; _|text|_ &le; 100000  
All characters in _text_ and _pat_ will be lowercase latin character ('_a_'-'_z_').  

**Sample Input**  

    4
    abcdef
    def
    computer
    muter
    stringmatchingmat
    ingmat
    videobox
    videobox

**Sample Output**  

    YES
    NO
    YES
    YES

**Explanation**  
*Test Case #00:* Here _"def"_ is present at the end of _"abcdef"_.  
*Test Case #01:* Though _"muter"_ is a subsequence here, but we need it to be asubstring.  
*Test Case #02:* _"ingmat"_ is present at index _3_  and _11_.  
*Test Case #03:* Both strings are same.  


## Constraints

1 ≤ T ≤ 10

1 ≤ |pat| ≤ |text| ≤ 100000

All characters in text and pat will be lowercase latin character ('a'-'z').

## Sample Input

abcdef
def
computer
muter
stringmatchingmat
ingmat
videobox
videobox

## Sample Output

YES
NO
YES
YES

## Explanation

Test Case #00: Here "def" is present at the end of "abcdef".

Test Case #01: Though "muter" is a subsequence here, but we need it to be asubstring.

Test Case #02: _"ingmat"_ is present at index 3  and 11.

Test Case #03: Both strings are same.

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
