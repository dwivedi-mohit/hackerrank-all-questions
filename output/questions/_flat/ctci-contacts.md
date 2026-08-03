# Tries: Contacts

---

| Field | Value |
|---|---|
| **Slug** | `ctci-contacts` |
| **Domain** |  |
| **Difficulty** | Hard |
| **Score** | 50 |
| **URL** | https://www.hackerrank.com/challenges/ctci-contacts |

---

## Preview

Create a Contacts application with the two basic operations: add and find.

## Problem Statement

We're going to make our own *Contacts* application! The application must perform two types of operations:

1. `add name`, where $name$ is a string denoting a contact name. This must store $name$ as a new contact in the application.

2. `find partial`, where $partial$ is a string that denotes a partial name to search the application for. It must count the number of contacts starting with $partial$ and print the count on a new line.

Given $n$ sequential *add* and *find* operations, perform each operation in order.

## Input Format

The first line contains a single integer, $n$, the number of operations to perform.

Each line $i$ of the $n$ subsequent lines contains an operation in one of the two forms defined above.

## Output Format

For each `find partial` operation, print the number of contact names starting with $partial$ on a new line.

## Constraints

- $1 \le n \le 10^5$

- $1 \le |name| \le 21$

- $1 \le |partial| \le 21$

- It is guaranteed that $name$ and $partial$ contain lowercase English letters only.
- The input does not have any duplicate $name$ for the $add$ operation.

## Sample Tests

### Test 1

```
4
add hack
add hackerrank
find hac
find hak
```

### Test 2

```
2
0
```
