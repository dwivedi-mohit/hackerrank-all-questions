# List Length

---

| Field | Value |
|---|---|
| **Slug** | `fp-list-length` |
| **Domain** | fp |
| **Difficulty** | Easy |
| **Score** | 10 |
| **URL** | https://www.hackerrank.com/challenges/fp-list-length |

---

## Preview

Count the number of elements in an array without using <code>count</code>.

## Problem Statement

Count the number of elements in an array without using *count, size* or *length* operators (or their equivalents). The input and output portions will be handled automatically by the grader. You only need to write a function with the recommended method signature.

**Input Format**


A list of $N$ integers, each on a separate line.


**Output Format**


Output a single integer $N$, the length of the list that was provided as input.


**Sample Input**


    2
    5
    1
    4
    3
    7
    8
    6
    0
    9

**Sample Output**

	10


**Constraints**


$0<=N<=100$  <br>
Each element, $X$, in the list: $0<=X<=100$


**Recommended Method Signature**

    Number Of Parameters: 1
    Parameters: [list]
    Returns: Number

**For Hackers Using Clojure**


This will be the outline of your function body (fill in the blank portion marked by underscores):


     (fn[lst]___________________________)


**For Hackers Using Scala** 

This will be the outline of your function body (fill in the blank portion marked by underscores):


     def f(arr:List[Int]):Int = __________________
   

**For Hackers Using Haskell**


This will be the outline of your function body (fill in the blank portion marked by underscores):


     len lst = __________________


**For Hackers Using other Languages**


You have to read input from standard input and write output to standard output. Please follow the input/output format mentioned above.

**NOTE**: You only need to submit the code above after filling in the blanks appropriately. The input and output section will be handled by us. The focus is on writing the correct function.

## Sample Tests

### Test 1

```
2
5
1
4
3
7
8
6
0
9
```

### Test 2

```
10
```

### Test 3

```
Number Of Parameters: 1
Parameters: [list]
Returns: Number
```

### Test 4

```
(fn[lst]___________________________)
```

### Test 5

```
def f(arr:List[Int]):Int = __________________
```

### Test 6

```
len lst = __________________
```
