# Java Threads: Students Registration

## Metadata

- **ID:** 417442
- **Type:** code
- **Difficulty:** 8.61111111111111
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Language Proficiency, Java, Multithreading, Easy, OOPS, OOP
- **Skills:** Java (Basic)
- **Languages:** j, a, v, a, ,, j, a, v, a, 1

## Summary

This coding question evaluates Java, multithreading, and object-oriented programming concepts, ideal for junior-level roles. The problem requires implementing a student registration portal using the Singleton design pattern with thread-safe methods for registration and retrieval of students.

## Problem Statement

Implement a student registration portal using the Singleton design pattern.

 

Create a class called RegistrationPortal with a data member List registeredStudents. The class should have the following methods:

	
- 
RegistrationPortal getRegistrationPortal(): Returns the instance of the registration portal. Ensure there is only one instance of the registration portal
	
- 
void register(Student student): Registers the given student
	
- 
List getRegisteredStudents(): Returns the list of registered students

The provided stub code will verify the correctness of the RegistrationPortal class implementation by registering students using multiple threads and printing the details of all registered students.

 

Constraints

	
- 1 ≤ threadsCount ≤ 10
	
- Each thread registers no more than 104 students.

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains the value of threadsCount, the total number of threads.

Each of the next threadsCount lines contains an integer studentsCount, the total number of students registered by each of the threads.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input 0

STDIN     Function
-----     --------
2    →    threadsCount = 2
3    →    studentsCount thread 0 = 3
2    →    studentsCount thread 1 = 2
```

Sample Output 0

5
id-1-1 name-1
id-2-1 name-1
id-1-2 name-2
id-2-2 name-2
id-1-3 name-3
```

Explanation 0

There are two threads:

	
- The first thread registers three students ("id-1-1", "name-1"), ("id-1-2", "name-2") and ("id-1-3", "name-3").
	
- The second thread registers two students ("id-2-1", "name-1") and ("id-2-2", "name-2").

## Sample Input/Output

## Preview

Implement a student registration portal using the Singleton design pattern.
