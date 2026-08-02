# Largest Permutation

- **Domain:** ai
- **Difficulty:** Easy
- **Max Score:** 30
- **Success Ratio:** 0.6670157323072428
- **Total Submissions:** 41062
- **Solved Count:** 27389
- **URL:** https://www.hackerrank.com/challenges/largest-permutation

## Problem Statement

You are given an unordered array of unique integers incrementing from $1$.  You can swap any two elements a limited number of times.  Determine the largest lexicographical value array that can be created by executing no more than the limited number of swaps.  

**Example**    
$arr=[1,2,3,4]$    
$k=1$    

The following arrays can be formed by swapping the $1$ with the other elements: 

```
[2,1,3,4]
[3,2,1,4]
[4,2,3,1]
```

The highest value of the four (including the original) is $[4,2,3,1]$.  If $k \ge 2$, we can swap to the highest possible value: $[4,3,2,1]$.

**Function Description**  

Complete the *largestPermutation* function in the editor below.  It must return an array that represents the highest value permutation that can be formed.  

largestPermutation has the following parameter(s):  

- *int k:* the maximum number of swaps  
- *int arr[n]:* an array of integers  


## Input Format

The first line contains two space-separated integers $n$ and $k$, the length of $arr$ and the maximum swaps that can be performed.
The second line contains $n$ distinct space-separated integers from $1$ to $n$ as $arr[i]$ where $1 \le arr[i] \le n$.

## Output Format

Print the lexicographically largest permutation you can make with **at most** $k$ swaps.   
**Sample Input 0**  
<pre>
STDIN		Function
-----		--------
5 1			n = 5, k = 1
4 2 3 5 1	arr = [4, 2, 3, 5, 1]
</pre>

**Sample Output 0**  

    5 2 3 4 1

**Explanation 0**  

You can swap any two numbers in $[4,2,3,5,1]$ and see the largest permutation is $[5,2,3,4,1]$

**Sample Input 1**

    3 1
    2 1 3
    
**Sample Output 1**  

    3 1 2

**Explanation 1**  

With 1 swap we can get $[1,2,3]$, $[3,1,2]$ and $[2,3,1]$.  Of these, $[3,1,2]$ is the largest permutation.  

**Sample Input 2**

    2 1
    2 1
    
**Sample Output 2**  

    2 1
    
**Explanation 2**  

We can see that $[2,1]$ is already the largest permutation.  We don't make any swaps. 

## Constraints

$1 \le n \le 10^5$  
$1 \le k \le 10^9$  


## Sample Input

STDIN       Function
-----       --------
5 1         n = 5, k = 1
4 2 3 5 1   arr = [4, 2, 3, 5, 1]

## Sample Output

5 2 3 4 1

## Explanation

You can swap any two numbers in  and see the largest permutation is

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
