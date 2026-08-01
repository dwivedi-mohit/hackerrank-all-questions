# Negative Lookahead

- **Domain:** c
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.9703945989013293
- **Total Submissions:** 23847
- **Solved Count:** 23141
- **URL:** https://www.hackerrank.com/challenges/negative-lookahead

## Problem Statement

__$\textsf{regex_1(?!regex_2)}$__

The negative lookahead (__?!__) asserts `regex_1` _not_ to be immediately followed by `regex_2`. Lookahead is excluded from the match (do not consume matches of `regex_2`), but only assert whether a match is possible or not. 

<img src="https://s3.amazonaws.com/hr-challenge-images/14902/1449648778-29c9e8978b-ach23.png" title="ach23.png" />
<sub>$$In \ above \ image \ Regex \ Pattern \ is \ matched \ with \ the \ Test \ String. $$</sub>

__Task__ 

You have a test String $S$.  
Write a regex which can match all characters which are not immediately followed by that same character.

__Example__ 

If $S$ = __goooo__, then regex should match __`g`ooo`o`__. Because the first `g` is not follwed by _g_ and the last `o` is not followed by _o_.

__Note__  

This is a regex only challenge. You are not required to write a code.   
You have to fill the regex pattern in the blank (`_________`).
