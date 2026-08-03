# Power Calculation

---

| Field | Value |
|---|---|
| **Slug** | `power-calculation` |
| **Domain** | mathematics |
| **Difficulty** | Advanced |
| **Score** | 25 |
| **URL** | https://www.hackerrank.com/challenges/power-calculation |

---

## Preview

Help Shashank in huge calculations.

## Problem Statement

Help Shashank in calculating the value of $S$, which is given as follows. Since the value of $S$ can be very large, he only wants the last 2 digits of $S$.

$$S = 1^N + 2^N + 3^N + \cdots + K^N$$

**Input Format**

The first line contains an integer $T$ i.e. number of the test cases.

The next $T$ lines will each contain a pair of integers, i.e. $K$ and $N$.


**Output Format** 

Print the last two digits of $S$ for each test case in separate lines.


**Constraints**

$1 \le T \le 10^4$

$2 \le K \le 10^{16}$

$2 \le N \le 10^{16}$



**Sample Input#00**


    3
    2 2
    2 3
    3 3
  

**Sample Output#00**


    05
    09
    36

**Sample Input#01**


	3
    5 2
    3 4
    3 3
  

**Sample Output#01**


	55
    98
    36

**Explanation**

For the first test case, $1^2 + 2^2 + 3^2 + 4^2 + 5^2 = 55$

## Sample Tests

### Test 1

```
3
2 2
2 3
3 3
```

### Test 2

```
05
09
36
```

### Test 3

```
3
5 2
3 4
3 3
```

### Test 4

```
55
98
36
```
