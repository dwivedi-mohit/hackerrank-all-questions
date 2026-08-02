# Branch Reset Groups

- **Domain:** ai
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.9519863629906719
- **Total Submissions:** 21119
- **Solved Count:** 20105
- **URL:** https://www.hackerrank.com/challenges/branch-reset-groups

## Problem Statement

__<sub>NOTE - `Branch reset group is supported by Perl, PHP, Delphi and R.`</sub>__ 

__$\textsf{(?|regex)}$__  

A [branch reset group](http://www.regular-expressions.info/branchreset.html) consists of alternations and capturing groups. _(?|(regex1)|(regex2))_   
Alternatives in branch reset group share same capturing group.  

<img src="https://s3.amazonaws.com/hr-challenge-images/14816/1449647722-07764d667a-ach20.png" title="ach20.png" />
<sub>$$In\ the \ above \ image, \ Regex \ Pattern \ is \ matched \ with \ the \ Test \ String. $$</sub>

___
__Task__ 

You have a test string $S$.    
Your task is to write a regex which will match $S$, with following condition(s):

- $S$ consists of 8 digits. 
- $S$ must have "---", "-", "." or ":" separator such that string $S$ gets divided in $4$ parts, with each part having exactly two digits.  
- $S$ string must have exactly one kind of separator.  
- Separators must have integers on both sides.


__Valid $S$__

	12-34-56-78
    12:34:56:78
    12---34---56---78
    12.34.56.78
    
__Invalid $S$__
	
    1-234-56-78
	12-45.78:10
    
__Note__  

This is a regex only challenge. You are not required to write any code.   
You only have to fill the regex pattern in the blank (`_________`).

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
