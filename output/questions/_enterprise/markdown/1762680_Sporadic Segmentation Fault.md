# Sporadic Segmentation Fault

## Metadata

- **ID:** 1762680
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Embedded C/C++, Easy, Firmware Development

## Summary

This multiple choice question evaluates array indexing, segmentation faults, and debugging concepts, ideal for junior-level roles. The problem requires identifying the root cause of sporadic segmentation faults in a function that sums array elements.

## Problem Statement

An embedded system experiences sporadic segmentation faults. Debugging reveals a single C function, get_sum, that calculates the sum of array elements is probably the culprit. Review the code assuming the array pointer and size are valid.

 

Which option is the root cause?

 

`uint32_t get_sum(uint32_t* array, uint32_t array_size)
{
   int32_t sum = 0;
   for (int i = 0; i <= array_size; i++)
   {
       sum += array[i];
   }
   return sum;
} `
```

## Preview

An embedded system experiences sporadic segmentation faults. Debugging reveals a
