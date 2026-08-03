# Word Order

---

| Field | Value |
|---|---|
| **Slug** | `word-order` |
| **Domain** | python |
| **Difficulty** | Medium |
| **Score** | 50 |
| **URL** | https://www.hackerrank.com/challenges/word-order |

---

## Preview

List the number of occurrences of the words in order.

## Problem Statement

You are given $n$ words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification. 

**Note:** Each input line ends with a **"\n"** character.

**Constraints:**

$1\le n\le 10^5$

The sum of the lengths of all the words do not exceed $10^6$

All the words are composed of lowercase English letters only.

## Input Format

The first line contains the integer, $n$.

The next $n$ lines each contain a word.

## Output Format

Output $2$ lines.

On the first line, output the number of distinct words from the input.

On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

## Sample Tests

### Test 1

```
4
bcdef
abcdefg
bcde
bcdef
```

### Test 2

```
3
2 1 1
```
