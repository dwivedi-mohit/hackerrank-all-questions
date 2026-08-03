# Saying Hi

---

| Field | Value |
|---|---|
| **Slug** | `saying-hi` |
| **Domain** | regex |
| **Difficulty** | Easy |
| **Score** | 15 |
| **URL** | https://www.hackerrank.com/challenges/saying-hi |

---

## Preview

Use a regex to print all the lines that start with "hi " but are not immediately followed by a 'd' or 'D'.

## Problem Statement

Given a sentence, $s$, write a RegEx to match the following criteria:	

1. The first character must be the letter $\textit{H}$ or $\textit{h}$.
2. The second character must be the letter $\textit{I}$ or $\textit{i}$.
3. The third character must be a single space (i.e.: $\textit{\\s}$). 
4. The fourth character *must not* be the letter $\textit{D}$ or $\textit{d}$.

Given $n$ lines of sentences as input, print each sentence matching your RegEx on a new line.

## Input Format

The first line contains an integer, $n$, denoting the number of lines of sentences.		
Each of the $n$ subsequent lines contains some sentence $s$ you must match.

## Output Format

Find each sentence, $s$, satisfying the RegEx criteria mentioned above, and print it on a new line.

## Constraints

- $1 \le n \le 10 $
- Each sentence, $s$, contains $1$ to $10$ words.
- Each word/token in a sentence is comprised only of upper and lowercase English letters.

## Sample Tests

### Test 1

```
5
Hi Alex how are you doing
hI dave how are you doing
Good by Alex
hidden agenda
Alex greeted Martha by saying Hi Martha
```

### Test 2

```
Hi Alex how are you doing
```
