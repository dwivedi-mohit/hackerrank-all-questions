# MetaClass Usage

## Metadata

- **ID:** 1529632
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Python, Medium, OOP
- **Skills:** Python (Intermediate)

## Summary

This multiple choice question evaluates metaclasses, class attributes, and Python OOP concepts, ideal for mid-level roles. The problem requires determining the output of accessing an attribute added by a metaclass in Python.

## Problem Statement

`class Meta(type):
    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dct)
        x.attr = 100
        return x

class MyClass(metaclass=Meta):
    pass
`
```

 

Given this Python code that defines a metaclass Meta, and a class MyClass that uses Meta as its metaclass, what is the output of the following line of code?

 

`print(MyClass.attr)
`
```

## Preview

class Meta(type):
