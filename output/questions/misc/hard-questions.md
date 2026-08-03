# Hard Questions

---

| Field | Value |
|---|---|
| **Slug** | `hard-questions` |
| **Domain** | misc |
| **Difficulty** | Easy |
| **Score** | 15 |
| **Contest** | 101hack50 |
| **URL** | https://www.hackerrank.com/challenges/hard-questions |

---

## Preview

Determine how well Vincent could have performed in a hard exam.

## Problem Statement

Vincent and Catherine are classmates who just took an exam in Math 55. The exam consists of $n$ multiple-choice questions. Each question has $5$ choices, each of which is represented by a single capital letter `A`, `B`, `C`, `D` and `E`. Each question has exactly one correct answer. A student's score is equal to the number of questions he/she correctly answered.

This was the hardest exam they've ever taken! No one was ever sure of their answer even after the exam, and some students weren't even able to answer all the questions. The questions were so hard that Vincent and Catherine strongly believe that *they can't both be correct in any question*. In other words, for each question, they believe that one or both of them must be incorrect.


Now, Vincent wants to know how well he could have performed in the exam. Given the answers of Vincent and Catherine, find the maximum score that Vincent could have gotten, *assuming that they can't both have gotten the correct answer to any particular question*.

## Input Format

The first line contains a single integer $n$, the number of questions.

The second line contains a string of length $n$ denoting the answers of Vincent.

The third line contains a string of length $n$ denoting the answers of Catherine.


Each answer string consists of only the characters `A`, `B`, `C`, `D`, `E` and `.` (dot character).

- If the $i$'th character is `A`, `B`, `C`, `D` or  `E`, then this character represents the student's answer for the $i$'th question.

- If the $i$'th character is `.`, then this means the student gave no answer for the $i$'th question.

## Output Format

Print a single line containing a single integer denoting the maximum score that Vincent could have gotten assuming that they can't both have gotten the correct answer to any particular question.

## Constraints

- $1 \le n \le 100$

## Sample Tests

### Test 1

```
24
CCACCBAEBAAAAAAAA.......
CCACCBAEBAAAAAAAA.......
```

### Test 2

```
0
```

### Test 3

```
7
ACCEDED
DECADE.
```

### Test 4

```
4
```

### Test 5

```
11
BEE..ADDED.
CAB.DAD.DEE
```

### Test 6

```
6
```
