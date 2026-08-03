# C#: User Inheritance

## Metadata

- **ID:** 859271
- **Type:** code
- **Difficulty:** 7.5
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Inheritance, C#, Easy
- **Skills:** C# (Basic)
- **Languages:** c, s, h, a, r, p

## Summary

This coding question evaluates class inheritance, object-oriented programming, and enum usage concepts, ideal for junior-level roles. The problem requires implementing a user system with an abstract class and derived classes for Admin and Moderator.

## Problem Statement

Implement a class inheritance hierarchy for a user system.

Create an abstract class User with:

	
- Member variables: type (string), name (string), gender (Gender enum), age (int)
	
- A constructor that assigns values to these variables
	
- Member functions: GetUserName(), GetUserType(), GetAge(), GetGender()

Create two derived classes:

	
- 
Admin - inherits from User

	
		
- Constructor takes name, gender, age and calls the base constructor with type "Admin"
	
	
	
- 
Moderator - inherits from User
	
		
- Constructor takes name, gender, and age and calls the base constructor with type "Moderator"
	
	

The Gender enum is defined as:

public enum Gender
{
   Male,
   Female,
   Other
}

```

 

The implementation will be tested by a stubbed code on several input files. Each input file contains parameters for the function calls. The functions will be called with those parameters, and the result of their executions will be printed to the standard output by the stubbed code.

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains 3 space-separated strings for building the Admin object: the user's name, their gender, and their age.

The second line contains 3 space-separated strings for building the Moderator object: the user's name, their gender, and their age.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

Oscar Male 23
Abel Other 36
```

Sample Output

Type of user Oscar is Admin
Age of user Oscar is 23
Gender of user Oscar is Male
Type of user Abel is Moderator
Age of user Abel is 36
Gender of user Abel is Other

```

Explanation

First, a user is created with type 'Admin', name 'Oscar', gender 'Male', and age 23. Then, all 4 functions are called: GetUserName, GetUserType, GetAge, and GetGender. The result is printed to the standard output. The same process occurs for the second user.

Sample Case 1

Sample Input For Custom Testing

Ace Male 29
Ali Female 36
```

Sample Output

Type of user Ace is Admin
Age of user Ace is 29
Gender of user Ace is Male
Type of user Ali is Moderator
Age of user Ali is 36
Gender of user Ali is Female

```

Explanation

First, a user is created with type 'Admin', name 'Ace', gender 'Male', and age 29. Then, all 4 functions are called: GetUserName, GetUserType, GetAge, and GetGender. The result is printed to the standard output. The same process occurs for the second user.

## Sample Input/Output

## Preview

Implement a class inheritance hierarchy for a user system.
