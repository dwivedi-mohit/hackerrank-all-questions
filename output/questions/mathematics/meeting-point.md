# Meeting Point

---

| Field | Value |
|---|---|
| **Slug** | `meeting-point` |
| **Domain** | mathematics |
| **Difficulty** | Hard |
| **Score** | 80 |
| **URL** | https://www.hackerrank.com/challenges/meeting-point |

---

## Preview

Find a meeting place which minimises total distance to everyone on a grid.

## Problem Statement

There is an infinite integer grid where  **N** people live in **N** different houses. They decide to create a meeting point at one person's house. 


From any given cell, all 8 adjacent cells can be reached in 1 unit of time, e.g. (x,y) can be reached from (x-1,y+1) in one unit of time. Find a common meeting place which minimizes the combined travel time of everyone.

  

**Input Format**  

A positive integer N that denotes N houses or people.

The following *N* lines will contain two integers x,y each that denote the coordinates of the respective house.

  

**Output Format**  

An integer, **M**, that denotes the minimum combined travel time of everyone.

  

  

**Constraints**

N <= 10<sup>5</sup>

The absolute value of each co-ordinate in the input will be at most 10<Sup>9</sup>

  

**HINT:** You may need 64-bit integer.

**Input #1**

<pre>
4 
0 1
2 5 
3 1 
4 0 
</pre>

**Output #1** 
<pre>
8
</pre> 


**Explanation**

The houses will have a travel-sum of 11, 13, 8, or 10. 8 is the minimum.


**Input #2** 

<pre>
6 
12 -14 
-3 3 
-14 7 
-14 -3 
2 -12 
-1 -6
</pre>

**Output #2**:
<pre>54</pre>

## Sample Tests

### Test 1

```
4 
0 1
2 5 
3 1 
4 0
```

### Test 2

```
8
```

### Test 3

```
6 
12 -14 
-3 3 
-14 7 
-14 -3 
2 -12 
-1 -6
```

### Test 4

```
54
```
