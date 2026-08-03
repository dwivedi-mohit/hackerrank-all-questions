# Thread Count

## Metadata

- **ID:** 1541141
- **Type:** code
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Medium, Greedy, Priority Queue, Interviewer Guidelines, Trees
- **Skills:** Problem Solving (Intermediate)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates problem solving, priority queues, and tree data structure concepts, ideal for mid-level roles. The task is to determine the optimal thread configuration for micro-services in a tree structure while minimizing the total number of threads.

## Problem Statement

A system has service_nodes micro-services connected in a tree structure. Each micro-service can have a maximum number of threads[i], and adjacent micro-services must have maximum threads differing by exactly 1.

 

Some configurations were lost, and only k micro-services have known thread values, provided as currentValues[i] = [micro-service index, maximum threads].

 

Find the maximum number of threads for each micro-service such that the total number of threads in the system is minimized.

 

Example

service_nodes = 5

service_from = [1, 2, 3, 4]

service_to = [2, 3, 4, 5]

k = 2

currentValues = [[1, 3], [5, 3]]

 

 

The micro-services are connected as: (1,2), (2,3), (3,4), (4,5). Known configurations: micro-service 1 has 3 threads, micro-service 5 has 3 threads.

 

The optimal thread configuration is [3, 2, 1, 2, 3], where adjacent services differ by exactly 1 and the total is minimized.

 

Function Description

Complete the function getMinSumNodeValues in the editor with the following parameter(s):

    int service_nodes: the number of micro-services in the system

    int service_from[service_nodes - 1]: one end of the edges

    int service_to[service_nodes - 1]: other end of the edges

    int k: number of known configurations

    int currentValues[k][2]: the [micro-service index, maximum threads] pairs.

 

Returns

    int[service_nodes]: the initial configuration of the micro-services with the minimum possible live threads overall.

 

Constraints

	
- 1 ≤ service_nodes ≤ 105

	
- 1 ≤ service_from[i], service_to[i] ≤ service_nodes
	
- 1 ≤ k ≤ service_nodes

	
- 1 ≤ currentValues[i][0] ≤ service_nodes

	
- 1 ≤ currentValues[i][1] ≤ 106

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains two space-separated integers, service_nodes and service_nodes - 1, the number of micro-services and the number of edges.

Each of the next service_nodes - 1 lines contains two space-separated integers service_from[i] and service_to[i].

The next line contains an integer, k, the number of configurations left.

The next line contains an integer, k, the number of rows in currentValues.

The next line contains an integer, 2, the number of columns in currentValues[i].

Each line i of the next k lines (where 0 ≤ i < k) contains two integers, currentValues[i][0], and currentValues[i][1].

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

STDIN         FUNCTION
-----         --------
4 3      →    service_nodes = 4, service_nodes - 1 = 3
1 2      →    service_from = [1, 2, 2], service_to = [2, 3, 4]
2 3
2 4
3        →    k = 3
3        →    currentValues[] size rows = 3
2        →    currentValues[][] size c = 2
1 3      →    currentValues = [[1, 3], [2, 4], [3, 3]]
2 4
3 3

```

Sample Output

3
4
3
3
```

Explanation

 

There are 4 micro-services, and 3 edges: (1, 2), (2, 3), and (2, 4).

There are 3 configurations left: 1, 2, and 3, with values 3, 4, and 3, respectively.

The initial configuration is [3, 4, 3, 3], with the maximum live threads on adjacent micro-services differing by exactly one.

Sample Case 1

Sample Input For Custom Testing

STDIN         FUNCTION
-----         --------
3 2      →    service_nodes = 3, service_nodes - 1 = 2
1 2      →    service_from = [1, 1], service_to = [2, 3]
1 3
2        →    k = 2
2        →    currentValues[] size r = 2
2        →    currentValues[][] size c = 2
2 4      →    currentValues = [[2, 4], [3, 6]]
3 6

```

Sample Output

5
4
6
```

Explanation

 

There are 3 micro-services, and 2 edges: (1, 2), and (1, 3).

There are 2 configurations left: 2 and 3, with values 4 and 6, respectively.

The initial configuration is [5, 4, 6], with the maximum live threads on adjacent micro-services differing by exactly one.

## Sample Input/Output

## Preview

A system has service_nodes micro-services connected in a tree structure. Each
