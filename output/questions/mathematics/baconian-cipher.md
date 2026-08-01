# Baconian Cipher

- **Domain:** mathematics
- **Difficulty:** Medium
- **Max Score:** 100
- **Success Ratio:** 0.40271493212669685
- **Total Submissions:** 221
- **Solved Count:** 89
- **URL:** https://www.hackerrank.com/challenges/baconian-cipher

## Problem Statement

BaconCipher is a substitution cipher where a message is concealed in the form 
of a series of characters. Given below is how each letter of the alphabet 
is represented as a baconian cipher. 

    'a' = ----- 'n' = -**-*
    'b' = ----* 'o' = -***-
    'c' = ---*- 'p' = -****
    'd' = ---** 'q' = *----
    'e' = --*-- 'r' = *---*
    'f' = --*-* 's' = *--*-
    'g' = --**- 't' = *--**
    'h' = --*** 'u' = *-*--
    'i' = -*--- 'v' = *-*-*
    'j' = -*--* 'w' = *-**-
    'k' = -*-*- 'x' = *-***
    'l' = -*-** 'y' = **---
    'm' = -**-- 'z' = **--*

**INPUT format**

    string

The <i>string</i> contains all of 26 letters of the english alphabet without any spaces between
successive letters. They are not necessarily in the same order.<br/>

**OUTPUT format**

    *-*-*
    *---*

The output of the code must be the substituted baconian cipher of every letter.
Each cipher must be separated by a newline.

**TASK**

Write a brainfuck program that takes the input and generates the required output.<br/>

**Score**

This is a codegolf challenge. Lesser the # of characters in source code, higher is the score. Score = (5000 - #of characters in source code)/50. 

**Note**

Wraparound is disabled. Please read the [environment](https://www.hackerrank.com/environment) section.
