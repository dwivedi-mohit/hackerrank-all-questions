# Java: Logistics Space Calculation

## Metadata

- **ID:** 1467183
- **Type:** code
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Java, Abstract Class, Hard, Classes, Interfaces, OOP
- **Skills:** Java (Advanced)
- **Languages:** j, a, v, a, ,, j, a, v, a, 1

## Summary

This coding question evaluates object-oriented programming, class inheritance, and interface implementation concepts, ideal for senior-level roles. The problem requires creating classes for different product types and calculating the total space needed for transportation based on specific formulas.

## Problem Statement

A logistics company needs to calculate the space required to transport different product types: solid, liquid, and jewelry. Each product type has specific dimensional variables and formulas to calculate required space.

 

Product specifications:

	
- 
	
Solid Product

	
		
- Dimensions: Weight, Volume

		
- 
Factor: 3
		
- Formula: Weight × Volume × Factor

	
	
	
- 
	
Liquid Product

	
		
- Dimensions: Liter

		
- 
Factor: 2
		
- Formula: Liter × Factor

	
	
	
- 
	
Jewel Product

	
		
- Dimensions: Count, RequiredBox

		
- 
Factor: 1
		
- Formula: Count × Factor + RequiredBox × Factor

	
	

Create SolidProduct, LiquidProduct, and JewelProduct classes by extending the Product class. Create the TransportUnit class implementing the ITransportUnit interface.

 

Example

Orders:

1 100 10
2 50

```

The first number is 1, 2, or 3 to indicate Solid, Liquid, and Jewel respectively. Next are the dimensions in the order listed above, e.g. Weight, Volume for Solid.

 

Order interpretation:

	
- A solid product (type 1) with Weight:100, Volume:10
	
- A liquid product (type 2) with Liter:50

Space calculation:

	
- Solid product: 100 × 10 × 3 = 3000 units
	
- Liquid product: 50 × 2 = 100 units
	
- Total space required: 3100 units

 

Function Description

	
- Create a class called SolidProduct that inherits from the Product class.

	
		
- Add two integer properties called Weight and Volume 
		
- In the constructor 
		
			
- Pass in values for Weight and Volume.
			
- Call the base class constructor with the appropriate arguments.
		
		
		
- Override the CalculateSpace method from the base Product class.
		
- Return the result of Weight * Volume * Factor.
	
	
	
- Create a class called LiquidProduct that inherits from the Product class.
	
		
- Add an integer property called Liter.
		
- In the constructor
		
			
- Pass in a value for Liter.
			
- Call the base class constructor with the appropriate arguments.
		
		
		
- Override the CalculateSpace method from the base Product class.
		
- Return the result of Liter * Factor.
	
	
	
- Create a class called JewelProduct that inherits from the Product class.
	
		
- Add two integer properties called Count and RequiredBox.
		
- In the constructor
		
			
- Pass in values for Count and requiredBox.
			
- Call the base class constructor with the appropriate arguments.
		
		
		
- Override the CalculateSpace method from the base Product class.
		
- Return the result of Count * Factor + RequiredBox * Factor.

	
	
	
- 
	
To create the TransportUnit class:

	
		
- Implement the ITransportUnit interface.
		
- Declare a private list of Product objects within the TransportUnit class. This list will be used to store the Product objects added to the TransportUnit.
		
- 
void AddProduct(Product product):
		
			
- add the Product object to the list of Product objects within the TransportUnit object.
		
		
		
- 
int GetTotalSpace():
		
			
- Use the CalculateSpace method of each Product object to calculate the total space taken up by all the Product objects.
			
- Return the total space required.
		
		
	
	

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains an integer n, the number of products.

Each of the next n lines contains product information.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input

6
1 6 90
1 5 8
1 5 75
2 35
1 93 18
2 92

```

Sample Output

Total Space Needed:8141

```

Explanation

 

 

There are four solids and two liquids.

 

For the solids, calculated Weight * Volume * Factor, where Factor is a constant of 3.

(6 * 90 + 5 * 8 + 5 * 75 + 93 * 18) * 3 = 7,887

 

For the liquids, calculated Liter * Factor, where Factor is a constant of 2.

(35 + 92) * 2 = 254

Sample Case 1

Sample Input For Custom Testing

6
3 52 2
1 98 40
3 92 40
3 60 46
1 59 83
2 71

```

Sample Output

Total Space Needed:26885

```

Explanation

 

There are 2 solids, calculated Weight * Volume * Factor, where Factor is a constant of 3.

(98 * 40 + 59 * 83) * 3 = 26,451

 

There is 1 liquid, calculated Liter * Factor, where Factor is a constant of 2.

71 * 2 = 142

 

For the jewels, calculated Count * Factor + RequiredBox * Factor, where Factor is a constant 1.

52 + 2 + 92 + 40 + 60 + 46 = 292

## Sample Input/Output

## Preview

A logistics company needs to calculate the space required to transport differe
