# Java: Nutrition Chain

## Metadata

- **ID:** 759740
- **Type:** code
- **Difficulty:** 7.222222222222222
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Java, OOPS, Easy, Classes, OOP
- **Skills:** Java (Basic)
- **Languages:** j, a, v, a, ,, j, a, v, a, 1

## Summary

This coding question evaluates object-oriented programming, class inheritance, and method overriding concepts, ideal for junior-level roles. The problem requires implementing a class structure for food items and their nutritional content.

## Problem Statement

Implement classes to represent food items and their nutritional content. Complete the following class structure:

	
- abstract class Food with the following properties:

	
		
- double proteins
		
- double fats
		
- double carbs
		
- double tastyScore
		
- 
void getMacroNutrients [Abstract Method]
	
	
	
- class Egg which extends class Food:
	
		
- Constructor to initialize proteins, fats, and carbs in that order
		
- 
int tastyScore = 7
		
- 
String type = "non-vegetarian"
		
- 
void getMacroNutrients => prints "An egg has [this.proteins] gms of protein, [this.fats] gms of fats and [this.carbs] gms of carbohydrates."
	
	
	
- class Bread which extends class Food:
	
		
- Constructor to initialize proteins, fats, and carbs in that order
		
- 
int tastyScore = 8
		
- 
String type = "vegetarian"
		
- 
void getMacroNutrients => prints "A slice of bread has [this.proteins] gms of protein, [this.fats] gms of fats and [this.carbs] gms of carbohydrates."
	
	

Note: The code stub handles input.

 

Example

There is one food item, "bread", with method calls "getType", "getMacros", and "getTaste".

Output:

Bread is vegetarian

A slice of bread has 4.0 gms of protein, 1.1 gms of fats and 13.8 gms of carbohydrates.

Taste: 8

 

Test Case Input Format

The first line contains an integer, n, the number of food items.

Each food item has 4 lines of input, where the first line is its name, and the next three lines are method calls (getType, getTaste, and getMacros) in random order.

## Sample Input/Output

## Preview

Implement classes to represent food items and their nutritional content. Compl
