# Iteration Order

## Metadata

- **ID:** 1752024
- **Type:** multiple_mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Medium, Collections, Go, Hash Map
- **Skills:** Go (Intermediate)

## Summary

This multiple choice question evaluates collections, Go, and hash map concepts, ideal for mid-level roles. The problem requires determining the possible outputs of a program that utilizes a map to store string keys and their corresponding indices.

## Problem Statement

What are the possible outputs of the following program?

`func main() {
  m:=make(map[string]int)
  for i, s:=range []string{"a","b","c","d","a","b","c"} {
    m[s]=i
  }
  for k,v:=range m {
    fmt.Println(k,v)
  }
}
`
```

## Preview

What are the possible outputs of the following program?
