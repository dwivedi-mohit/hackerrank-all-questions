# Linked Lists: Detect a Cycle

---

| Field | Value |
|---|---|
| **Slug** | `ctci-linked-list-cycle` |
| **Domain** |  |
| **Difficulty** | Easy |
| **Score** | 25 |
| **URL** | https://www.hackerrank.com/challenges/ctci-linked-list-cycle |

---

## Preview

Given a pointer to the head of a linked list, determine whether the list has a cycle.

## Problem Statement

A linked list is said to contain a *cycle* if any node is visited more than once while traversing the list. For example, in the following graph there is a cycle formed when node $5$ points back to node $3$.


![image](https://s3.amazonaws.com/hr-assets/0/1527604250-43ac8fbfaf-filtrationExample.png)

**Function Description**

Complete the function *has_cycle* in the editor below. It must return a boolean *true* if the graph contains a cycle, or *false*.


has_cycle has the following parameter(s):

- *head*: a pointer to a *Node* object that points to the head of a linked list.

**Returns** 


- *boolean:* True if there is a cycle, False if there is not



**Note:** If the list is empty, $head$ will be *null*.

## Input Format

There is no input for this challenge.  A random linked list is generated at runtime and passed to your function.

## Constraints

- $0 \le \textit{ list size } \le 100$

## Sample Tests

### Test 1

```
0
1
```
