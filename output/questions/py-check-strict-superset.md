# Check Strict Superset

- **Domain:** ai
- **Difficulty:** Easy
- **Max Score:** 10
- **Success Ratio:** 0.9584997634546402
- **Total Submissions:** 166987
- **Solved Count:** 160057
- **URL:** https://www.hackerrank.com/challenges/py-check-strict-superset

## Problem Statement

You are given a set $A$ and $n$ other sets.   
Your job is to find whether set $A$ is a strict superset of each of the $N$ sets.   

Print `True`, if $A$ is a *strict superset* of each of the $N$ sets. Otherwise, print `False`. 

A strict superset has at least one element that does not exist in its subset.  

**Example**  
Set$([1, 3, 4])$ is a _strict superset_ of set$([1,3])$.  
Set$([1, 3, 4])$ is not a _strict superset_ of set$([1, 3, 4])$.   
Set$([1, 3, 4])$ is not a _strict superset_ of set$([1, 3, 5])$.  

## Input Format

The first line contains the space separated elements of set $A$.  
The second line contains integer $n$, the number of other sets.   
The next $n$ lines contains the space separated elements of the other sets.  



## Output Format

Print `True` if set $A$ is a _strict superset_ of all other $N$ sets. Otherwise, print `False`.

## Constraints

+ $0 < len(set(A)) < 501$   
+ $0 < N < 21 $  
+ $0 < len(otherSets) < 101$  



## Sample Input

1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12

## Sample Output

False

## Explanation

Set  is the strict superset of the set but not of the set because  is not in set .

Hence, the output is False.

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
