# TypeScript: Sequential Promise Resolution

## Metadata

- **ID:** 1494605
- **Type:** code
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Hard, Promises, async await
- **Skills:** TypeScript (Advanced)
- **Languages:** t, y, p, e, s, c, r, i, p, t

## Summary

This coding question evaluates promises, async/await, and error handling concepts, ideal for senior-level roles. The problem requires implementing a function to resolve promises in a specified order, handling potential rejections appropriately.

## Problem Statement

Implement a function sequentialResolution that takes:

	
- An array of promises (promises)
	
- An array of indices (order)

The promises should be resolved in the order specified by the order array. After each promise resolves, push its returned value to a global array called resolvedPromises.

 

If a promise fails to resolve, the function should throw an error with the message "Error Thrown" and no further promises should be resolved.

Each promise i uses the variable promises[i] from the input:

	
- If promises[i] is not equal to 0, the promise resolves and returns promises[i]

	
- If promises[i] equals 0, the promise rejects with the error message "Error Thrown"

The function should not return anything.

 

Example

promises = [1, 2, 1] order = [2, 1, 3]

	
- Second promise resolves first (value 2)
	
- First promise resolves second (value 1)
	
- Third promise resolves last (value 1)

Promises are resolved as [2, 1, 1].

 

Function Description

Complete the function sequentialResolution in the editor below. The function should resolve promises sequentially and should not return anything. If any promise fails to resolve, the function should throw an error, and no further promises should be resolved.

 

sequentialResolution has the following parameters:

    promises[promises[0],...promises[n-1]]:  an array of promises

    order[order[0],...order[n-1]]:  an array of indices

 

Constraints

	
- 1 ≤ n, promises[i] ≤ 100
	
- Array order is a permutation of integers 1 to n.

	
- It is guaranteed that either one or no promise is rejected.

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains an integer, n, the number of elements in promises.

Each line i of the n subsequent lines (where 0 ≤ i < n) contains an integer, promises[i].

The next line contains an integer, n, the number of elements in order.

Each line i of the n subsequent lines (where 0 ≤ i < n) contains an integer, order[i].

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

STDIN    Function
-----    --------
4        promises[] size n = 4
1        promises = [1, 2, 0, 1]
2
0
1
4        order[] size n = 4
2        order = [2, 1, 3, 4]
1
3
4
```

Sample Output

2
1
Error Thrown

```

Explanation

 

The second promise should be resolved first followed by the first. The third promise is rejected, and an error is thrown with the message "Error Thrown".

Sample Case 1

Sample Input For Custom Testing

STDIN    Function
-----    --------
4        promises[] size n = 4
3        promises = [3, 4, 1, 3]
4
1
3
4        order[] size n = 4
1        order = [1, 4, 2, 3]
4
2
3
```

Sample Output

3
3
4
1
```

Explanation

 

The first promise should be resolved first followed by the fourth, the second, and the third. No promise is rejected.

## Sample Input/Output

## Preview

Implement a function sequentialResolution that takes:
