# TypeScript: Fetching Data

## Metadata

- **ID:** 1479605
- **Type:** code
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Promises, Fetch, Hard, async await
- **Skills:** TypeScript (Advanced)
- **Languages:** t, y, p, e, s, c, r, i, p, t

## Summary

This coding question evaluates asynchronous programming, promises, and data management concepts, ideal for senior-level roles. The task requires implementing a Fetcher class with methods to get and post data while handling errors for existing and non-existing IDs.

## Problem Statement

Implement a data fetching class with asynchronous methods.

 

Task: Create a Fetcher class with two methods:

 

get method:

	
- Accepts an id parameter.
	
- Returns an object corresponding to that id.
	
- Throws an error if the id is not found.

post method:

	
- Accepts parameters id and x (a number).
	
- Stores the value x for the given id.
	
- Throws an error if the id already exists.

 

The class should use an existing DB class with read and create methods that return promises resolving in 10 milliseconds. Initially, DB is empty.

 

Example

Let fetch be the object of the class Fetcher. Consider the following calls and corresponding output or action. Initially, DB is empty.

 

	
		
			Function calls
			Output
			Action
		
	
	
		
			
			
fetch.get(1)

			
			-1
			Error:  no such id
		
		
			
			
fetch.post(1, 10)

			
			 
			save id = 1 with value 10 in DB)
		
		
			
			
fetch.post(2, 20)

			
			 
			save id = 2 with value 20 in DB
		
		
			
			
fetch.get(2)

			
			20
			return the value of id 2
		
		
			
			
fetch.post(2, 11)

			
			-1
			Error: id exists
		
	

 

 

Constraints

	
- 1 ≤ q ≤ 500 ( q represents the number of queries )
	
- 
t = { 1, 2 } ( t denotes the type of query: 1 = get and 2 = post ) 
	
- 1 ≤ id , x ≤ 1000

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains an integer, q, the number of queries.

Each line i of the q subsequent lines (where 0 ≤ i < q) contains an integer array, query[i].

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

4
1 1
2 1 11
2 2 12
1 2

```

Sample Output

-1
12
```

Explanation

 

	
		
			Function calls
			Output
			Action
		
	
	
		
			fetch.get(1)
			-1
			Error: id not present
		
		
			fetch.post(1, 11)
			 
			save id = 1 with value 11
		
		
			fetch.post(2, 12)
			 
			save id = 2 with value 12
		
		
			fetch.get(2)
			12
			return the value of id 2
		
	

 

Sample Case 1

Sample Input For Custom Testing

3
2 1 11
2 2 22
1 1

```

Sample Output

11
```

Explanation

 

	
		
			Function calls
			Output
			Action
		
	
	
		
			fetch.post(1, 11)
			 
			save id = 1 with value 11
		
		
			fetch.post(2, 22)
			 
			save id = 2 with value 22
		
		
			fetch.get(1)
			11
			return the value of id 1

## Sample Input/Output

## Preview

Implement a data fetching class with asynchronous methods.
