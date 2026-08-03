# Tell the Average

---

| Field | Value |
|---|---|
| **Slug** | `tell-the-average` |
| **Domain** | mathematics |
| **Difficulty** | Medium |
| **Score** | 25 |
| **URL** | https://www.hackerrank.com/challenges/tell-the-average |

---

## Preview

Tell me average of all list value.

## Problem Statement

James is very naive in Mathematics, He always makes new things out of a given list of integers. Today he is given a list $L$, so he creates a value $S$ out of it.


$S$ from a given list can be calculated as follows.

    value_of_S(list L)
    {
        while ((number of elements in L) > 1)
        {
            a = L[0]
            b = L[1]
            delete L[1]
            L[0] = a+b+ab
        }
        return L[0] % 1000000007
    }
  

James has an ample amount of time, so he calculates the values of $S$ for all the permutations of the given list $L$ and finds their average value. Then he asks you to report that value.
 
**Input Format**

The first line contains an integer $N$, the number of integers in the list.

The second line contains $N$ integral values, $L[0], \ldots, L[N-1]$, separated by single spaces.

**Output Format**

Print the [floor](http://en.wikipedia.org/wiki/Floor_and_ceiling_functions) of the average value.

**Constraints**

$2 \le N \le 10^4$

$2 \le L[i] \le 10^6$

**Sample Input**


    2
    2 3

**Sample Output**


    11

**Explanation**

The $S$ value corresponding to the two permutations of the given list is $11$.

## Sample Tests

### Test 1

```
value_of_S(list L)
{
 while ((number of elements in L) > 1)
 {
 a = L[0]
 b = L[1]
 delete L[1]
 L[0] = a+b+ab
 }
 return L[0] % 1000000007
}
```

### Test 2

```
2
2 3
```

### Test 3

```
11
```
