# Matrix Script

---

| Field | Value |
|---|---|
| **Slug** | `matrix-script` |
| **Domain** | python |
| **Difficulty** | Hard |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/matrix-script |

---

## Preview

Decode the Matrix.

## Problem Statement

Neo has a complex *matrix script*. The *matrix script* is a $N $ X $ M$ grid of strings. It consists of alphanumeric characters, spaces and  symbols (!,@,#,$,%,&).

<img src="https://s3.amazonaws.com/hr-challenge-images/12524/1442753362-1075bd12d9-Capture.JPG" title="Capture.JPG" />

To decode the script, Neo needs to read each column and select only the alphanumeric characters and connect them. Neo reads the column from top to bottom and starts reading from the leftmost column.

If there are symbols or spaces between two alphanumeric characters of the decoded script, then Neo replaces them with a *single* space '$ \ $' for better readability.


Neo feels that there is no need to use '`if`' conditions for decoding.

*Alphanumeric characters* consist of: [A-Z, a-z, and 0-9].

## Input Format

The first line contains space-separated integers $N$ (rows) and $M$ (columns) respectively.

The next $N$ lines contain the row elements of the *matrix script*. 

__Constraints__


$0 < N, M < 100$


**Note**: A $0$ score will be awarded for using '`if`' conditions in your code.

## Output Format

Print the decoded *matrix script*.

## Sample Tests

### Test 1

```
7 3
Tsi
h%x
i #
sM 
$a 
#t%
ir!
```

### Test 2

```
This is Matrix# %!
```

### Test 3

```
This$#is% Matrix# %!
```

### Test 4

```
This is Matrix# %!
```
