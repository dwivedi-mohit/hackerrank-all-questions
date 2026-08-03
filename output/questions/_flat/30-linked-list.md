# Day 15: Linked List

---

| Field | Value |
|---|---|
| **Slug** | `30-linked-list` |
| **Domain** | tutorials |
| **Difficulty** | Easy |
| **Score** | 30 |
| **URL** | https://www.hackerrank.com/challenges/30-linked-list |

---

## Preview

Complete the body of a function that adds a new node to the tail of a Linked List.

## Problem Statement

**Objective**	
Today we will work with a *Linked List*. Check out the [Tutorial](/challenges/30-linked-list/tutorial) tab for learning materials and an instructional video.


****

A *Node* class is provided for you in the editor. A *Node* object has an integer data field, $data$, and a *Node* instance pointer, $next$, pointing to another node (i.e.: the next node in the list).

A *Node insert* function is also declared in your editor. It has two parameters: a pointer, $head$, pointing to the first node of a linked list, and an integer, $data$,  that must be added to the end of the list as a new *Node* object. 

**Task**	
Complete the *insert* function in your editor so that it creates a new *Node* (pass $data$ as the *Node* constructor argument) and inserts it at the tail of the linked list referenced by the $head$ parameter. Once the new node is added, return the reference to the $head$ node. 	

**Note:** The $head$ argument is *null* for an empty list.

## Input Format

The first line contains *T*, the number of elements to insert. 	
Each of the next $T$ lines contains an integer to insert at the end of the list.

## Output Format

Return a reference to the $head$ node of the linked list.

## Sample Tests

### Test 1

```
STDIN Function
----- --------
4 T = 4
2 first data = 2
3
4
1 fourth data = 1
```

### Test 2

```
2 3 4 1
```
