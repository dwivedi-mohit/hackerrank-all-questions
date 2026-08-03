# Ruby Array - Deletion

---

| Field | Value |
|---|---|
| **Slug** | `ruby-array-deletion` |
| **Domain** | ruby |
| **Difficulty** | Easy |
| **Score** | 10 |
| **URL** | https://www.hackerrank.com/challenges/ruby-array-deletion |

---

## Problem Statement

The array class has various methods of removing elements from the array.

Let's look at the array

<pre> arr = [5, 6, 5, 4, 3, 1, 2, 5, 4, 3, 3, 3] </pre>

+ Delete an element from the end of the array

<pre> > arr.pop
 => 3</pre>

+ Delete an element from the beginning of the array

<pre> > arr.shift
 => 5</pre>

+ Delete an element at a given position

<pre> > arr.delete_at(2)
 => 4</pre>

+ Delete all occurrences of a given element

<pre> > arr.delete(5)
 => 5
 > arr
 => [6, 3, 1, 2, 4, 3, 3]</pre>

Your task is to complete the functions below using syntax as explained above.

## Sample Tests

### Test 1

```
arr = [5, 6, 5, 4, 3, 1, 2, 5, 4, 3, 3, 3]
```

### Test 2

```
> arr.pop
 => 3
```

### Test 3

```
> arr.shift
 => 5
```

### Test 4

```
> arr.delete_at(2)
 => 4
```

### Test 5

```
> arr.delete(5)
 => 5
 > arr
 => [6, 3, 1, 2, 4, 3, 3]
```
