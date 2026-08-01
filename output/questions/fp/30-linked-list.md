# Day 15: Linked List

- **Domain:** fp
- **Difficulty:** Easy
- **Max Score:** 30
- **Success Ratio:** 0.9880356659840025
- **Total Submissions:** 207032
- **Solved Count:** 204555
- **URL:** https://www.hackerrank.com/challenges/30-linked-list

## Problem Statement

**Objective**	
Today we will work with a *Linked List*. Check out the [Tutorial](/challenges/30-linked-list/tutorial) tab for learning materials and an instructional video.  

****

A *Node* class is provided for you in the editor. A *Node* object has an integer data field, $data$, and a *Node* instance pointer, $next$, pointing to another node (i.e.: the next node in the list).

A *Node insert* function is also declared in your editor. It has two parameters: a pointer, $head$, pointing to the first node of a linked list, and an integer, $data$,  that must be added to the end of the list as a new *Node* object. 

**Task**	
Complete the *insert* function in your editor so that it creates a new *Node* (pass $data$ as the *Node* constructor argument) and inserts it at the tail of the linked list referenced by the $head$ parameter. Once the new node is added, return the reference to the $head$ node. 	

**Note:** The $head$ argument is *null* for an empty list.  

## Input Format

The first line contains *T*, the number of elements to insert. 	
Each of the next $T$ lines contains an integer to insert at the end of the list.  



## Output Format

Return a reference to the $head$ node of the linked list. 

## Sample Input

STDIN   Function
-----   --------
4       T = 4
2       first data = 2
3
4
1       fourth data = 1

## Sample Output

2 3 4 1

## Explanation

, so your method will insert  nodes into an initially empty list.

First the code returns a new node that contains the data value  as the  of the list. Then create and insert nodes , , and  at the tail of the list.
