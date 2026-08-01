# Lego Blocks

- **Domain:** python
- **Difficulty:** Medium
- **Max Score:** 100
- **Success Ratio:** 0.9090909090909091
- **Total Submissions:** 1331
- **Solved Count:** 1210
- **URL:** https://www.hackerrank.com/challenges/three-month-preparation-kit-lego-blocks

## Problem Statement

You have an infinite number of 4 types of lego blocks of sizes given as (depth x height x width):

```
d	h	w
1	1	1
1	1	2
1	1	3
1	1	4
```

Using these blocks, you want to make a wall of height $n$ and width $m$. Features of the wall are:  
<br>
- The wall should not have any holes in it.   
- The wall you build should be one solid structure, so there should not be a straight vertical break across all rows of bricks.   
- The bricks must be laid horizontally.   

How many ways can the wall be built?

**Example**  

$n = 2$   
$m = 3$  

The height is $2$ and the width is $3$.  Here are some configurations:  

![image](https://s3.amazonaws.com/hr-assets/0/1526322298-72d127a6f7-bricks.png)  

These are not all of the valid permutations.  There are $9$ valid permutations in all.  

**Function Description**  

Complete the *legoBlocks* function in the editor below.  

legoBlocks has the following parameter(s):

- *int n:* the height of the wall  
- *int m:* the width of the wall   

**Returns**  
- *int:* the number of valid wall formations modulo $(10^9+7)$  

## Input Format

The first line contains the number of test cases $t$.  

Each of the next $t$ lines contains two space-separated integers $n$ and $m$.  


## Constraints

$1 \le t \le 100$  
$1 \le n,m \le 1000$  


## Sample Input

STDIN   Function
-----   --------
4       t = 4
2 2     n = 2, m = 2
3 2     n = 3, m = 2
2 3     n = 2, m = 3
4 4     n = 4, m = 4

## Sample Output

7
9
3375

## Explanation

For the first case, we can have:

For the second case, each row of the wall can contain either two blocks of width 1, or one block of width 2. However, the wall where all rows contain two blocks of width 1 is not a solid one as it can be divided vertically. Thus, the number of ways is  and .
