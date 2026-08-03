# Sparse Arrays

---

| Field | Value |
|---|---|
| **Slug** | `sparse-arrays` |
| **Domain** | data-structures |
| **Difficulty** | Medium |
| **Score** | 25 |
| **URL** | https://www.hackerrank.com/challenges/sparse-arrays |

---

## Preview

Determine the number of times a string has previously appeared.

## Problem Statement

There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings. Return an array of the results. 

**Example**


$stringList = ['ab','ab','abc']$

$queries = ['ab','abc','bc']$


There are $2$ instances of '$ab$', $1$ of '$abc$', and $0$ of '$bc$'. For each query, add an element to the return array: $results = [2, 1, 0]$.

**Function Description**

Complete the function $matchingStrings$ with the following parameters:

-  $string\ stringList[n]$: an array of strings to search

-  $string\ queries[q]$: an array of query strings


**Returns**


- $int[q]$: the results of each query

## Input Format

The first line contains and integer $n$, the size of $stringList[]$.

Each of the next $n$ lines contains a string $stringList[i]$.

The next line contains $q$, the size of $queries[]$.

Each of the next $q$ lines contains a string $queries[i]$.

## Constraints

$1 \leq n \leq 1000$

$1 \leq q \leq 1000$

$1 \leq |stringList[i]|,|queries[i]| \leq 20$ .
