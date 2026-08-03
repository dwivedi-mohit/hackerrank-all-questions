# Pointer Operations

## Metadata

- **ID:** 1762681
- **Type:** multiple_mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Embedded C/C++, Pointers, Easy

## Summary

This multiple choice question evaluates pointers, memory management, and data corruption concepts, ideal for junior-level roles. The problem identifies flaws in an encryption method that can lead to data corruption and potential segmentation faults due to improper pointer usage.

## Problem Statement

A simple encryption method is being developed for an application. It takes a byte array and does a predetermined modification on each byte of the array. Decryption does not yield the original data.

 

What is wrong with this approach?

 

`
void encrypt_array(uint8_t* byte_array, uint32_t array_size)
{
  uint16_t *p_temp_val;
  for(uint32_t el = 0; el < array_size; el++)
  {
    p_temp_val = &byte_array[el];  
    p_temp_val = (p_temp_val | 0xFF) + 15;
  }
}`
```

## Preview

A simple encryption method is being developed for an application. It takes a byt
