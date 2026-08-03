# Ruby Tutorial - Object Method Parameters

---

| Field | Value |
|---|---|
| **Slug** | `ruby-tutorials-object-method-parameters` |
| **Domain** | ruby |
| **Difficulty** | Easy |
| **Score** | 10 |
| **URL** | https://www.hackerrank.com/challenges/ruby-tutorials-object-method-parameters |

---

## Preview

This is an easy challenge to help you understand object method parameters in Ruby

## Problem Statement

A method may take zero or more parameters as input. To demonstrate this, we look at the asserts we use on HackerRank. Sometimes, we have to check whether a given number `a` is within the range `b` and `c` (where `b` $\le$ `c`, and both inclusive ). 

Three variables `a`, `b`, and `c` are already defined. Your task is to write code that checks whether `a` is within the range of `b` and `c` by calling the method `range?` (which we have defined for you as a method for this example) on `a` and passing `b` and `c` as arguments.


**Hint**


    a.between?(b, c)
  

or 

    return a.between?(b, c)
  

or 

    a.between? b, c
  

or

    return a.between? b, c

## Sample Tests

### Test 1

```
a.between?(b, c)
```

### Test 2

```
return a.between?(b, c)
```

### Test 3

```
a.between? b, c
```

### Test 4

```
return a.between? b, c
```
