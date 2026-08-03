# The Ultimate Question

---

| Field | Value |
|---|---|
| **Slug** | `the-ultimate-question` |
| **Domain** | misc |
| **Difficulty** | Easy |
| **Score** | 15 |
| **Contest** | indeed-prime-codesprint |
| **URL** | https://www.hackerrank.com/challenges/the-ultimate-question |

---

## Preview

Given three integers, you have to put two operators between them so that an equation becomes true.

## Problem Statement

[42](https://en.wikipedia.org/wiki/Phrases_from_The_Hitchhiker%27s_Guide_to_the_Galaxy#The_number_42) is the answer to "The Ultimate Question of Life, The Universe, and Everything". But what *The Ultimate Question* really is? We may never know!

---

Given three integers, $a$, $b$, and $c$, insert two operators between them so that the following equation is true: $a\ (operator1)\ b\ (operator2)\ c=42$.

You may only use the addition $(+)$ and multiplication $(*)$ operators. You *can't* change the order of the variables. 

If a valid equation exists, print it; otherwise, print **This is not the ultimate question**.

## Input Format

A single line consisting three space-separated integers: $a$, $b$, and $c$.

**Constraints:**		
$0 \le a,b,c \le 42$

## Output Format

Print the equation with *no whitespace* between the operators and the three numbers. If there is no answer, print **This is not the ultimate question**.

**Note:** It is guaranteed that there is no more than one valid equation per test case.

## Sample Tests

### Test 1

```
12 5 6
```

### Test 2

```
10 20 12
```

### Test 3

```
5 12 6
```

### Test 4

```
12+5*6
```

### Test 5

```
10+20+12
```

### Test 6

```
This is not the ultimate question
```
