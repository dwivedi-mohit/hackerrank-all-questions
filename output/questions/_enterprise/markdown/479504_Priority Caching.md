# Priority Caching

## Metadata

- **ID:** 479504
- **Type:** code
- **Difficulty:** 8.61111111111111
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Medium, Implementation, Problem Solving
- **Skills:** Problem Solving (Intermediate)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates caching mechanisms, priority management, and log processing concepts, ideal for mid-level roles. The problem requires implementing a function to determine which items are in the cache based on access logs and priority rules.

## Problem Statement

A caching system uses 'priority' to determine which memory items are moved to the cache. All items start in the main memory with a priority of 0. The system follows these rules:

	
- The priority of all items decreases by 1 per second.
	
- When an item is accessed, its priority is increased by 2 instead of being decremented.
	
- The minimum priority is 0.
	
- When an item's priority exceeds 5, it is moved to the cache.
	
- When the priority of an item in the cache becomes less than or equal to 3, it is moved back to the main memory.
	
- If an item is accessed multiple times in the same second, its priority is increased by 2 times the number of accesses in that second.

 

The logs of all calls to access memory items will be provided in the format below, which may not be in sorted order:

`
<timestamp> <item_id>
`
```

 

Return the item IDs of all items in the cache in ascending order once the final log entry is made. If there are no items in the cache, return the array [-1].

 

For example, the logs are callLogs = [[1, 1], [2, 1], [2, 1], [4, 2], [5, 2], [6, 2]].  Both of the items start at priority 0. In the table below, the number of times an item is accessed at a time is shown in the "access" column. An item is in the cache at the times it has an asterisk. At the end, only item 2 is in the cache. Note that at second 2, item 1 was accessed twice, so its priority increased 2 * times accessed that second = 4.

 

Time    Item 1           Item 2
        access priority  access priority
0                0                0
1         1      2                0
2         2      6*               0
3                5*               0
4                4*        1      2
5                3         1      4
6                2         1      6*

```

 

Function Description

 

Complete the cacheContents function in the editor with the following parameter(s):

    int callLogs[n][2]: the logs of the calls made to memory

 

Returns

    int[]: the items present in the cache

 

Constraints

	
- 1 ≤ n ≤ 105
	
- 1 ≤ callLogs[i][j] ≤ 103

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains an integer, n, the number of log entries.

The next line contains an integer, 2, the number of parameters to describe a log entry.

Each line i of the n subsequent lines (where 0 ≤ i < n) contains the log entry in the form described above.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

STDIN   Function
-----   --------
6       callLogs[] size n = 6
2       callLogs[][] size = 2 always
1 1     callLogs = [[1, 1], [2, 1], [3, 1], [4, 2], [5, 2], [6, 2]]
2 1
3 1
4 2
5 2
6 2

```

Sample Output

2
```

Explanation

	
- 
3 calls are made for item 1, and by time 3, since the priority is 6, it is moved to the cache. Now its priority decays by 1 every second till time 6 at which it is moved back to the main memory.
	
- Similarly, 3 calls are made for item 2, and at time 6 it will be moved to the cache.

Sample Case 1

Sample Input For Custom Testing

6
2
1 1
2 1
3 2
4 2
5 1
6 1
```

Sample Output

1
```

Explanation

	
- At time 1, the priority of 1 is 2.

	
- At time 2, the priority of 1 is 4.
	
- At time 5, the priority of 1 is 4.

	
- At time 6, the priority of 1 is 6.

So, 1 is in the cache just after the last entry. The priority of item 2 does not reach 5.

## Sample Input/Output

## Preview

A caching system uses 'priority' to determine which memory items are moved to
