# nCr table

---

| Field | Value |
|---|---|
| **Slug** | `ncr-table` |
| **Domain** | mathematics |
| **Difficulty** | Medium |
| **Score** | 30 |
| **URL** | https://www.hackerrank.com/challenges/ncr-table |

---

## Preview

Help Jim calculating nCr values

## Problem Statement

Jim is doing his discrete maths homework which requires him to repeatedly calculate <sup>n</sup>C<sub>r</sub>(n choose r) for different values of n. Knowing that this is time consuming, he goes to his sister June for help. June,  being a computer science student knows how to convert this into a computer program and generate the answers quickly. She tells him, by storing the lower values of <sup>n</sup>C<sub>r</sub>(n choose r), one can calculate the higher values using a very simple formula. 

If you are June, how will you calculate <sup>n</sup>C<sub>r</sub> values for different values of n?

Since $^nC_r$values will be large you have to calculate them modulo $10^9$.


**Input Format**

The first line contains the number of test cases T.

T lines follow each containing an integer n. 

**Output Format**

For each n output the list of <sup>n</sup>C<sub>0</sub> to <sup>n</sup>C<sub>n</sub> each separated by a single space in a new line. If the number is large, print only the last 9 digits. i.e. modulo 10<sup>9</sup>

**Constraints**

1<=T<=200

1<=n< 1000

**Sample Input**

    3
    2
    4
    5

**Sample Output**

    1 2 1
    1 4 6 4 1
    1 5 10 10 5 1

**Explanation**

For 2 we can check <sup>2</sup>C<sub>0</sub>  <sup>2</sup>C<sub>1</sub> and <sup>2</sup>C<sub>2</sub> are 1, 2 and 1 respectively. The other inputs' answer follow similar pattern.

## Sample Tests

### Test 1

```
3
2
4
5
```

### Test 2

```
1 2 1
1 4 6 4 1
1 5 10 10 5 1
```
