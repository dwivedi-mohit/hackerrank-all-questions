# JavaScript: Async Generators

## Metadata

- **ID:** 1481359
- **Type:** code
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Generators, Promises, Hard, async await
- **Skills:** JavaScript (Advanced)
- **Languages:** j, a, v, a, s, c, r, i, p, t

## Summary

This coding question evaluates generator functions, promises, and async/await concepts, ideal for senior-level roles. The problem requires creating a generator function that processes input values based on their validity and yields corresponding results.

## Problem Statement

Create a JavaScript generator function named checker that takes an argument x.

 

If x is valid, meaning x ≤ 50, the function should yield the string “Processing”. After processing, it should yield either "Success" or "Error". "Success" occurs when x ≥ 25.

 

If x is not valid, it should yield the string "Invalid argument" and no further processing should be done.

 

There are n values of x provided. The validity and processing status of each x should be checked using two provided functions, isValid and processX, both of which return a promise that resolves or rejects based on the validity or processing result.

 

For example, if x = 30, the function should yield a value of "Processing", and then "Success". If x = 15, the function should yield "Processing", and then "Error". If x = 55, it should yield "Invalid argument".

 

Function Description

Complete the function checker in the editor below. The function should yield 1 or 2 strings.

 

checker has the following parameter(s):

    int x: a number

 

Constraints

	
- 1 ≤ x ≤ 100

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains an integer, n, the number of inputs.

Each line i of the n subsequent lines (where 0 ≤ i < n) contains an integer x.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

1
30
```

Sample Output

Processing
Success

```

Explanation

Output is based on two successful tests: 30 ≤ 50 and 25 ≤ 30.

Sample Case 1

Sample Input For Custom Testing

1
100
```

Sample Output

Invalid argument 
```

Explanation

 

Output is based on one unsuccessful test: 100 ≤ 50 is false, so isValid returns a promise.reject('Invalid argument').

## Sample Input/Output

## Preview

Create a JavaScript generator function named checker that takes an argument x.
