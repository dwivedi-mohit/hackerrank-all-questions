# Game of Kyles

- **Domain:** sql
- **Difficulty:** Advanced
- **Max Score:** 80
- **Success Ratio:** 0.7289719626168224
- **Total Submissions:** 535
- **Solved Count:** 390
- **URL:** https://www.hackerrank.com/challenges/game-of-kyles

## Problem Statement

Bowling refers to a sport in which a player rolls or throws a bowling ball towards a group of pins. The target is usually to knock down the pins at the end of a lane.  

Rules have been slightly modified for this problem. Now there are $N$ pins and all the pins are arranged in a horizontal line, instead of a triangular formation. Two players have to play this game, and they alternate their turns. Whoever knocks down the last pin(s) will be declared the winner.  

You and your friends are playing this game. Both of you have become proficient at the sport and can knock down any single pin, or any two adjacent pins at one throw of a bowling ball. You have already played some of the shots. Suddenly you realize that it is possible to find whether this game can be won or not. And luckily it's your turn right now.  

A configuration is represented by a string consisting of latin letters `X` and `I`, where `I` represents a position containing a pin, and `X` represents a position where a pin has been knocked down. An example of such a configuration is shown in the image below. Here $N = 13$, and $2^{nd}$ pin has been knocked down already.  

![Pins](http://hr-challenge-images.s3.amazonaws.com/2526/pins.png)

It's representation will be `IXIIIIIIIIIII`.

You are given the current configuration of the pins. If both of you play optimally, find whether you can win this game or not. 

## Input Format

The first line will contain an integer, $T$, which represents the number of test cases. Then $T$ test cases follows.  
For each test case, the first line contains an integer $N$, which represents the number of pins before the start of the game. And the second line contains a string of $N$ letters, where each letter is either `I` or `X`.  

## Output Format

For each test case, print `WIN` if you can win this game, otherwise print `LOSE`.  

## Constraints

+ $1 \le T \le 1000$  
+ $1 \le N \le 300$  
+ Each letter of string (representing configuration) is either `I` or `X`.  
+ There will be at least one `I` in the string.   

**Note:**   
- A player has to knock down at least one pin in his chance.   
- Both players play optimally.  

## Sample Input

4
4
IXXI
4
XIIX
5
IIXII
5
IIIII

## Sample Output

LOSE
WIN
LOSE
WIN

## Explanation

Test Case #00: As the  pins are not adjacent, they can't be knocked down in a single chance. Therefore you can only knock down one of the two pins. Then in next chance, your friend will knock down the last pin.

Test Case #01: You can knock down both the adjacent pins in your first turn.

Test Case #02: You can knock one or two pins from either side. Your friend can just copy your move on the other side and will be able to finish the game.

Test Case #03: You can knock middle pin, thus resulting into configuration IIXII for your friend. Now this configuration is the same as the previous test case. The difference is that now it is your friend's chance and you can copy his shot on the other side.
