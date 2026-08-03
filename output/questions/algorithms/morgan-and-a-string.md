# Morgan and a String

---

| Field | Value |
|---|---|
| **Slug** | `morgan-and-a-string` |
| **Domain** | algorithms |
| **Difficulty** | Expert |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/morgan-and-a-string |

---

## Preview

Find the lexicographically minimal string that can be formed by the combination of two strings.

## Problem Statement

Jack and Daniel are friends. Both of them like letters, especially uppercase ones.

They are cutting uppercase letters from newspapers, and each one of them has his collection of letters stored in a stack. 

One beautiful day, Morgan visited Jack and Daniel. He saw their collections. He wondered what is the lexicographically minimal string made of those two collections. He can take a letter from a collection only when it is on the top of the stack.  Morgan wants to use all of the letters in their collections.


As an example, assume Jack has collected $a = [A,C,A]$ and Daniel has $b = [B,C,F]$.  The example shows the top at index $0$ for each stack of letters. Assemble the string  as follows:


```
Jack	Daniel	result
ACA	BCF
CA	BCF	A
CA	CF	AB
A	CF	ABC
A	CF	ABCA
    	F	ABCAC
    		ABCACF
```
**Note** the choice when there was a tie at `CA` and `CF`.

**Function Description**


Complete the *morganAndString* function in the editor below.


morganAndString has the following parameter(s):


- *string a*: Jack's letters, top at index $0$

- *string b*: Daniel's letters, top at index $0$


Returns

- *string*: the completed string

## Input Format

The first line contains the an integer $t$, the number of test cases.


The next $t$ pairs of lines are as follows:

- The first line contains string $a$

- The second line contains string $b$.

## Constraints

- $1 \le T \le 5$

- $1 \le |a|, |b| \le 10^5$

- $a$ and $b$ contain upper-case letters only, ascii[A-Z].

## Sample Tests

### Test 1

```
Jack
Daniel
result
ACA
BCF
CA
BCF
A
CA
CF
AB
A
CF
ABC
A
CF
ABCA
F
ABCAC
ABCACF
```

### Test 2

```
2
JACK
DANIEL
ABACABA
ABACABA
```

### Test 3

```
DAJACKNIEL
AABABACABACABA
```
