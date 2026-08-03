# Migratory Birds

---

| Field | Value |
|---|---|
| **Slug** | `migratory-birds` |
| **Domain** | algorithms |
| **Difficulty** | Easy |
| **Score** | 10 |
| **URL** | https://www.hackerrank.com/challenges/migratory-birds |

---

## Preview

Determine which type of bird in a flock occurs at the highest frequency.

## Problem Statement

Given an array of bird sightings where every element represents a bird type id, determine the id of the most frequently sighted type.  If more than 1 type has been spotted that maximum amount, return the smallest of their ids.

**Example**  

$arr = [1,1,2,2,3]$ 


There are two each of types $1$ and $2$, and one sighting of type $3$.  Pick the lower of the two types seen twice: type $1$.


**Function Description**

Complete the *migratoryBirds* function in the editor below.  


migratoryBirds has the following parameter(s):


- *int arr[n]*: the types of birds sighted 


**Returns** 


- *int:* the lowest type id of the most frequently sighted birds

## Input Format

The first line contains an integer, $n$, the size of $arr$.		
The second line describes $arr$ as $n$ space-separated integers, each a type number of the bird sighted.

## Constraints

+ $5 \le n \le 2 \times 10^5$
- It is guaranteed that each type is $1$, $2$, $3$, $4$, or $5$.

## Sample Tests

### Test 1

```
6
1 4 4 4 5 3
```

### Test 2

```
4
```

### Test 3

```
11
1 2 3 4 5 4 3 2 1 3 4
```

### Test 4

```
3
```
