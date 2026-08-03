# Group(), Groups() & Groupdict()

---

| Field | Value |
|---|---|
| **Slug** | `re-group-groups` |
| **Domain** | python |
| **Difficulty** | Easy |
| **Score** | 20 |
| **URL** | https://www.hackerrank.com/challenges/re-group-groups |

---

## Preview

Using group(), groups(), and groupdict(), find the subgroup(s) of the match.

## Problem Statement

###<sub>[group()](https://docs.python.org/2/library/re.html#re.MatchObject.group)</sub>

A *group()* expression returns one or more subgroups of the match.

<sub>__Code__</sub>
	
    >>> import re
    >>> m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
    >>> m.group(0)       # The entire match 
    'username@hackerrank.com'
    >>> m.group(1)       # The first parenthesized subgroup.
    'username'
    >>> m.group(2)       # The second parenthesized subgroup.
    'hackerrank'
    >>> m.group(3)       # The third parenthesized subgroup.
    'com'
    >>> m.group(1,2,3)   # Multiple arguments give us a tuple.
    ('username', 'hackerrank', 'com')

---
###<sub>[groups()](https://docs.python.org/2/library/re.html#re.MatchObject.groups)</sub>
A *groups()* expression returns a tuple containing all the subgroups of the match.

<sub>__Code__</sub>

    >>> import re
    >>> m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
    >>> m.groups()
	('username', 'hackerrank', 'com')
  

---
###<sub>[groupdict()](https://docs.python.org/2/library/re.html#re.MatchObject.groupdict)</sub>
A *groupdict()* expression returns a dictionary containing all the named subgroups of the match, keyed by the subgroup name.

<sub>__Code__</sub>

    >>> m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')
    >>> m.groupdict()
    {'website': 'hackerrank', 'user': 'myname', 'extension': 'com'}
  

---
__Task__


You are given a string $S$.

Your task is to find the first occurrence of an alphanumeric character in $S$ (read from left to right) that has consecutive repetitions.

## Input Format

A single line of input containing the string $S$.

__Constraints__

$0 < len(S) < 100$

## Output Format

Print the first occurrence of the repeating character. If there are no repeating characters, print `-1`.

## Sample Tests

### Test 1

```
>>> import re
>>> m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
>>> m.group(0) # The entire match 
'username@hackerrank.com'
>>> m.group(1) # The first parenthesized subgroup.
'username'
>>> m.group(2) # The second parenthesized subgroup.
'hackerrank'
>>> m.group(3) # The third parenthesized subgroup.
'com'
>>> m.group(1,2,3) # Multiple arguments give us a tuple.
('username', 'hackerrank', 'com')
```

### Test 2

```
>>> import re
>>> m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
>>> m.groups()
('username', 'hackerrank', 'com')
```

### Test 3

```
>>> m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')
>>> m.groupdict()
{'website': 'hackerrank', 'user': 'myname', 'extension': 'com'}
```

### Test 4

```
..12345678910111213141516171820212223
```

### Test 5

```
1
```
