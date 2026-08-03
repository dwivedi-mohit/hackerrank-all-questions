# Ruby Array - Index, Part 2

---

| Field | Value |
|---|---|
| **Slug** | `ruby-array-index-ii` |
| **Domain** | ruby |
| **Difficulty** | Easy |
| **Score** | 10 |
| **URL** | https://www.hackerrank.com/challenges/ruby-array-index-ii |

---

## Problem Statement

Here are some other ways to access array objects in Ruby.


To access the elements from the end of the list, we can use negative
indices. 

For the array,


<pre>arr = [9, 5, 1, 2, 3, 4, 0, -1]</pre>

<pre> > arr[-1]
 => -1</pre>

+ The first element of the array can be accessed using

<pre> > arr.first
 => 9</pre>

+ The last element of the array can be accessed using

<pre> > arr.last
 => -1</pre>

+ The first `n` elements of the array can be accessed using

<pre> arr.take(3)
 => [9, 5, 1]</pre>

+ Everything but the first `n` elements of the array can be accessed using

<pre> arr.drop(3)
 => [2, 3, 4, 0, -1]</pre>

In this challenge, you have to use the syntax as explained above and complete the functions accordingly.

## Sample Tests

### Test 1

```
arr = [9, 5, 1, 2, 3, 4, 0, -1]
```

### Test 2

```
> arr[-1]
 => -1
```

### Test 3

```
> arr.first
 => 9
```

### Test 4

```
> arr.last
 => -1
```

### Test 5

```
arr.take(3)
 => [9, 5, 1]
```

### Test 6

```
arr.drop(3)
 => [2, 3, 4, 0, -1]
```
