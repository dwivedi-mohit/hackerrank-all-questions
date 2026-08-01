# Mars Exploration

- **Domain:** c
- **Difficulty:** Easy
- **Max Score:** 15
- **Success Ratio:** 0.9405561803149918
- **Total Submissions:** 176957
- **Solved Count:** 166438
- **URL:** https://www.hackerrank.com/challenges/mars-exploration

## Problem Statement

A space explorer's ship crashed on Mars! They send a series of `SOS` messages to Earth for help. 

<img src="https://s3.amazonaws.com/hr-challenge-images/16032/1453204202-9e3fd295bb-NASA_Mars_Rover.jpg" title="NASA_Mars_Rover.jpg" />

Letters in some of the `SOS` messages are altered by cosmic radiation during transmission. Given the signal received by Earth as a string, $s$, determine how many letters of the `SOS` message have been changed by radiation.

**Example**  

$s = \text{'SOSTOT'}$  

The original message was `SOSSOS`.  Two of the message's characters were changed in transit.  

**Function Description**

Complete the *marsExploration* function in the editor below.  

marsExploration has the following parameter(s):

- *string s:* the string as received on Earth  

**Returns**  

- *int:* the number of letters changed during transmission  

## Input Format

There is one line of input: a single string, $s$. 


## Output Format

 


## Constraints

* $1 \le \text{ length of }s \le 99$
* $ \text{ length of }s \text{ modulo } \ 3=0$
* $s$ will contain only uppercase English letters, ascii[A-Z].

## Sample Input

SOSSPSSQSSOR

## Sample Output

3

## Explanation

= SOSSPSSQSSOR, and signal length . They sent  SOS messages (i.e.: ).

Expected signal: SOSSOSSOSSOS
Recieved signal: SOSSPSSQSSOR
Difference:          X  X   X
