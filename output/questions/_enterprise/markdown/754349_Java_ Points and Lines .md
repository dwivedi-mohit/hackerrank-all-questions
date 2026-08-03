# Java: Points and Lines 

## Metadata

- **ID:** 754349
- **Type:** code
- **Difficulty:** 7.5
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Java, OOPS, Easy, OOP
- **Skills:** Java (Basic)
- **Languages:** j, a, v, a, ,, j, a, v, a, 1

## Summary

This coding question evaluates object-oriented programming, class implementation, and data structure concepts, ideal for junior-level roles. The problem requires implementing a class that manages a list of lines and provides methods to retrieve the longest line and lines starting from a given point.

## Problem Statement

Given two fully implemented classes, Point and Line, review the provided code to understand their functionalities. Your task is to implement the class LineList, which should adhere to the ListOfLines interface to perform various operations on a list of lines. The ListOfLines interface includes:

	
- An attribute Vector<Line> list_of_lines that stores a collection of lines.
	
- A constructor that takes a Vector<Line> parameter to initialize the list_of_lines attribute.
	
- A method Line getLineWithMaxLength() that returns the first line with the maximum length from the list.
	
- A method Vector<Line> getLinesStartingFromPoint(Point p) that returns a list of all lines starting from the specified point p.

 

Note: The code stub will handle reading input and method calls.

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains an integer, n, denoting the number of lines.

Next, n lines are the coordinates for each line in the format [x[1] y[1] x[2] y[2]], where (x[1], y[1]) is the starting point and (x[2], y[2]) is the endpoint of the line.

The last line is the starting point for comparison. Format: [x y]

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input

STDIN        Function
-----        --------
4            number of lines n = 4
3 8 13 14    (x1, y1, x2, y2)[0] = 3, 8, 13, 14
8 4 3 12     (x1, y1, x2, y2)[1] = 8, 4, 3, 12
-7 -4 17 6   (x1, y1, x2, y2)[2] = -7, -4, 17, 6
7 3 1 2      (x1, y1, x2, y2)[3] = 7, 3, 1, 2
8 4          starting point (x, y) = 8, 4
```

Sample Output

Longest Line --> Start: (-7.0, -4.0) End: (17.0, 6.0)
Length: 26.00
All the Lines starting from point: (8.0, 4.0)
Start: (8.0, 4.0) End: (3.0, 12.0)
```

Explanation

4 is the total number of lines and (8, 4) is the point to find all the lines starting from this point.

Sample Case 1

Sample Input

STDIN        Function
-----        --------
5            number of lines n = 5
23 15 -4 8   (x1, y1, x2, y2)[0] = 23, 15, -4, 8
7 3 2 1      (x1, y1, x2, y2)[1] = 7, 3, 2, 1
-5 4 13 8    (x1, y1, x2, y2)[2] = -5, 4, 13, 8
7 3 19 -12   (x1, y1, x2, y2)[3] = 7, 3, 19, -12
3 8 1 0      (x1, y1, x2, y2)[4] = 3, 8, 1, 0
7 3          starting point (x, y) = 7, 3
```

Sample Output

Longest Line --> Start: (23.0, 15.0) End: (-4.0, 8.0)
Length: 27.89
All the Lines starting from point: (7.0, 3.0)
Start: (7.0, 3.0) End: (2.0, 1.0)
Start: (7.0, 3.0) End: (19.0, -12.0)
```

Explanation

5 is the total number of lines and (7, 3) is the point to find all the lines starting from this point.

## Sample Input/Output

## Preview

Given two fully implemented classes, Point and Line, review the provided code
