# Java: Zoo Management

## Metadata

- **ID:** 1601839
- **Type:** code
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Inheritance, Interfaces, Java, Easy
- **Skills:** Java (Basic)
- **Languages:** j, a, v, a, ,, j, a, v, a, 1

## Summary

This coding question evaluates inheritance, interfaces, and object-oriented programming concepts, ideal for junior-level roles. The problem requires implementing a zoo management system with classes for animals and the zoo, including methods for adding, removing, and counting animals.

## Problem Statement

Implement a system to manage animals in a zoo with the following components:

	
- 
Animal class implementing IAnimal with properties:

	
		
- 
id (int): unique identifier
		
- 
species (string): the species
		
- 
name (string): the animal's name
		
- 
age (int): the animal's age
	
	
	
- 
Zoo class implementing IZoo with:
	
		
- Private field animals (List)

		
- Methods:
		
			
- 
addAnimal(IAnimal animal): adds an animal to the list
			
- 
removeAnimal(int id): removes an animal by ID
			
- 
countAnimals(): returns the number of animals
			
- 
getAnimalsBySpecies(String species): returns animals of a specific species
			
- 
getAnimalsByAge(): returns a map of age to list of animals
		
		
	
	

Example

With two animals:

	
- Id=1, Species=Mammals, Name = Tiger, Age=6
	
- Id=2, Species=Mammals, Name = Whale, Age=8

Operations:

	
- Count animals: 2
	
- List by species (Mammals): Tiger (6 years old), Whale (8 years old)
	
- List by age:
	
		
- 6 years old: Tiger (Mammals)
		
- 8 years old: Whale (Mammals)
	
	
	
- Remove one animal and count again: 1

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains an integer n, the number of animals.

Each of the next n lines contains the animal information separated by space (Id Species Name Age).

The next line contains a string, the species to filter.

The next line contains the integer m, which is the animal Id to remove.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

STDIN                Function
-----                --------
3                    number of animals n = 3
1 Spec-2 Animal-0 17 1st animal: Id = 1, Species = "Spec-2" Name = "Animal-0" Age = 17
2 Spec-2 Animal-1 11
3 Spec-3 Animal-2 9
Spec-2                species to filter is "Spec-2"
2                     remove animal with Id = 2

```

Sample Output

There are 3 animals in the zoo
Spec-2:
Animal-0 (17 years old)
Animal-1 (11 years old)
Animals by age:
17 year(s) old:
- Animal-0 (Spec-2)
11 year(s) old:
- Animal-1 (Spec-2)
9 year(s) old:
- Animal-2 (Spec-3)
There are now 2 animals in the zoo

```

Explanation

There are 3 animals to add to the list. Filter the list by "Spec-2". Group animals by age. Remove the animal with Id = 2, and determine how many animals are left.

Sample Case 1

Sample Input For Custom Testing

4
1 Spec-2 Animal-0 18
2 Spec-1 Animal-1 2
3 Spec-3 Animal-2 10
4 Spec-2 Animal-3 12
Spec-3
3

```

Sample Output

There are 4 animals in the zoo
Spec-3:
Animal-2 (10 years old)
Animals by age:
18 year(s) old:
- Animal-0 (Spec-2)
12 year(s) old:
- Animal-3 (Spec-2)
10 year(s) old:
- Animal-2 (Spec-3)
2 year(s) old:
- Animal-1 (Spec-1)
There are now 3 animals in the zoo

```

Explanation

There are 4 animals to add to the list. Filter the list by "Spec-3". Group animals by age. Remove the animal with Id = 3, and determine how many animals are left.

## Sample Input/Output

## Preview

Implement a system to manage animals in a zoo with the following components:
