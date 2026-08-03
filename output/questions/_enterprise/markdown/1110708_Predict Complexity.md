# Predict Complexity

## Metadata

- **ID:** 1110708
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Algorithms, Time Complexity, Medium
- **Skills:** Problem Solving (Intermediate)

## Summary

This multiple choice question evaluates sorting algorithms, time complexity, and problem-solving concepts, ideal for mid-level roles. The problem requires identifying the sorting algorithm implemented in the provided pseudocode and determining its time complexity.

## Problem Statement

Which sorting algorithm does this code implement? What is its time complexity?

 

`void sort(int arr[])
    {
        int n = arr.length;
        for (int i = 1; i < n; ++i) {
            int key = arr[i];
            int j = i - 1;
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j = j - 1;
            }
            arr[j + 1] = key;
        }
    }`
```

## Preview

Which sorting algorithm does this code implement? What is its time complexity?
