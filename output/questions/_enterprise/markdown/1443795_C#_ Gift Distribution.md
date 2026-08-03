# C#: Gift Distribution

## Metadata

- **ID:** 1443795
- **Type:** code
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Abstract Class, Hard, Classes, Interfaces, C#
- **Skills:** C# (Advanced)
- **Languages:** c, s, h, a, r, p

## Summary

This coding question evaluates abstract classes, interfaces, and queue data structures concepts, ideal for senior-level roles. The problem requires implementing a gift distribution application that allocates gifts to employees based on a FIFO principle.

## Problem Statement

Implement classes for a gift distribution application that allocates gifts to employees based on a first-in-first-out (FIFO) principle.

The system handles three types of gifts: Laptops, Mobile Phones, and Shopping Gift Cards. The application tracks available gifts and distributes them to employees.

 

As a software developer for this company, implement the gift class for each type of gift and implement the functions described.

	
- Create the Gift abstract class by implementing the IGift interface.

	
		
- It has a BrandName property.
		
- The constructor takes a string for the BrandName property.
		
- It has an abstract method called GetName().

	
	
	
- Create the Company class by implementing ICompany interface.
	
		
- It should contain 3 integer properties, LaptopCount, MobilePhoneCount, and ShoppingGiftCardCount.
		
			
- Each of these properties should be initialized to 0.
		
		
		
- It should have a private field called _gifts, a queue of Gift objects.
		
- Implement the AddGift method.
		
			
- Accept a Gift object as an argument.
			
- Add it to the _gifts queue.
			
- Increment the appropriate property.
		
		
		
- Implement the Giveaway method.
		
			
- Remove the first element from _gifts.

			
- Return the value removed, or null if the queue was empty.
			
- Do not decrement the properties LaptopCount, MobilePhoneCount, or ShoppingGiftCardCount.

		
		
		
- Implement 3 similar methods: GetLaptopCount, GetMobilePhoneCount, and GetShoppingGiftCardCount.
		
			
- Return the value of the corresponding property.
		
		
	
	
	
- Create the Employee class by implementing IEmployee interface.
	
		
- It has two properties: string Name, and List<Gift> GiftsOwned.

		
- The constructor accepts a string for Name and initializes GiftsOwned.

		
- Implement the WinGift method.
		
			
- It accepts a Gift object or null.

			
- If it gets a Gift object, it adds it to the GiftsOwned list.
		
		
		
- Implement the GetOwnedGiftNames method.
		
			
- Return a list of strings, the names of the items in GiftsOwned.

		
		
	
	
	
- Implement 3 similar classes: Laptop, MobilePhone, and ShoppingGiftCard .
	
		
- Use Gift as the base class.
		
- Have a constructor that accepts a string argument that represents the brand name.
		
- Call the base constructor with this argument.
		
- Override the GetName method to return a string in the format "Laptop: {BrandName}", "Mobile phone: {BrandName}", or "Shopping gift card: {BrandName}".
	
	

 

Example 

There are 5 gifts and 3 employees. In test case inputs, Gifts are type 1, 2, or 3, followed by a space and the BrandName string. Types 1, 2, and 3 represent laptop, mobile phone, and shopping gift card.

 

Gifts:

1 Laptop1

2 MobilePhone1

1 Laptop2

3 ShoppingCard1

2 MobilePhone2

Employee names:

employee1

employee2

employee3

 

Output:

`Laptop:2
MobilePhone:2
ShoppingGiftCard:1
employee1
Laptop: Laptop1
Shopping gift card: ShoppingCard1
employee2
Mobile phone: MobilePhone1
Mobile phone: MobilePhone2
employee3
Laptop: Laptop2`
```

 

First, the inventory of available gifts is shown. There are 2 laptops, 2 mobile phones, and 1 shopping card as shown in the first 3 lines of output.

 

Next, gifts are distributed to employees. The list of employees is treated as circular. Since employees were added in the order employee1, employee2, employee3, that is the order of distribution.

 

	
- "Laptop1", "MobilePhone1", and "Laptop2" are given in the first round.
	
- "ShoppingCard1" and "MobilePhone2" go to the first two employees in the second round. There are not enough gifts for employee3 to receive a second gift.

Each employee's name is printed, followed by their list of gifts. Existing code reads input, calls the methods, and handles the output.

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains an integer n, the number of gifts.

Each of the next n lines contains the gift information, separated by a space. (Gift type, gift name).

The next line contains an integer m, the number of employees.

Each of the next m lines contains an employee name.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

STDIN                         FUNCTION
-----                         --------
5                      →      n = 5
3 ShoppingGiftCard1    →      [Gift type, gift name] = [[3, "ShoppingGiftCard1"],
2 MobilePhone2                                          [2, "MobilePhone2"]
1 Laptop3                                               [1, "Laptop3"]
1 Laptop4                                               [1, "Laptop4"]
2 MobilePhone5                                          [2, "MobilePhone5"]
2                      →      m = 5
Employee1              →      [Employee Name] = ["Employee1", "Employee2"]
Employee2

```

Sample Output

Laptop:2
MobilePhone:2
ShoppingGiftCard:1
Employee1
Shopping gift card: ShoppingGiftCard1
Laptop: Laptop3
Mobile phone: MobilePhone5
Employee2
Mobile phone: MobilePhone2
Laptop: Laptop4

```

Explanation

Add 5 gifts to the gift list and 2 employees.

The first 3 lines contain the count of gifts by type.

The remaining lines contain employee names and the gifts they won.

 

Sample Case 1 

Sample Input For Custom Testing

STDIN                           FUNCTION
-----                           --------
5                       →       n = 5
3 ShoppingGiftCard1     →       [Gift type, gift name] = [[3, "ShoppingGiftCard1"],
1 Laptop2                                                 [1, "Laptop2"],
1 Laptop3                                                 [1, "Laptop3"],
1 Laptop4                                                 [1, "Laptop4"],
1 Laptop5                                                 [1, "Laptop5"],
4                       →       m = 5
Employee1               →       [Employee Name] = ["Employee1", "Employee2", "Employee3", "Employee4"]
Employee2
Employee3
Employee4

```

Sample Output

Laptop:4
MobilePhone:0
ShoppingGiftCard:1
Employee1
Shopping gift card: ShoppingGiftCard1
Laptop: Laptop5
Employee2
Laptop: Laptop2
Employee3
Laptop: Laptop3
Employee4
Laptop: Laptop4

```

Explanation

There are 5 gifts and 4 employees. The first 3 lines contain the count of gifts by type. The remaining lines contain employees and gift names they won.

## Sample Input/Output

## Preview

Implement classes for a gift distribution application that allocates gifts to
