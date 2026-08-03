# Tree: Level Order Traversal

---

| Field | Value |
|---|---|
| **Slug** | `tree-level-order-traversal` |
| **Domain** | data-structures |
| **Difficulty** | Easy |
| **Score** | 20 |
| **URL** | https://www.hackerrank.com/challenges/tree-level-order-traversal |

---

## Preview

Level order traversal of a binary tree.

## Problem Statement

Given a pointer to the root of a binary tree, you need to print the level order traversal of this tree. In level-order traversal, nodes are visited level by level from left to right. Complete the function $levelOrder$ and print the values in a single line separated by a space.

For example:

         1
    	  \
		   2
			\
			 5
			/  \
		   3    6
			\
			 4	

For the above tree, the level order traversal is $1 -> 2 -> 5 -> 3 -> 6 -> 4$.

## Input Format

You are given a function,

	void levelOrder(Node * root) {
    	
    }

## Output Format

Print the values in a single line separated by a space.

## Constraints

$1$ $\leq$Nodes in the tree  $\leq$ $500$

## Sample Tests

### Test 1

```
1
 \
 2
 \
 5
 / \
 3 6
 \
 4
```

### Test 2

```
void levelOrder(Node * root) {
}
```

### Test 3

```
1
 \
 2
 \
 5
 / \
 3 6
 \
 4
```
