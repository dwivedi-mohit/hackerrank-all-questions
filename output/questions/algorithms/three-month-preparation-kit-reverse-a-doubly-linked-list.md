# Reverse a doubly linked list

- **Domain:** algorithms
- **Difficulty:** Easy
- **Max Score:** 100
- **Success Ratio:** 0.97517200119653
- **Total Submissions:** 3343
- **Solved Count:** 3260
- **URL:** https://www.hackerrank.com/challenges/three-month-preparation-kit-reverse-a-doubly-linked-list

## Problem Statement

<sub>This challenge is part of a tutorial track by [MyCodeSchool](http://www.youtube.com/mycodeschool)</sub>


Given the pointer to the head node of a doubly linked list, reverse the order of the nodes in place. That is, change the *next* and *prev* pointers of the nodes so that the direction of the list is reversed. Return a reference to the head node of the reversed list. 

**Note:** The head node might be NULL to indicate that the list is empty.  

**Function Description**

Complete the _reverse_ function in the editor below.  

reverse has the following parameter(s):

- *DoublyLinkedListNode head*: a reference to the head of a DoublyLinkedList  

Returns  
- *DoublyLinkedListNode*: a reference to the head of the reversed list  

## Input Format

The first line contains an integer $t$, the number of test cases.  

Each test case is of the following format:

-  The first line contains an integer $n$, the number of elements in the linked list.  
-  The next $n$ lines contain an integer each denoting an element of the linked list.

## Output Format

Return a reference to the head of your reversed list.  The provided code will print the reverse array as a one line of space-separated integers for each test case.  


## Constraints

- $1 \le t \le 10$  
- $0 \le n \le 1000$  
- $0 \le DoublyLinkedListNode.data \le 1000$   

## Sample Input

4
1
2
3
4

## Sample Output

4 3 2 1

## Explanation

The initial doubly linked list is:

The reversed doubly linked list is:
