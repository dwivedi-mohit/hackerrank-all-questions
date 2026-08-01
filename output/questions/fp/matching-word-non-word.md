# Matching Word & Non-Word Character

- **Domain:** fp
- **Difficulty:** Easy
- **Max Score:** 5
- **Success Ratio:** 0.9857519441149334
- **Total Submissions:** 75870
- **Solved Count:** 74789
- **URL:** https://www.hackerrank.com/challenges/matching-word-non-word

## Problem Statement

__$\textsf{\w}$__

The expression **\w** will match any word character.   
Word characters include alphanumeric characters ($a$-$z$, $A$-$Z$ and $0$-$9$) and underscores (_).

<img src="https://s3.amazonaws.com/hr-challenge-images/14140/1449635286-cce6ae164d-ach03_01.png" title="ach03_01.png" />

<sub>$$In\ the \ above \ image, \ Regex \ Pattern \ is \ matched \ with \ the \ Test \ String. $$</sub>

---
__$\textsf{\W}$__ 

**\W** matches any non-word character.   
Non-word characters include characters other than alphanumeric characters ($a$-$z$, $A$-$Z$ and $0$-$9$) and underscore (_).

<img src="https://s3.amazonaws.com/hr-challenge-images/14140/1449635294-194aef2d68-ach03_02.png" title="ach03_02.png" />
<sub>$$In\ the \ above \ image, \ Regex \ Pattern \ is \ matched \ with \ the \ Test \ String. $$</sub>

__Task__ 

You have a test string $S$. Your task is to match the pattern $xxxXxxxxxxxxxxXxxx$   
Here $x$ denotes any word character and $X$ denotes any non-word character.

__Note__  

This is a regex only challenge. You are not required to write any code.   
You only have to fill the regex pattern in the blank (`_________`).
