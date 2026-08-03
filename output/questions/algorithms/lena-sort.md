# Lena Sort

---

| Field | Value |
|---|---|
| **Slug** | `lena-sort` |
| **Domain** | algorithms |
| **Difficulty** | Medium |
| **Score** | 30 |
| **URL** | https://www.hackerrank.com/challenges/lena-sort |

---

## Preview

Construct an array of a specific length that Lena's sorting algorithm will sort in a specific number of comparisons.

## Problem Statement

Lena developed a sorting algorithm described by the following pseudocode:

```cpp
lena_sort(array nums) {
    if (nums.size <= 1) {
        return nums;
    }
    pivot = nums[0];
    array less;
    array more;
    for (i = 1; i < nums.size; ++i) {
    	// Comparison
        if (nums[i] < pivot) {
            less.append(nums[i]);
        }
        else {
            more.append(nums[i]);
        }
    }
    sorted_less = lena_sort(less);
    sorted_more = lena_sort(more);
    ans = sorted_less + pivot + sorted_more;
  

    return ans;
}
```

We consider a *comparison* to be any time some $nums[i]$ is compared with $pivot$. 

You must solve $q$ queries where each query $i$ consists of some $len_i$ and $c_i$. For each query, construct an array of $len_i$ distinct elements in the inclusive range between $1$ and $10^9$ that will be sorted by $\text{lena_sort}$ in exactly $c_i$ comparisons, then print each respective element of the unsorted array as a single line of $len_i$ space-separated integers; if no such array exists, print `-1` instead.

## Input Format

The first line contains a single integer denoting $q$ (the number of queries).

Each line $i$ of the $q$ subsequent lines contains two space-separated integers describing the respective values of $\mathit{len}_i$ (the length of the array) and $c_i$ (the number of comparisons) for query $i$.

## Output Format

Print the answer to each query on a new line. For each query $i$, print $\mathit{len}_i$ space-separated integers describing each respective element in an unsorted array that Lena's algorithm will sort in exactly $c_i$ comparisons; if no such array exists, print `-1` instead.

## Constraints

+ $1 \le q \le 10^5$

+ $1 \le \mathit{len}_i \le 10^5$

+ $0 \le c_i \le 10^9$

+ $1 \le$ the sum of $\mathit{len}_i$ over all queries $ \le 10^6$

## Sample Tests

### Test 1

```
lena_sort
(
array
nums
)
{
if
(
nums
.
size
<=
1
)
{
return
nums
;
}
pivot
=
nums
[
0
];
array
less
;
array
more
;
for
(
i
=
1
;
i
<
nums
.
size
;
++
i
)
{
// Comparison
if
(
nums
[
i
]
<
pivot
)
{
less
.
append
(
nums
[
i
]);
}
else
{
more
.
append
(
nums
[
i
]);
}
}
sorted_less
=
lena_sort
(
less
);
sorted_more
=
lena_sort
(
more
);
ans
=
sorted_less
+
pivot
+
sorted_more
;
return
ans
;
}
```

### Test 2

```
2
5 6
5 100
```

### Test 3

```
4 2 1 3 5
-1
```

### Test 4

```
3
1 0
4 6
3 2
```

### Test 5

```
1
4 3 2 1
2 1 3
```
