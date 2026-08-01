# Maximum Element

- **Domain:** sql
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.7488881265391637
- **Total Submissions:** 163238
- **Solved Count:** 122247
- **URL:** https://www.hackerrank.com/challenges/maximum-element

## Problem Statement

You have an empty sequence, and you will be given $N$ queries. Each query is one of these three types:

	1 x  -Push the element x into the stack.
    2    -Delete the element present at the top of the stack.
    3    -Print the maximum element in the stack.

**Function Description**  

Complete the *getMax* function in the editor below.   

*getMax* has the following parameters:  
- *string operations[n]:* operations as strings   

**Returns**  
- *int[]:* the answers to each type 3 query   

## Input Format

The first line of input contains an integer, $n$. The next $n$ lines each contain an above mentioned query.   



## Output Format

  

## Constraints

 **Constraints**  
$1 \le n \le 10^5$  
$1 \le x \le 10^9$  
$1 \le type \le 3$   
All queries are valid.  



## Sample Input

STDIN   Function
-----   --------
10      operations[] size n = 10
1 97    operations = ['1 97', '2', '1 20', ....]
2
1 20
2
1 26
1 20
2
3
1 91
3

## Sample Output

91
