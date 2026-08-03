# PHP: Find Distinct Values

## Metadata

- **ID:** 1099992
- **Type:** code
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** PHP, Easy
- **Skills:** PHP (Basic)
- **Languages:** p, h, p

## Summary

This coding question evaluates PHP, array manipulation, and unique value extraction concepts, ideal for junior-level roles. The problem requires writing a function that returns unique string representations of numeric values from various PHP data types.

## Problem Statement

Write a function called getNumericSerial that accepts any number of parameters of any PHP basic types and returns an array of unique string representations of numeric values in the order they are encountered.

 

Parameters that have the same numeric value (e.g., string "3" and integer 3) should appear only once in the result.

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

Each line contains a representation of some PHP basic data type such as string, integer, double, boolean, array, object, or NULL.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

NULL
true
"5307960008521383065"
(array) []
NULL
"40677969607080247"
"ufxnbdykaznsdjmvcxtzjgykndzwfrcneqwsww ehhrfvghluvbraoikiplo alapdudtw xhvatcryeoejbis mcjpbpgsqzsnxgqktmlgqtyfummxzpoecbiiykrquvhjfo l"
"40677969607080247"
(array) ["n","v","x","s","y","h","t","a","g","o","p","e","z","u","w","r","f","d","k","q","l","c","b","m","j","i"]
(array) ["p","i","k","c","w","u","s","g","h","b","e","t","v","f","l","o","d","m","q","z","r","x","j","n","y","a"]
""

```

Sample Output

Array
(
    [0] => 5307960008521383065
    [1] => 40677969607080247
)
```

Explanation

First there is one instance of "5307960008521383065". Later there are two instances of "40677969607080247". Return a string array with one instance of each, in that order.

Sample Case 1

Sample Input For Custom Testing

-1582100940029737916
"-3551543384285510568"
false
3234111455748959455
""
"3705467050913974522"
(object) ["x","f","a","i","q","m","h","r","j","d","l","u","w","n","y","p","t","e","g","o","z","v","b","k","s","c"]
NULL
3234111455748959455
NULL
0
-1582100940029737916

```

Sample Output

Array
(
    [0] => -1582100940029737916
    [1] => -3551543384285510568
    [2] => 3234111455748959455
    [3] => 3705467050913974522
    [4] => 0
)

```

Explanation

One instance of each distinct numeric parameter value is returned.

## Sample Input/Output

## Preview

Write a function called getNumericSerial that accepts any number of parameters
