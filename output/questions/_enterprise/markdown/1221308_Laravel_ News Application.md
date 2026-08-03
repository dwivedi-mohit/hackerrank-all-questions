# Laravel: News Application

## Metadata

- **ID:** 1221308
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Laravel, Easy, CRUD
- **Skills:** Laravel (Basic)

## Summary

This back-end development question evaluates REST API implementation, JSON handling, and CRUD operations concepts, ideal for junior-level roles. The problem requires creating a REST API to manage news articles with specific validation and response requirements.

## Problem Statement

In this challenge, your task is to implement a simple REST API to manage a collection of news articles.

 

Each article is a JSON entry with the following keys:

	
- 
`id`: The unique article ID. (Integer)
	
- 
`title`: The title of the article. (String)
	
- 
`content`: The content of the article. (String)
	
- 
`author`: Name of the author of the article. (String)
	
- 
`category`: The category of the article. (String)
	
- 
`published_at`: The publishing date of the article. (Date)

 

Here is an example of an article JSON object:

`{
    "id": 1,
    "title": "New photography exhibition",
    "content": "In a new exhibition at the Royal Botanic Garden Edinburgh, famous photographer explores the astonishing diversity of nature.",
    "author": "Oscar Davies",
    "category": "Nature",
    "published_at": "2020-02-10"
}`
```

 

You are provided with the implementation of the Article model. The task is to implement the REST service that exposes the `/articles` endpoint, which allows for managing the collection of articles in the following way:

 

`POST` request to `/articles`:

	
- Validates the following conditions:
	
		
- title is provided
		
- length of title is less than 30 characters long
		
- content is provided
		
- author is provided
		
- category is provided
		
- published_at is provided
	
	
	
- If any of the above requirements fail, the server should return the response code 400. Otherwise, in the case of a successful request, the server should return the response code 201 and the article information in JSON format.
	
- expects a JSON article object without an id property as a body payload.
	
- adds the given article object to the collection of articles and assigns a unique integer id to it. The first created article must have id 1, the second one 2, and so on.
	
- the response code is 201, and the response body is the created article object.

 

`GET` request to `/articles`:

	
- returns JSON of a collection of all articles, ordered by id in increasing order
	
- returns response code 200

 

`GET` request to `/articles/:id`:

	
- returns an article with the given id
	
- if the matching article exists, the response code is 200 and the response body is the matching article object
	
- if there is no article with the given id in the collection, the response code is 404

 

`PUT` request to `/articles/:id`:

	
- Update a particular article object which has the given id
	
- expects a JSON object of article events for a successful 200 response
	
- if there is no article with the given id in the collection, the response code is 404

 

`DELETE` request to `/articles/:id`:

	
- Delete a particular article object which has the given id
	
- expects successful 200 response message
	
- if there is no article with the given id in the collection, the response code is 404

 

You should complete the given project so that it passes all the test cases when running the provided RSpec tests. The project by default supports the use of the SQLite3 database.

 

Example requests and responses

`POST` request to `/articles`

Request body:

`{
    "title": "New photography exhibition",
    "content": "In a new exhibition at the Royal Botanic Garden Edinburgh, famous photographer explores the astonishing diversity of nature.",
    "author": "Oscar Davies",
    "category": "Nature",
    "published_at": "2020-02-10"
}`
```

The response code is 201, and when converted to JSON, the response body is:

`{
    "id": 1,
    "title": "New photography exhibition",
    "content": "In a new exhibition at the Royal Botanic Garden Edinburgh, famous photographer explores the astonishing diversity of nature.",
    "author": "Oscar Davies",
    "category": "Nature",
    "published_at": "2020-02-10"
}`
```

This adds a new object to the collection with the given properties and id 1.

 

`GET` request to `/articles`

The response code is 200, and when converted to JSON, the response body (assuming that the below objects are all objects in the collection) is as follows:

`[
   {
    "id": 1,
    "title": "New photography exhibition",
    "content": "In a new exhibition at the Royal Botanic Garden Edinburgh, famous photographer explores the astonishing diversity of nature.",
    "author": "Oscar Davies",
    "category": "Nature",
    "published_at": "2020-02-10"
   },
   {
     "id": 2,
     "title": "Sakura Park Reconstruction",
     "content": "The work will include installing a new fountain and resetting the existing granite walls.",
     "author": "Edward Evans",
     "category": "Nature",
     "published_at": "2020-02-11"
   }
]`
```

 

`GET` request to `/articles/1`

Assuming that the object with id 1 exists, then the response code is 200 and the response body, when converted to JSON, is as follows:

`{
    "id": 1,
    "title": "New photography exhibition",
    "content": "In a new exhibition at the Royal Botanic Garden Edinburgh, famous photographer explores the astonishing diversity of nature.",
    "author": "Oscar Davies",
    "category": "Nature",
    "published_at": "2020-02-10"
}`
```

If an object with id 1 doesn't exist, then the response code is 404 and there are no particular requirements for the response body.

 

`DELETE` request to `/articles/1`

The response code is 404 and there are no particular requirements for the response body.

## Preview

In this challenge, your task is to implement a simple REST API to manage a col
