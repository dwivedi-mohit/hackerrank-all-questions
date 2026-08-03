# Special Arrays of 1 and 2

---

| Field | Value |
|---|---|
| **Slug** | `special-arrays-of-1-and-2` |
| **Domain** | misc |
| **Difficulty** | Hard |
| **Score** | 100 |
| **Contest** | 101hack27 |
| **URL** | https://www.hackerrank.com/challenges/special-arrays-of-1-and-2 |

---

## Problem Statement

Consider all possible arrays of length $N$ formed by only $1$ and $2$.

Now remove those arrays from above in which the sum of any consecutive $5$ numbers from the array have $prohibited$_$sum$.


    Function Find(int A[])
    {
        int sum = 0;
        int i = 1;
        while(i <= N) {
        	sum = sum + A[i];
            i = i + A[i];
        }
        return sum;
    }
  

Output the sum of the values returned by Function Find for all remaining Arrays modulo $10^9+7$.

## Input Format

The first line contains $T$, the number of test cases to follow. 

Each test case contains two space-separated integers $N$ and $prohibited$_$sum$ in a separate line.

## Output Format

Output the anwer of each query modulo $10^9+7$ as explained above.


**Constraints**

$1 \le T \le 10000$

$5 \le N \le 50000$

$0 \le$ **prohibited_sum** $\le 100$

$5 \le$ **Sum of** $N$ **over all test cases** $\le 50000$

## Sample Tests

### Test 1

```
Function Find(int A[])
{
 int sum = 0;
 int i = 1;
 while(i <= N) {
 sum = sum + A[i];
 i = i + A[i];
 }
 return sum;
}
```

### Test 2

```
4
5 4
6 5
7 6
8 7
```

### Test 3

```
171
386
662
718
```
