# Correctness and the Loop Invariant

- **Domain:** data-structures
- **Difficulty:** Easy
- **Max Score:** 30
- **Success Ratio:** 0.9806692494529979
- **Total Submissions:** 149451
- **Solved Count:** 146562
- **URL:** https://www.hackerrank.com/challenges/correctness-invariant

## Problem Statement

In the previous challenge, you wrote code to perform an _Insertion Sort_ on an unsorted array. But how would you prove that the code is correct? I.e. how do you show that for any input your code will provide the right output?

**Loop Invariant**  
In computer science, you could prove it formally with a _loop invariant_, where you state that a desired property is maintained in your loop. Such a proof is broken down into the following parts:

 - _Initialization_: It is true (in a limited sense) before the loop runs.
 - _Maintenance_: If it's true before an iteration of a loop, it remains true before the next iteration.
 - _Termination_: It will terminate in a useful way once it is finished. 

**Insertion Sort's Invariant**  
Say, you have some InsertionSort code, where the outer loop goes through the whole array $A$:

    for(int i = 1; i < A.length; i++){
    //insertion sort code

You could then state the following loop invariant:

> At the start of every iteration of the outer loop (indexed with $i$), the subarray until $ar[i]$ consists of the original elements that were there, but in sorted order. 

To prove Insertion Sort is correct, you will then demonstrate it for the three stages:

- _Initialization_ - The subarray starts with the first element of the array, and it is (obviously) sorted to begin with.

- _Maintenance_ - Each iteration of the loop expands the subarray, but keeps the sorted property. An element $V$  gets inserted into the array only when it is greater than the element to its left. Since the elements to its left have already been sorted, it means $V$ is greater than all the elements to its left, so the array remains sorted. (In _Insertion Sort 2_ we saw this by printing the array each time an element was properly inserted.)  
 
- _Termination_ - The code will terminate after $i$ has reached the last element in the array, which means the sorted subarray has expanded to encompass the entire array. The array is now fully sorted.

![Loop Invariant Chart](https://s3.amazonaws.com/hr-challenge-images/insertion-sort/InsertionSortCorrect-small.png)

You can often use a similar process to demonstrate the correctness of many algorithms. You can see [these notes](http://www.cs.uofs.edu/~mccloske/courses/cmps144/invariants_lec.html) for more information.

**Challenge**

In the InsertionSort code below, there is an error. Can you fix it? Print the array only once, when it is fully sorted. 



## Input Format

 There will be two lines of input:

 - $s$ - the size of the array
 - $arr$ - the list of numbers that makes up the array
 

## Output Format

Output the numbers in order, space-separated on one line.
 

## Constraints

 $1 \le s \le 1000$   
$-1500 \le V \le 1500, V ∈ arr$


## Sample Input

7 4 3 5 6 2

## Sample Output

2 3 4 5 6 7

## Explanation

The corrected code returns the sorted array.
