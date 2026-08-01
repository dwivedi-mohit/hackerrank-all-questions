# The Minion Game

- **Domain:** data-structures
- **Difficulty:** Medium
- **Max Score:** 40
- **Success Ratio:** 0.8792248225640484
- **Total Submissions:** 379010
- **Solved Count:** 333235
- **URL:** https://www.hackerrank.com/challenges/the-minion-game

## Problem Statement

Kevin and Stuart want to play the '__The Minion Game__'.<br>


__Game Rules__<br>

Both players are given the same string, $S$.<br>
Both players have to make substrings using the letters of the string $S$.<br>
Stuart has to make words starting with *consonants*.<br>
Kevin has to make words starting with *vowels*. <br>
The game ends when both players have made all possible substrings.
<br>


__Scoring__<br>
A player gets `+1` point for each occurrence of the substring in the string $S$.<br>

**For Example**:<br>
String $S$ = *BANANA*<br>
Kevin's vowel beginning word = *ANA*<br>
Here, *ANA* occurs twice in *BANANA*. Hence, Kevin will get `2` Points.
<br><br>
For better understanding, see the image below: <br>

<img src="https://s3.amazonaws.com/hr-challenge-images/9693/1450330231-04db904008-banana.png" title="banana.png" />

Your task is to determine the winner of the game and their score.

**Function Description**   

Complete the *minion_game* in the editor below.    

*minion_game* has the following parameters:   

- *string string:* the string to analyze   

**Prints**   

- *string:* the winner's name and score, separated by a space on one line, or `Draw` if there is no winner   

## Input Format

A single line of input containing the string $S$.  
**Note**: The string $S$ will contain only uppercase letters: $[A-Z]$.  



## Constraints

$0 < len(S) \leq 10^6$<br>
 

## Sample Input

BANANA

## Sample Output

Stuart 12

Note :

Vowels are only defined as . In this problem,  is not considered a vowel.
