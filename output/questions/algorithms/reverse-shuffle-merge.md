# Reverse Shuffle Merge

---

| Field | Value |
|---|---|
| **Slug** | `reverse-shuffle-merge` |
| **Domain** | algorithms |
| **Difficulty** | Advanced |
| **Score** | 50 |
| **URL** | https://www.hackerrank.com/challenges/reverse-shuffle-merge |

---

## Preview

Given a string, find the lexicographically smallest substring that satisfies the given conditions.

## Problem Statement

Given a string, $A$, we define some operations on the string as follows:

>a. _$reverse(A)$_ denotes the string obtained by reversing string $A$. Example: $\texttt{reverse("abc") = "cba"}$

<br>

>b. _$shuffle(A)$_ denotes any string that's a permutation of string $A$. Example: $\texttt{shuffle("god") ∈  ['god', 'gdo', 'ogd', 'odg', 'dgo', 'dog']}$ 

<br>

>c. _$merge(A1,A2)$_ denotes any string that's obtained by interspersing the two strings $A1$ & $A2$, maintaining the order of characters in both. For example, $\texttt{A1 = "abc"}$ & $\texttt{A2 = "def"}$, one possible result of $merge(A1,A2)$ could be $\texttt{"abcdef"}$, another could be $\texttt{"abdecf"}$, another could be $\texttt{"adbecf"}$ and so on.


Given a string $s$ such that $\texttt{s ∈ merge(reverse(A), shuffle(A))}$ for some string $A$, find the [lexicographically](http://en.wikipedia.org/wiki/Lexicographical_order) smallest $A$.

For example, $s = abab$.  We can split it into two strings of $ab$.  The reverse is $ba$ and we need to find a string to shuffle in to get $abab$.  The middle two characters match our reverse string, leaving the $a$ and $b$ at the ends.  Our shuffle string needs to be $ab$.  Lexicographically $ab \lt ba$, so our answer is $ab$.


**Function Description**

Complete the *reverseShuffleMerge* function in the editor below.  It must return the lexicographically smallest string fitting the criteria.


reverseShuffleMerge has the following parameter(s):

- *s*: a string

## Input Format

A single line containing the string $s$.

## Output Format

Find and return the string which is the lexicographically smallest valid $A$.

## Constraints

+ $s$ contains only lower-case English letters, *ascii[a-z]*

+ $1 \le |s| \le 10000$

## Sample Tests

### Test 1

```
eggegg
```

### Test 2

```
egg
```

### Test 3

```
abcdefgabcdefg
```

### Test 4

```
agfedcb
```

### Test 5

```
aeiouuoiea
```

### Test 6

```
aeiou
```
