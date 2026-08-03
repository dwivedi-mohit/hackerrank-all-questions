# What is the expected output? 2

## Metadata

- **ID:** 147537
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Python, Easy
- **Skills:** Python (Basic)

## Summary

This multiple choice question evaluates Python generators, yield statements, and function behavior concepts, ideal for junior-level roles. The problem requires determining the output of a generator function that uses yield and send methods.

## Problem Statement

What is the expected output?

 

`def foo(value):
    while True:
        value = (yield value)

bar = foo(1)
print(next(bar))
print(next(bar))
print(bar.send(2))`
```

## Preview

What is the expected output?
