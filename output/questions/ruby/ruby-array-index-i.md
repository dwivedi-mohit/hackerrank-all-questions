# Ruby Array - Index, Part 1

---

| Field | Value |
|---|---|
| **Slug** | `ruby-array-index-i` |
| **Domain** | ruby |
| **Difficulty** | Easy |
| **Score** | 10 |
| **URL** | https://www.hackerrank.com/challenges/ruby-array-index-i |

---

## Problem Statement

Array collections offer various ways to access their elements. 

The positions are `0` indexed. Objects of the array can be accessed using the `[]` method which may take various arguments, as explained below.


<pre>
arr = [9, 5, 1, 2, 3, 4, 0, -1]
</pre>

+ A number which is the position of element
  

<pre>>>arr[4]
  => 3</pre>


or

<pre>>>arr.at(4)
  => 3 </pre>


+ A range indicating the start and the end position 

<pre>>>arr[1..3] # .. indicates both indices are inclusive. 
  => [5,1,2]
>>arr[1...3] # ... indicates the last index is excluded.
  => [5,1]</pre>

+ Start index and the length of the range

<pre>>>arr[1,4]
  => [5, 1, 2, 3]</pre>


For this challenge, your task is to complete the functions using syntax as explained above.

## Sample Tests

### Test 1

```
arr = [9, 5, 1, 2, 3, 4, 0, -1]
```

### Test 2

```
>>arr[4]
 => 3
```

### Test 3

```
>>arr.at(4)
 => 3
```

### Test 4

```
>>arr[1..3] # .. indicates both indices are inclusive. 
 => [5,1,2]
>>arr[1...3] # ... indicates the last index is excluded.
 => [5,1]
```

### Test 5

```
>>arr[1,4]
 => [5, 1, 2, 3]
```
