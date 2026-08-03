# Area calculator

## Metadata

- **ID:** 1411208
- **Type:** code
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** OOPS, C++, Easy, OOP
- **Skills:** C++ (Basic)
- **Languages:** c, p, p, ,, c, p, p, 1, 4, ,

## Summary

This coding question evaluates object-oriented programming, class design, and method implementation concepts, ideal for junior-level roles. The problem requires implementing a TriangleArea class to calculate the area of a triangle using both Pythagorean and Heron's formulas.

## Problem Statement

This problem involves calculating the area of a triangle with different formulas.

 

 Pythagorean Formula  =  0.5 × B × H 

B and H are the base and height of a triangle.

 

 

 Heron's Formula  =    s ( s - a ) ( s - b ) ( s - c )   

a, b and c are sides of the triangle, and s is the semi-perimeter of the triangle given by the formula s  = (a + b + c) / 2.

 

Implement the classes and methods defined below.

 

	
- A class named TriangleArea:

	
		
			
				Instance Variables
			
			
				Name
				Functionality
			
			
				B
				Stores the base of the triangle
			
			
				H
				Stores the height of the triangle
			
			
				a
				Stores the length of the first side of the triangle
			
			
				b
				Stores the length of the second side of the triangle
			
			
				c
				Stores the length of the third side of the triangle
			
		
	
	
	
- 
	
 

	
		
			
				Constructor
			
			
				Name
				Functionality
			
			
				TriangleArea(int B, int H)
				
				
A parameterized constructor that initializes the instance variables with base and height.

				
			
			
				TriangleArea(int a, int b, int c)
				A parameterized constructor that initializes the instance variables with the lengths of sides of the triangle.
			
		
	
	
	
-  
	
		
			
				Methods
			
			
				Name
				Functionality
			
			
				void getArea()
				
				
Prints the area of the triangle for both methods separated by a new line.

				
			
		
	

	
 

	

A main method is provided in the locked portion of the editor. It parses five values. The first two values are the base and height of the triangle. The next three values are (a, b, c) sides of the triangle. 

 

While printing area as ans by Pythagorean formula, 2*ans should be printed.

While printing area as ans by Heron's formula, return the value square of ans (ans*ans) as the answer.

 

The output must be in the order of Area calculated by the Pythagorean formula and Heron's Formula separated by a new line.

 

Note: Areas might differ for the same triangle since the input configurations might differ while calculating area from Heron's and Pythagorean formulas. 

 

Constraints

	
- -100 ≤ a, b, c, base, height ≤ 100
	
- It is guaranteed that the value of the perimeter is even.

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first two lines contains two integers, height and base, denoting the height and base of the triangle.

The next three lines contains three integers, a, b, c, denoting the length of sides of the triangle.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

STDIN          FUNCTION
-------        ----------
1         →    height = 1, base = 3
3
2         →    a = 2, b = 2, c = 2
2
2

```

Sample Output

3
3

```

Explanation

Area by Pythagorean formula = 1.5, 2*ans = 3

Area by Herons formula = sqrt(3), ans*ans = 3

Sample Case 1

Sample Input For Custom Testing

 STDIN          FUNCTION
-------        ----------
1         →    height = 1, base = 10
10
3         →    a = 3, b = 3, c = 4
3
4
```

Sample Output

10
20
```

Explanation

Area by Pythagorean formula = 5, 2*ans = 10

Area by Herons formula = sqrt(20), ans*ans = 20

## Sample Input/Output

## Preview

This problem involves calculating the area of a triangle with different formul
