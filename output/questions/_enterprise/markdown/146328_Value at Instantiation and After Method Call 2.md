# Value at Instantiation and After Method Call 2

## Metadata

- **ID:** 146328
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Medium, Ruby, Output, Programming
- **Skills:** Ruby (Intermediate)

## Summary

This multiple choice question evaluates Ruby, object-oriented programming, and method manipulation concepts, ideal for mid-level roles. The problem requires determining the output of a Ruby program that defines a class with getter and setter methods for an instance variable.

## Problem Statement

What is the output of the following program?

   class MyClass
    def initialize
      @foo = 28
    end
 
    def foo
      return @foo
    end
 
    def foo=(value)
      @foo = value
    end
  end
 
  instance = MyClass.new
  print instance.foo
  print " "
  instance.foo = 496
  print instance.foo 
```

## Preview

What is the output of the following program?
