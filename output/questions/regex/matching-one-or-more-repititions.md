# Matching One Or More Repetitions

---

| Field | Value |
|---|---|
| **Slug** | `matching-one-or-more-repititions` |
| **Domain** | regex |
| **Difficulty** | Easy |
| **Score** | 20 |
| **URL** | https://www.hackerrank.com/challenges/matching-one-or-more-repititions |

---

## Preview

Match zero or more repetitions of character/character class/group with the + symbol.

## Problem Statement

__$+$__ 

The __+__ tool will match one or more repetitions of character/character class/group.

<img src="https://s3.amazonaws.com/hr-challenge-images/14524/1449644856-94a5bdd2ae-ach13.png" title="ach13.png" />
<sub>$$In \ the \ above \ image, \ the \ Regex \ Pattern \ is \ matched \ with \ the \ Test \ String. $$</sub>

**For Example**:

__w\+__ : It will match the character `w` $1$ or more times. 

__[xyz]\+__ : It will match the character `x`, `y` or `z` $1$ or more times.<br>
__\d\+__ : It will match any digit $1$ or more times. 

___
__Task__ 

You have a test string $S$. 

Your task is to write a regex that will match $S$ using the following conditions:


- $S$ should begin with $1$ or more __`digits`__.
- After that, $S$ should have $1$ or more __`uppercase letters`__. 
- $S$ should end with $1$ or more __`lowercase letters`__.

__Note__


This is a regex only challenge. You are not required to write any code. 

You have to fill the regex pattern in the blank (`_________`).

## Sample Tests

### Test 1

```
w
```

### Test 2

```
x
```

### Test 3

```
y
```

### Test 4

```
z
```

### Test 5

```
digits
```

### Test 6

```
uppercase letters
```

### Test 7

```
lowercase letters
```

### Test 8

```
_________
```
