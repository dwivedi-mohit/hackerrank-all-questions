# Matching Same Text Again & Again

- **Domain:** java
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.9782154580722172
- **Total Submissions:** 30159
- **Solved Count:** 29502
- **URL:** https://www.hackerrank.com/challenges/matching-same-text-again-again

## Problem Statement

__$\textsf{\group_number}$__

This tool (__\1__ references the first capturing group) matches the same text as previously matched by the capturing group.

<img src="https://s3.amazonaws.com/hr-challenge-images/14740/1449647091-1e4a2a040e-ach18.png" title="ach18.png" />
<sub>$$In \ the \ above \ image, \ the \ Regex \ Pattern \ is \ matched \ with \ the \ Test \ String. $$</sub>

**For Example**: <br>

__(\d)\1__: It can match `00`, `11`, `22`, `33`, `44`, `55`, `66`, `77`, `88` or `99`.

___
__Task__ 

You have a test string $S$.   
Your task is to write a regex that will match $S$ with the following conditions:  

-	$S$ must be of length: __`20`__
-	$1^{st}$ character: __`lowercase letter`__.
-	$2^{nd}$ character: __`word character`__.
-	$3^{rd}$ character: __`whitespace character`__.
-	$4^{th}$ character: __`non word character`__.
-	$5^{th}$ character: __`digit`__.
-	$6^{th}$ character: __`non digit`__.
-	$7^{th}$ character: __`uppercase letter`__.
-	$8^{th}$ character: __`letter`__ (either lowercase or uppercase).
-	$9^{th}$ character: __`vowel`__ (a, e, i , o , u, A, E, I, O or U).
-	$10^{th}$ character: __`non whitespace character`__.
-	$11^{th}$ character: should be same  as __`1st character`__.
-	$12^{th}$ character: should be same  as __`2nd character`__.
-	$13^{th}$ character: should be same  as __`3rd character`__.
-	$14^{th}$ character: should be same  as __`4th character`__.
-	$15^{th}$ character: should be same  as __`5th character`__.
-	$16^{th}$ character: should be same  as __`6th character`__.
-	$17^{th}$ character: should be same  as __`7th character`__.
-	$18^{th}$ character: should be same  as __`8th character`__.
-	$19^{th}$ character: should be same  as __`9th character`__.
-	$20^{th}$ character: should be same  as __`10th character`__.


__Note__  

This is a regex only challenge. You are not required to write code.   
You have to fill the regex pattern in the blank (`_________`).
