# React Native: Transactions List

## Metadata

- **ID:** 1118695
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** React Native, Medium, Mobile Development, Props
- **Skills:** React Native (Intermediate)

## Summary

This mobile development question evaluates React Native, props, and component rendering concepts, ideal for mid-level roles. The problem requires creating a transactions list application that meets specific functionality and rendering requirements using React Native components.

## Problem Statement

Create a transactions list application, as shown below. Application requirements follow and the finished application must pass all of the unit tests.

Hide animation Show animation

 

Functionality Requirements

 

Complete the implementation of the app according to the following requirements:

	
- The Transactions component takes an array of transactions as a prop. Each element of this array denotes a single transaction and is an object with the following shape:

`{
   "id": 42,
   "date": "30-01-2019",
   "txnType": "credit",
   "amount": "$2,084.06",
   "location": {
     "id": 6,
     "address": "206, Portaline, Brooklyn Avenue",
     "city": "Brownlee",
     "zipCode": 80358
   }
}`
```

	
- The list of transactions is taken from 'src/transactions.json' and should be used to pass the data around.
	
- The possible values for txnType are "credit" and "debit".
	
- Each transaction is rendered by the TransactionItem component which takes an individual transaction as a prop.
	
- In the Transactions component, use the FlatList component of React Native to render a list of transactions. Each transaction in the array must be rendered as a TransactionItem component.
	
- Complete the TransactionItem component by providing the address, city, amount, and date of each transaction.
	
- The Header component contains a list of 3 buttons for filtering the data present in the list below. Clicking on each button should filter the transactions as defined below:
	
		
- All button: Display all the transactions.
		
- Credit button: Display all the transactions that have the txnType set to 'credit'.
		
- Debit button: Display all the transactions that have the txnType set to 'debit'.
	
	
	
- The Header component accepts transaction type denoting the currently active filter of transactions. This is used purely for styling purposes.
	
- You can assume that the passed transactions array contains at least one transaction.

 

Initially, the file is filled with boilerplate code. Note the following:

	
- Each transaction item must have testID="transaction-item"
	
- Each transaction's address must be rendered as a <Text> element with testID="address".
	
- Each transaction's city name must be rendered as a <Text> element with testID="city".
	
- Each transaction's amount rating must be rendered as a <Text> element with testID="amount".
	
- Each transaction's date count must be rendered as a <Text> element with testID="date".
	
- The debit filter button must have testID="debit-button".
	
- The credit filter button must have testID="credit-button".
	
- The all filter button must have testID="all-button".

 

The component has these testID attributes for test cases and certain classes and ids for rendering purposes. They should not be changed.

## Preview

Create a transactions list application, as shown below. Application requiremen
