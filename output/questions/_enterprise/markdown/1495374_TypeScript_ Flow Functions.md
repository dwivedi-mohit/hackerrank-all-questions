# TypeScript: Flow Functions

## Metadata

- **ID:** 1495374
- **Type:** code
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Medium, Functions, TypeScript
- **Skills:** TypeScript (Intermediate)
- **Languages:** t, y, p, e, s, c, r, i, p, t

## Summary

This coding question evaluates functions, TypeScript, and functional programming concepts, ideal for mid-level roles. The problem requires implementing a function that creates a flow between a list of functions, passing results sequentially as arguments.

## Problem Statement

Implement a function called flow that takes in a list of functions (functionsList) and creates a flow between them. When invoked, the result of the first function is passed as arguments to the second function, and so on.

 

The function flow should return a function. Only the first function in the list can have a variable number of arguments. Each subsequent function requires one argument, which is the return value of the previous function.

 

The functions used are:

	
- 
add(): Takes a variable number of arguments and returns the sum of the arguments
	
- 
square(a): Takes a number as an argument and returns the square of a
	
- 
splitter(a): Takes a number as an argument, splits the number into 2 halves, and returns a list of length 2
	
- 
max(a): Takes a number or array of numbers as an argument and returns the maximum value
	
- 
min(a): Takes a number or array of numbers as an argument and returns the minimum value

 

Example

functionList = ["add", "splitter"]

 

The function call flow(functionList) should return a function, (call it functionsFlow for this example). If argumentsList = [2, 3], then functionsFlow(2, 3) should return [2, 3]:

	
- 
add(2, 3) returns 5
	
- 
splitter(5) returns [2, 3]

 

Function Description

Complete the function flow in the editor with the following parameters:

    string functionList[fn]: an array of functions

 

Returns

 

Constraints

	
- 1 ≤ n ≤ 15
	
- functionList[0] = add
	
- 
functionList[i] = {square, splitter, max, min}, where i ≠ 0
	
- 1 ≤ q ≤ 10, length of argumentsList

	
- 1 ≤ argumentsList[i] ≤ 10
	
- It is guaranteed that the list of functions generates a valid flow.

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains an integer, n, denoting the number of elements in functionList.

Each line i of the n subsequent lines (where 0 ≤ i < n) contains a string describing functionList[i].

The first line contains an integer, q, denoting the number of elements in argumentsList.

Each line i of the q subsequent lines (where 0 ≤ i < q) contains an integer describing argumentsList[i].

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

STDIN        Function
-----        --------
3            functionList[] size n = 3
add          functionList = ["add", "splitter", "max"]
splitter
max
3            argumentsList[] size q = 3
2            arguentsList = [2, 1, 3]
1
3
```

Sample Output

3
```

Explanation

functionsFLow(2, 1, 3) is processed as:

	
- 
add(2, 1, 3) -> 6
	
- 
splitter(6) -> [3, 3]
	
- 
max([3, 3]) -> 3

Sample Case 1

Sample Input For Custom Testing

STDIN        Function
-----        --------
3            functionList[]size n = 3
add          functionList = ["add", "square", "splitter"]
square
splitter
2
2
4
```

Sample Output

18
18
```

Explanation

 

functionsFlow(2, 4) is processed as:

	
- 
add(2, 4) -> 6
	
- 
square(6) -> 36
	
- 
splitter(36) -> [18, 18]

## Sample Input/Output

## Preview

Implement a function called flow that takes in a list of functions (functionsL
