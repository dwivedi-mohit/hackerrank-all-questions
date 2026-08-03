# Advanced Decorators

## Metadata

- **ID:** 1529633
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Medium, Python, Decorators
- **Skills:** Python (Intermediate)

## Summary

This multiple choice question evaluates Python decorators, function behavior modification, and execution order concepts, ideal for mid-level roles. The problem requires determining the output of a decorated function call in Python.

## Problem Statement

`def dec1(func):
    def wrapper(*args, **kwargs):
        print("Entering dec1")
        result = func(*args, **kwargs)
        print("Exiting dec1")
        return result
    return wrapper

def dec2(func):
    def wrapper(*args, **kwargs):
        print("Entering dec2")
        result = func(*args, **kwargs)
        print("Exiting dec2")
        return result
    return wrapper

@dec1
@dec2
def greet(message):
    print(message)

greet("Hello World")`
```

 

In Python, decorators are a powerful tool that allows one to modify the behavior of a function or class. What is the output of this code?

## Preview

def dec1(func):
