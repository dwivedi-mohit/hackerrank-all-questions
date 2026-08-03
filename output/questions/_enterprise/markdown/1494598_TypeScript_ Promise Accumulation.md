# TypeScript: Promise Accumulation

## Metadata

- **ID:** 1494598
- **Type:** code
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Medium, async await, Promises
- **Skills:** TypeScript (Intermediate)
- **Languages:** t, y, p, e, s, c, r, i, p, t

## Summary

This coding question evaluates generator functions, promise handling, and asynchronous programming concepts, ideal for mid-level roles. The problem requires implementing a generator function that processes promises, yielding values based on their resolution or rejection.

## Problem Statement

Implement a generator function promiseAccumulation() that processes an arbitrary number of promises according to specific rules.

The generator function should:

	
- Receive any number of promises as input
	
- Yield the returned value if a promise resolves
	
- Yield -1 if a promise rejects, and then stop yielding values

Example

For the promises [Promise.resolve(10), Promise.reject(), Promise.resolve(20)]:

	
- The generator should yield 10 (from the first resolved promise)
	
- Then yield -1 (from the rejected promise)
	
- Then stop (without yielding the value from the third promise)

Note: The test cases guarantee that there will be at most 1 rejected promise.

 

Function Description

Complete the function promiseAccumulation() in the editor below. promiseAccumulation() should yield an integer value based on the value in promiseArr.

 

promiseAccumulation() has a single parameter

    promiseArr: an array of promises.

 

Constraints

	
- 1 ≤ n ≤ 50
	
- 1 ≤ x ≤ 100

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains an integer n, the number of numbers. 

The following n lines contain a single integer, x.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

STDIN    Function
-----    --------
2        n = 2
75       x values passed are 75, 26
26

```

Sample Output

75
26

```

Explanation

 

The function promiseReturn() returns a resolve for both numbers.

Sample Case 1

Sample Input For Custom Testing

STDIN    Function
-----    --------
5        n = 5
72       x values are 72, 81, 47, 29, 97
81
47
29
97

```

Sample Output

-1

```

Explanation

 

The function promiseReturn() returns a reject for 72. No promises are resolved after that.

## Sample Input/Output

## Preview

Implement a generator function promiseAccumulation() that processes an arbi
