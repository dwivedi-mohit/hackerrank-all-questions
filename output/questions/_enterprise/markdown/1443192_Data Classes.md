# Data Classes

## Metadata

- **ID:** 1443192
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Kotlin, Easy
- **Skills:** Kotlin (Basic)

## Summary

This multiple choice question evaluates Kotlin basics, data classes, and exception handling concepts, ideal for junior-level roles. The problem requires determining the output of a code snippet that utilizes a data class and its component functions.

## Problem Statement

What is the output of the following code snippet?

`fun main() {
    val user = User("John", 23, "France")
    try {
        print("Name: ${user.component1()}, Age: ${user.component2()}")
    } catch(e: Exception) {
        
    }
}

data class User(val name: String, val age: Int, val country: String)
`
```

## Preview

What is the output of the following code snippet?
