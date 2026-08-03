# The Trigram

---

| Field | Value |
|---|---|
| **Slug** | `the-trigram` |
| **Domain** | ai |
| **Difficulty** | Easy |
| **Score** | 10 |
| **URL** | https://www.hackerrank.com/challenges/the-trigram |

---

## Preview

Identify the most frequent trigram in the provided chunk of text.

## Problem Statement

Given a large chunk of text, identify the most frequently occurring trigram in it. If there are multiple trigrams with the same frequency, then print the one which occurred first.

Assume that trigrams are groups of three consecutive words in the same sentence which are separated by nothing but a single space and are case insensitive. The size of the input will be less than 10 kilobytes.


	Input: I love games. I love to code.
	Here "games I love" is not a trigram because all the three words in trigram should be from the 
    same sentence.

## Input Format

A large chunk of text.

## Output Format

The most popular trigram - three words, with nothing but a space in between them. The output should be in lowercase. (If a trigram ends with dot then you should remove the dot.)

## Constraints

The input contains lowercase or uppercase alphabets, whitespaces and dots.

## Sample Tests

### Test 1

```
Input: I love games. I love to code.
Here "games I love" is not a trigram because all the three words in trigram should be from the 
same sentence.
```

### Test 2

```
I came from the moon. He went to the other room. She went to the drawing room.
```

### Test 3

```
went to the
```

### Test 4

```
I love to dance. I like to dance I. like to play chess.
```

### Test 5

```
i love to
```
