# Car Inheritance

## Metadata

- **ID:** 317734
- **Type:** code
- **Difficulty:** 8.88888888888889
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Polymorphism, Easy, Abstraction, Java, C++, C#
- **Skills:** Java (Basic), C# (Basic), C++ (Basic)
- **Languages:** c, p, p, ,, c, p, p, 1, 4, ,

## Summary

This coding question evaluates polymorphism, abstraction, and object-oriented programming concepts, ideal for junior-level roles. The problem requires building an abstract class and derived classes to instantiate car objects and implement specific methods.

## Problem Statement

Build on an abstract class and create instances of each derived class with specific variables. The program will verify the implementation by accessing the stored data.

 

The provided code performs the following tasks:

	
- Defines an abstract class called Car with implementations for the methods getIsSedan() and getSeats(), and an abstract method named getMileage()

	
- Instantiates a WagonR, HondaCity, or InnovaCrysta object based on input (0 for WagonR, 1 for HondaCity, and 2 for InnovaCrysta)
	
- Invokes the getIsSedan(), getSeats(), and getMileage() methods on the object

 

 

Details for each car are as follows:

	
- WagonR is not a sedan and has 4 seats.
	
- HondaCity is a sedan and has 4 seats.
	
- InnovaCrysta is not a sedan and has 6 seats.

Example

Inputs:

0     →  type of car to instantiate = 0 (WagonR)

22    →  mileage = 22

Output:

A WagonR is not Sedan, is 4-seater, and has a mileage of around 22 kmpl.

 

Function Description 

Complete the code in the editor below to implement the following:

	
- Create classes named `WagonR`, `HondaCity`, and `InnovaCrysta` that all inherit from the `Car `class.
	
- Each class must have a constructor that receives one integer argument representing the mileage of the car.
	
- Each class must implement a `getMileage() `method which returns a string in the form of '`<mileage> kmpl'` where `<mileage>` is the value provided to the constructor.

 

Constraints

	
- 0 ≤ type of car ≤ 2
	
- 5 ≤ mileage ≤ 30

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains an integer that describes the type of car to instantiate.

The second line contains an integer, the mileage of the car.

## Sample Input/Output

## Preview

Build on an abstract class and create instances of each derived class with spe
