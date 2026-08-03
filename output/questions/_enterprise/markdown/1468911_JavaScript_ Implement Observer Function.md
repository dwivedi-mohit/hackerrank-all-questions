# JavaScript: Implement Observer Function

## Metadata

- **ID:** 1468911
- **Type:** code
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Medium, Closures, apply
- **Skills:** JavaScript (Intermediate)
- **Languages:** j, a, v, a, s, c, r, i, p, t

## Summary

This coding question evaluates closures, function application, and observability concepts, ideal for mid-level roles. The problem requires creating an observer function that enhances another function with observability features, including storing function name, arguments, and results.

## Problem Statement

Create a function named observer() that accepts another function and returns a new function with identical signature and functionality, but with added observability features.

 

The observer() function should add three functionalities to the base function:

	
- Store the function name
	
- Store the arguments passed to the function
	
- Store the function result

There is an instance of the Observe class called observeObj with three properties:

	
- 
name: to store the function name
	
- 
args: to store the arguments passed to the function
	
- 
result: to store the function result

The enhanced function should:

	
- Execute with the same behavior as the original function
	
- Update the observeObj with appropriate values during execution
	
- Pass observeObj to the base function as an additional parameter

The result will be automatically set when observeObj is passed to the base function, and the output is handled by the provided code.

 

For example, if f1 is observer(power), and f1 is called as f1(2,5), the result is "power was called with arguments 2, 5 and returned 32". power is the function name, 2, 5 are the arguments, and 32 is the result.

 

Function Description

Complete the function observer() in the editor with the following parameter: a function, named func.

 

It should return a function with the same signature and implementation as the function passed in its arguments.

 

Constraints

	
- 1 ≤ x,y ≤ 10

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first and only line should contain 2 integers x and y.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

2 5
```

Sample Output

power was called with arguments 2, 5 and returned 32
add was called with arguments 2, 5 and returned 7
```

Explanation

Provided code calls power and add with arguments 2 and 5, then prints the results as shown.

Sample Case 1

Sample Input For Custom Testing

6 5

```

Sample Output

power was called with arguments 6, 5 and returned 7776
add was called with arguments 6, 5 and returned 11

```

Explanation

Provided code calls power and add with arguments 2 and 5, then prints the results as shown.

## Sample Input/Output

## Preview

Create a function named observer() that accepts another function and returns a
