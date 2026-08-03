# Adding Shapes

## Metadata

- **ID:** 1531226
- **Type:** code
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Easy, Classes, Operator Overloading, C++
- **Skills:** C++ (Basic)
- **Languages:** c, p, p, ,, c, p, p, 1, 4, ,

## Summary

This coding question evaluates classes, operator overloading, and geometric shapes concepts, ideal for junior-level roles. The problem requires implementing classes for Shapes, Circle, and Square, and overloading the addition operator to combine these objects effectively.

## Problem Statement

Implement three classes: Shapes, Circle, and Square, with operator overloading to combine these geometric objects.

 

The Circle class contains a public variable radius that stores the radius of the circle.

The Square class contains a public variable side that stores the length of a square's side.

The Shapes class acts as a container for multiple circles and squares, storing:

	
- 
set<int> circles_radius: a set containing the radii of all circles
	
- 
set<int> squares_side: a set containing the side lengths of all squares

Your task is to overload the addition operator (+) for the Shapes class to handle:

	
- Adding a Circle object to a Shapes object
	
- Adding a Square object to a Shapes object
	
- Adding two Shapes objects together

In all cases, the operation should return a new Shapes object that contains all the shapes from both operands.

 

 

 

Example

Shapes shapes;
shapes.circles_radius = {1,2,3};
shapes.squares_side = {5,6,7};

Circle circle;
circle.radius = 4;

Square square;
square.side = 8;

Shapes result1 = (shapes + circle); 
// result1.circles_radius contains {1,2,3,4}, result1.squares_side contains {5,6,7} 

Shapes result2 = (shapes + square);
// result2.circles_radius contains {1,2,3}, result2.squares_side contains {5,6,7,8} 

Shapes result3 = (result1 + result2);
// result3.circles_radius contains {1,2,3,4}, result3.squares_side contains {5,6,7,8} 

```

In this example:

	
- When adding a Circle with radius 4 to the Shapes object, the resulting Shapes object includes the new radius in its circles_radius set.
	
- When adding a Square with side 8 to the Shapes object, the resulting Shapes object includes the new side in its squares_side set.
	
- When adding two Shapes objects together, the resulting Shapes object contains the union of both circles_radius sets and both squares_side sets.

The program will process multiple queries that involve adding different objects together and will print the resulting sets in sorted order.

 

Query Format :

There are n1 instances of class Circle, n2 instances of class Square, and n3 instances of class Shapes.

Then there are q queries of format <class1> <index1> <class2> <index2> and add the index1th instance of class1 to index2th instance of class2. 

 

Notes:

	
- 
class1 is always equal to "Shapes" in the input.
	
- The provided code stub prints the resultant Shape for each query. For each query, in one line, the data in circles_radius is printed in sorted order, and in the next line, the data in squares_side is printed in sorted order.

 

Constraints

	
- 1 ≤ n1, n2, n3, q ≤ 100
	
- 1 ≤ side[i], radius[i] ≤ 1000
	
- 1 ≤ |circles_radius[i]| , |squares_side[i]| ≤ 10
	
- 1 ≤ circles_radius[i][j], squares_side[i][j] ≤ 1000
	
- 
class1 = "Shapes"
	
- 
class2 = {"Circle", "Square", "Shapes"}
	
- 1 ≤ index1 ≤ n3

	
- 1 ≤ index2 ≤ number of instances of class class2 

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains an integer, n1, the number of instances of class Circle.

The next line contains n1 space-separated integers denoting radius[i].

The next line contains an integer, n2, the number of instances of class Square.

The next line contains n2 space-separated integers denoting side[i].

The next line contains an integer, n3, the number of instances of class Shapes.

The next section contains 2 * n3 lines (2 for each instance of Shapes), the circles_radius[i] and squares_side[i]. Here, the first and second lines of each Shapes contains space-separated integers denoting circles_radius[i], and squares_side[i], respectively.

The next line contains an integer, q, the number of queries.

Each line i of the q subsequent lines (where 0 ≤ i < q) contains a query in format <class1> <index1> <class2> <index2>.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

STDIN                   Function
-----                   --------
2                       number of Circle objects n1 = 2
1 2                     circle radii = [1, 2]
2                       number of Square objects n2 = 2
5 9                     square sides = [5, 9]
1                       number of Shapes objects n3 = 1
1 4                     it has circles with radii [1, 4]
4                       and squares with sides [4]
2                       number of queries q = 2
Shapes 1 Circle 2       first query
Shapes 1 Shapes 1       second query 
```

Sample Output

1 2 4
4
1 4
4
```

Explanation

Create 2 instances of class Circle with radius 1 and 2.

Create 2 instances of class Square with side 5 and 9.

Create 1 instance of class Shapes with set circles_radius containing values {1, 4} and set squares_side containing values {4}.

Queries are -

	
- Shapes 1 Circle 2 - Adding both results in an instance of class Shapes with set circles_radius containing values {1, 2, 4} and set squares_side containing values {4}.
	
- Shapes 1 Shapes 1 - Adding both results in an instance of class Shapes with set circles_radius containing values {1, 4} and set squares_side containing values {4}.

Sample Case 1

Sample Input For Custom Testing

3
2 1 7
2
6 2
2
7 3 2
8 2
1 2 1
1
3
Shapes 1 Circle 2
Shapes 1 Shapes 2
Shapes 2 Square 2
```

Sample Output

1 2 3 7
2 8
1 2 3 7
1 2 8
1 2
1 2
```

Explanation

Here, n1 = 3, radius = [2, 1, 7], n2 = 2, side = [6, 2], n3 = 2, circles_radius = [[7, 3, 2], [1, 2, 1]], squares_side = [[8, 2], [1]], q = 3, queries = ["Shapes 1 Circle 2", "Shapes 1 Shapes 2", "Shapes 2 Square 2"]

Create 3 instances of class Circle with radius 2, 1, and 7.

Create 2 instances of class Square with side 6 and 2.

Create 2 instances of class Shapes with set circles_radius containing values {2, 3, 7} and set squares_side containing values {2, 8} as well as with set circles_radius containing values {1, 2} and set squares_side containing values {1}.

Queries are -

	
- Shapes 1 Circle 2 - Adding both results in an instance of class Shapes with set circles_radius containing values {1, 2, 3, 7} and set squares_side containing values {2, 8}.
	
- Shapes 1 Shapes 2 - Adding both results in an instance of class Shapes with set circles_radius containing values {1, 2, 3, 7} and set squares_side containing values {1, 2, 8}.
	
- Shapes 2 Square 2 - Adding both results in an instance of class Shapes with set circles_radius containing values {1, 2} and set squares_side containing values {1, 2}.

## Sample Input/Output

## Preview

Implement three classes: Shapes, Circle, and Square, with operator overloading
