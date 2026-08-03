# Generator Pagination

## Metadata

- **ID:** 1521197
- **Type:** code
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Python, Generators, Easy, OOP
- **Skills:** Python (Basic)
- **Languages:** p, y, p, y, ,, p, y, p, y, 3

## Summary

This coding question evaluates Python, generators, and object-oriented programming concepts, ideal for junior-level roles. The problem requires implementing a generator function that divides an array into pages of equal size and yields these pages.

## Problem Statement

Implement a function that divides an array into pages of equal size and returns a generator to iterate through these pages.

Your function should implement a generator called create_paginator that yields subarrays (pages) of the original array, with each subarray having the specified page size.

 

Example

items = [1, 2, 3, 4, 5, 6]

pageSize = 2

 

With page size 2, the generator yields:

	
- First iteration: [1, 2]
	
- Second iteration: [3, 4]
	
- Third iteration: [5, 6]

 

Function Description

Complete the function create_paginator in the editor below. The function must act as a generator.

 

create_paginator takes the following parameter(s):

    int items[n]:  the items to display

    int pageSize: the number of items on a page

 

Constraints

	
- 1 ≤ n ≤ 105

	
- 1 ≤ items[i] ≤ 109

	
- 1 ≤ pageSize ≤ 105

	
- 
n is a multiple of pageSize.

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains an integer, n, the number of elements in items.

Each line i of the n subsequent lines (where 0 ≤ i < n) contains an integer, items[i].

The last line contains an integer, pageSize.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

STDIN    Function
-----    --------
4        items[] size n = 4
1        items = [1, 3, 4, 6]
3
4
6
2        pageSize = 2

```

Sample Output

[1, 3]
[4, 6]
```

Explanation

 

	
- The size of a page is 2, so on the first iteration, the generator object yields [1, 3].
	
- On the next iteration, the object yields [4, 6].

Sample Case 1

Sample Input For Custom Testing

STDIN    Function
-----    --------
5        items[] size n = 5
15       items = [15, 20, 10, 12, 18]
20 
10 
12 
18 
1        pageSize = 1
```

Sample Output

[15] 
[20] 
[10] 
[12] 
[18]
```

Explanation

 

Since the page size is 1, the returned generator object returns items one by one.

## Sample Input/Output

## Preview

Implement a function that divides an array into pages of equal size and return
