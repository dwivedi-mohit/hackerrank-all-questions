# Iterate It

- **Domain:** regex
- **Difficulty:** Expert
- **Max Score:** 90
- **Success Ratio:** 0.432021815348656
- **Total Submissions:** 2567
- **Solved Count:** 1109
- **URL:** https://www.hackerrank.com/challenges/iterate-it

## Problem Statement

Consider the following pseudocode, run on an array $A = [a_0, a_1, \ldots, a_{n - 1}]$ of length $n$:

```pascal
rep := 0
while A not empty:
    B := []
    for x in A, y in A:
        if x != y: append absolute_value(x - y) to B
    A := B
    rep := rep + 1
```

Given the values of $n$ and array $A$, compute and print the final value of $rep$ after the pseudocode above terminates; if the loop will never terminate, print `-1` instead.

## Input Format

The first line contains a single integer, $n$, denoting the length of array $A$. 	 
The second line contains $n$ space-separated integers describing the respective values of $a_0, a_1, \ldots, a_{n - 1}$.

## Output Format

Print the final value of $rep$ after the pseudocode terminates; if the loop will never terminate, print `-1` instead.

## Constraints

+ $1 \le n \le 10^5$  
+ $1 \le a_i \le 5 \times 10^4 ~ \forall ~ 1 \le i \le n$

## Sample Input

3
1 3 4

## Sample Output

4

## Explanation

After the first loop,  becomes . After the second loop, the array only contains 's and 's. After the third loop, the array only contains 's. After the fourth loop, the array is empty. Because the value of  is incremented after each loop,  at the time the loop terminates. Thus, we print 4 as our answer.
