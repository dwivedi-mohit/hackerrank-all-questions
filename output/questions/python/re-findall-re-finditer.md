# Re.findall() & Re.finditer()

---

| Field | Value |
|---|---|
| **Slug** | `re-findall-re-finditer` |
| **Domain** | python |
| **Difficulty** | Easy |
| **Score** | 20 |
| **URL** | https://www.hackerrank.com/challenges/re-findall-re-finditer |

---

## Preview

Find all the pattern matches using the expressions re.findall() and re.finditer().

## Problem Statement

###<sub>[re.findall()](https://docs.python.org/2/library/re.html#re.findall)</sub>

The expression *re.findall()* returns all the non-overlapping matches of patterns in a string as a list of strings.

<sub>__Code__</sub>

    >>> import re
    >>> re.findall(r'\w','http://www.hackerrank.com/')
    ['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']
  

###<sub>[re.finditer()](https://docs.python.org/2/library/re.html#re.finditer)</sub> 

The expression *re.finditer()* returns an iterator yielding `MatchObject` instances over all non-overlapping matches for the *re* pattern in the string.

<sub>__Code__</sub>

	>>> import re
    >>> re.finditer(r'\w','http://www.hackerrank.com/')
	<callable-iterator object at 0x0266C790>
    >>> map(lambda x: x.group(),re.finditer(r'\w','http://www.hackerrank.com/'))
	['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']
  

---
__Task__

You are given a string $S$. It consists of alphanumeric characters, spaces and symbols(`+`,`-`).

Your task is to find all the substrings of $S$ that contains $2$ or more vowels.

Also, these substrings must lie in between $2$ consonants and should contain vowels only.

<sub>__Note :

Vowels are defined as: `AEIOU` and `aeiou`.

Consonants are defined as: `QWRTYPSDFGHJKLZXCVBNM` and `qwrtypsdfghjklzxcvbnm`__.</sub>

## Input Format

A single line of input containing string $S$.

__Constraints__

$0 < len(S) < 100$

## Output Format

Print the matched substrings in their order of occurrence on separate lines. 

If no match is found, print `-1`.

## Sample Tests

### Test 1

```
>>> import re
>>> re.findall(r'\w','http://www.hackerrank.com/')
['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']
```

### Test 2

```
>>> import re
>>> re.finditer(r'\w','http://www.hackerrank.com/')
<callable-iterator object at 0x0266C790>
>>> map(lambda x: x.group(),re.finditer(r'\w','http://www.hackerrank.com/'))
['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']
```

### Test 3

```
rabcdeefgyYhFjkIoomnpOeorteeeeet
```

### Test 4

```
ee
Ioo
Oeo
eeeee
```
