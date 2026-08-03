# Angular: HackerMaps

## Metadata

- **ID:** 837171
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Easy, Angular, Component State Management, Front-End Development, TypeScript, MVC Framework
- **Skills:** Angular (Basic)

## Summary

This front-end development question evaluates Angular, component state management, and TypeScript concepts, ideal for junior-level roles. The problem requires creating a navigation application with specific functionalities and ensuring it passes all unit tests.

## Problem Statement

Create a basic navigation application, as shown. Some core functionalities are implemented, but the application is not complete. The finished application must pass all of the unit tests.

 

 Hide animation Show animation 

The app has one component: the Navigation view. The list of locations to display is provided in the app.

 

The app should have the following functionalities:

	
- 
	
The locations should be initially displayed in their respective <li> tags in the same order in which they are provided.

	
	
- 
	
Each location can have one or two icon buttons, depending on its position in the list:

	
		
- 
		
The first location should only have the Move Down icon button.

		
		
- 
		
The last location should only have the Move Up icon button.

		
		
- 
		
All the other locations should have both the Move Up and the Move Down buttons.

		
	
	
	
- 
	
Clicking on the Move Down button should move the location down by one position in the list.

	
	
- 
	
Clicking the Move Up button should move the location up by one position in the list.

	
	
- 
	
When a location is moved up or down, it should exchange its position with the location positioned just above (if moving up) or below (if moving down).

	
	
- 
	
The list of locations is passed as input to the Navigation component.

	

 

The locations list is an array of strings, with each item representing a location in the list.

 

Note: The utility function isLast is provided to help with determining if the current location is the last item in the list. Also, the function getClasses is present in the template to aid in rendering. Please do not modify this function.

 

The following data-test-id/class attributes are required in the component for the tests to pass:

	
- 
	
The parent container of the location list <ul> should have the data-test-id attribute 'location-list'.

	
	
- 
	
Each location item in the list should have the data-test-id attribute 'location-0', 'location-1', 'location-2', and so on.

	
	
- 
	
Each location name paragraph tag <p> should have the data-test-id attribute 'location'.

	
	
- 
	
Each Move Up button should have the data-test-id attribute 'up-button'.

	
	
- 
	
Each Move Down button should have the data-test-id attribute 'down-button'.

	

 

Please note that the component has these data-test-id attributes for test cases and certain classes and IDs for rendering purposes. They should not be changed.

## Preview

Create a basic navigation application, as shown. Some core functionalities are i
