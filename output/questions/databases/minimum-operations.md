# Minimum Operations

- **Domain:** databases
- **Difficulty:** Medium
- **Max Score:** 45
- **Success Ratio:** 0.6656441717791411
- **Total Submissions:** 4238
- **Solved Count:** 2821
- **URL:** https://www.hackerrank.com/challenges/minimum-operations

## Problem Statement

In this challenge, the task is to debug the existing code to successfully execute all provided test files.
________________________________________________________________________________________

There are $n$ boxes in front of you. For each $i$, box $i$ contains $r[i]$ red balls, $g[i]$ green balls, and $b[i]$ blue balls. 
 
You want to separate the balls by their color. In each operation, you can pick a single ball from some box and put it into another box. The balls are separated if no box contains balls of more than one color.

Debug the given function `min_operations` and compute the minimal number of operations required to separate the balls.

Note: In this problem you can modify at most *six* lines of code and you cannot add any new lines.

*To restore the original code, click on the icon to the right of the language selector.*


## Input Format

The first line contains a single integer $n$.
The next $n$ lines $i$ contain three space-separated integers, $r[i]$, $g[i]$, and $b[i]$, respectively.



## Output Format

Print the minimal number of operations required to separate the balls. If this is impossible, return $-1$.


## Constraints

$1 \le n \le 100$  
$0 \le r[i],\ g[i],\ b[i] \le 105$ 

## Sample Input

1 1 1
1 1 1
1 1 1

## Explanation

Each box contains 1 ball of each color.  In this explanation, the goal will be to let the first box contain only red balls, the second box only blue balls, and the third box only green balls.

- Move 1 blue ball and 1 green ball from the first box to the second and third boxes.

- Move 1 red ball and 1 green ball from the second box to the first and third boxes.

- Move 1 red ball and 1 blue ball from the third box to the first and second boxes.

The number of operations is 6.
