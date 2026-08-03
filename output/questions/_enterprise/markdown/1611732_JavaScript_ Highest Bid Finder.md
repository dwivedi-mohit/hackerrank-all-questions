# JavaScript: Highest Bid Finder

## Metadata

- **ID:** 1611732
- **Type:** code
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Functions, JavaScript, Easy, Objects
- **Skills:** JavaScript (Basic)
- **Languages:** j, a, v, a, s, c, r, i, p, t

## Summary

This coding question evaluates functions, JavaScript, and objects concepts, ideal for junior-level roles. The problem requires writing functions to manage a unique auction system with specific bidding rules.

## Problem Statement

A new type of auction has been introduced with unique bidding rules:

	
- Unlike normal auctions where the highest bidder wins, this auction requires the highest bid paired with a claim using callBid to win the item.
	
- If there are no prior bids, the item can be claimed at its initial price.
	
- A new bid is successful only if it is higher than the highest existing bid.
	
- Once an item is claimed, no more bids can be placed on it.

Write functions that take a list of existing bids and a new bid, and return whether the new bid can successfully claim the item.

 

Example

 

Three participants, A, B, and C, bid on the item, which has an initial price of 100.

	
- 
A places the first bid at 150, which is successful as it is higher than the initial price.
	
- Then, B places a bid of 200, surpassing A's bid, thus it is successful.
	
- Next, C bids 210. Since C's bid is higher than the current highest bid of 200, this bid is successful, and C claims the item.

 

Function Description

Implement the program with the following methods:

	
- 
	
startAuction(auctions: object, entity: string, startingPrice: number): void - This function initializes an auction for an item at the starting price. It takes in three parameters:

	
		
- 
		
auctions: an object that holds the auction details

		
		
- 
		
entity: the name of the item

		
		
- 
		
startingPrice: the minimum starting bid

		
		
- 
		
The function does not return any value but updates the 'auctions' object with the details for the entity.

		
	
	
	
- 
	
updatePrice(auctions: object, entity: string, bidPrice: number): void - This function updates the current bid price if the new bid is higher than the current bid and the starting price. It takes in three parameters:

	
		
- 
		
auctions: an object that holds the auction details

		
		
- 
		
entity: the name of the item

		
		
- 
		
bidPrice: the new bid

		
		
- 
		
The function does not return any value but modifies the 'auctions' object with the updated bid amount.

		
	
	
	
- 
	
callBid(auctions: object, entity: string, callPrice: number): string - This function evaluates a bid for an item based on the call price. It takes in three parameters:

	
		
- 
		
auctions: the item details

		
		
- 
		
entity: the name of the item

		
		
- 
		
callPrice: the price at which the bid is called

		
		
- 
		
The function returns a string, either "successful" if the bid is valid, or "unsuccessful" if it does not meet the criteria.

		
	
	

 

Constraints

	
- All item names are unique and consist of lowercase English letters only.
	
- Item names have a length between 1 and 100 characters, inclusive.
	
- 1 ≤ startingPrice, bidPrice, callPrice ≤ 105

	
- Once an Item is sold, it cannot be claimed again.

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

Each line contains a function to call (startAuction, updatePrice, or callBid), followed by the entity's name and the price, separated by spaces.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

startAuction vase 100
updatePrice vase 150
updatePrice vase 200
callBid vase 210
```

Sample Output

successful
```

Explanation

The auction for "vase" begins with a starting price of 100. The bid price is then raised to 150 and updated again to 200. Finally, an attempt to claim the vase for 210 is successful.

Sample Case 1

Sample Input For Custom Testing

startAuction car 5000
callBid car 4500
callBid car 5000
```

Sample Output

unsuccessful
successful

```

Explanation

The auction for "car" starts at a price of 5000. Since call price of 4500 is less than starting price, the call is unsuccessful. Since the call price of 5000 is equal to the starting bid price, the call is successful.

## Sample Input/Output

## Preview

A new type of auction has been introduced with unique bidding rules:
