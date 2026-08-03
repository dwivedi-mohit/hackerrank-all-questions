# JavaScript: Inventory List

## Metadata

- **ID:** 802077
- **Type:** code
- **Difficulty:** 7.777777777777778
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** ES6, Easy, Closures, JavaScript, OOPS, Methods, OOP
- **Skills:** JavaScript (Basic)
- **Languages:** j, a, v, a, s, c, r, i, p, t

## Summary

This coding question evaluates JavaScript, closures, and object-oriented programming concepts, ideal for junior-level roles. The problem requires implementing a function to manage a collection of unique item names with methods to add, remove, and retrieve the list of items.

## Problem Statement

Implement a function called inventoryList that maintains a collection of unique item names and provides the following methods:

	
- 
add(name) - Adds the item with the given name to the collection if it does not already exist
	
- 
remove(name) - Removes the item with the given name from the collection if it exists
	
- 
getList() - Returns an array of all item names in the order they were added

Your implementation will be tested with several inputs, and the results will be printed to standard output. The testing code will join the strings returned by getList() with commas and print the result. If getList() returns an empty array, "No Items" will be printed.

 

Example

The first line contains the number of commands, n.

5
add Shirt
add Trouser
getList
remove Shirt
getList

```

Output

Shirt,Trouser
Trouser
```

Items 'Shirt' and 'Trouser' are added by the add function. Then, getList is called, and the result is printed. Item 'Shirt' is removed by calling the remove function. Finally, getList is called, and the result is printed.

 

Constraints

	
- The size of the collection will not exceed 10 at any point.
	
- All names passed to add(name) and remove(name) are non-empty.

Test Case Input Format

The first line contains an integer n.

The next n lines contain a command string.

## Sample Input/Output

## Preview

Implement a function called inventoryList that maintains a collection of uniqu
