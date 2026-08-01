# Matching {x, y} Repetitions

- **Domain:** mathematics
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.9788874872063409
- **Total Submissions:** 42013
- **Solved Count:** 41126
- **URL:** https://www.hackerrank.com/challenges/matching-x-y-repetitions

## Problem Statement

__$\textsf{{x,y}}$__ 

The __{x,y}__ tool will match between $x$ and $y$ (both inclusive) repetitions of character/character class/group.

<img src="https://s3.amazonaws.com/hr-challenge-images/14522/1449644591-67495110c4-ach11.png" title="ach11.png" />
<sub>$$In \ the \ above \ image, \ the \ Regex \ Pattern \ is \ matched \ with \ the \ Test \ String. $$</sub>

**For Example**:

__w{3,5}__ : It will match the character `w` $3$, $4$ or $5$ times.   
__[xyz]{5,}__ : It will match the character `x`, `y` or `z` $5$ or more times.  
__\d{1, 4}__ : It will match any digits $1$, $2$, $3$, or $4$ times.

___
__Task__ 

You have a test string $S$.   
Your task is to write a regex that will match $S$ using the following conditions: 

- $S$ should begin with $1$ or $2$ __`digits`__.
- After that, $S$ should have $3$ or more __`letters`__ (both lowercase and uppercase). 
- Then $S$ should end with up to $3$ __`.`__ symbol(s). You can end with $0$ to $3$  `.` symbol(s), inclusively.

__Note__  

This is a regex only challenge. You are not required to write any code.   
You have to fill the regex pattern in the blank (`_________`).
