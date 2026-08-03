# Laravel: Payments API

## Metadata

- **ID:** 1236854
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Laravel, Medium
- **Skills:** Laravel (Intermediate)

## Summary

This back-end development question evaluates REST API implementation, data retrieval, and payment processing concepts, ideal for mid-level roles. The problem requires creating a REST API to manage accounts and payments while adhering to specified requirements and handling various request types.

## Problem Statement

Implement a REST API to accept simplified online payments. There are two kinds of entities the API must handle: Accounts and Payments.

 

The definitions and detailed requirements list follow. The application is graded on whether it performs data retrieval and manipulation based on given use cases exactly as described in the requirements.

 

Each account is a JSON object with the following properties:

	
- 
`id`: a unique integer ID of the account
	
- 
`balance`: an integer, the account balance in cents calculated as the sum of all payments made to the account

 

Here is an example of an account JSON object:

`{
   "id": 1,
   "balance": 1200
}`
```

 

Each payment is a JSON object with the following properties:

	
- 
`id`: a unique integer ID of the payment
	
- 
`account`: the integer account ID to receive the payment
	
- 
`amount`: an integer, the payment in cents

 

Here is an example of an account JSON object:

`{
   "id": 1,
   "account": 1,
   "amount": 1200
}`
```

 

The REST service must expose the `/accounts/` and `/payments/`endpoints, which allow for managing the collection of Accounts and Payments in the following way:

 

`POST` request to `/accounts/`:

	
- creates a new account
	
- expects an empty body payload
	
- adds the given account to the collection of accounts and assigns a unique integer id to it. The first created account must have id 1, the second one 2, and so on.
	
- the response code is 201, and the response body is the created account object

 

`GET` request to `/accounts/<id>/`:

	
- returns an account with the given id
	
- if the matching account exists, the response code is 200 and the response body is the matching account object
	
- if there is no account with the given id in the collection, the response code is 404

 

`POST` request to `/payments/` :

	
- creates a new payment
	
- It expects a body payload containing account and amount.
	
- If the given account does not exist, the response code is 404.
	
- If the account exists, it creates a new payment with the given amount, relates it to the given account, and assigns a unique integer id to it. The first created payment must have id 1, the second one 2, and so on.
	
- If the payment was successfully created, the response code is 201 and the response body is the created payment object.

 

Complete the given project so that it passes all the test cases when running the provided unit tests. The implementation of the model is given and read-only so you are not allowed to modify it. The project by default supports the use of the SQLite3 database. Implement the POST request to `/accounts/` first because testing the other methods requires it to work correctly.

 

Example requests and responses

`POST` request to `/accounts/`

The request body is empty.

 

The response code is 201, and the response body (when converted to JSON) is:

`{
   "id": 1,
   "balance": 0
}`
```

This adds a new account with id 1 to the collection of accounts.

 

`POST` request to `/payments/`

Request body:

`{
   "account": 1,
   "amount": 1000
}`
```

The response code is 201, and the response body (when converted to JSON) is:

`{
   "id": 1,
   "account": 1,
   "amount": 1000
}`
```

This adds a new payment with id 1 to the collection of payments and relates it to the account with id 1.

 

`GET` request to `/accounts/1/`

 

Assuming that the account with id 1 exists, and has two payments related to it with amounts 1000 and 1500 respectively, then the response code is 200 and the response body (when converted to JSON) is:

`{
   "id": 1,
   "balance": 2500
}`
```

 

If an account with id 1 does not exist, then the response code is 404 and there are no particular requirements for the response body.

## Preview

Implement a REST API to accept simplified online payments. There are two kinds
