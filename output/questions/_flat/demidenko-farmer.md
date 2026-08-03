# Farmer

---

| Field | Value |
|---|---|
| **Slug** | `demidenko-farmer` |
| **Domain** | mathematics |
| **Difficulty** | Advanced |
| **Score** | 80 |
| **URL** | https://www.hackerrank.com/challenges/demidenko-farmer |

---

## Preview

Help the farmer to build a barn.

## Problem Statement

The farmer decided to build a barn on his farm. But on his farm there are trees and other buildings, which he does not want to remove. 


For simplicity, we represent the farm as a rectangular grid of height $N$ and width $M$. Each of the trees and buildings are located in one or more cells of the grid. The barn is a rectangle and should be built on the free cells of the grid. 


Help the farmer to find out how many ways there are to place the barn, for all possible sizes of barns.


**Input Format**

The first line contains two integers $N$ and $M$ - the dimensions of the farm.

The next $N$ lines contains description of the farm: each line contains $M$ characters - `0` or `1` (`1` means the cell is available/free for building the barn).


**Output Format**

Write $N$ lines with $M$ integers in each line. The $j^{th}$ value in the $i^{th}$ line must be equal to the number of ways to place a barn with height $i$ and width $j$ in the farm.


**Constraints**

$1 \le N, M \le 1024$


**Sample input**


    3 3
    011
    110
    110

**Sample Output**


    6 3 0
    3 1 0
    1 0 0

**Explanation**

Barns with height 1 and width 1:

    0*1    01*    011    011    011    011
    110    110    *10    1*0    110    110
    110    110    110    110    *10    1*0

Barns with height 1 and width 2:

    0**    011    011
    110    **0    110
    110    110    **0

Barns with height 2 and width 1:

    0*1    011    011
    1*0    *10    1*0
    110    *10    1*0
  

Barns with height 2 and width 2 (there is only one):

    011
    **0
    **0
  

Barns with height 3 and width 1 (there is only one):

    0*1
    1*0
    1*0

<sub>Time Limits: C/C++ 1 sec, Java/C# 2 sec, other languages follow standard TL given in [Environment](https://hackerrank.com/environment)</sub>

## Sample Tests

### Test 1

```
3 3
011
110
110
```

### Test 2

```
6 3 0
3 1 0
1 0 0
```

### Test 3

```
0*1 01* 011 011 011 011
110 110 *10 1*0 110 110
110 110 110 110 *10 1*0
```

### Test 4

```
0** 011 011
110 **0 110
110 110 **0
```

### Test 5

```
0*1 011 011
1*0 *10 1*0
110 *10 1*0
```

### Test 6

```
011
**0
**0
```

### Test 7

```
0*1
1*0
1*0
```
