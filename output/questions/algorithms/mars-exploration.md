# Mars Exploration

---

| Field | Value |
|---|---|
| **Slug** | `mars-exploration` |
| **Domain** | algorithms |
| **Difficulty** | Easy |
| **Score** | 15 |
| **URL** | https://www.hackerrank.com/challenges/mars-exploration |

---

## Preview

Save Our Ship!

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

## Constraints

* $1 \le \text{ length of }s \le 99$
* $ \text{ length of }s \text{ modulo } \ 3=0$
* $s$ will contain only uppercase English letters, ascii[A-Z].

## Sample Tests

### Test 1

```
SOSSPSSQSSOR
```

### Test 2

```
3
```

### Test 3

```
Expected signal: SOSSOSSOSSOS
Recieved signal: SOSSPSSQSSOR
Difference: X X X
```

### Test 4

```
SOSSOT
```

### Test 5

```
1
```

### Test 6

```
Expected Signal: SOSSOS 
Received Signal: SOSSOT
Difference: X
```

### Test 7

```
SOSSOSSOS
```

### Test 8

```
0
```
