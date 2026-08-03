# Proxy Validator

## Metadata

- **ID:** 1517322
- **Type:** code
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Custom Validators, Easy, Error Handling
- **Skills:** JavaScript (Basic)
- **Languages:** j, a, v, a, s, c, r, i, p, t

## Summary

This coding question evaluates custom validators, error handling, and proxy usage concepts, ideal for junior-level roles. The problem requires writing a function that validates user properties and enforces specific rules using a proxy.

## Problem Statement

Write a function named createValidatedUser that accepts a user object and returns a proxy for this object. The user object should have three properties: name, email, and age. 

The proxy must enforce the following validation rules:

	
- The name property should be a non-empty string with a maximum length of 100 characters.
	
- The email property must be a valid email address with a maximum length of 100 characters.
	
- The age property should be an integer between 18 and 120, inclusive.

 

If an invalid value is set for any property, the proxy should throw an error with a corresponding message:

	
- "Name property is invalid"
	
- "Email property is invalid"
	
- "Age property is invalid"

 

Note: A valid email address follows the regex pattern:

`[a-z0-9]+@[a-z0-9]+\.[a-z]{2,}`
```

 

Example

 

Create an object of user with property name = "chris", email = "chris@yahoo.com", age = 19. Pass this object to function createValidatedUser, and now change the returned object properties name, email, and age with newName = "chris", newEmail = "@yahoo.com", newAge = 10 respectively. Here newEmail is not a valid email so it should throw an error with the message "Email property is invalid" (without quotes). Likewise, newAge age is below 18, so it should throw an error with the message "Age property is invalid".

 

Function Description

Complete the function createValidatedUser in the editor with the following parameter:

    user:  a user object

 

Returns

    A proxy of the object that satisfies the properties.

 

Constraints

	
- 1 ≤ |name|, |email| ≤ 100
	
- 1 ≤ |newName|, |newEmail|  ≤ 200
	
- 18 ≤ age ≤ 120
	
- 1 ≤ newAge ≤ 200
	
- 
email and newEmail contain digits, lowercase English letters, '@', and '.'
	
- 
name and newName contain lowercase English letters only.

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains a string, name.

The next line contains a string, email.

The next line contains an integer, age.

The next line contains a string, newName.

The next line contains a string, newEmail.

The last line contains an integer, newAge.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

alex
alex@gmail.com
20
chris
chris@gmailcom
30

```

Sample Output

alex
alex@gmail.com
20
chris
Email property is invalid
30

```

Explanation

Initially, there is an object of user with name = "alex", email = "alex@gmail.com", age = 20. Pass this object to function createValidatedUser, and now change the returned object properties name, email, and age with newName = "chris", newEmail = "chris@gmailcom", newAge = 30 respectively.

Since newEmail is not a valid email it should throw an error with the message "Email property is invalid" (without quotes)

Sample Case 1

Sample Input For Custom Testing

alex
alex@gmail.com
20
alex
chris@gmail.com
12
```

Sample Output

alex
alex@gmail.com
20
alex
chris@gmail.com
Age property is invalid
```

Explanation

Initially, there is an object of user with property name = "alex", email = "alex@gmail.com", age = 20. This object is passed to createValidatedUser. Now change the returned object properties name, email, and age to newName = 345, newEmail = "chris@gmailcom", newAge = 12 respectively.

newAge is below 18, so it should throw an error with the message "Age property is invalid".

## Sample Input/Output

## Preview

Write a function named createValidatedUser that accepts a user object and retu
