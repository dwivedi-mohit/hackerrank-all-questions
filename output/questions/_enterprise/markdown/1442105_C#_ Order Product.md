# C#: Order Product

## Metadata

- **ID:** 1442105
- **Type:** code
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Data Structures, Theme:  E-commerce, Implementation, Hard, Classes, Interfaces, C#, OOP
- **Skills:** C# (Advanced)
- **Languages:** c, s, h, a, r, p

## Summary

This coding question evaluates data structures, object-oriented programming, and C# concepts, ideal for senior-level roles. The problem requires implementing a system to process customer orders based on inventory and account balance using defined classes and interfaces.

## Problem Statement

Implement a system to process customer orders based on inventory and account balance.

 

Create the following classes:

Product class implementing IProduct interface with properties:

	
- Id
	
- Name
	
- Price
	
- ShippingCost

The constructor should initialize all these properties.

 

User class implementing IUser interface with properties:

	
- Id
	
- Name
	
- Balance
	
- 
Orders (a list of tuples containing IProduct and quantity)

The constructor should initialize Id, Name, and Balance properties, and create a new empty list for Orders.

 

Company class implementing ICompany interface with properties:

	
- 
Products (a list of tuples containing IProduct and quantity)
	
- 
Users (a list of IUser)

The constructor should initialize these properties.

 

Implement these methods in the Company class:

MakeOrder method:

	
- Accepts a list of products and a user as parameters.
	
- Verifies sufficient inventory for each product.
	
- Identifies the highest shipping cost among all ordered items.
	
- Calculates the total cost as the sum of (unit price × quantity) for each product, plus the highest shipping cost.
	
- Verifies the user has sufficient funds.
	
- If all conditions are met:
	
		
- Deducts the total cost from the user's balance
		
- Updates the product quantities in inventory
		
- Adds the products to the user's orders list
	
	

AddProduct method:

	
- Accepts a product and quantity as parameters.
	
- If the product exists in the Products list, increases its quantity.
	
- Otherwise, adds the new product with its quantity to the Products list.

AddUser method:

	
- Accepts a user as a parameter.
	
- Adds the user to the Users list.

 

Example

There are 2 products and 1 user. This user orders 3 Laptop and 1 Phone with 100 funds on account.

 

	
		
			Id
			Name
			Price
			Shipping Cost
			Quantity*
		
	
	
		
			1
			Laptop
			20
			5
			20
		
		
			2
			Phone
			30
			3
			10
		
	

*Quantity will be used when adding product to company.

 

	
		
			Id
			Name
			Balance
		
	
	
		
			1
			User1
			100
		
	

 

There are more than 3 Laptop and 1 Phone available.

The higher shipping cost is 5.

Total cost is (3 * 20) + (1 * 30) + 5 = 95.

User1 has enough funds for the purchase so balances are updated.

 

The new quantities of products are 17 Laptop and 9 Phone. These values are printed by the provided code.

 

Constraints

	
- Product IDs are distinct for each product.

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains an integer n, the number of products.

Each of the next n lines contains the (Id, Name, Price, ShippingCost, Quantity) of the product.

The next line contains an integer m, the number of users.

Each of the next m lines contains the (Id, Name, Balance) of the user.

The next line contains an integer k, the number of orders

Each of the next k lines contains the (UserId,ProductId|Quantity,ProductId|Quantity,...) of the order information. ("," for separate products, "|" for separate product and order quantity)

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input

2
1,product1,20,2,20
2,product2,30,1,10
1
1,user1,500
1
1,1|5,2|2
```

Sample Output

product1:15
product2:8
```

Explanation

Looking at the order, user1 orders 5 units of product1 and 2 units of product2. The higher price for shipping is 2 for product1.

There are plenty of units on hand, 20 of product1 and 10 of product2.

The total cost is (5 * 20) + (2 * 30) + 2 = 162.

The user has plenty of funds, so the order is filled and product quantities are updated.

Sample Case 1

Sample Input

3
1,product1,20,2,20
2,product2,30,1,10
3,product3,25,3,60
2
1,user1,120
2,user2,1000
2
1,1|5,2|2
2,2|1,3|3,1|2

```

Sample Output

product1:18
product2:9
product3:57
```

Explanation

user1 wants to purchase 5 units of product1 at 20 and 2 units of product2 at 10. The shipping is 2, so the total cost is 122. There are not enough funds so the order cannot be filled.

Product balances are updated for user2's purchase.

## Sample Input/Output

## Preview

Implement a system to process customer orders based on inventory and account b
