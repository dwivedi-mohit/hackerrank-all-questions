# Function Call Logger

## Metadata

- **ID:** 2270491
- **Type:** code
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Python, Easy, String Formatting, List Manipulation, Functions
- **Skills:** Python (Basic)
- **Languages:** p, y, t, h, o, n, ,, p, y, t

## Summary

This coding question evaluates string formatting, list manipulation, and functions concepts, ideal for junior-level roles. The problem requires implementing a logging function that records function calls, their arguments, and return values in a list.

## Problem Statement

You're building a debugging tool to track which functions are being called and what they return. You need a simple logging function that records function execution without adding print statements everywhere. 

Your task is to implement a function that logs function calls and stores them in a list. The function should record the function name, the arguments used, and what the function returned.

 

Example 1

Input: 

add
2
2 3
5 7
```

Output: 

add(2, 3) -> 5 
add(5, 7) -> 12
```

Explanation:

The logger is created for an "add" function. Two calls are made: first with arguments 2 and 3 (returns 5), second with 5 and 7 (returns 12).

  

Example 2

Input: 

get_user
1
100
```

Output: 

get_user(100) -> User_100
```

Explanation:

The logger is created for a "get_user" function. One call is made with argument 100, which returns "User_100".

Function Parameters

- 
function_name (str): The name of the function being called

- 
args (list): List of arguments passed to the function

- 
result: The return value of the function

Returns

- 
None (stores the log entry in the global call_logs list)

Constraints

- 1 ≤ number of function calls ≤ 20

- Arguments are simple types: int, str, or bool

- Each function takes 1-2 arguments

- Function names contain only alphanumeric characters and underscores

- 1 ≤ length of function name ≤ 20

Input Format for Custom Testing

Input from stdin will be processed as follows and passed to the function:

Line 1: Function name (string)

Line 2: Number of function calls (n)

Next n lines: Space-separated arguments for each call (1-2 arguments per line)

## Sample Input/Output

## Preview

You're building a debugging tool to track which functions are being called and
