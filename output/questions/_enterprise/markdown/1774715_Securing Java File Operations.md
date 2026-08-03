# Securing Java File Operations

## Metadata

- **ID:** 1774715
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Path Traversal Vulnerability, Easy, Broken Access Control
- **Skills:** OWASP Top 10

## Summary

This multiple choice question evaluates path traversal vulnerabilities and broken access control concepts, ideal for junior-level roles. The problem requires identifying the vulnerability in a Java code snippet that improperly handles user input for file operations.

## Problem Statement

`import java.io.File;

public class FileOperations {
    public static void main(String[] args) {
        String filename = System.getProperty("user.home") + "/documents/" + args[0];
        File file = new File(filename);
        
        // Check if the file exists and delete it
        if (file.exists()) {
            file.delete();
            System.out.println("File deleted successfully.");
        } else {
            System.out.println("File not found.");
        }
    }
}`
```

What vulnerability is present in this Java code snippet?

## Preview

import java.io.File;
