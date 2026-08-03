# 'Awk' - 2

---

| Field | Value |
|---|---|
| **Slug** | `awk-2` |
| **Domain** | shell |
| **Difficulty** | Medium |
| **Score** | 2 |
| **URL** | https://www.hackerrank.com/challenges/awk-2 |

---

## Preview

Let's play around with 'awk'.

## Problem Statement

**Objective** <br>
In this challenge, we practice using the *awk* command for text-munging and data processing tasks. 

**Resources** <br>
The *awk* interpreter may be used for a lot of text-munging and data-processing tasks that require some quick scripting work. 



The following links show examples with *awk*: <br> 
[Print Examples](http://www.thegeekstuff.com/2010/01/awk-introduction-tutorial-7-awk-print-examples/)

[Conditionals with Awk](http://www.thegeekstuff.com/2010/02/awk-conditional-statements/) 


**Task**

You are given a file with four space separated columns containing the scores of students in three subjects. The first column contains a single character ($A-Z$), the student identifier. The next three columns have three numbers each. The numbers are between $0$ and $100$, both inclusive. These numbers denote the scores of the students in English, Mathematics, and Science, respectively. 

Your task is to identify whether each of the students has passed or failed.

A student is considered to have passed if (s)he has a score $50$ or more in *each* of the three subjects.

## Input Format

There will be no more than $10$ rows of data. <br>
Each line will be in the following format: <br>
*[Identifier]<space>[English Score]<space>[Math Score]<space>[Science Score]*

## Output Format

Depending on the scores, display the following for each student:

	[Identifier] : [Pass] 
  or


	[Identifier] : [Fail]

## Sample Tests

### Test 1

```
[Identifier] : [Pass]
```

### Test 2

```
[Identifier] : [Fail]
```

### Test 3

```
A 25 27 50
B 35 37 75
C 75 78 80
D 99 88 76
```

### Test 4

```
A : Fail
B : Fail
C : Pass
D : Pass
```
