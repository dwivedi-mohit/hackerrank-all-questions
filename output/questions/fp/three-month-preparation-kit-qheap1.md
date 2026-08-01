# QHEAP1

- **Domain:** fp
- **Difficulty:** Easy
- **Max Score:** 100
- **Success Ratio:** 0.9294037011651817
- **Total Submissions:** 1459
- **Solved Count:** 1356
- **URL:** https://www.hackerrank.com/challenges/three-month-preparation-kit-qheap1

## Problem Statement

This question is designed to help you get a better understanding of *basic heap* operations.  

There are $3$ types of query:

- "$1$ $v$"  - Add an element $v$ to the heap.  
- "$2$ $v$"  - Delete the element $v$ from the heap.  
- "$3$" - Print the minimum of all the elements in the heap.

**NOTE**: It is guaranteed that the element to be deleted will be there in the heap. Also, at any instant, only distinct elements will be in the heap.

## Input Format

The first line contains the number of queries, $Q$.    
Each of the next $Q$ lines contains one of the $3$ types of query.   

**Constraints**  
$ 1 \le Q \le 10^5 $  
$ -10^9 \le v \le 10^9 $

## Output Format

For each query of type $3$, print the minimum value on a single line.  

## Sample Input

STDIN       Function
-----       --------
5           Q = 5
1 4         insert 4
1 9         insert 9
3           print minimum
2 4         delete 4
3           print minimum

## Sample Output

9

## Explanation

After the first  queries, the heap contains {}. Printing the minimum gives  as the output. Then, the  query deletes  from the heap, and the  query gives  as the output.
