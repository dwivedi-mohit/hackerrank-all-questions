# Lena Sort

- **Domain:** algorithms
- **Difficulty:** Medium
- **Max Score:** 30
- **Success Ratio:** 0.6433841613379242
- **Total Submissions:** 2033
- **Solved Count:** 1308
- **URL:** https://www.hackerrank.com/challenges/lena-sort

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

## Sample Input

2
5 6
5 100

## Sample Output

4 2 1 3 5
-1

## Explanation

We perform the following  queries:

- One array with  elements is . The sequence of sorting operations looks like this:

- Run  on . Compare  with , , , and  for a total of  comparisons. We're then left with  and ; we only need to continue sorting , as  is sorted with respect to itself because it only contains one element.

- Run  on . Compare  with  and  for a total of  comparisons. We're then left with  and , so we stop sorting.

We sorted  in  comparisons and , so we print 4 2 1 3 5 on a new line.

- It's not possible to construct an array with  elements that  will sort in exactly  comparisons, so we print -1 on a new line.
