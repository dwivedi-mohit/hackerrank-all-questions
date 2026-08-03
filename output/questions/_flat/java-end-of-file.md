# Java End-of-file

---

| Field | Value |
|---|---|
| **Slug** | `java-end-of-file` |
| **Domain** | java |
| **Difficulty** | Easy |
| **Score** | 10 |
| **URL** | https://www.hackerrank.com/challenges/java-end-of-file |

---

## Preview

Learn how to read from standard input until EOF.

## Problem Statement

> "In computing, *End Of File* (commonly abbreviated *EOF*) is a condition in a computer operating system where no more data can be read from a data source."
&mdash; <cite>([Wikipedia: End-of-file](https://en.wikipedia.org/wiki/End-of-file))</cite>
  

The challenge here is to read $n$ lines of input until you reach *EOF*, then number and print all $n$ lines of content.

**Hint:** Java's *Scanner.hasNext()* method is helpful for this problem.

## Input Format

Read some unknown $n$ lines of input from *stdin(System.in)* until you reach *EOF*; each line of input contains a non-empty *String*.

## Output Format

For each line, print the line number, followed by a single space, and then the line content received as input.

## Sample Tests

### Test 1

```
Hello world
I am a file
Read me until end-of-file.
```

### Test 2

```
1 Hello world
2 I am a file
3 Read me until end-of-file.
```
