# Spring Boot: Stock Trades API

## Metadata

- **ID:** 879036
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Spring Boot, Hard, Back-End Development
- **Skills:** Spring Boot (Advanced)

## Summary

This back-end development question evaluates REST API design, JSON handling, and trade management concepts, ideal for senior-level roles. The task involves implementing a REST API to manage stock trades with specific endpoints and response requirements.

## Problem Statement

In this challenge, your task is to implement a simple REST API to manage a collection of stock trades.

 

Each trade is a JSON entry with the following keys:

	
- 
id: The unique trade ID. (Integer)
	
- 
type: The trade type, either 'buy' or 'sell'. (String)
	
- 
userId: The unique user ID. (Integer)
	
- 
symbol: The stock symbol. (String)
	
- 
shares: The total number of shares traded. The traded shares value is between 10 and 30 shares, inclusive. (Integer)
	
- 
price: The price of one share of stock at the time of the trade. (Integer)
	
- 
timestamp: The epoch time of the stock trade in milliseconds. (Long)

Here is an example of a trade JSON object:

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

 

The task is to implement the REST service that exposes the /trades endpoint, which allows for managing the collection of trade records in the following way:

POST request to /trades:

	
- Creates a new trade.
	
- Expects a JSON trade object without an id property as a body payload. You can assume that the given object is always valid.
	
- Adds the given trade object to the collection of trades and assigns a unique integer id to it. The first created trade must have id 1, the second one 2, and so on.
	
- The response code is 201, and the response body is the created trade object.

GET request to /trades:

	
- Returns a collection of all trades.
	
- The response code is 200, and the response body is an array of all trade objects ordered by their IDs in increasing order.
	
- Optionally accepts query parameters type and userId, for example /trades/?type=buy&userId=122. All these parameters are optional. In case they are present, only objects matching the parameters must be returned.

GET request to /trades/<id>:

	
- Returns a trade with the given id.
	
- If the matching trade exists, the response code is 200 and the response body is the matching trade object.
	
- If there is no trade with the given id in the collection, the response code is 404.

DELETE, PUT, PATCH request to /trades/<id>:

	
- The response code is 405 because the API does not allow deleting or modifying trades for any id value.

You should complete the given project so that it passes all the test cases when running the provided unit tests. The project by default supports the use of the H2 database.

 

Example requests and responses

`POST` request to `/trades`

Request body:

`{
   "type": "buy",
   "userId": 1,
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
   "userId": 1,
   "symbol": "AC",
   "shares": 28,
   "price": 162,
   "timestamp" : 1591514264000
}`
```

This adds a new object to the collection with the given properties and id 1. If the share value is not in the range [1, 100], or the type value is not 'buy' or 'share', then the response code is 400.

 

`GET` request to `/trades`

The response code is 200, and when converted to JSON, the response body (assuming that the below objects are all objects matching the filter) is as follows:

`[
   {
      "id": 1,
      "type": "buy",
      "userId": 1,
      "symbol": "AC",
      "shares": 28,
      "price": 162,
      "timestamp" : 1591514264000
   },
   {
      "id": 2,
      "type": "sell",
      "userId": 1,
      "symbol": "AC",
      "shares": 28,
      "price": 162,
      "timestamp" : 1591514264000
   }
]`
```

 

`GET` request to `/trades/?type=buy`

The response code is 200, and when converted to JSON, the response body (assuming that the below objects are all objects matching the filter) is as follows:

`[
   {
      "id": 1,
      "type": "buy",
      "userId": 1,
      "symbol": "AC",
      "shares": 28,
      "price": 162,
      "timestamp" : 1591514264000
   }
]`
```

 

`GET` request to `/trades/?userId=2`

The response code is 200, and when converted to JSON, the response body (assuming that the below objects are all objects matching the filter) is as follows:

`[
   {
      "id": 1,
      "type": "buy",
      "userId": 2,
      "symbol": "AC",
      "shares": 28,
      "price": 162,
      "timestamp" : 1591514264000
   },
   {
      "id": 2,
      "type": "sell",
      "userId": 2,
      "symbol": "AC",
      "shares": 28,
      "price": 162,
      "timestamp" : 1591514264000
   }
]`
```

 

`GET` request to `/trades/1`

Assuming that the object with id 1 exists, then the response code is 200 and the response body, when converted to JSON, is as follows:

`{
   "id": 1,
   "type": "buy",
   "userId": 1,
   "symbol": "AC",
   "shares": 28,
   "price": 162,
   "timestamp" : 1591514264000
}`
```

If an object with id 1 doesn't exist, then the response code is 404 and there are no particular requirements for the response body.

 

`DELETE` request to `/trades/1`

The response code is 405 and there are no particular requirements for the response body.

## Preview

In this challenge, your task is to implement a simple REST API to manage a col
