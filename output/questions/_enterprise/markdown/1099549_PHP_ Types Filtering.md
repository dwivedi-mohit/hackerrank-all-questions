# PHP: Types Filtering

## Metadata

- **ID:** 1099549
- **Type:** code
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Easy, PHP
- **Skills:** PHP (Basic)
- **Languages:** p, h, p

## Summary

This coding question evaluates class definition, array manipulation, and method implementation concepts, ideal for junior-level roles. The problem requires defining a class that processes an array to return distinct numbers and strings while preserving their order.

## Problem Statement

Define a class called FilterClass with the following specifications:

The constructor accepts a single parameter $data, which is an array that can contain various types of elements.

Implement three public methods:

	
- 
getNumbers(): Returns an array of all distinct numbers in $data, preserving their original order of appearance
	
- 
getStrings(): Returns an array of all distinct strings in $data, preserving their original order of appearance
	
- 
getAll(): Returns an array of all elements in $data, irrespective of their type, preserving their original order of appearance

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

Each line contains an array element of any type, e.g., string, integer, double, boolean, array, object, or NULL.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

"Lorem ipsum dolor sit amet, consectetur adipiscing elit"
true
"Lorem ipsum dolor sit amet, consectetur adipiscing elit"
47801
"ed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
18042

```

Sample Output

Array
(
    [numbers] => Array
        (
            [0] => 47801
            [1] => 18042
        )

    [strings] => Array
        (
            [0] => Lorem ipsum dolor sit amet, consectetur adipiscing elit
            [1] => ed do eiusmod tempor incididunt ut labore et dolore magna aliqua
        )

    [all] => Array
        (
            [0] => Lorem ipsum dolor sit amet, consectetur adipiscing elit
            [1] => 1
            [2] => Lorem ipsum dolor sit amet, consectetur adipiscing elit
            [3] => 47801
            [4] => ed do eiusmod tempor incididunt ut labore et dolore magna aliqua
            [5] => 18042
        )

)
```

Explanation

Returns the elements as described. Note that the returned boolean value true is automatically represented as 1 in the output.

Sample Case 1

Sample Input For Custom Testing

""
(array) []
""
"Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore"
"ed do eiusmod tempor"

```

Sample Output

Array
(
    [numbers] => Array
        (
        )

    [strings] => Array
        (
            [0] => 
            [1] => Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore
            [2] => ed do eiusmod tempor
        )

    [all] => Array
        (
            [0] => 
            [1] => Array
                (
                )

            [2] => 
            [3] => Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore
            [4] => ed do eiusmod tempor
        )

)

```

Explanation

Returns the elements as described. Note that empty values, strings, and arrays in this sample are included in the returned array.

## Sample Input/Output

## Preview

Define a class called FilterClass with the following specifications:
