# Save the Prisoner!

- **Domain:** ai
- **Difficulty:** Easy
- **Max Score:** 15
- **Success Ratio:** 0.8376456104169036
- **Total Submissions:** 255047
- **Solved Count:** 213639
- **URL:** https://www.hackerrank.com/challenges/save-the-prisoner

## Problem Statement

A jail has a number of prisoners and a number of treats to pass out to them.  Their jailer decides the fairest way to divide the treats is to seat the prisoners around a circular table in sequentially numbered chairs.  A chair number will be drawn from a hat.  Beginning with the prisoner in that chair, one candy will be handed to each prisoner sequentially around the table until all have been distributed.

The jailer is playing a little joke, though.  The last piece of candy looks like all the others, but it tastes *awful*.  Determine the chair number occupied by the prisoner who will receive that candy.

**Example**  

$n = 4$  
$m = 6$  
$s = 2$  

There are $4$ prisoners, $6$ pieces of candy and distribution starts at chair $2$.  The prisoners arrange themselves in seats numbered $1$ to $4$.  Prisoners receive candy at positions $2, 3, 4, 1, 2, 3$.  The prisoner to be warned sits in chair number $3$.  

**Function Description**

Complete the *saveThePrisoner* function in the editor below.  It should return an integer representing the chair number of the prisoner to warn.  

saveThePrisoner has the following parameter(s):  

- *int n*:  the number of prisoners  
- *int m*:  the number of sweets  
- *int s*:  the chair number to begin passing out sweets from  

**Returns**  

- *int:* the chair number of the prisoner to warn

## Input Format

The first line contains an integer, $t$, the number of test cases. 	
The next $t$ lines each contain $3$ space-separated integers: 

- $n$: the number of prisoners  
- $m$: the number of sweets  
- $s$: the chair number to start passing out treats at  


## Constraints

* $1 \le t \le 100$  
* $1 \le n \le 10^9$
* $1 \le m \le 10^9$
* $1 \le s \le n$


## Sample Input

2
5 2 1
5 2 2

## Sample Output

2
3

## Explanation

In the first query, there are  prisoners and  sweets. Distribution starts at seat number .  Prisoners in seats numbered  and  get sweets.  Warn prisoner .

In the second query, distribution starts at seat  so prisoners in seats  and  get sweets.  Warn prisoner .

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
