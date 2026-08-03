# Java Stack

---

| Field | Value |
|---|---|
| **Slug** | `java-stack` |
| **Domain** | java |
| **Difficulty** | Medium |
| **Score** | 20 |
| **URL** | https://www.hackerrank.com/challenges/java-stack |

---

## Preview

Use a stack to determine if a sequence of parentheses is balanced or not.

## Problem Statement

In computer science, a stack or LIFO (last in, first out) is an abstract data type that serves as a collection of elements, with two principal operations: push, which adds an element to the collection, and pop, which removes the last element that was added.(Wikipedia)


A string containing only parentheses is balanced if the following is true:
1. if it is an empty string
2. if A and B are correct, AB is correct,
3. if A is correct, (A) and {A} and [A] are also correct.


Examples of some correctly balanced strings are: "{}()",  "[{()}]",  "({()})" <br>

Examples of some unbalanced strings are: "{}(",  "({)}",  "[[",  "}{" etc.<br>

 
Given a string, determine if it is balanced or not.

## Input Format

There will be multiple lines in the input file, each having a single non-empty string. You should read input till end-of-file.

The part of the code that handles input operation is already provided in the editor.

## Output Format

For each case, print 'true' if the string is balanced, 'false' otherwise.

## Sample Tests

### Test 1

```
In computer science, a stack or LIFO (last in, first out) is an abstract data type that serves as a collection of elements, with two principal operations: push, which adds an element to the collection, and pop, which removes the last element that was added.(Wikipedia)
```

### Test 2

```
{}()
({()})
{}(
[]
```

### Test 3

```
true
true
false
true
```
