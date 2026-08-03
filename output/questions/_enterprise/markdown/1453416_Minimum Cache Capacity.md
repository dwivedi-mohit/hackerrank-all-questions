# Minimum Cache Capacity

## Metadata

- **ID:** 1453416
- **Type:** code
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Binary Search, Real-World, Easy
- **Skills:** Problem Solving (Basic)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates binary search, cache management, and algorithm optimization concepts, ideal for junior-level roles. The problem requires determining the minimum cache size needed to achieve a specified number of successful cache lookups from a sequence of item requests.

## Problem Statement

A system maintains a cache of fixed size. When the cache becomes full, the least recently added entry is removed to make room for the next one.

Given a sequence of item requests, determine the minimum cache size needed to achieve the desired number of successful cache lookups. A lookup is considered successful if the requested item is already present in the cache. If it is not possible to achieve the desired number of hits, return -1.

 

Example

Suppose requests = ["item1", "item2", "item3", "item1", "item3", “item4”], and the desired number of successful lookups (k) is 1.

 

If we use a cache size of 2, we get:

	
		
			Request Index
			Request
			Cache Before
			Cache After
			Cache Hit
		
	
	
		
			1
			item1
			[]
			[item1]
			No
		
		
			2
			item2
			[item1]
			[item1,item2]
			No
		
		
			3
			item3
			[item1,item2]
			[item2,item3]
			No
		
		
			4
			item1
			[item2,item3]
			[item3,item1]
			No
		
		
			5
			item3
			[item3,item1]
			[item1,item3]
			Yes
		
		
			6
			item4
			[item1,item3]
			[item3,item4]
			No
		
	

 

With any smaller cache size, we would not have had any successful cache lookups, therefore the answer is 2.

 

Function Description

Complete the function getMinimumSize in the editor with the following parameter(s):

    string requests[n]: the sequence of item access requests.

    int k: the minimum number of cache hits required for a valid cache size.

 

Returns

    int: the minimum possible cache size or -1

 

Constraints

	
- 1 ≤ k ≤ n ≤ 105

	
- 
requests[i] consists of lowercase characters and digits only, [a-z,0-9].

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains an integer, n, the number of elements in requests.

Each of the next n lines contains a string, requests[i].

The next line contains an integer, k.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

STDIN        FUNCTION
-----        --------
5       →    n = 5
item3   →    requests = ["item3", "item2", "item1", "item2", "item3"]
item2
item1
item2
item3
1       →    k = 1

```

Sample Output

2
```

Explanation

	
		
			Request Index
			Request
			Cache Before
			Cache After
			Cache Hit
		
	
	
		
			1
			item3
			[]
			[item3]
			No
		
		
			2
			item2
			[item3]
			[item2, item3]
			No
		
		
			3
			item1
			[item2, item3]
			[item1, item2]
			No
		
		
			4
			item2
			[item1, item2]
			[item2, item1]
			Yes
		
		
			5
			item3
			[item2, item1]
			[item3, item2]
			No
		
	

 

It is not possible to get k hits with cache size 1. However, with a cache size of 2, exactly one hit can be achieved.

Sample Case 1

Sample Input For Custom Testing

STDIN        FUNCTION
-----        --------
1        →   n = 1
item1    →   requests = ["item1"]
1        →   k = 1
```

Sample Output

-1
```

Explanation

No matter what's the size of our cache, we won't have at least 1 hit request in the end.

## Sample Input/Output

## Preview

A system maintains a cache of fixed size. When the cache becomes full, the lea
