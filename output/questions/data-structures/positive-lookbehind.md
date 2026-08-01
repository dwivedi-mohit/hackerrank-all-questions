# Positive Lookbehind

- **Domain:** data-structures
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.9842472752043597
- **Total Submissions:** 23488
- **Solved Count:** 23118
- **URL:** https://www.hackerrank.com/challenges/positive-lookbehind

## Problem Statement

__$\textsf{(?<=regex_2)regex_1}$__

The positive lookbehind (__?<=__) asserts `regex_1` to be immediately preceded by `regex_2`. Lookbehind is excluded from the match (do not consume matches of `regex_2`), but only assert whether a match is possible or not. 

<img src="https://s3.amazonaws.com/hr-challenge-images/14903/1449648924-81d5f2a6d0-ach24.png" title="ach24.png" />
<sub>$$In \ above \ image \ Regex \ Pattern \ is \ matched \ with \ the \ Test \ String. $$</sub>

__Task__ 

You have a test String $S$.  
Write a regex which can match all the occurences of digit which are immediately preceded by odd digit.

__Note__  

This is a regex only challenge. You are not required to write a code.   
You have to fill the regex pattern in the blank (`_________`).

<sub>__`JavaScript do not support lookbehind.`__</sub>
