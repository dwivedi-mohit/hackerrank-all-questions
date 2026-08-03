# React(TypeScript): Customer List

## Metadata

- **ID:** 1925397
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** React, Front-End Frameworks, Easy, Component State Management, Hooks, TypeScript
- **Skills:** React (Basic)

## Summary

This front-end development question evaluates React, component state management, and hooks concepts, ideal for junior-level roles. The problem requires creating a customer list component with specific functionalities for adding and displaying customer names.

## Problem Statement

Create a customer list component as shown.

 

  
    
      Hide animation
      Show animation
    
    
      
    
  
  

 

The component must have the following functionalities:

	
- 
	
The input should initially be empty.

	
	
- 
	
If no value is entered, clicking on the 'Add Customer' button should not do anything.

	
	
- 
	
Clicking on the 'Add Customer' button should add the input value to the list below. For this, add <li>{input}</li> to the <ul data-testid="customer-list"> element.

	
	
- 
	
After the value is added to the list, it should clear the value in the input box.

	
	
- 
	
Please note that the customer list <ul> element should only be rendered if it has at least one customer added, i.e. at least one <li> child. When the app is mounted, since no customers are added, the <ul> element should not be rendered.

	
	
- 
	
All the values added by the button should be rendered in the list below.

	

 

The following data-testid attributes are required in the component for the tests to pass.

 

	
		
			Component
			Attribute
		
	
	
		
			Input
			app-input
		
		
			Button
			submit-button
		
		
			Customer list <ul>
			customer-list
		
		
			List elements
			list-item0, list-item1, ...
		
	

 

Please note that components have these data-testid attributes for test cases, and certain classes and ids for rendering purposes. They should not be changed.

## Preview

Create a customer list component as shown.
