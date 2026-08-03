# Copy Assignment Operator: Swapping Objects

## Metadata

- **ID:** 312525
- **Type:** code
- **Difficulty:** 9.722222222222221
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** OOPS, Medium, C++, Language Proficiency, Problem Solving, OOP
- **Skills:** C++ (Intermediate)
- **Languages:** c, p, p, ,, c, p, p, 1, 4

## Summary

This coding question evaluates object-oriented programming, C++ proficiency, and problem-solving concepts, ideal for mid-level roles. The problem requires creating two Contest objects, swapping their scores, and printing the results before and after the swap.

## Problem Statement

Swap the references to objects

Create two instances of the Contest class using lists of scores data, and then swap the scores data between them. When each object is instantiated, a message indicating the initial scores will be printed. After the swap routine is executed, messages indicating the scores post-swap will be printed.

 

Your function should follow these steps:

	
- Instantiate a Contest object named first_contest with the scores from the array first.
	
- Instantiate a Contest object named second_contest with the scores from the array second.
	
- Swap the scores between the first_contest and second_contest objects.

 

Example 1

first = [1, 2, 3]

second = [2, 3, 4]

 

After swapping the scores, the first_contest object's scores become [2, 3, 4] and the second_contest object's scores become [1, 2, 3].

 

Provided code prints the results:

`Before swapping the scores: 1 2 3 
Before swapping the scores: 2 3 4 
After swapping the scores: 2 3 4 
After swapping the scores: 1 2 3`
```

Note: The locked code stub in the editor defines the Contest class. It has a private data member, vector<int> scores, describing the scores of all the challenges featured in a contest. It handles all data output.

 

Constraints

0 ≤ first[i],second[j] ≤ 100

1 ≤ length of first, length of second ≤ 10

## Sample Input/Output

## Preview

Swap the references to objects
