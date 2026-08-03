# Dynamic Path Accessor

## Metadata

- **ID:** 1510541
- **Type:** code
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Python, Easy, Hash Map, OOP
- **Skills:** Python (Basic)
- **Languages:** p, y, t, h, o, n, ,, p, y, t

## Summary

This coding question evaluates Python, object-oriented programming, and hash map concepts, ideal for junior-level roles. The problem requires creating a function that retrieves values from a nested dictionary based on a specified string path.

## Problem Statement

Create a function named get_dict_value that:

	
- Accepts two parameters:
	
		
- 
dct: A dictionary
		
- 
path: A string representing nested keys separated by dots
	
	
	
- Returns:
	
		
- The value found at the specified path
		
- 
None if the path is not valid
	
	

Example

dct = {"a": {"b": {"c": 42}}}
get_dict_value(dct "a.b.c") # Returns 42
get_dict_value(dct, "a.b.d") # Returns None

```

 

Function Description

Complete the function get_dict_value in the editor with the following parameters:

    dct: a Python dictionary

    string path: the path to the desired value if it exists

 

Returns

    the value at the specified path, or None (the Python null value, not a string) if the path does not exist

 

Constraints

	
- 1 ≤ n (number of strings) ≤ 500
	
- 2 ≤ length of s[i] ≤ 100
	
- 1 ≤ m ≤ 200
	
- 1 ≤ paths[i] ≤ 200

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains an integer, n, denoting the number of lines for representing the object.

Each line i of the n subsequent lines (where 0 ≤ i < n) contains a string describing s[i].

The following line contains an integer, m, denoting the number of elements in the array path. 

Each line i of the m subsequent lines (where 0 ≤ i < m) contains a string describing paths[i]

Sample Case 0

Sample Input For Custom Testing

9
{
    "student" : {
        "roll_number" : "10",
        "class" : "1st"
    },
    "teacher" : {
        "school" : "ABC"
    }
}
2
student.roll_number
teacher.roll_number
```

Sample Output

10
None
```

Explanation

 

 

	
- 
paths[0] = student.roll_number, function should return dct["student"]["roll_number"] which is 10.
	
- 
paths[1] = teacher.roll_number, the function should return None since no such path exists.

Sample Case 1

Sample Input For Custom Testing

10
{
    "student" : {
        "roll_number" : "1",
        "class" : "10",
        "subject" : {
            "maths" : "true",
            "science" : "false"
        }
    }
}
2
student.roll_number
student.subject.physics
```

Sample Output

1
None
```

Explanation

	
- 
paths[0] = student.roll_number, the function should return dct[student][roll_number] which is 1.
	
- 
paths[1] = student.subject.physics, the function should return None since the path is undefined.

## Sample Input/Output

## Preview

Create a function named get_dict_value that:
