# C: Max and min

## Metadata

- **ID:** 1190912
- **Type:** code
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Structures, Pointers, References, Easy
- **Skills:** C (Basic)
- **Languages:** c

## Summary

This coding question evaluates structures, pointers, and references concepts, ideal for junior-level roles. The problem requires implementing functions to manipulate structure instances using pointers, including swapping values, finding the maximum, and nullifying the minimum.

## Problem Statement

Implement three functions that manipulate two structure instances using their pointers.

 

Given two different instances of the same structure with member variables obj1.value and obj2.value, implement the following functions:

	
- 
swap(): Exchange the values of the member variables using their pointers
	
- 
find_Maximum(): Return the larger of the two integer values
	
- 
Nullify_Min(): Set the pointer with the lower value to NULL

 

Constraints

	
- 
	
1 ≤ obj1.value, obj2.value ≤ 105

	
	
- 
	
obj1.value != obj2.value

	

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

 

The only line contains two space-separated Integers.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

8 9
```

Sample Output

OBJ1 : 9
NULL

```

 

Explanation

After swapping, obj1.value = 9 and obj2.value = 8. After Nullify_Min, the pointer to obj2 is NULL.

Sample Case 1

Sample Input For Custom Testing

20 15
```

Sample Output

OBJ2 : 20
NULL

```

Explanation

After swapping, obj2.value = 20, which is higher than obj1.value = 15.

## Sample Input/Output

## Preview

Implement three functions that manipulate two structure instances using their
