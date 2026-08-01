# Delete a Node

- **Domain:** data-structures
- **Difficulty:** Easy
- **Max Score:** 5
- **Success Ratio:** 0.9532929374979469
- **Total Submissions:** 334853
- **Solved Count:** 319213
- **URL:** https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list

## Problem Statement

<sub>This challenge is part of a tutorial track by [MyCodeSchool](http://www.youtube.com/mycodeschool) and is accompanied by a video lesson.</sub>


Delete the node at a given position in a linked list and return a reference to the head node. The head is at position 0. The list may be empty after you delete the node. In that case, return a null value. 

**Example**  

$llist = 0 \rightarrow 1 \rightarrow 2 \rightarrow 3$  
$position=2$  

After removing the node at position $2$, $llist' = 0 \rightarrow 1 \rightarrow 3$.  

**Function Description**  

Complete the *deleteNode* function in the editor below.  

*deleteNode* has the following parameters:  
- *SinglyLinkedListNode pointer llist:*  a reference to the head node in the list  
- *int position:*  the position of the node to remove

**Returns**  
- *SinglyLinkedListNode pointer:* a reference to the head of the modified list  

## Input Format

The first line of input contains an integer $n$, the number of elements in the linked list.  
Each of the next $n$ lines contains an integer, the node data values in order.  
The last line contains an integer, $position$, the position of the node to delete.  


## Constraints

- $1 \le n \le 1000$  
- $1 \le list[i] \le 1000$, where $list[i]$ is the $i^{th}$ element of the linked list.

## Sample Input

20
6
2
19
7
4
15
9
3

## Sample Output

20 6 2 7 4 15 9

## Explanation

The original list is . After deleting the node at position , the list is  .
