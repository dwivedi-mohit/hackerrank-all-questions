# C#: Authentication State

## Metadata

- **ID:** 1442111
- **Type:** code
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Medium, Authentication, Classes, Interfaces, C#, OOP
- **Skills:** C# (Intermediate)
- **Languages:** c, s, h, a, r, p

## Summary

This coding question evaluates authentication, object-oriented programming, and interface implementation concepts, ideal for mid-level roles. The problem requires implementing functions for a website's authentication system, including user registration, login, and logout with specific constraints.

## Problem Statement

Implement three functions for a website's authentication system: register, login, and logout. Users register with email, password, and location information.

 

Key requirements:

	
- Users can only log in from allowed locations.
	
- A user is blocked after 3 consecutive failed login attempts.
	
- The failed attempt counter resets after a successful login.
	
- A user cannot be logged in from multiple locations simultaneously.

Return appropriate messages based on the status of each operation.

 

The messages that should be returned according to status are shown.

	
		
			Register
			Login
			Logout
		
	
	
		
			
			
User1@email.com registered successfully!

			
			
			
User1@email.com is not registered!

			
			
			
User1@email.com is not logged in!

			
		
		
			User1@email.com is already registered!
			
			
User1@email.com logged in successfully!

			
			User1@email.com logged out successfully!
		
		
			 
			
			
User1@email.com is already logged in!

			
			 
		
		
			 
			
			
User1@email.com is already logged in from another location!

			
			 
		
		
			 
			
			
User1@email.com is blocked!

			
			 
		
		
			 
			
			
User1@email.com is not allowed to login from this location!

			
			 
		
		
			 
			User1@email.com password is incorrect!
			 
		
	

 

Example

Given the following allowed locations = ["Location1", "Location2"] and commands:

 

	
		
			Commands
			Output
		
	
	
		
			
			
Register User1@email.com with location Location1

			
			User1@email.com registered successfully!
		
		
			
			
Login User1@email.com from Location1

			
			User1@email.com logged in successfully!
		
		
			
			
Login User1@email.com from Location2

			
			User1@email.com is already logged in from another location!
		
		
			Login User2@email.com without registration.
			User2@email.com is not registered!
		
	

 

 

Function Description

	
- Create the User class and implement the IUser interface.

	
		
- This class should have:
		
			
- a constructor which takes id, email, password, and location.
			
- 
Id, Email, Password, Location, and IncorrectAttempt properties.
			
				
- These properties are initialized with the passed values by the constructor.
				
- 
IncorrectAttempt is initialized to 0. 
			
			
		
		
	
	
	
- Create the ApplicationAuthState class and implement the IApplicationAuthState interface.
	
		
- This class should have:
		
			
- a constructor which
			
				
- takes a list of allowed locations 
				
- initializes the AllowedLocations property with the provided list
				
- initializes the RegisteredUsers and UsersLoggedIn properties to new instances of List<IUser>
			
			
			
- the public Register method -
			
				
- The method takes a parameter user of type IUser and returns a string.
				
- It verifies
				
					
- that the user is not yet registered
				
				
				
- If the user is not yet registered
				
					
- add the user to RegisteredUsers

					
- return the success message
				
				
				
- If the user is already registered
				
					
- return the appropriate message
				
				
			
			
			
- the public Login method -
			
				
- The method takes a parameter user of type IUser and returns a string.
				
- It verifies 
				
					
- that the provided email is registered 
					
- that the user does not have too many failed login attempts
					
- that the password is correct
					
- that the user is not logged in already
					
- that the user is from an allowed location 
				
				
				
- If all tests pass
				
					
- add the user to the UsersLoggedIn list
					
- reset the IncorrectAttempt property to 0
					
- return the success message
				
				
				
- Otherwise
				
					
- increment the IncorrectAttempt property (only when an incorrect password is entered)
					
- return the appropriate message
				
				
			
			
			
- the public Logout method -
			
				
- The method takes a parameter user of type IUser and returns a string
				
- It verifies
				
					
- that the user is logged in
				
				
				
- If the user is logged in, remove the user from the UsersLoggedIn list and return the success message.
				
- If the user is not logged in, return the appropriate message.
			
			
		
		
	
	

 

 DO NOT REMOVE THIS LINE-->

Input Format for Custom Testing

The first line contains an integer n, the number of allowed locations.

Each of the next n lines contains the allowed location name.

The next line contains an integer m, the number of users.

Each of the next m lines contains the (Id, Email, Password, Location) of the user information.

The next line contains an integer k, the number of operations.

Each of the next k lines contains the function name and User index separated by ":"

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input

1
location4
4
16,user16@email.com,14165,location16
8,user8@email.com,89680,location8
17,user17@email.com,26883,location17
16,user16@email.com,36862,location16
10
Register:2
Register:2
Login:1
Register:2
Login:0
Login:0
Login:0
Register:2
Register:1
Register:2

```

Sample Output

user17@email.com registered successfully!
user17@email.com is already registered!
user8@email.com is not registered!
user17@email.com is already registered!
user16@email.com is not registered!
user16@email.com is not registered!
user16@email.com is not registered!
user17@email.com is already registered!
user8@email.com registered successfully!
user17@email.com is already registered!

```

Explanation

location4 is added to AllowedLocations. 10 commands are issued for various users. The numbers at the end of each liner refer to the index of users in the input list.

Sample Case 1

Sample Input

2
location1
location2
3
7,user7@email.com,90559,location7
10,user10@email.com,41853,location10
2,user2@email.com,80573,location2
5
Register:1
Register:1
Login:0
Login:1
Register:2

```

Sample Output

user10@email.com registered successfully!
user10@email.com is already registered!
user7@email.com is not registered!
user10@email.com is not allowed to login from this location!
user2@email.com registered successfully!

```

Explanation

AllowedLocations = ['location1', 'location2']. 3 users are added, then 5 operations are requested.

## Sample Input/Output

## Preview

Implement three functions for a website's authentication system: register, log
