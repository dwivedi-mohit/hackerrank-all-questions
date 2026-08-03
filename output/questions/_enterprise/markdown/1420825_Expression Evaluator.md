# Expression Evaluator

## Metadata

- **ID:** 1420825
- **Type:** code
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Easy, C++, Implementation, Strings
- **Skills:** C++ (Basic)
- **Languages:** c, p, p, ,, c, p, p, 1, 4, ,

## Summary

This coding question evaluates C++, string manipulation, and mathematical expression evaluation concepts, ideal for junior-level roles. The problem requires implementing a class to check if the result of a mathematical expression fits within the C++ int data type.

## Problem Statement

Implement an Evaluator class that determines whether the result of a mathematical expression can be stored in the C++ int data type.

class Evaluator{
  public:
    bool check(string expression){

    }
};

```

The expression consists of space-separated integers and operators (+ and - only).

 

Example

expression = "134 + 13 - 19"

	
- The expression evaluates to 128.
	
- 128 can be stored in the int data type.
	
- The check method should return true.

Note that the expression is always valid, with operators properly separated by spaces and integers.

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains an integer q, the number of calls.

Each line i of the q subsequent lines (where 0 ≤ i < q) contains a string, expression.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

STDIN                     Function
-----                     --------
2                      →  the number of calls, q = 2
128 - 13 - 2                
398198412981 - 1   
```

Sample Output

1
0

```

Explanation

 

	
- 
expression[0] = "128 - 13 - 2" evaluates to 113, which can be stored in the int data type.
	
- 
expression[1] = "398198412981 - 1" evaluates to 398198412980, which cannot be stored in the int data type.

 

Sample Case 1

Sample Input For Custom Testing

STDIN                     Function
-----                     --------
1                      →  the number of calls, q = 1
1 + 1 + 1 + 10

```

Sample Output

1
```

Explanation

 

	
- 
expression[0] = "1 + 1 + 1 + 10" evaluates to 13, which can be stored in the int data type.

## Sample Input/Output

## Preview

Implement an Evaluator class that determines whether the result of a mathemati
