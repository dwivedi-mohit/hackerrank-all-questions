# HTTP Header Canonicalizer

## Metadata

- **ID:** 2268737
- **Type:** code
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Easy, Python, String Manipulation, Hash Maps
- **Skills:** Python (Basic)
- **Languages:** p, y, t, h, o, n, 3

## Summary

This coding question evaluates string manipulation, hash maps, and data normalization concepts, ideal for junior-level roles. The problem requires implementing a function to parse HTTP headers into a standardized dictionary format, handling duplicates and invalid lines appropriately.

## Problem Statement

Your web proxy service aggregates HTTP responses from multiple backend servers, but each returns headers with inconsistent casing and duplicates. This causes cache misses and routing errors when clients expect standardized headers.

Implement the parse_headers function, which takes raw header lines and returns a dictionary with canonical Title-Case keys, and parse each non-blank line as "Name: value", strip whitespace, and join duplicate headers with ", " in order of appearance. 

## Example 1

Input:

n = 3
content-type: application/json
ACCEPT: text/html
accept: application/json
```

Output: 

{"Content-Type": "application/json", "Accept": "text/html, application/json"}
```

Explanation:

- Three non‑blank lines are processed.

- Names are stripped and validated, then canonicalized to Title‑Case:

- content-type → Content-Type

- ACCEPT/accept → Accept

- Values are stripped.

- Duplicate Accept values are joined in order with ", " → "text/html, application/json".

## Example 2

Input:

n = 1
invalid line with no colon
```

Output: 

ValueError
```

The line lacks a ":" delimiter, making it invalid. A ValueError is raised.

 

## Function Parameters

- 
lines: List of strings, each expected to be in "Name: value" format.

## Returns

- 
dict[str, str]: Dictionary mapping canonical header names to combined values. Names are Title-Case (split on "-" and capitalize each part, e.g., x-request-id -> X-Request-Id). 

- 
Raises ValueError if any non-blank line lacks ":" or has an empty header name.

## Constraints

- 1 ≤ number of lines ≤ 3000

- 0 ≤ length of each line ≤ 1000 characters

- Empty values are allowed

 

## Input Format for Custom Testing

Input from stdin will be processed as follows and passed to the function:

The first line contains an integer n, the number of header lines

Next n lines contain one raw header string

## Sample Input/Output

## Preview

Your web proxy service aggregates HTTP responses from multiple backend servers,
