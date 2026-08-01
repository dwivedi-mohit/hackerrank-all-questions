# Merge List

- **Domain:** regex
- **Difficulty:** Medium
- **Max Score:** 40
- **Success Ratio:** 0.7851145038167939
- **Total Submissions:** 2620
- **Solved Count:** 2057
- **URL:** https://www.hackerrank.com/challenges/merge-list

## Problem Statement

Shashank is very excited after learning about the *linked list*. He learned about how to *merge* two linked lists. When we merge two linked lists, the order of the elements of each list doesn't change. For example, if we merge $[1, 2, 3]$ and $[4,5,6]$, $[1,4,2,3,5,6]$ is a valid merge, while $[1,4,3,2,5,6]$ is not a valid merge because $3$ appears before $2$. 

Shashank wants you to solve a problem for him: You are given two lists having sizes $N$ and $M$. How many ways can we merge both the lists? It is given that all $N+M$ elements are distinct. As your answer can be quite large, Shashank wants you to print it $\bmod 10^9+7$. 

## Input Format

The first line contains an integer $T$, the number of test cases.  
Each of the next $T$ lines contains two integers $N$ and $M$.  


## Output Format

Print the value of the answer $\bmod 10^9+7$. 

## Constraints

+ $ 1\le T \le 10$  
+ $ 1\le N \le  100$  
+ $ 1\le M \le  100$  

## Sample Input

1
2 2

## Sample Output

6

## Explanation

Suppose the two lists are  and . The different ways of merging these lists are given below:
