# Super Stack

## Metadata

- **ID:** 111730
- **Type:** code
- **Difficulty:** 9.166666666666668
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Hard, Algorithms, Problem Solving, Data Structures, Stacks
- **Skills:** Problem Solving (Advanced)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates algorithms, data structures, and stack concepts, ideal for senior-level roles. The problem requires implementing a stack that performs a series of operations and prints the top element after each operation.

## Problem Statement

Implement a simple stack and perform a sequence of operations.

Implement a stack that accepts the following commands and performs the operations described:

	
- 
push v: Push integer v onto the top of the stack
	
- 
pop: Pop the top element from the stack
	
- 
inc i v: Add v to each of the bottom i elements of the stack

After each operation, print the value at the top of the stack. If the stack is empty, print the string 'EMPTY'.

 

Example

operations = ["push 4", "push 5", "inc 2 1", "pop", "pop"]

 

```

 

Expected output:

4
5
6
5
EMPTY

```

 

Function Description

Complete the superStack function in the editor below. After each operation, print the value of the stack's top element on a new line. If the stack is empty, print EMPTY instead.

 

superStack has the following parameter(s):

    string operations[n]:  an array of strings that represent operations on the stack

 

Prints

   string: the value of the stack's top element; if the stack is empty, print EMPTY, no return value is expected

 

Constraints

	
- 1 ≤ n ≤ 2 × 105

	
- -109 ≤ v ≤ 109

	
- 1 ≤ i ≤ |S|, where |S| is the size of the stack at the time of the operation.
	
- It is guaranteed that "pop" is never called on an empty stack.

Input Format for Custom Testing

The first line contains an integer n, the size of the array operations.

The next n lines each contain a string, operations[i].

Sample Case 0

Sample Input

STDIN     Function
-----     -----
12     →  operations[] size n = 12
push 4 →  operations = ["push 4", "pop", "push 3", "push 5", "push 2", "inc 3 1", "pop", "push 1", "inc 2 2", "push 4", "pop", "pop"]
pop
push 3
push 5
push 2
inc 3 1
pop
push 1
inc 2 2
push 4
pop
pop
```

 

Sample Output

4
EMPTY
3
5
2
3
6
1
1
4
1
8
```

 

Explanation

The diagram below depicts the stack after each operation:

After performing each operation, print the value at the top of the stack on a new line.

 

Start with an empty stack, S, expressed as an array where the lowest indexed element is the bottom of the stack and the highest is its top. Perform n = 12 operations as given:

	
- 
push 4: Push 4 onto the stack, so S = [4]. Print the top element, 4, on a new line.
	
- 
pop: Pop the top element from the top of the stack, so S = []. Print 'EMPTY' on a new line.
	
- 
push 3: Push 3 onto the stack, S = [3]. Print 3, and the top of the stack after each of the following operations.
	
- 
push 5: Push 5 onto the stack, S = [3, 5].
	
- 
push 2: Push 2 onto the stack, S = [3, 5, 2]. 
	
- 
inc 3 1: Add v = 1 to the bottom i = 3 elements of the stack, S = [4, 6, 3]. 
	
- 
pop: Pop the top element from the stack, S = [4, 6]. 
	
- 
push 1: Push 1 onto the stack, S = [4, 6, 1]. 
	
- 
inc 2 2: Add v = 2 to bottom i = 2 elements of the stack,  S = [6, 8, 1]. 
	
- 
push 4: Push 4 onto the stack, S = [6, 8, 1, 4]. 
	
- 
pop: Pop the top element from the stack, S = [6, 8, 1]. 
	
- 
pop: Pop the top element from the stack, S = [6, 8].

## Sample Input/Output

## Preview

Implement a simple stack and perform a sequence of operations.
