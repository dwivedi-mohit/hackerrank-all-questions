# Reverse a linked list

- **Domain:** fp
- **Difficulty:** Easy
- **Max Score:** 100
- **Success Ratio:** 0.9757146471034657
- **Total Submissions:** 3953
- **Solved Count:** 3857
- **URL:** https://www.hackerrank.com/challenges/three-month-preparation-kit-reverse-a-linked-list

## Problem Statement

<sub>This challenge is part of a tutorial track by [MyCodeSchool](http://www.youtube.com/mycodeschool) and is accompanied by a video lesson.</sub>

Given the pointer to the head node of a linked list, change the <code>next</code> pointers of the nodes so that their order is reversed. The head pointer given may be null meaning that the initial list is empty.  

**Example**  
$head$ references the list $1 \rightarrow 2 \rightarrow 3 \rightarrow NULL$  

Manipulate the $next$ pointers of each node in place and return $head$, now referencing the head of the list $3 \rightarrow 2 \rightarrow 1 \rightarrow NULL$.  

**Function Description**  

Complete the *reverse* function in the editor below.  

*reverse* has the following parameter:  

- *SinglyLinkedListNode pointer head:*  a reference to the head of a list  

**Returns**  

- *SinglyLinkedListNode pointer:*  a reference to the head of the reversed list  
 

## Input Format

The first line contains an integer $t$, the number of test cases.  

Each test case has the following format:  

The first line contains an integer $n$, the number of elements in the linked list.  
Each of the next $n$ lines contains an integer, the $data$ values of the elements in the linked list.  

## Output Format

  

## Constraints

- $1 \le t \le 10$  
- $1 \le n \le 1000$  
- $1 \le list[i] \le 1000$, where $list[i]$ is the $i^{th}$ element in the list.


## Sample Input

5
1
2
3
4
5

## Sample Output

5 4 3 2 1

## Explanation

The initial linked list is: .

The reversed linked list is: .
