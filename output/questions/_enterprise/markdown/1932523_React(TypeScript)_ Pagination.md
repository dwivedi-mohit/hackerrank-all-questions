# React(TypeScript): Pagination

## Metadata

- **ID:** 1932523
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** React, Easy, React Component, React Props, React States, TypeScript
- **Skills:** React (Basic)

## Summary

This front-end development question evaluates React components, pagination functionality, and state management concepts, ideal for junior-level roles. The problem requires completing a React pagination application to meet specified unit test criteria.

## Problem Statement

Complete a React pagination application as shown below in order to pass all the unit tests. Certain core React functionalities have already been implemented.

 

 

  
    
      Hide animation
      Show animation
    
    
      
    
  
  

 

The list of countries and their capitals is imported as "data" to render in the table.

 

The application has 2 components:

 

	
- The Table component displays the entire data in the form of a table.
	
- The Pagination component allows the user to select the number of rows rendered and toggle between different pages.

 

The application has the following functionalities:

 

	
- The Table component displays the imported data to the user.
	
- The select field must have three values, 5, 10, and 15, which denote the number of table rows to be displayed on each page.
	
- Initially, 15 buttons should be rendered on screen. 
	
- The following functionality should be implemented when the user changes the value of the select field:
	
		
- The number of rows displayed on each page should change according to the value selected.
		
- The number of buttons should be recalculated and only the required number of buttons should be rendered on the screen.
	
	Each page should display the number of rows selected in the Input component.
	
- The values displayed on each page should match the data given in info.json.

 

The following data-testid attributes are required in the component for the tests to pass:

 

	
- The 'Table' should have the data-testid attribute 'table'.
	
- The 'Table Body' should have the data-testid attribute 'tableBody'.
	
- The 'Buttons' header should have the data-testid attribute 'buttonDiv'.
	
- The 'Select' input should have the data-testid attribute 'selectInput'.

 

The component has data-testid attributes for test cases and certain classes and ids for rendering purposes. They should not be changed.

## Preview

Complete a React pagination application as shown below in order to pass all the
