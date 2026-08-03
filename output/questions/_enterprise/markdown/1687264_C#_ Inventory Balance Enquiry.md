# C#: Inventory Balance Enquiry

## Metadata

- **ID:** 1687264
- **Type:** code
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** C#, Medium, Lambda Expression, LINQ
- **Skills:** C# (Intermediate)
- **Languages:** c, s, h, a, r, p

## Summary

This coding question evaluates C#, lambda expressions, and LINQ concepts, ideal for mid-level roles. The problem requires implementing a system to monitor product inventory levels and identify products below a safety stock threshold.

## Problem Statement

Implement a system to monitor product inventory levels in an e-commerce warehouse. The system should identify products with stock levels below a specified safety threshold to prevent stockouts.

Implement two classes:

	
- A DictionaryStockLevelQuery class that implements the IStockLevelQuery interface with:

	
		
- Property: stockLevels (Dictionary<string, int>)

		
- Constructor: DictionaryStockLevelQuery(Dictionary<string, int> stockLevels)

		
- Method: GetCurrentStockLevel(string productId) that returns the current stock level for the specified product
	
	
	
- An InventoryChecker class with:
	
		
- Constructor: InventoryChecker(IStockLevelQuery stockLevelQuery)

		
- Method: FindProductsBelowThreshold(List<string> productIds, int threshold) that returns a list of product IDs with stock levels below the specified threshold
	
	

Function Description

Complete the classes DictionaryStockLevelQuery and InventoryChecker in the editor below.

 

Constraints

	
- Use bullet points and a separate line for each variable.
	
- 1 ≤ productIds.Count ≤ 1000
	
- Each string in productIds has a length of at least 1 and a maximum of 20 characters and contains only uppercase English letters and digits.
	
- 1 ≤ threshold ≤ 1000
	
- The GetCurrentStockLevel method always returns a non-negative integer less than or equal to 1000.

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

For each test case, the input follows this format:

	
- A line containing a single integer n, the number of product identifiers.
	
- A line with n space-separated strings, each representing a product identifier.
	
- A line containing a single integer threshold, the safety stock threshold for the products.
	
- 
n lines, each containing a string productId followed by an integer stockLevel, that represents the stock level for the given product identifier. Each pair (productID and stockLevel) is separated by a space.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

3
A12B3 C4D56 E789F
50 
A12B3 100
C4D56 45
E789F 60
```

Sample Output

C4D56
```

Explanation

There are three product identifiers with a safety stock threshold of 50. For each product identifier, the stock level is provided as follows:

	
- “A12B3” has a stock level of 100, which is above the threshold and, therefore, not included in the output.
	
- “C4D56” has a stock level of 45, which is below the threshold, so it is included in the output.
	
- “E789F” has a stock level of 60, which is above the threshold, so it is not included in the output.

The output is “C4D56” since it is the only product identifier with a stock level below the threshold.

Sample Case 1

Sample Input For Custom Testing

4
G10H11 XYZ123 ABC789 PQR456
100
G10H11 20
XYZ123 150
ABC789 80
PQR456 90
```

Sample Output

G10H11
ABC789
PQR456
```

Explanation

There are four product identifiers and a threshold of 100. The stock levels are as follows:

	
- “G10H11” has a stock level of 20, which is below the threshold, so it is included in the output.
	
- “XYZ123” has a stock level of 150, which is above the threshold, so it is not included in the output.
	
- “ABC789” has a stock level of 80, which is below the threshold, so it is included in the output.
	
- “PQR456” has a stock level of 90, which is below the threshold, so it is included in the output.

The output lists “G10H11”, “ABC789” and “PQR456” as the product identifiers with stock levels below the threshold.

## Sample Input/Output

## Preview

Implement a system to monitor product inventory levels in an e-commerce wareho
