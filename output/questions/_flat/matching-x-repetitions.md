# Matching {x} Repetitions

---

| Field | Value |
|---|---|
| **Slug** | `matching-x-repetitions` |
| **Domain** | regex |
| **Difficulty** | Easy |
| **Score** | 20 |
| **URL** | https://www.hackerrank.com/challenges/matching-x-repetitions |

---

## Preview

Match exactly x repetitions using the tool {x}.

## Problem Statement

__$\textsf{{x}}$__ 

The tool __{x}__ will match exactly $x$ repetitions of character/character class/groups.

<img src="https://s3.amazonaws.com/hr-challenge-images/14525/1449644438-27dbaa69fd-ach10.png" title="ach10.png" />
<sub>$$In \ the \ above \ image, \ the \ Regex \ Pattern \ is \ matched \ with \ the \ Test \ String. $$</sub>

**For Example**:

__w{3}__ : It will match the character `w` exactly $3$ times. 

__[xyz]{5}__ : It will match the string of length $5$ consisting of characters {`x`, `y`, `z`}. For example it will match `xxxxx`, `xxxyy` and `xyxyz`.		
__\d{4}__ : It will match any digit exactly $4$ times.

___
__Task__ 

You have a test string $S$. 

Your task is to write a regex that will match $S$ using the following conditions: 

- $S$ must be of length equal to __`45`__.
- The first $40$ characters should consist of __`letters`__(both lowercase and uppercase), or of __`even digits`__.

- The last $5$ characters should consist of __`odd digits`__ or __`whitespace characters`__.

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
xxxxx
```

### Test 6

```
xxxyy
```

### Test 7

```
xyxyz
```

### Test 8

```
45
```

### Test 9

```
letters
```

### Test 10

```
even digits
```

### Test 11

```
odd digits
```

### Test 12

```
whitespace characters
```

### Test 13

```
_________
```
