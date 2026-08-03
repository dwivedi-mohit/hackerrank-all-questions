# NodeJS: Stock Trades API 

## Metadata

- **ID:** 887826
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Medium, Node.js, ExpressJS, Back-End Development
- **Skills:** Node.js (Intermediate), Express.js (Intermediate)

## Summary

This back-end development question evaluates REST API design, JSON data handling, and database interaction concepts, ideal for mid-level roles. The problem requires implementing a REST API to manage stock trades with specific endpoints and functionalities.

## Problem Statement

In this challenge, you will implement a REST API to manage a collection of stock trades.

 

Each trade is a JSON object with the following properties:

	
- 
id: Unique trade identifier (Integer)
	
- 
type: Trade type, either 'buy' or 'sell' (String)
	
- 
user_id: Unique user identifier (Integer)
	
- 
symbol: Stock symbol (String)
	
- 
shares: Number of shares traded, between 10 and 30 inclusive (Integer)
	
- 
price: Price per share at trade time (Integer)
	
- 
timestamp: Epoch time of the trade in milliseconds (Integer)

 

Example trade object:

{
    "id": 1,
    "type": "buy",
    "user_id": 23,
    "symbol": "ABX",
    "shares": 30,
    "price": 134,
    "timestamp": 1531522701000
}

```

 

The model implementation is provided and read-only. It includes a timestamp field of DateTime type that must be serialized to/from JSON's integer timestamp.

 

Implement a REST service exposing the /trades endpoint with these features:

	
- POST request to /trades:

	
		
- Creates a new trade
		
- Expects a JSON trade object without an id property
		
- Adds the trade to the collection and assigns a unique integer id (starting from 1)
		
- Returns status code 201 with the created trade object
	
	
	
- GET request to /trades:
	
		
- Returns all trades
		
- Returns status code 200 with an array of all trades ordered by id (ascending)
		
- Optionally accepts query parameters type and user_id (e.g., /trades?type=buy&user_id=122)
		
- When parameters are present, returns only matching objects
	
	
	
- GET request to /trades/:
	
		
- Returns a trade with the given id
		
- If found, returns status code 200 with the matching trade object
		
- If not found, returns status code 404 with text "ID not found"
	
	
	
- DELETE, PUT, PATCH requests to /trades/:
	
		
- Returns status code 405 (method not allowed)
	
	

Complete the project to pass all unit tests. The project supports SQLite3 database by default.

 

Example requests and responses

POST request to /trades

Request body:

`{
   "type": "buy",
   "user_id": 1,
   "symbol": "AC",
   "shares": 28,
   "price": 162,
   "timestamp" : 1591514264000
}`
```

The response code is 201, and when converted to JSON, the response body is:

`{
   "id": 1,
   "type": "buy",
   "user_id": 1,
   "symbol": "AC",
   "shares": 28,
   "price": 162,
   "timestamp" : 1591514264000
}`
```

This adds a new object to the collection with the given properties and id 1.

 

GET request to /trades

The response code is 200, and when converted to JSON, the response body (assuming that the below objects are all objects in the collection) is as follows:

`[
   {
      "id": 1,
      "type": "buy",
      "user_id": 1,
      "symbol": "AC",
      "shares": 28,
      "price": 162,
      "timestamp" : 1591514264000
   },
   {
      "id": 2,
      "type": "sell",
      "user_id": 1,
      "symbol": "AC",
      "shares": 28,
      "price": 162,
      "timestamp" : 1591514264000
   }
]`
```

 

GET request to /trades?type=buy

The response code is 200, and when converted to JSON, the response body (assuming that the below objects are all objects matching the filter) is as follows:

`[
   {
      "id": 1,
      "type": "buy",
      "user_id": 1,
      "symbol": "AC",
      "shares": 28,
      "price": 162,
      "timestamp" : 1591514264000
   }
]`
```

 

GET request to /trades?user_id=2

The response code is 200, and when converted to JSON, the response body (assuming that the below objects are all objects matching the filter) is as follows:

`[
   {
      "id": 1,
      "type": "buy",
      "user_id": 2,
      "symbol": "AC",
      "shares": 28,
      "price": 162,
      "timestamp" : 1591514264000
   },
   {
      "id": 2,
      "type": "sell",
      "user_id": 2,
      "symbol": "AC",
      "shares": 28,
      "price": 162,
      "timestamp" : 1591514264000
   }
]`
```

 

GET request to /trades/1

Assuming that the object with id 1 exists, then the response code is 200 and the response body, when converted to JSON, is as follows:

`{
   "id": 1,
   "type": "buy",
   "user_id": 1,
   "symbol": "AC",
   "shares": 28,
   "price": 162,
   "timestamp" : 1591514264000
}`
```

If an object with id 1 doesn't exist, then the response code is 404 with the response body having the text `ID not found`.

 

DELETE request to /trades/1

The response code is 405, and there are no particular requirements for the response body.

## Preview

In this challenge, you will implement a REST API to manage a collection of sto
