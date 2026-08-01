# Quicksort 1 - Partition

- **Domain:** python
- **Difficulty:** Easy
- **Max Score:** 10
- **Success Ratio:** 0.9623640841068384
- **Total Submissions:** 131975
- **Solved Count:** 127008
- **URL:** https://www.hackerrank.com/challenges/quicksort1

## Problem Statement

The previous challenges covered [Insertion Sort](https://en.wikipedia.org/wiki/Insertion_sort), which is a simple and intuitive sorting algorithm with a running time of $O(n^2)$. In these next few challenges, we're covering a *divide-and-conquer* algorithm called [Quicksort](https://en.wikipedia.org/wiki/Quicksort) (also known as *Partition Sort*).  This challenge is a modified version of the algorithm that only addresses partitioning.  It is implemented as follows: 

**Step 1: Divide** 	
Choose some pivot element, $p$, and partition your unsorted array, $arr$, into three smaller arrays: $left$, $right$, and $equal$, where each element in $left \lt p$, each element in $right \gt p$, and each element in $equal = p$. 

**Example**   
$arr = [5, 7, 4, 3, 8]$   

In this challenge, the pivot will always be at $arr[0]$, so the pivot is $5$.
 
$arr$ is divided into $left = \{4, 3\}$, $equal = \{5\}$, and $right = \{7, 8\}$.  
Putting them all together, you get $\{4, 3, 5, 7, 8\}$. There is a flexible checker that allows the elements of $left$ and $right$ to be in any order.  For example, $\{3,4, 5,8,7\}$ is valid as well.    
  
Given $arr$ and $p=arr[0]$, partition $arr$ into $left$, $right$, and $equal$ using the *Divide* instructions above. Return a 1-dimensional array containing each element in $left$ first, followed by each element in $equal$, followed by each element in $right$.   

**Function Description**  

Complete the *quickSort* function in the editor below.     

quickSort has the following parameter(s):  

- *int arr[n]:* $arr[0]$ is the pivot element    

**Returns**   

- *int[n]:* an array of integers as described above   

## Input Format

The first line contains $n$, the size of $arr$.			
The second line contains $n$ space-separated integers $arr[i]$ (the unsorted array). The first integer, $arr[0]$, is the pivot element, $p$.


## Output Format

  

## Constraints

- $1 \le n \le 1000$   
- $-1000 \le arr[i] \le 1000$ where $0 \leq i \lt n$   
- All elements are distinct.


## Sample Input

STDIN       Function
-----       --------
5           arr[] size n =5
4 5 3 7 2   arr =[4, 5, 3, 7, 2]

## Sample Output

3 2 4 5 7

## Explanation

Pivot: .

; ;

, so it is added to .

; ;

, so it is added to .

; ;

, so it is added to .

; ;

, so it is added to .

; ;

Return the array .

The order of the elements to the left and right of  does not need to match this answer.  It is only required that  and  are to the left of , and  and  are to the right.
