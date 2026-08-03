# Recover the Arrays

---

| Field | Value |
|---|---|
| **Slug** | `recover-the-array` |
| **Contest** | hourrank-19 |
| **Difficulty** | Easy |
| **Score** | 20 |
| **URL** | https://www.hackerrank.com/challenges/recover-the-array |

---

## Problem Statement

Dani is writing some arrays in her favorite text editor HackerEdit. Each line of the document describes an array in the following format:

$$e\ a_0\ a_1\ ...\ a_{e-1} $$

Here $e$ is the array's number of elements and $a_0, a_1, \ldots, a_{e-1}$ are its contents.

Dani wrote $m$ arrays in the file and left for lunch. To her dismay, her little brother Nik deleted all the newline characters from the file while she was gone! For example, consider the file in the table below:


![image](https://s3.amazonaws.com/hr-assets/0/1490948889-8b0d9659ac-recover4.png)

Given the contents of Dani's HackerEdit file with all the newlines removed, find the value of $m$ (i.e., the number of arrays in the initial file).

## Input Format

The first line contains an integer denoting $n$ (the number of integers in the file).	
The second line contains $n$ space-separated integers describing each respective value in the file.

## Output Format

Print a single integer denoting $m$.

## Constraints

* $2 \le n \le 10^5$
