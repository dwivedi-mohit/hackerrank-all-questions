# How Will You Compare?

## Metadata

- **ID:** 203089
- **Type:** code
- **Difficulty:** 9.166666666666668
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Java, C++, C#, Overloading, OOPS, Easy, OOP
- **Skills:** Java (Basic), C# (Basic), C++ (Basic)
- **Languages:** c, p, p, ,, c, p, p, 1, 4, ,

## Summary

This coding question evaluates method overloading, string comparison, and array comparison concepts, ideal for junior-level roles. The problem requires creating a Comparator class with overloaded compare methods for different data types.

## Problem Statement

Create a Comparator class that includes three overloaded compare methods:

	
- 
boolean compare(string a, string b): Return true if a = b, otherwise return false.
	
- 
boolean compare(int a, int b): Return true if a = b, otherwise return false.
	
- 
boolean compare(int[] a, int[] b): Return true if both of the following conditions hold true. Otherwise, return false:
	
		
- The length of a = the length of b.
	

	
		
- Elements a[i] = b[i] for all indices.
	
	

 

Note for C++ implementations: Use Vector<int> for the array parameters.

 

Example

Suppose there are three tests: 

	
		
			Test Case
			type
			a
			b
			Output
			Explanation
		
	
	
		
			1
			1
			"hello world"
			"hello world"
			"Same"
			The strings are the same.
		
		
			2
			2
			3
			4
			"Different"
			The two integers are different (3 ≠ 4).
		
		
			3
			3
			{1,2,3}
			{1,2,3}
			"Same"
			Both arrays have the same number of elements, and each element a[i] = b[i]
		
		
			4
			1
			"Abc"
			"abc"
			"Different"
			The strings do not match the case.
		
	

 

Constraints

	
- For strings, 1 ≤ length of a, length of b ≤ 2000
	
- For integers, 0 ≤ a, b ≤ 10000000
	
- For integer arrays, 1 ≤ length of a, length of b ≤ 10

 

Test Case Input Format

 

The first line contains an integer T, the number of test cases.

Each of the next T sets of lines is in one of the following formats:

	
- The first line contains the integer 1 representing the comparison type (1, 2, or 3 for int, string, or array comparisons, respectively). The next two lines contain strings a and b.
	
- The first line contains the integer 2 representing the overloaded function type. The next two lines contain integers a and b.
	
- The first line contains the integer 3 representing the overloaded function type. The next three lines contain the following:
	
		
- Two space-separated integers n and m, the lengths of arrays a and b.
		
- A line of n space-separated integers a[i].
		
- A line of m space-separated integers b[i].

## Sample Input/Output

## Preview

Create a Comparator class that includes three overloaded compare methods:
