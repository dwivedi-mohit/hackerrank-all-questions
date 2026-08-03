# Pascal's Triangle

---

| Field | Value |
|---|---|
| **Slug** | `pascals-triangle` |
| **Domain** | fp |
| **Difficulty** | Easy |
| **Score** | 10 |
| **URL** | https://www.hackerrank.com/challenges/pascals-triangle |

---

## Preview

Display N rows of Pascal's Triangle.

## Problem Statement

For a given integer $K$, print the first $K$ rows of [Pascal's Triangle](https://en.wikipedia.org/wiki/Pascal%27s_triangle). Print each row with each value separated by a single space. The value at the $n$<sup>$th$</sup> row  and $r$<sup>$th$</sup>  column of the triangle is equal to $n! / (r! * (n-r)!)$ where indexing starts from $0$. These values are the binomial coefficients.


**The Pascal Triangle**

    1
    1 1
    1 2 1
    1 3 3 1
    1 4 6 4 1
    ....


**Input Format** 

A single line of input, integer $K$.


**Constraints**


$2 <= K <= 10$




**Output Format**


Output the first $K$ rows of Pascal's triangle.


**Sample Input**


    4


**Sample Output**


    1

    1 1

    1 2 1

    1 3 3 1

## Sample Tests

### Test 1

```
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
....
```

### Test 2

```
4
```

### Test 3

```
1 
1 1 
1 2 1 
1 3 3 1
```
