# Class Interactions

## Metadata

- **ID:** 146323
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Ruby, Hard, Output, Programming
- **Skills:** Ruby (Advanced)

## Summary

This multiple choice question evaluates Ruby programming, class inheritance, and variable scope concepts, ideal for senior-level roles. The problem requires determining the output of a Ruby program involving class methods and variable manipulation.

## Problem Statement

What is the output of the following program?

class Parent
  @@value = 4
  def self.value
    @@value
  end
  def self.inc_value
    @@value += 1
  end
end

class Child < Parent
  @@value = 87
end

puts Parent.value
puts Parent.inc_value
puts Child.value
```

## Preview

What is the output of the following program?
