# System Design: Flash Sales

## Metadata

- **ID:** 1050193
- **Type:** whiteboard
- **Difficulty:** 5.0
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Queue-Based Processing, Concurrency Control, Inventory Management, Async Response, Hard
- **Skills:** System Design

## Summary

This whiteboard question evaluates system design, scalability, and user experience concepts, ideal for mid-level roles. The problem requires designing a robust system for managing flash sales with limited stock and handling user requests on a first-come-first-serve basis.

## Problem Statement

Your company has launched a hot new product. The marketing team has recommended promoting it through flash sales. The features of a flash product sale are as follows:

	
- The sale starts at a particular time.
	
- The requests to purchase the product may be greater than the stock count for the product.
	
- Each user can purchase only one unit of the product.
	
- There is no "Add to Cart" functionality.
	
- Each order should be placed on a first-come-first-serve basis.  The product should go out of stock the moment the entire stock of the product is exhausted

 

Using the diagramming tools provided, design a system that implements these features in a robust, scalable way.

 

Ideal  workflows:

 

Happy Path - 

 

 Hide animation Show animation 

 

 

Unhappy Path: 

 

 Hide animation Show animation

## Preview

Your company has launched a hot new product. The marketing team has recommende
