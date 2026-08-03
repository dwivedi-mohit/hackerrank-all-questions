# Divisibility of Power

---

| Field | Value |
|---|---|
| **Slug** | `divisibility-of-power` |
| **Domain** | mathematics |
| **Difficulty** | Medium |
| **Score** | 60 |
| **URL** | https://www.hackerrank.com/challenges/divisibility-of-power |

---

## Preview

Divisibility Test.

## Problem Statement

You are given an array $A$ of size $N$. You are asked to answer $Q$ queries. 

Each query is of the form : 

$\text{i j x}$ 

You need to print `Yes` if $x$ divides the value returned from $find(i,j)$ function, otherwise print `No`.

	find(int i,int j)
	{
        if(i>j)	return 1;
        ans = pow(A[i],find(i+1,j))
        return ans
    }

**Input Format**

First line of the input contains $N$. Next line contains $N$ space separated numbers. The line, thereafter, contains $Q$ , the number of queries to follow. Each of the next $Q$ lines contains three positive integer $i$, $j$ and $x$.

**Output Format**

For each query display `Yes` or `No` as explained above.

**Constraints**

$2 \le N \le 2 \times 10^{5}$

$2 \le Q \le 3 \times 10^{5}$

$1 \le i,j \le N$

$i \le j$

$1 \le x \le 10^{16}$

$0 \le $ value of array element $\le 10^{16}$

No 2 consecutive entries in the array will be zero.

**Sample Input**

    4
    2 3 4 5
    2
    1 2 4
    1 3 7

**Sample Output**

    Yes
    No

## Sample Tests

### Test 1

```
find(int i,int j)
{
 if(i>j) return 1;
 ans = pow(A[i],find(i+1,j))
 return ans
}
```

### Test 2

```
4
2 3 4 5
2
1 2 4
1 3 7
```

### Test 3

```
Yes
No
```
