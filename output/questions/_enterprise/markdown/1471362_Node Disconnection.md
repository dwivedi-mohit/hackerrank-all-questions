# Node Disconnection

## Metadata

- **ID:** 1471362
- **Type:** code
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Strings, Dynamic Programming, Hard, Real-World
- **Skills:** Problem Solving (Advanced)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates problem solving, dynamic programming, and string manipulation concepts, ideal for senior-level roles. The problem requires determining the minimum number of operations to disconnect all nodes in a compromised communication network represented by a string.

## Problem Statement

Secure a compromised communication network by disconnecting all nodes.

 

There is a series of nodes represented by lowercase English letters in a string. In a single operation, you can disconnect any number of adjacent nodes that are the same letter.

 

Determine the minimum number of operations required to disconnect all nodes and secure the network.

 

Example

series = "aabbaa":

 

The minimum number of operations required is 2:

	
- Disconnect the group "bb".
	
- Disconnect the remaining group "aaaa".

 

Function Description

Complete the function getMinOperations in the editor with the following parameter:

    string series: a series of nodes

 

Returns

    int: the minimum number of operations required to delete the entire series

 

Constraints

	
- 1 ≤ length of series ≤ 500
	
- It is guaranteed that series contains lowercase English letters only.

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The only line contains a string, series.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

STDIN         FUNCTION
-----         --------
abaca    →    series = "abaca"
```

Sample Output

3
```

Explanation

It is optimal to delete the substrings "b" and "c" first in two operations to get the string "aaa" which can be deleted in the next operation.

Sample Case 1

Sample Input For Custom Testing

STDIN         FUNCTION
-----         --------
abcddcba   →  series = "abcddcba"
```

Sample Output

4
```

Explanation

It is optimal to delete "dd" first to get "abccba", then "cc" to leave "abba", "bb" to get "aa", and finally, delete "aa".

## Sample Input/Output

## Preview

Secure a compromised communication network by disconnecting all nodes.
