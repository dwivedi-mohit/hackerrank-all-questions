# Server Transition

## Metadata

- **ID:** 1637379
- **Type:** code
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Hash Map, Comparison, Prefix Sum, Linear Search, Arrays, Easy, Brute Force
- **Skills:** Problem Solving (Basic)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates problem solving, linear search, and prefix sum concepts, ideal for junior-level roles. The task is to calculate the minimum total time required to visit a sequence of servers in a circular network, considering transition times between them.

## Problem Statement

A circular network contains m servers labeled 1 to m, with server 1 adjacent to server m. From any server, you may move to either adjacent server (previous or next in the circle).

An array transitionTime of length m is given, where transitionTime[i] is the time (in seconds) required to move from server i to either of its adjacent servers.

You are also given an array requestedServers of length n, representing the servers that must be visited in the exact order listed, starting from server 1.

Find the minimum total time required to visit every server in requestedServers in order.

	
- Visiting the server you are already on takes 0 time.
	
- For each move between consecutive required servers, choose the direction (clockwise or counterclockwise) that yields the smaller total transition time along the path.

 

 

-->

 

Example

m = 3

n = 4

transitionTime = [3, 2, 1]

requestedServers = [1, 3, 3, 2]

 

	
- The pointer is initially at server 1, and the first server to be visited is number 1, hence it takes 0 seconds to visit it.
	
- To move from server 1 to 3, the path followed could be 1 → 2 → 3, which takes 3 + 2 = 5 seconds, or the path could be 1 → 3, which takes 3 seconds. Choosing the shorter path, server 3 is visited in 3 seconds.
	
- The pointer is already at server 3, so the third server takes no time to visit.
	
- To move from server 3 to 2, either the path could be 3 → 2, which takes 1 second, or the path could be 3 → 1 → 2, which takes 1 + 3 = 4 seconds. Choosing the shorter path, the fourth required server is visited in 1 second after visiting the third server.

Hence, the total minimum possible time to visit all the required servers is 4 seconds.

 

Function Description

Complete the function getMinimumTime in the editor with the following parameter(s):

    int requestedServers[n]: the sequence of servers to be visited

    int transitionTime[m]: the time taken to switch connections from each server and connect to its adjacent server

 

Returns

    long: the minimum total time required to visit all the requested servers, considering the transition time of servers

 

Constraints

	
- 1 ≤ n ≤ 2 * 105

	
- 1 ≤ requestedServers[i]  ≤ m

	
- 1 ≤ m ≤ 1000
	
- 1 ≤ transitionTime[i]  ≤ 106

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains an integer n, the number of elements in requestedServers.

Each of the next n lines contains an integer, requestedServers[i].

The next line contains an integer m, the number of elements in transitionTime.

Each of the next m lines contains an integer, transitionTime[i].

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

STDIN     FUNCTION
-----     ---------
4     →   requestedServers[] size n = 4
2     →   requestedServers = [2, 3, 3, 1]
3
3
2
3     →   transitionTime[] size m = 3
3     →   transitionTime = [3, 2, 1]
2
1
```

Sample Output

6
```

Explanation

	
- The pointer is initially at server 1. To move from server 1 to 2, the path followed could be 1 → 2, which takes 3 seconds, or the path could be 1 → 3 → 2, which takes 3 + 1 = 4 seconds. Choosing the shorter path, server 2 is visited in 3 seconds.
	
- To move from server 2 to 3, the path followed could be 2 → 1 → 3, which takes 3 + 2 = 5 seconds, or the path could be 2 → 3, which takes 2 seconds. Choosing the shorter path, server 3 is visited in 2 seconds.
	
- The pointer is already at server 3, so the third server takes no time to visit.
	
- Finally, to move from server 3 to 1, either the path could be 3 → 1, which takes 1 second, or the path could be 3 → 2 → 1, which takes 1 + 2 = 3 seconds. Choosing the shorter path, the fourth required server is visited in 1 second after visiting the third server.

The minimum possible time to visit all the required servers is 3 + 2 + 0 + 1 = 6 seconds.

Sample Case 1

Sample Input For Custom Testing

STDIN     FUNCTION 
-----     --------
3     →   requestedServers[] size n = 3
1     →   requestedServers = [1, 2, 1]
2
1
2     →   transitionTime[] size m = 2
1     →   transitionTime = [1, 2]
2

```

Sample Output

3
```

Explanation

	
- 
	
The pointer is initially at server 1. Therefore, it takes no time to reach the first server.

	
	
- 
	
To move from server 1 to 2, the path followed is 1 → 2, which takes 1 second.

	
	
- 
	
Finally, to move from 2 to 1, the path is 2 → 1, which takes 2 seconds.

	

The minimum possible time to visit all the required servers is 0 + 1 + 2 = 3 seconds.

## Sample Input/Output

## Preview

A circular network contains m servers labeled 1 to m, with server 1 adjacent t
