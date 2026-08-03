# Decrypting the Secret Code

## Metadata

- **ID:** 1255828
- **Type:** code
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Graphs, Problem Solving, Hard, Disjoint Set Union
- **Skills:** Problem Solving (Advanced)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates problem solving, graphs, and disjoint set union concepts, ideal for senior-level roles. The task requires determining indices of a secret array based on given sum queries, utilizing graph theory and union-find techniques.

## Problem Statement

There is a secret array arr of length n, along with a 2D array query with dimensions m × 2. Each row in query represents a pair (L, R) which gives the sum of elements arr[L] + arr[L+1] + ... + arr[R].

 

Your task is to determine all indices of arr whose values can be identified using the given information. Return a sorted list of these indices. If no value can be determined, return -1.

 

Example

n = 4

query = [[1, 3], [1, 2], [4, 4]]

	
- The first query gives the value of arr[1] + arr[2] + arr[3]

	
- The second query gives the value of arr[1] + arr[2]

	
- By subtracting the second from the first, we can determine arr[3]

	
- The third query directly gives the value of arr[4]

Therefore, return [3, 4].

 

Function Description

Complete the function findIndices in the editor with the following parameter(s):

    int n: the number of elements in the secret array

    int query[m][2]:  the queries

 

Returns

    int[]: each element denotes the index whose value can be determined, or a single element -1 if there are none

 

Constraints

	
- 1 ≤ n ≤ 105

	
- 1 ≤ m ≤ 105

	
- 1 ≤ l ≤ r ≤ n

 

Input Format for Custom Testing

The first line contains an integer n, the length of the secret array arr.

The second line contains an integer m, the length of the 2D array query.

The third line contains an integer 2, the length of each row of the 2D array query.

Each of the next m lines contains two space-separated integers (l[i], r[i]).

Sample Case 0

Sample Input 0

STDIN	    FUNCTION
-----	    --------
3      →    n = 3
3      →    the number of rows m = 3
2      →    the number of columns = 2
1 3    →    query = [[1, 3], [2, 2], [1, 2]]
2 2
1 2

```

Sample Output 0

1
2
3

```

Explanation

Determine the value of arr[1] by subtracting the value of the second query from the third query.

Determine the value of arr[2] from the second query.

Determine the value of arr[3] by subtracting the value of the second query from the first query.

 

The indexes are sorted and returned.

Sample Case 1

Sample Input 1

STDIN	    FUNCTION
-----	    --------
5      →    n = 5
4      →    the number of rows m = 4
2      →    the number of columns = 2
1 2    →    query = [[1, 2], [2, 3], [3, 4], [4, 5]]
2 3
3 4
4 5

```

Sample Output 1

-1

```

Explanation

There is no way to determine the value of any index.

## Sample Input/Output

## Preview

There is a secret array arr of length n, along with a 2D array query with dime
