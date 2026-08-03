# Goroutine Synchronization Using Channels

## Metadata

- **ID:** 1752001
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Go, Concurrency, Medium
- **Skills:** Go (Intermediate)

## Summary

This multiple choice question evaluates concurrency, goroutines, and race conditions concepts, ideal for mid-level roles. The problem requires determining the output of a Go program that involves concurrent modifications to a variable.

## Problem Statement

What does this program print?

`func main() {
  i:=0
  ch:=make(chan struct{})
  go func() {
     i++
     close(ch)
     i++
  }()
  <-ch
  fmt.Println(i)
}
`
```

## Preview

What does this program print?
