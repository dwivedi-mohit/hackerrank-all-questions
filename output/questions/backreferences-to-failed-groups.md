# Backreferences To Failed Groups

- **Domain:** ai
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.9455798808369128
- **Total Submissions:** 28868
- **Solved Count:** 27297
- **URL:** https://www.hackerrank.com/challenges/backreferences-to-failed-groups

## Problem Statement

Backreference to a capturing group that match nothing is different from backreference to a capturing group that did not participate in the match at all.

__Capturing group that match nothing__

<img src="https://s3.amazonaws.com/hr-challenge-images/14743/1449647327-074d8e0329-ach19_1.png" title="ach19_1.png" />
<sub>$$In\ the \ above \ image, \ Regex \ Pattern \ is \ matched \ with \ the \ Test \ String. $$</sub>

Here, `b?` is optional and matches nothing.   
Thus, `(b?)` is successfully matched and capture nothing.   
`o` is matched with __o__ and `\1` successfully matches the nothing captured by the group.

__Capturing group that didn't participate in the match at all__

<img src="https://s3.amazonaws.com/hr-challenge-images/14743/1449647382-1800101173-ach19_2.png" title="ach19_2.png" />
<sub>$$In\ the \ above \ image, \ Regex \ Pattern \ is \ not \ matching \ the \ Test \ String. $$</sub>

In most regex flavors (excluding JavaScript), `(b)?o\1` fails to match __o__.  
Here, `(b)` fails to match at all. Since, the whole group is optional the regex engine does proceed to match __o__.  
The regex engine now arrives at `\1` which references a group that did not participate in the match attempt at all.  
Thus, the backreference fails to match at all.

___
__Task__ 

You have a test string $S$.    
Your task is to write a regex which will match $S$, with following condition(s):

- $S$ consists of 8 digits. 
- $S$ may have "$-$" separator such that string $S$ gets divided in $4$ parts, with each part having exactly two digits. (Eg. 12-34-56-78)

__Valid $S$__

	12345678
    12-34-56-87
    
__Invalid $S$__
	
    1-234-56-78
	12-45-7810
    
__Note__  

This is a regex only challenge. You are not required to write any code.   
You only have to fill the regex pattern in the blank (`_________`).

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
