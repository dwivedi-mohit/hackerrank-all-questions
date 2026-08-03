# Task Scheduling

## Metadata

- **ID:** 1468934
- **Type:** code
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Real-World, Medium
- **Skills:** Problem Solving (Intermediate)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates problem solving, binary search, and task scheduling concepts, ideal for mid-level roles. The problem requires determining the minimum time to process tasks based on memory requirements and types, with constraints on parallel processing.

## Problem Statement

Given an array taskMemory of n positive integers representing memory required for each task, an array taskType of n positive integers representing task types, and an integer maxMemory, find the minimum time required to process all tasks.

 

Each task takes 1 unit of time. The server can process at most two tasks in parallel only if they are the same type and together require no more than maxMemory units.

 

Example

Suppose n = 4, taskMemory = [7, 2, 3, 9], taskType = [1, 2, 1, 3], and maxMemory = 10.

 

One efficient schedule is shown.

	
		
			Task Pair
			Task 1
			Task 2
			Task Type
			Memory Requirement
			Within Max Memory
			Can Process in Parallel
		
	
	
		
			1
			0
			2
			Same
			7 + 3 = 10
			Yes
			Yes
		
		
			2
			1
			3
			Different
			9 + 2 = 11
			No
			No
		
	

 

Tasks 0 and 2 are processed concurrently, but the other two must be processed separately due to their memory requirements and because they are not the same type. The minimum amount of time required to process all the tasks is 3 units.

 

Function Description

Complete the function getMinTime in the editor with the following parameter(s):

    int taskMemory[n]: the memory required by the tasks

    int taskType[n]: the type of the tasks

    int maxMemory: the maximum total memory that can be allocated to the tasks

 

Returns

    int: the minimum time required to process all tasks

 

Constraints

	
- 1 ≤ n ≤ 2*105

	
- 1 ≤ maxMemory ≤ 109

	
- 1 ≤ taskMemory[i] ≤ maxMemory

	
- 1 ≤ taskType[i] ≤ 109

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains an integer, n, the number of elements in taskMemory.

The following n lines contain an integer, taskMemory[i].

The next line contains an integer, n, the number of elements in taskType.

The following n lines contain an integer, taskType[i].

The last line contains an integer, maxMemory.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

STDIN          FUNCTION
-----          --------
5        →     n = 5
1        →     taskMemory = [1, 2, 3, 4, 2]
2
3
4
2
5        →     n = 5
1        →     taskType = [1, 2, 1, 2, 3]
2
1
2
3
4        →     maxMemory = 4
```

Sample Output

4
```

Explanation

The first and the third tasks are processed in parallel. The other three tasks need to be processed individually. The second and fourth use too much memory together, and the fifth is a unique type.

Sample Case 1

Sample Input For Custom Testing

STDIN          FUNCTION
-----          --------
3        →     n = 3
1        →     taskMemory = [1, 2, 5]
2
5
3        →     n = 3
1        →     taskType = [1, 2, 3]
2
3
6        →     maxMemory = 6
```

Sample Output

3
```

Explanation

All the tasks are of different types and must be processed separately.

## Sample Input/Output

## Preview

Given an array taskMemory of n positive integers representing memory required
