# Matching {x} Repetitions

- **Domain:** databases
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.9576776486543362
- **Total Submissions:** 42767
- **Solved Count:** 40957
- **URL:** https://www.hackerrank.com/challenges/matching-x-repetitions

## Problem Statement

__$\textsf{{x}}$__ 

The tool __{x}__ will match exactly $x$ repetitions of character/character class/groups.

<img src="https://s3.amazonaws.com/hr-challenge-images/14525/1449644438-27dbaa69fd-ach10.png" title="ach10.png" />
<sub>$$In \ the \ above \ image, \ the \ Regex \ Pattern \ is \ matched \ with \ the \ Test \ String. $$</sub>

**For Example**:

__w{3}__ : It will match the character `w` exactly $3$ times.   
__[xyz]{5}__ : It will match the string of length $5$ consisting of characters {`x`, `y`, `z`}. For example it will match `xxxxx`, `xxxyy` and `xyxyz`.		
__\d{4}__ : It will match any digit exactly $4$ times.

___
__Task__ 

You have a test string $S$.   
Your task is to write a regex that will match $S$ using the following conditions: 

- $S$ must be of length equal to __`45`__.
- The first $40$ characters should consist of __`letters`__(both lowercase and uppercase), or of __`even digits`__.  
- The last $5$ characters should consist of __`odd digits`__ or __`whitespace characters`__.

__Note__  

This is a regex only challenge. You are not required to write any code.   
You have to fill the regex pattern in the blank (`_________`).
