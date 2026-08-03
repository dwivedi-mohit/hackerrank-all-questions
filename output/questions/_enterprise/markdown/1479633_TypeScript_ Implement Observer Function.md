# TypeScript: Implement Observer Function

## Metadata

- **ID:** 1479633
- **Type:** code
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Medium, Closures, apply
- **Skills:** TypeScript (Intermediate)
- **Languages:** t, y, p, e, s, c, r, i, p, t

## Summary

This coding question evaluates closures, function monitoring, and TypeScript concepts, ideal for mid-level roles. The problem requires implementing an observer function that tracks the name, arguments, and results of a given function without altering its behavior.

## Problem Statement

Implement a function observer() that enhances a given function with monitoring capabilities without changing its behavior. The enhanced function will track its name, arguments, and results.

 

The observer() function should work with an existing Observe class instance called observeObj that has three properties:

	
- 
name: stores the function name
	
- 
args: stores the arguments passed to the function
	
- 
result: stores the function's return value

 

Requirements

When using the observer() function:

	
- The returned function should behave exactly like the original
	
- The function name should be stored in observeObj.name`
	
- The arguments should be stored in `observeObj.args

	
- The result will be automatically stored in observeObj.result

 

Example

function power(x, y) {
    return Math.pow(x, y);
}

const observedPower = observer(power);
observedPower(2, 5);

```

This would output: "power was called with arguments 2, 5 and returned 32"

 

Here is what happens step by step:

	
- The observer() wraps the power function
	
- When observedPower(2, 5) is called:
	
		
- "power" is stored as the function name
		
- [2, 5] is stored as the arguments
		
- 32 (25) is stored as the result
		
- The original function behavior is preserved
	
	

 

Function Description

Complete the function observer() in the editor with the following parameters:

    function func: the function to observe

 

 

It should return a function with the same signature and implementation as the function passed in its arguments.

 

Constraints

	
- 1 ≤ x, y ≤ 10

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first and only line contains two space-separated integers x and y.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

STDIN   Function
-----   --------
2 5     x = 2, y = 5
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

Implement a function observer() that enhances a given function with monitoring
