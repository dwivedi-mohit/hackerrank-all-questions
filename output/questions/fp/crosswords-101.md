# Crosswords-101

---

| Field | Value |
|---|---|
| **Slug** | `crosswords-101` |
| **Domain** | fp |
| **Difficulty** | Advanced |
| **Score** | 30 |
| **URL** | https://www.hackerrank.com/challenges/crosswords-101 |

---

## Preview

Given a Crossword Grid, and a set of words, fill up the crossword.

## Problem Statement

A $10 \times 10$ Crossword grid is provided to you, along with a set of words (or names of places) which need to be filled into the grid.

The cells in the grid are initially, either `+` signs or `-` signs.

Cells marked with a `+` have to be left as they are. Cells marked with a `-` need to be filled up with an appropriate character.

## Input Format

The input contains $10$ lines, each with $10$ characters (which will be either + or - signs).

After this follows a set of words (typically nouns and names of places), separated by semi-colons (;).

## Output Format

Position the words appropriately in the $10 \times 10$ grid, and then display the $10\times 10$ grid as the output. So, your output will consist of $10$ lines with $10$ characters each.

## Constraints

There will be no more than ten words. Words will only be composed of upper-case `A-Z` characters. There will be no punctuation (hyphen, dot, etc.) in the words.

## Sample Tests

### Test 1

```
+-++++++++
+-++++++++
+-++++++++
+-----++++
+-+++-++++
+-+++-++++
+++++-++++
++------++
+++++-++++
+++++-++++
LONDON;DELHI;ICELAND;ANKARA
```

### Test 2

```
+L++++++++
+O++++++++
+N++++++++
+DELHI++++
+O+++C++++
+N+++E++++
+++++L++++
++ANKARA++
+++++N++++
+++++D++++
```

### Test 3

```
+-++++++++
+-++++++++
+-------++
+-++++++++
+-++++++++
+------+++
+-+++-++++
+++++-++++
+++++-++++
++++++++++
AGRA;NORWAY;ENGLAND;GWALIOR
```

### Test 4

```
+E++++++++
+N++++++++
+GWALIOR++
+L++++++++
+A++++++++
+NORWAY+++
+D+++G++++
+++++R++++
+++++A++++
++++++++++
```
