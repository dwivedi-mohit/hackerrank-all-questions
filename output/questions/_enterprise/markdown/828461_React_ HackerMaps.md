# React: HackerMaps

## Metadata

- **ID:** 828461
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** React, Easy, Component State Management, Front-End Development, Class Components, JavaScript
- **Skills:** React (Basic)

## Summary

This front-end development question evaluates React, component state management, and class components concepts, ideal for junior-level roles. The problem requires implementing a navigation application with specific button functionalities and rendering requirements.

## Problem Statement

Implement a basic navigation application, as shown below. Some core functionalities have already been implemented, but the application is incomplete. Requirements are given below the image, and the finished application must pass  the unit tests.

 

 Hide animation Show animation 

 

Requirements:

	
- The app consists of one component: the Navigation view
	
- The location list is provided as props to the Navigation component
	
- Locations should be displayed as <li> tags in the same order they are provided
	
- Each location can have one or two icon buttons:
	
		
- First location: Only the Move Down button
		
- Last location: Only the Move Up button
		
- All other locations: Both Move Up and Move Down buttons
	
	
	
- Button functionality:
	
		
- Clicking Move Down: Moves the location down one position
		
- Clicking Move Up: Moves the location up one position
		
- When a location moves, it exchanges positions with the adjacent location
	
	

Note: The utility functions isLast and getClasses are provided in the template. Do not modify getClasses.

 

Required data-testid attributes:

	
- 'location-list' for the parent container <ul>

	
- 'location-0', 'location-1', etc. for each location item
	
- 'location' for each location name <p> tag
	
- 'up-button' for each Move Up button
	
- 'down-button' for each Move Down button

Do not change the data-testid attributes, classes, or IDs as they are required for testing and rendering.

## Preview

Implement a basic navigation application, as shown below. Some core functionalit
