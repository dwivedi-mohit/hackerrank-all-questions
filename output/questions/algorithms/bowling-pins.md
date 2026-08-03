# Bowling Pins

---

| Field | Value |
|---|---|
| **Slug** | `bowling-pins` |
| **Domain** | algorithms |
| **Difficulty** | Hard |
| **Score** | 60 |
| **URL** | https://www.hackerrank.com/challenges/bowling-pins |

---

## Preview

Determine the winner in a game of bowling with modified rules.

## Problem Statement

Bowling is a sport in which a player rolls a bowling ball towards a group of pins, the target being to knock down the pins at the end of a lane.
_____________________________________________________________________________________

In this challenge, the rules of the game are slightly modified. Now, there are a given number of pins, and the pins are arranged in a horizontal line instead of a triangular formation. Two players have to play this game, taking alternate turns. Whoever knocks down the last pin(s) will be declared the winner.


You are playing this game with your friend, and both of you have become proficient at it. You can knock down any single pin, or any two adjacent pins at one throw of a bowling ball, however, these are the only moves that you can perform. Some moves have already been played. Suddenly, you realize that it is possible to determine whether this game can be won or not, assuming optimal play. And luckily it's your turn right now.


A configuration is represented by a string consisting of the letters `X` and `I`, where: 

- `I` represents a position containing a pin.
- `X` represents a position where a pin has been knocked down.
 

An example of such a configuration is shown in the image below. Here, the number of pins is $13$, and the $2^\text{nd}$ pin has already been knocked down.


![Pins](http://hr-challenge-images.s3.amazonaws.com/2526/pins.png)

Its representation will be `IXIIIIIIIIIII`.

Complete the function `isWinning` that takes the number of pins and the configuration of the pins as input, and return `WIN` or `LOSE` based on whether or not you will win. 

Given the current configuration of the pins, if both of you play optimally, determine whether you will win this game or not. 

**Note** 


- A player has to knock down at least one pin in his turn.
- Both players play optimally.

## Input Format

The first line contains an integer, $t$, the number of test cases. Then $t$ test cases follow.


For each test case, the first line contains a single integer $n$, denoting the number of pins. The second line contains a string of $n$ letters, where each letter is either `I` or `X`.

## Output Format

For each test case, print a single line containing `WIN` if you will win this game, otherwise `LOSE`.

## Constraints

- $1 \le t \le 1000$

- $1 \le n \le 300$

- Each letter of the string (representing the configuration) is either `I` or `X`.

- There will be at least one `I` in the string.

## Sample Tests

### Test 1

```
4
4
IXXI
4
XIIX
5
IIXII
5
IIIII
```

### Test 2

```
LOSE
WIN
LOSE
WIN
```
