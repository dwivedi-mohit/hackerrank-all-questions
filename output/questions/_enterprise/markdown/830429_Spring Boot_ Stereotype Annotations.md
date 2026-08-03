# Spring Boot: Stereotype Annotations

## Metadata

- **ID:** 830429
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Spring Boot, Annotations, Easy
- **Skills:** Spring Boot (Basic)

## Summary

This back-end development question evaluates Spring Boot annotations, RESTful services, and database interactions concepts, ideal for junior-level roles. The problem requires implementing a Contact Management System with specific REST endpoints for saving and retrieving contact information.

## Problem Statement

There is a tiny `Contact Management System`, and this problem is focused on maintaining a person's name and mobile number in the database.

 

The definitions and detailed requirements list follow. You will be graded on whether your application performs data retrieval and manipulation based on given use cases exactly as described in the requirements.

 

The following architectural components for this application have already been provided as standard Java classes:

	
- 
`ContactController`: the controller class where you have to define REST endpoints for the POST and GET methods
	
- 
`ContactService`: the service class, expected to be used by the controller class to save/retrieve contacts to/from the repository
	
- 
`ContactRepository`: repository class, expected to be used by the service class to save/retrieve contacts to/from the database
	
- 
`Person`: the model class to hold the contact information

 

You have two tasks:

	
- Annotate these classes using appropriate Spring Boot stereotypes.
	
- Define the following 2 REST endpoints in the controller class.

 

Here is an example of a person data JSON object:

`
{
 "id": 1,
 "name": "Foo Bar",
 "mobile": "987465238"
}
`
    
```

 

The 2 REST endpoints to be exposed are:

 

`POST` request to `/contact/save`:

	
- expects a valid person data object as its body payload, except that it does not have an id property; you can assume that the given object is always valid
	
- adds the given object to the database and assigns a unique integer id to it
	
- the response code is 201 and the response body is the created record, including its unique id

 

`GET` request to `/contact/retrieve/{id}`:

	
- the response code is 200 and the response body is the matching object
	
- expect that the requested id exists in the database

 

You need to complete the given project so that it passes all the test cases when running the provided unit tests. The project by default supports the use of the H2 database.

 

Example requests and responses

`POST` request to `/contact/save`

Request body:

    `
{
   "name": "Foo Bar",
   "mobile": "987465238"
}
    `
```

The response code is 201, and when converted to JSON, the response body is:

    `
{
   "id": 1,
   "name": "Foo Bar",
   "mobile": "987465238"
}`
```

This adds a new object to the database with the given properties and id 1.

 

`GET` request to `/contact/retrieve/1`

Assuming that the object with id 1 exists, then the response code is 200 and the response body, when converted to JSON, is as follows:

    `
{
   "id": 1,
   "name": "Foo Bar",
   "mobile": "987465238"
}
    `
```

## Preview

There is a tiny Contact Management System, and this problem is focused on main
