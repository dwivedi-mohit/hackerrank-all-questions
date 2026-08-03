# Ruby on Rails: Stock Trades API

## Metadata

- **ID:** 887112
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Ruby on Rails, REST API, Hard
- **Skills:** RoR (Advanced)

## Summary

This back-end development question evaluates REST API implementation, data validation, and JSON handling concepts, ideal for senior-level roles. The problem requires creating a REST API to manage stock trades with specific validation and response criteria.

## Problem Statement

In this challenge, your task is to implement a simple REST API to manage a collection of stock trades.

 

Each trade is a JSON entry with the following keys:

	
- 
`id`: The unique trade ID. (Integer)
	
- 
`trade_type`: The trade type, either 'buy' or 'sell'. (String)
	
- 
`user_id`: The unique user ID. (Integer):
	
- 
`symbol`: The stock symbol. (String)
	
- 
`shares`: The total number of shares traded. (Integer)
	
- 
`price`: The price of one share of stock at the time of the trade. (Integer)
	
- 
`timestamp`: The epoch time of the stock trade in milliseconds. (Integer)

 

Here is an example of a trade JSON object:

`{
  "id":1,
  "trade_type": "buy",
  "user_id": 23,
  "symbol": "ABX",
  "shares": 30,
  "price": 134,
  "timestamp": 1531522701000
}`
```

 

The task is to implement the REST service that exposes the `/trades` endpoint, which allows for managing the collection of trade records in the following way:

 

`POST` request to `/trades`:

	
- creates a new trade
	
- expects a JSON trade object without an id property as a body payload
	
- validates the following conditions:
	
		
- 
share is in a range of [0, 100]
		
- 
trade_type is either 'sell' or 'buy'
	
	
	
- if any of the above validations fail, returns status code 400
	
- otherwise, adds the given trade object to the collection of trades and assigns a unique integer id to it. The first created trade must have id 1, the second one 2, and so on.
	
- the response code is 201, and the response body is the created trade object

 

`GET` request to `/trades`:

	
- returns a JSON of the collection of all trades, ordered by id in increasing order
	
- the response code is 200
	
- accepts an optional query parameter user_id. When user_id is provided, it returns trades of a specified user only.
	
- accepts an optional query parameter trade_type. When trade_type is provided, it returns trades of a specified type only.

 

`GET` request to `/trades/<id>`:

	
- returns a JSON of a trade with the given id
	
- if the matching trade exists, the response code is 200 and the response body is the matching trade object
	
- if there is no trade with the given id in the collection, the response code is 404

 

`DELETE`, `PUT`, `PATCH` requests to `/trades/<id>`:

	
- the response code is 405 because the API does not allow deleting or modifying trades for any id value

 

You should complete the given project so that it passes all the test cases when running the provided RSpec tests. The project by default supports the use of the SQLite3 database.

 

Example requests and responses

`POST /trades`

Request body:

`{
  "trade_type": "buy",
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
  "trade_type": "buy",
  "user_id": 1,
  "symbol": "AC",
  "shares": 28,
  "price": 162,
  "timestamp" : 1591514264000
}`
```

This adds a new object to the collection with the given properties and id 1.

 

`GET /trades`

The response code is 200, and when converted to JSON, the response body (assuming that the below objects are all objects in the collection) is as follows:

`[
  {
    "id": 1,
    "trade_type": "buy",
    "user_id": 1,
    "symbol": "AC",
    "shares": 28,
    "price": 162,
    "timestamp" : 1591514264000
  },
  {
    "id": 2,
    "trade_type": "sell",
    "user_id": 2,
    "symbol": "AC",
    "shares": 28,
    "price": 162,
    "timestamp" : 1591514264000
  }
]`
```

 

`GET /trades/user_id=1`

The response code is 200, and when converted to JSON, the response body (assuming that the below objects are all objects in the collection) is as follows:

`[
  {
    "id": 1,
    "trade_type": "buy",
    "user_id": 1,
    "symbol": "AC",
    "shares": 28,
    "price": 162,
    "timestamp" : 1591514264000
  }
]`
```

 

`GET /trades?trade_type=sell`

The response code is 200, and when converted to JSON, the response body (assuming that the below objects are all objects in the collection) is as follows:

`[
  {
    "id": 2,
    "trade_type": "sell",
    "user_id": 2,
    "symbol": "AC",
    "shares": 28,
    "price": 162,
    "timestamp" : 1591514264000
  }
]`
```

 

`GET /trades/1`

Assuming that the object with id 1 exists, then the response code is 200 and the response body, when converted to JSON, is as follows:

`{
  "id": 1,
  "trade_type": "buy",
  "user_id": 1,
  "symbol": "AC",
  "shares": 28,
  "price": 162,
  "timestamp" : 1591514264000
}`
```

If an object with id 1 doesn't exist, then the response code is 404 and there are no particular requirements for the response body.

 

`DELETE /trades/1`

The response code is 405 and there are no particular requirements for the response body.

## Preview

In this challenge, your task is to implement a simple REST API to manage a col
