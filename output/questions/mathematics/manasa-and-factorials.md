# Manasa and Factorials

---

| Field | Value |
|---|---|
| **Slug** | `manasa-and-factorials` |
| **Domain** | mathematics |
| **Difficulty** | Hard |
| **Score** | 40 |
| **URL** | https://www.hackerrank.com/challenges/manasa-and-factorials |

---

## Preview

Think about number of zeros in k!

## Problem Statement

Manasa was sulking her way through a boring class when suddenly her teacher singled her out and asked her a question. He gave her a number **n** and Manasa has to come up with the smallest number **m** which contains atleast **n** number of zeros at the end of **m!**. Help Manasa come out of the sticky situation. 

**Input Format**

The first line contains an integer _T_ i.e. the number of Test cases.

Next T lines will contain an integer n.


**Output Format**

Print smallest such number m. 

**Constraints**

1 &le; _T_ &le; 100 <br>
1 &le; _n_ &le; 10<sup>16</sup>


**Sample Input**


	3
	1
	2
	3

  

**Sample Output**


	5
    10
    15


**Explanation**

1. As 4! = 24 and 5! = 120, so minimum value of m will be 5.
2. As 9! = 362880 and 10! = 3628800, so minimum value of m will be 10.
3. As 14! = 87178291200 and 15! = 1307674368000, so minimum value of m will be 15.

## Sample Tests

### Test 1

```
3
1
2
3
```

### Test 2

```
5
10
15
```
