# JavaScript: Bank Statement

## Metadata

- **ID:** 1783497
- **Type:** code
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Medium, Object-Oriented Programming, JavaScript, Inheritance, Static Methods, Implementation, async await, Classes, Objects, OOP
- **Skills:** JavaScript (Intermediate)
- **Languages:** j, a, v, a, s, c, r, i, p, t

## Summary

This coding question evaluates object-oriented programming, JavaScript classes, and asynchronous methods concepts, ideal for mid-level roles. The task involves implementing a BankStatement class with inheritance for a SavingsAccount, managing account functionalities and properties.

## Problem Statement

An organization has partnered with a bank to develop software that manages bank accounts. As a developer, the task is implementing a JavaScript class BankStatement that supports various functions. Some properties should hidden (private), and others should be publicly accessible. Additionally, some functions, like transferring money between accounts, should be asynchronous.

 

To further extend the functionality, implement inheritance where a SavingsAccount class extends the BankStatement class. The SavingsAccount should have an additional property for interest rate and a method to apply interest to the balance.

 

Complete the classes BankStatement and SavingsAccount classes. The requirements for the classes are shown below

	
- 
	
Properties:

	
		
- 
BankStatement:

		
			
- Public Properties:
			
				
- 
accountNumber: A unique identifier for the account.
				
- 
balance: The current balance of the account.
			
			
			
- Private Properties:
			
				
- 
accountHolder: The name of the account holder (should be accessible only within the class).
			
			
		
		
		
- SavingsAccount:
		
			
- Public Properties:
			
				
- 
interestRate: The interest rate for the savings account.
			
			
		
		
	
	
	
- 
	
Methods:

	
		
- 
BankStatement:

		
			
- Public Methods:
			
				
- 
create(name, number, balance): creates an account with accountName, accountNumber and balance(optional, defaults to 0)
				
- 
deposit(amount, number): Synchronously adds a specified amount to the given number's account balance.
				
- 
withdraw(amount, number): Synchronously subtracts a specified amount from the given number's account balance if sufficient funds are available.
				
- 
getAccountInfo(number): Returns a JSON string containing the account number, balance, and account holder name of the given account number.
			
			
			
- Async Method:
			
				
- 
transfer(amount, to): Asynchronously transfers a specified amount to another BankStatement instance (target account) if sufficient funds are available in the source account.
			
			
		
		
		
- 
SavingsAccount:
		
			
- Public Methods:
			
				
- 
applyInterest(rate): Applies the interest rate to the balance and returns the value after 10 years.
			
			
		
		
	
	

 

Returns

	
- 
create(name, number, balance):

	
		
- If balance<0, return "Cannot open account".
		
- If the number already exists in BankStatement or Savings, return "Cannot open account".
		
- In all other cases, return "Account created successfully". Balance is an optional value. Both name and number will be provided.
	
	
	
- 
deposit(number, amount):
	
		
- If the amount is greater than zero, return "Deposited successfully"; otherwise return "Invalid amount".
		
- If the account does not exist, return "Account not found".
	
	
	
- 
withdraw(number, amount):
	
		
- If the amount is greater than zero, return "Withdrawn successfully;" otherwise, return "Invalid amount".
		
- If the holder's account does not have sufficient funds, return "Insufficient funds available".
		
- If the account does not exist, return "Account not found".
	
	
	
- 
getAccountInfo(number): 
	
		
- A JSON string containing the account information with accountNumber, accountName, and balance as the object keys for the given number. 
		
- If the account does not exist, return "Account not found".
	
	
	
- 
transfer(amount, from, to):
	
		
- If to or from doesn't exist, return "Account not found".
		
- If the amount is anything less than or equal to zero, or is an invalid string, return "Invalid amount".
		
- If the holder's account does not have sufficient funds, return "Insufficient funds available".
		
- Otherwise, return "Transfer success". This is an async function, so the return should be a promise resolving to the above values.
	
	
	
- 
applyInterest(rate, number):
	
		
- Applies the interest rate to the balance and returns the new balance after 10 years.
		
			
- future balance = b*( 1+0.01*r)n  where r is the annual rate, n is the period, and b is the initial balance. 
		
		
		
- If the interest rate is given a negative value or an invalid string, return "Invalid rate given".
		
- If the account does not exist, return "Account not found".
		
- Otherwise, return the balance after 10 years in string format, rounded down to the nearest integer value (the floor).
	
	

Note:

	
- All functions created should be static. See the code snippet to see the usage.

Constraints

All the values are either string, number, or JSON arrays/objects.

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The only line contains a JSON object containing two keys: numberOfOperations and operations.

Operations can be one of the following types:

1. createAccount

This operation creates a new instance of the BankStatement class.

	
- 
Operation Type: "createAccount"
	
- 
Description: Initializes a BankStatement object with the given account number, account holder name, and initial balance. The balance is optional and defaults to 0 if not provided.

`{ "type": "createAccount", "accountNumber": "12345", "accountHolder": "Alice", "balance": 1000 },`
```

2. createSavingsAccount

This operation creates a new instance of the SavingsAccount class, which extends BankStatement.

	
- 
Operation Type: "createSavingsAccount"
	
- 
Description: Initializes a SavingsAccount object with the given account number, account holder name, and initial balance.

`{ "type": "createSavingsAccount", "accountNumber": "11223", "accountHolder": "Charlie", "balance": 1000, "interestRate": 5 }
`
```

 

3. deposit

This operation adds a specified amount to the balance of an existing account.

	
- 
Operation Type: "deposit"
	
- 
Description: Finds the account by its account number and adds the specified amount to its balance.

`{ "type": "deposit", "accountNumber": "12345", "amount": 200 }
`
```

4. withdraw

This operation subtracts a specified amount from the balance of an existing account if sufficient funds are available.

	
- 
Operation Type: "withdraw"
	
- 
Description: Find the account by its account number and subtract the specified amount from its balance.

`{ "type": "withdraw", "accountNumber": "12345", "amount": 200 }
`
```

 

5. transfer

This operation asynchronously transfers a specified amount from one account to another if sufficient funds are available.

	
- 
	
Operation Type: "transfer"

	
	
- 
	
Description: Finds both the source and target accounts by their account numbers. If the source account has sufficient funds, it subtracts the amount from the source account and adds it to the target account asynchronously.

	

`{ "type": "transfer", "from": "12345", "to": "67890", "amount": 400 }
`
```

 

6. applyInterest

This operation applies the interest rate to the balance of a savings account.

	
- 
Operation Type: "applyInterest"
	
- 
Description: Find the savings account by its account number and apply the interest rate to its balance.

`{ "type": "applyInterest", "accountNumber": "11223", "rate": 10 }
`
```

Sample Case 0

Sample Input For Custom Testing

STDIN                                         FUNCTION
-----                                         --------
{                                      →      jsonObj
  "numberOfOperations": 1,
  "operations": [
    {
      "type": "createAccount",
      "accountNumber": "12345",
      "accountHolder": "Alex",
      "balance": 1000
    }
  ]
}

```

Sample Output

Account created successfully

```

Explanation

All the given details are correct. The account is created successfully.

Sample Case 1

Sample Input For Custom Testing

STDIN                                       FUNCTION
-----                                       --------
{                                    →      jsonObj
  "numberOfOperations": 1,
  "operations": [
    {
      "type": "createAccount",
      "accountNumber": "67890",
      "accountHolder": "Sam",
      "balance": -500
    }
  ]
}

```

Sample Output

Cannot open account

```

Explanation

The balance is less than 0.

## Sample Input/Output

## Preview

An organization has partnered with a bank to develop software that manages ban
