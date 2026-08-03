# SpringBoot Java: Flight API

## Metadata

- **ID:** 1294763
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Spring Boot, Hard, Response, Request, Back-End Development, REST API, Error Handling, Advanced APIs
- **Skills:** Spring Boot (Advanced)

## Summary

This back-end development question evaluates REST APIs, error handling, and data management concepts, ideal for senior-level roles. The problem requires implementing REST endpoints for flight data management, including creating and retrieving records with specific response codes.

## Problem Statement

In this project, data is given regarding flights. Your task is to implement several REST endpoints to handle this data.

 

Here is an example of a flight data JSON object:

`{
   "id": 1,
   "flight": "MH17"
   "origin": "Malaysia",
   "destination": "China",
   "speed_series": [200, 350, 400, 500, 650, 740, 600]
}`
```

 

The application should adhere to the following API format and response codes:

 

`POST /flight`:

	
- Creates a new flight data record.
	
- Expects a valid flight data object as its body payload, except it does not have an ID property. You can assume that the given object is always valid.
	
- Adds the given object to the collection and assigns a unique integer ID to it.
	
- The response code is 201, and the response body is the created record, including its unique ID.

`GET /flight`:

	
- The response code is 200, and the response body is an array of matching records, ordered by their IDs in increasing order.
	
- It accepts an optional query string parameter, origin, for example `/flight/?origin=KTM`. Only the records with the matching origin are returned when this parameter is present.
	
- Accepts an optional query string parameter, orderBy, that can take one of two values: either "destination" or "-destination". If the value is "destination", the ordering is by destination in ascending order. If it is "-destination", the ordering is by date in descending order. If there are two records with the same destination, the one with the smaller ID must come first.

`GET /flight/<id>`:

	
- Returns a record with the given ID.
	
- If the matching record exists, the response code is 200 and the response body is the matching object.
	
- If there is no record in the collection with the given ID, the response code is 404.

## Preview

In this project, data is given regarding flights. Your task is to implement se
