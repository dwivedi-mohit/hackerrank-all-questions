# Securing File Operations

## Metadata

- **ID:** 1777646
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Path Traversal Vulnerability, Easy, Broken Access Control
- **Skills:** OWASP Top 10

## Summary

This multiple choice question evaluates path traversal vulnerability, broken access control, and file handling concepts, ideal for junior-level roles. The problem requires identifying the vulnerability in a Python code snippet that allows directory traversal through user input.

## Problem Statement

`import os

def delete_file(filename):
  filepath = os.path.join(os.path.expanduser("~"), "documents", filename)
  if os.path.exists(filepath):
    os.remove(filepath)
    print("File deleted successfully.")
  else:
    print("File not found.")

if __name__ == "__main__":
  filename = input("Enter filename to delete: ")
  delete_file(filename)`
```

What vulnerability is present in this Python code snippet?

## Preview

import os
