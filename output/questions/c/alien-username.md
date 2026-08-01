# Alien Username

- **Domain:** c
- **Difficulty:** Easy
- **Max Score:** 10
- **Success Ratio:** 0.9528025437994887
- **Total Submissions:** 16039
- **Solved Count:** 15282
- **URL:** https://www.hackerrank.com/challenges/alien-username

## Problem Statement

In a galaxy far, far away, on a planet different from ours, each computer username uses the following format:

1. It *must* begin with either an underscore, `_` (ASCII value $95$), or a period, `.` (ASCII value $46$).
2. The first character *must* be immediately followed by *one or more* digits in the range $0$ through $9$.
3. After some number of digits, there *must* be $0$ or more English letters (uppercase and/or lowercase).
4. It *may* be terminated with an optional `_` (ASCII value $95$). Note that if it's not terminated with an underscore, then there should be no characters after the sequence of $0$ or more English letters.

Given $n$ strings, determine which ones are valid alien usernames. If a string is a valid alien username, print `VALID` on a new line; otherwise, print `INVALID`.

## Input Format

The first line contains a single integer, $n$, denoting the number of usernames.		
Each line $i$ of the $n$ subsequent lines contains a string denoting an alien username to validate.

## Output Format

Iterate through each of the $n$ strings in order and determine whether or not each string is a valid alien username. If a username is a valid alien username, print `VALID` on a new line; otherwise, print `INVALID`.

## Constraints

- $1 \le n \le 100$

## Sample Input

_0898989811abced_
_abce
_09090909abcD0

## Sample Output

VALID
INVALID
INVALID

## Explanation

We validate the following three usernames:

- _0898989811abced_ is valid as it satisfies the requirements specified above. Thus, we print VALID.

- _abce is invalid as the beginning _ is not followed by one or more digits. Thus, we print INVALID.

- _09090909abcD0 is invalid as the sequence of English alphabetic letters is immediately followed by a number. Thus, we print INVALID.
