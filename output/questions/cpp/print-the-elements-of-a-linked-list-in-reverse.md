# Print in Reverse

- **Domain:** cpp
- **Difficulty:** Easy
- **Max Score:** 5
- **Success Ratio:** 0.979597156100441
- **Total Submissions:** 318436
- **Solved Count:** 311939
- **URL:** https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list-in-reverse

## Problem Statement

<sub>This challenge is part of a tutorial track by [MyCodeSchool](http://www.youtube.com/mycodeschool) and is accompanied by a video lesson.</sub>

Given a pointer to the head of a singly-linked list, print each $data$ value from the reversed list.  If the given list is empty, do not print anything.

**Example**  

$head*$ refers to the linked list with $data$ values $1 \rightarrow 2 \rightarrow 3 \rightarrow NULL$  

Print the following:  
`
3  
2  
1  
`

**Function Description**  

Complete the *reversePrint* function in the editor below.  

*reversePrint* has the following parameters:  

- *SinglyLinkedListNode pointer head:*  a reference to the head of the list

**Prints**  

The $data$ values of each node in the reversed list.  


## Input Format

The first line of input contains $t$, the number of test cases.  

The input of each test case is as follows:  

- The first line contains an integer $n$, the number of elements in the list.  
- Each of the next *n* lines contains a data element for a list node.

## Constraints

- $1 \le n \le 1000$  
- $1 \le list[i] \le 1000$, where $list[i]$ is the $i^{th}$ element in the list.  

## Sample Input

5
16
12
4
2
5
3
7
3
9
5
5
1
18
3
13

## Sample Output

2
4
12
16
9
3
7
13
3
18
1
5

## Explanation

There are three test cases.  There are no blank lines between test case output.

The first linked list has  elements: . Printing this in reverse order produces:

5

2

4

12

16

The second linked list has  elements: . Printing this in reverse order produces:

9

3

7

The third linked list has  elements: . Printing this in reverse order produces:

13

3

18

1

5
