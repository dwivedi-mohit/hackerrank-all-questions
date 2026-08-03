# C++ Inheritance: Area

## Metadata

- **ID:** 161180
- **Type:** code
- **Difficulty:** 8.333333333333334
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** C++, Easy, Problem Solving, Interviewer Guidelines
- **Skills:** C++ (Basic)
- **Languages:** c, p, p, ,, c, p, p, 1, 4

## Summary

This coding question evaluates class implementation, multiple inheritance, and area calculation concepts, ideal for junior-level roles. The problem requires implementing Rectangle and Triangle classes that inherit from Polygon and Output, with methods to calculate and return their areas.

## Problem Statement

Implement two classes with multiple inheritance.

Implement two classes using multiple inheritance:

	
- A Rectangle class that:

	
		
- Inherits from both Polygon and Output classes
		
- Implements an area method that returns the rectangle's area
	
	
	
- A Triangle class that:
	
		
- Inherits from both Polygon and Output classes
		
- Implements an area method that returns the triangle's area
	
	

The area formulas are:

	
- Rectangle area = width × height

	
- Triangle area = (width × height) / 2

The implementation will work with existing Polygon and Output classes. The area methods must return an integer that denotes the area of the shape it is being called on. This is printed to stdout by the Output::print(int i) method called by locked stub code in the editor.

 

Note: Recall that the area of a rectangle is width × height and the area of a triangle is (width × height)⁄2.

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

Locked stub code in the editor creates Rectangle and Triangle objects and tests their implementations using the following input, which it reads from stdin:

A single line of two space-separated integers, the values of width and height.

Sample Case 0

Sample Input 0

9 8

```

 

Sample Output 0

Output class STDOUT: 72
Output class STDOUT: 36
```

 

Explanation

The values for width and height are 9 and 8.

area(rectangle(width, height)) = width × height = 9 × 8 = 72

area(triangle(width, height)) =(width × height)⁄2 = (9 × 8)⁄2 = 36

## Sample Input/Output

## Preview

Implement two classes with multiple inheritance.
