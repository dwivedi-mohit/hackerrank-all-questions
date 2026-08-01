# Excluding Specific Characters

- **Domain:** mathematics
- **Difficulty:** Easy
- **Max Score:** 10
- **Success Ratio:** 0.9785353040341866
- **Total Submissions:** 51014
- **Solved Count:** 49919
- **URL:** https://www.hackerrank.com/challenges/excluding-specific-characters

## Problem Statement

__$\textsf{[^]}$__

The negated character class __`[^]`__ matches any character that is *not* in the square brackets.

<img src="https://s3.amazonaws.com/hr-challenge-images/14273/1449643683-8e249ed955-ach08.png" title="ach08.png" />
<sub>$$In \ the \ above \ image, \ the \ Regex \ Pattern \ is \ matched \ with \ the \ Test \ String. $$</sub>

__Task__ 

You have a test string $S$.   
Your task is to write a regex that will match $S$ with the following conditions: 

-	$S$ must be of length __`6`__.
-	First character should *not* be a __`digit`__ ( $1, 2, 3, 4, 5, 6, 7, 8, 9$ or $0$ ).
-	Second character should *not* be a __`lowercase vowel`__ ( $a, e, i, o$ or $u$ ).
-	Third character should *not* be __`b`__, __`c`__, __`D`__ or __`F`__.
-	Fourth character should *not* be a __`whitespace character`__ ( \r, \n, \t, \f or &lt;space\> ).
-	Fifth character should *not* be a __`uppercase vowel`__ ( $A, E, I, O$ or $U$ ).
-	Sixth character should *not* be a __`.`__ or __`,`__ symbol.

__Note__  

This is a regex only challenge. You are not required to write any code.   
You have to fill the regex pattern in the blank (`_________`).
