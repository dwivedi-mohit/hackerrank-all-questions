# Server Upgrade

## Metadata

- **ID:** 1643429
- **Type:** code
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Easy, Arrays, Sorting, Greedy Algorithms
- **Skills:** Problem Solving (Basic)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates arrays, sorting, and greedy algorithms concepts, ideal for junior-level roles. The problem requires maximizing the total efficiency of server batches based on their upgrade capacities.

## Problem Statement

You are given n servers, where capacity[i] is the upgrade capacity of the ith server.

You must partition all servers into exactly k batches:

	
- Batch sizes are fixed and given by numServers[0..k-1].
	
- 
sum(numServers) = n, so every server is used exactly once.

For any batch:

	
- Let maxCap be the maximum capacity among servers in the batch.
	
- Let minCap be the minimum capacity among servers in the batch.
	
- The batch’s efficiency is maxCap - minCap.

Your goal is to assign servers to the k batches to:

	
- maximize the total efficiency
	
		
- efficiency(batch1) + efficiency(batch2) + ... + efficiency(batchk)
	
	

Return the maximum possible total efficiency.

 

Example

n = 4

k = 2

capacity = [3, 6, 1, 2]

numServers = [1, 3]

 

One optimal assignment is:

	
- Batch 1 takes the first server. Its efficiency is 3 - 3 = 0.
	
- Batch 2 takes the servers at indices 1, 2, and 3. Its efficiency is 6 - 1 = 5.

The sum of efficiencies is 0 + 5 = 5.

 

Function Description

Complete the function getMaximumEfficiency in the editor with the following parameter(s):

    int capacity[n]: the upgrade capacity of each server

    int numServers[k]: the number of servers in each upgrade batch

 

Returns

    long: the maximum possible sum of efficiencies of k upgrade batches

 

Constraints

	
- 1 ≤ n ≤ 2 * 105

	
- 1 ≤ k ≤ n

	
- 1 ≤ capacity[i] ≤ 109

	
- 1 ≤ numServers[i] ≤ n

	
- ∑ numServers[i] = n

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains an integer n, the number of elements in capacity.

Each of the next n lines contains an integer capacity[i].

The next line contains an integer k, the number of elements in numServers.

Each of the next k lines contains an integer numServers[i].

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

STDIN         FUNCTION
-----         --------
4        →    capacity[] size n = 4
1        →    capacity = [1, 2, 3, 4]
2
3
4
1        →    numServers[] size k = 1
4        →    numServers = [4]

```

Sample Output

3
```

Explanation

Since there is only one batch to upgrade all the servers, the efficiency of the batch is 4 - 1 = 3.

Sample Case 1

Sample Input For Custom Testing

STDIN         FUNCTION 
-----         --------
3        →    capacity[] size n = 3
4        →    capacity = [4, 2, 1]
2
1
3        →    numServers[] size k = 3
1        →    numServers = [1, 1, 1]
1
1

```

Sample Output

0
```

Explanation

Since the size of each server upgrade batch is 1, all 3 servers are upgraded in different batches, and the efficiency of each batch is 0.

## Sample Input/Output

## Preview

You are given n servers, where capacity[i] is the upgrade capacity of the ith
