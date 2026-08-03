# Matching Zero Or More Repetitions

---

| Field | Value |
|---|---|
| **Slug** | `matching-zero-or-more-repetitions` |
| **Domain** | regex |
| **Difficulty** | Easy |
| **Score** | 20 |
| **URL** | https://www.hackerrank.com/challenges/matching-zero-or-more-repetitions |

---

## Preview

Match zero or more repetitions of character/character class/group using the * symbol in regex.

## Problem Statement

__$*$__ 

The __*__ tool will match zero or more repetitions of character/character class/group.

<img src="https://s3.amazonaws.com/hr-challenge-images/14523/1449644741-70706a36e1-ach12.png" title="ach12.png" />
<sub>$$In \ the \ above \ image, \ the \ Regex \ Pattern \ is \ matched \ with \ the \ Test \ String. $$</sub>

**For Example**:

__w\*__ : It will match the character `w` $0$ or more times. 

__[xyz]\*__ : It will match the characters `x`, `y` or `z` $0$ or more times. 

__\d\*__ : It will match any digit $0$ or more times. 

___
__Task__ 

You have a test string $S$. 

Your task is to write a regex that will match $S$ using the following conditions: 

- $S$ should begin with $2$ or more __`digits`__.
- After that, $S$ should have $0$ or more __`lowercase letters`__. 
- $S$ should end with $0$ or more __`uppercase letters`__

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
lowercase letters
```

### Test 7

```
uppercase letters
```

### Test 8

```
_________
```
