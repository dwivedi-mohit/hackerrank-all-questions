# Lecture Notes

---

| Field | Value |
|---|---|
| **Slug** | `lecture-notes` |
| **Domain** | misc |
| **Difficulty** | Easy |
| **Score** | 20 |
| **Contest** | 101hack41 |
| **URL** | https://www.hackerrank.com/challenges/lecture-notes |

---

## Preview

Simple string problem

## Problem Statement

Alex has a habit of falling asleep during lectures! In order to complete the day's homework, he must determine if he has any friends that stayed awake so he can borrow their notes.

There are $n$ other students in Alex's class, and each student has a distinct ID number from $1$ to $n$. You are  given a string, $s$, of $n$ binary characters where the $i^{th}$ character denotes whether the $i^{th}$ student slept during the lecture or not. If the $i^{th}$ character is a $0$, then the $i^{th}$ student stayed awake and took notes; otherwise, the $i^{th}$ character is a $1$ which indicates the student fell asleep and did not take notes.		

Alex has $k$ friends in his class and you are given a list of integers corresponding to their respective ID numbers. If Alex can borrow the lecture notes *from one of his friends*, print `YES`; otherwise, print `NO`.

## Input Format

The first line contains two space-separated integers denoting the respective values of $n$ (the number of students in Alex's class) and $k$ (Alex's number of friends in the class).			
The second line contains a single binary string (i.e., $0$'s and $1$'s) of length $n$. If the $i^{th}$ character is a $1$, then Alex can't get notes from them; otherwise, it's a $0$, indicating the $i^{th}$ student took lecture notes.		
The next line contains $k$ distinct space-separated integers where each integer denotes the ID number of one of Alex's friends.

## Output Format

Print `YES` on a new line if Alex can get the lecture notes *from one of his friends*; otherwise, print `NO`.

## Constraints

- $1 \le k \le n \le 1000$

## Sample Tests

### Test 1

```
3 2
101
1 3
```

### Test 2

```
NO
```
