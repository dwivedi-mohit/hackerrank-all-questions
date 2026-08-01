# Order exercises

- **Domain:** python
- **Difficulty:** Advanced
- **Max Score:** 100
- **Success Ratio:** 0.7723704866562009
- **Total Submissions:** 637
- **Solved Count:** 492
- **URL:** https://www.hackerrank.com/challenges/order-exercises

## Problem Statement

During a math class, a teacher wanted to practice ordering with students. He gave an array of $N$ integers, $a = \{a_1, a_2,\ldots, a_N\}$ to the students along with following definitions:

- Subarray is a contiguous segment of array. For example $a[l, r] = \{a_l, a_{l+1},\ldots, a_r\}$ is a subarray, where $1 \le l \le r \le N$

- We say that a sum of a subarray is a sum of elements in this subarray

- We say that subarray $X (= a[xl, xr] = \{a_{xl}, a_{xl+1},\ldots,a_{xr}\} )$ is greater than subarray $Y (= a[yl, yr] = \{a_{yl}, a_{yl+1},\ldots,a_{yr}\})$ if and only if:
 - $X$ has a greater sum than $Y$ 
 - $X$ and $Y$ has the same sum and $X$ begins earlier
 - $X$ and $Y$ has the same sum, they start in the same place and the length of $X$ is smaller than the length of $Y$

Since the teacher doesn't like number 0, there is no 0 in the array $a$. Other than array $a$, the teacher also gave an integer $K$. The task is to lists as many as possible, but not more than $K$, subarrays with a _positive sum_ in the following order.  

- The first subarray is the greatest subarray in the array according to above definition.

- The $i^{th}$ subarray is the greatest subarray disjoint to any of the $j^{th}$ subarray, where $j < i$ (disjoint means that they have no common elements).

Of course in order to win with others, you have to solve the problem first.   
 
**Input**  
In the first line there are two integers $N$ and $K$ separated by a single space.  
In the second line there are $N$ integers separated by single space denoting the array $arr$.

**Output**  
Print no more than $K$ lines. In the $i^{th}$ line print the sum of the $i^{th}$ sequence in the above order.  

**Constraints**  
$1 \le N \le 10^5$  
$1 \le K \le N$  
$0 < |a_i| \le 10^4, where\ i \in [1, N]$  



**Sample Input 00**

    5 3
    2 4 -10 2 -2

**Sample Output 00**

    6
    2

**Explanation**

Subarray $a[1, 2] = \{a_1, a_2\}$ has sum 6 and this is the greatest value in the whole array. Next disjoint greatest subarray is $a[4, 4] = {a_4}$  with sum = 2. There are no more subsequences with a positive value disjoint with the first and the second subsequence.

**Sample Input 01**

    4 2
    -2 5 -1 -8

**Sample Output 01**

    5    

**Explanation**

Subarray $a[2, 2] = \{a_2\}$ has sum 5 and this is the greatest value in the whole array. There are no more subsequences with a positive value disjoint with the first one, so even if K = 2, we print out just one value.

---
**Tested by** [Abhiranjan](/abhiranjan)


## Sample Input

5 3
2 4 -10 2 -2

## Sample Output

6
2

## Explanation

Subarray  has sum 6 and this is the greatest value in the whole array. Next disjoint greatest subarray is   with sum = 2. There are no more subsequences with a positive value disjoint with the first and the second subsequence.
