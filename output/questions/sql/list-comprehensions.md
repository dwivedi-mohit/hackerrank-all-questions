# List Comprehensions

- **Domain:** sql
- **Difficulty:** Easy
- **Max Score:** 10
- **Success Ratio:** 0.9767576930269117
- **Total Submissions:** 1262052
- **Solved Count:** 1232719
- **URL:** https://www.hackerrank.com/challenges/list-comprehensions

## Problem Statement

Let's learn about list comprehensions! You are given three integers $x, y$ and $z$ representing the dimensions of a cuboid along with an integer $n$. Print a list of all possible coordinates given by $(i, j, k)$ on a 3D grid where the sum of $i + j + k$ is not equal to $n$. Here, $0 \le i \le x; 0 \le j \le y; 0 \le k \le z$.  Please use list comprehensions rather than multiple loops, as a learning exercise.  

 **Example**  
 $x = 1$  
 $y = 1$  
 $z = 2$  
 $n = 3$
 
 All permutations of $[i, j, k]$ are:  
$[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 1, 2], [1, 0, 0], [1, 0, 1], [1, 0, 2], [1, 1, 0], [1, 1, 1], [1, 1, 2]]$. 
 
 Print an array of the elements that do not sum to $n = 3$.  
 
$[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 2]]$



## Input Format

Four integers $x, y, z$ and $n$, each on a separate line. 

## Constraints

Print the list in lexicographic increasing order.

## Sample Input

1
1
1
2

## Sample Output

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

## Explanation

Each variable  and  will have values of  or .  All permutations of lists in the form .

Remove all arrays that sum to  to leave only the valid permutations.
