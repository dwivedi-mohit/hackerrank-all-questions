# Insertion Sort - Part 1

- **Domain:** shell
- **Difficulty:** Easy
- **Max Score:** 30
- **Success Ratio:** 0.8866086631592803
- **Total Submissions:** 235503
- **Solved Count:** 208799
- **URL:** https://www.hackerrank.com/challenges/insertionsort1

## Problem Statement

**Sorting**  
One common task for computers is to sort data. For example, people might want to see all their files on a computer sorted by size. Since sorting is a simple problem with many different possible solutions, it is often used to introduce the study of algorithms. 

**Insertion Sort**  
These challenges will cover _Insertion Sort_, a simple and intuitive sorting algorithm. We will first start with a nearly sorted list.

**Insert element into sorted list**  
Given a sorted list with an unsorted number $e$ in the rightmost cell, can you write some simple code to insert $e$ into the array so that it remains sorted?  

Since this is a learning exercise, it won't be the most efficient way of performing the insertion.  It will instead demonstrate the brute-force method in detail.   

Assume you are given the array $arr=[1, 2, 4, 5, 3]$ indexed $0 \ldots 4$.  Store the value of $arr[4]$.  Now test lower index values successively from $3$ to $0$ until you reach a value that is lower than $arr[4]$, at $arr[1]$ in this case.  Each time your test fails, copy the value at the lower index to the current index and print your array.  When the next lower indexed value is smaller than $arr[4]$, insert the stored value at the current index and print the entire array.

**Example**    
$n = 5$  
$arr = [1, 2, 4, 5, 3]$  
Start at the rightmost index.  Store the value of $arr[4]=3$.  Compare this to each element to the left until a smaller value is reached.  Here are the results as described:  

    1 2 4 5 5
    1 2 4 4 5
    1 2 3 4 5
    
**Function Description**

Complete the *insertionSort1* function in the editor below.  

insertionSort1 has the following parameter(s):

- *n*: an integer, the size of $arr$  
- *arr*: an array of integers to sort  

**Returns**  

- *None:*  Print the interim and final arrays, each on a new line.  No return value is expected.  

## Input Format

The first line contains the integer $n$, the size of the array $arr$.  
The next line contains $n$ space-separated integers $arr[0]...arr[n-1]$. 

## Output Format

 Print the array as a row of space-separated integers each time there is a shift or insertion.

## Constraints

$1 \le n  \le 1000$   
$-10000 \le arr[i] \le 10000$  
 

## Sample Input

2 4 6 8 3

## Sample Output

2 4 6 8 8
2 4 6 6 8
2 4 4 6 8
2 3 4 6 8

## Explanation

is removed from the end of the array.

In the st line , so  is shifted one cell to the right.

In the nd line , so  is shifted one cell to the right.

In the rd line , so  is shifted one cell to the right.

In the th line , so  is placed at position .

Next Challenge

In the next Challenge, we will complete the insertion sort.
