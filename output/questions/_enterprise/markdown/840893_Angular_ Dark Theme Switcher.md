# Angular: Dark Theme Switcher

## Metadata

- **ID:** 840893
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Angular, Node ^12.18.3, DOM Manipulation, Easy, Angular 10, TypeScript, Controlled Component
- **Skills:** Angular (Basic)

## Summary

This front-end development question evaluates Angular, DOM manipulation, and TypeScript concepts, ideal for junior-level roles. The problem requires creating a dark theme blog application with specific functionalities and unit test requirements.

## Problem Statement

Create a dark theme blog application, as shown below. Some core functionalities have already been implemented, but the application is not complete. Application requirements are given below, and the finished application must pass the unit tests.

 

  
    
      Hide animation
      Show animation
    
    
      
    
  
  

The app has two components: the Blog component and the Theme Switcher component. The list of the blog posts to be displayed is provided. 

 

The app should implement the following functionalities:

	
- 
	
The blog posts should be initially displayed in their respective <article> tags in the same order that they are provided.

	
	
- 
	
The Theme Switcher component should have a button titled 'Light Theme' initially.  

	
	
- 
	
Clicking on the 'Light Theme' button should add the class 'theme--dark' to the body of the page (e.g., <body class="theme--dark">) and should update the button text from 'Light Theme' to 'Dark Theme'.

	
	
- 
	
Clicking on the same button again should toggle the theme to Light, and the class 'theme--dark' should be removed from the body of the page. The text of the button should also be updated to 'Light Theme'.

	

 

Each blog post is an array of objects, and the included markup includes all the necessary details required to render a blog post item.

 

Note: The styling required to change the theme of the app from light to dark is already provided in the project. Adding the class 'theme--dark' will automatically change the related styles throughout the page.

 

The following data-test-id/class attributes are required in the component for the tests to pass.

	
- 
	
The parent container of the blog post items should have the data-test-id attribute 'blog-posts'.

	
	
- 
	
Each blog post item should have the data-test-id attribute 'blog-item-0', 'blog-item-1', 'blog-item-2', and so on.

	
	
- 
	
Each blog title paragraph tag <p> should have the data-test-id attribute 'blog-title'.

	
	
- 
	
The Theme switcher button should have the data-test-id attribute 'switcher-button'.

	
	
- 
	
The span containing the text inside the Theme switcher button should have the data-test-id attribute 'current-theme'.

	

 

Please note that the component has these data-test-id attributes for test cases, and certain classes and ids for rendering purposes. You should not change them.

## Preview

Create a dark theme blog application, as shown below. Some core functionalities
