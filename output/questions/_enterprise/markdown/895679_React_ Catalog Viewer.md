# React: Catalog Viewer

## Metadata

- **ID:** 895679
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Medium, Component State Management, React, Cross-Platform, JavaScript, Hooks, Front-End Frameworks
- **Skills:** React (Intermediate)

## Summary

This front-end development question evaluates component state management, React hooks, and cross-platform functionality concepts, ideal for mid-level roles. The problem requires completing a React catalog viewer application to meet specified functionalities and pass unit tests.

## Problem Statement

There is a partially completed React catalog viewer application. Complete the application as shown to pass the unit tests.

 

  
    
      Hide animation
      Show animation
    
    
      
    
  
  

 

The application has 2 components:

	
- The Viewer component, which displays the selected product in a large size.
	
- The Thumbs component, which presents a full list of product thumbnails. The list of images is passed to the Thumbs component.

 

The application has the following functionalities:

	
- 
	
Initially, the catalog displays the first image in the Viewer.

	
	
- 
	
Clicking on the previous or next button displays the previous or next image respectively. The thumbnail list is circular:

	
		
- 
		
Clicking the next button when the last image is showing should display the first image.

		
		
- 
		
Clicking the previous button when the first image is showing should display the last image.

		
	
	
	
- 
	
Clicking on any thumbnail loads the appropriate image in the Viewer.

	
	
- 
	
The checkbox with the label "Start Slide Show" has the following features: 

	
		
- 
		
When checked, starts the automatic display of images in the Viewer, beginning with the currently displayed image and cycling to the next every 3 seconds

		
		
- When unchecked, stops the automatic cycling of images
		
- During cycling, the user can interact as before (click any thumbnail or the next or previous buttons), after which cycling continues from that image
	
	

 

The following data-testid attributes are required in the component for the tests to pass:

	
- The Viewer component should have the data-testid attribute 'catalog-view'.
	
- The previous button should have the data-testid attribute 'prev-slide-btn'.
	
- The next button should have the data-testid attribute 'next-slide-btn'.
	
- The thumbnail buttons should have the data-testid attributes 'thumb-button-0', 'thumb-button-1', 'thumb-button-2', and 'thumb-button-3'.
	
- The "Start Slide Show" checkbox should have the data-testid attribute 'toggle-slide-show-button'.

 

Note that the component has the above data-testid attributes for test cases and certain classes and ids for rendering purposes. These should not be changed.

## Preview

There is a partially completed React catalog viewer application. Complete the
