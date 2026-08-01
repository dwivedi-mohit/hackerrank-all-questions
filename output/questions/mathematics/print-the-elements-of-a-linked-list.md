# Print the Elements of a Linked List

- **Domain:** mathematics
- **Difficulty:** Easy
- **Max Score:** 5
- **Success Ratio:** 0.9711771559241329
- **Total Submissions:** 552756
- **Solved Count:** 536824
- **URL:** https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list

## Problem Statement

This challenge is part of a [MyCodeSchool](http://www.youtube.com/mycodeschool) tutorial track and is accompanied by a [video lesson](http://www.youtube.com/embed/vcQIFT79_50?theme=light).

----

This exercise focuses on traversing a linked list. You are given a pointer to the $head$ node of a linked list. The task is to print the $data$ of each node, one per line. If the head pointer is $null$, indicating the list is empty, nothing should be printed.  
  

**Function Description**  

Complete the $printLinkedList$ function with the following parameter(s):  

-	$SinglyLinkedListNode\ head$: a reference to the head of the list  

**Print**  

-	For each node, print its $data$ value on a new line (console.log in Javascript).

## Input Format

The first line of input contains $n$, the number of elements in the linked list.  
The next $n$ lines contain one element each, the $data$ values for each node.


**Note:** Do not read any input from stdin/console. Complete the printLinkedList function in the editor below.

## Output Format

  

## Constraints

- $1 \le n \le 1000$  
- $1 \le list[i] \le 1000$, where $list[i]$ is the $i^{th}$ element of the linked list.

## Sample Input

STDIN   Function
-----   --------
2       n = 2
16      first data value = 16
13      second data value = 13

## Sample Output

13

## Explanation

There are two elements in the linked list. They are represented as 16 -> 13 -> NULL. So, the  function should print 16 and 13 each on a new line.
