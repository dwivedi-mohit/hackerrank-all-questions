# NodeJS: Kanban  Board API

## Metadata

- **ID:** 945598
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Node.js, Easy, REST API, ExpressJS
- **Skills:** Node.js (Basic)

## Summary

This back-end development question evaluates REST API, Node.js, and Express.js concepts, ideal for junior-level roles. The problem requires implementing a REST service with specific endpoints for creating and updating TODO items.

## Problem Statement

Implement a REST service that exposes the /boards endpoint.

 

Each item is a JSON object with the following properties:

	
- 
id: Unique reminder identifier (Integer)
	
- 
title: Title of the TODO item (String)
	
- 
stage: Current stage of the item (Integer)

 

Example item object:

{
    "id": 2,
    "stage": 1,
    "title": "Create a new project"
}

```

 

The model implementation is provided and read-only.

 

Implement these features:

	
- POST request to /boards:

	
		
- Creates a new item in the board
		
- Expects a JSON object without id and stage properties
		
- Adds the item to the board with a unique integer id (starting from 1)
		
- Sets stage to 1 for new items
		
- Returns status code 201 with the created item
	
	
	
- PUT request to /boards/:id:
	
		
- Accepts a stage property with the new stage value
		
- Updates the stage of the specified item
		
- If stage value is not 1, 2, or 3, returns status code 400
		
- If stage value is valid, returns status code 200 with the updated item
		
- Assumes the passed item ID always exists
	
	

 

Complete the project to pass all unit tests. The project supports SQLite3 database by default.

 

Example requests and responses

POST request to /boards

Request body:

`{
   "title": "Create a new project"
}`
```

The response code is 201, and when converted to JSON, the response body is:

`{
    "id": 1,
    "stage": 1,
    "title": "Create a new project"
}`
```

This adds a new object to the collection with the given properties, id 1, with the stage set to 1.

 

PUT request to /boards/1

Request body:

`{
   "stage": 2
}`
```

 

The response code is 200, the stage of item 1 has been updated to 2, and the updated item object is sent in the response body:

`{ 
	"id": 1, 
	"stage": 2, 
	"title": "Create a new project" 
}`
```

 

PUT request to /boards/1

Request body:

`{
   "stage": 4
}`
```

 

The response code is 400 with no requirements for the response body.

## Preview

Implement a REST service that exposes the /boards endpoint.
