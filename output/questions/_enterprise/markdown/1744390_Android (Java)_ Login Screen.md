# Android (Java): Login Screen

## Metadata

- **ID:** 1744390
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Android, Mobile Development, Java, Authentication, Easy
- **Skills:** Android (Basic)

## Summary

This mobile development question evaluates Android, Java, and authentication concepts, ideal for junior-level roles. The problem requires creating a login screen with specific design and functionality requirements, ensuring proper validation and user feedback.

## Problem Statement

Create a login screen, as shown. Application requirements are given below, and the finished application must pass all of the unit tests.

Hide animation Show animation

 

Functionality Requirements

Complete the implementation of MainActivity, ValidationUtils, and activity_main.xml according to the following requirements:

Screen Contents

The login screen contains one circular logo, one title, two inputs: username and password, and a login button.

Design Specifications

Background:

	
- Must be equal to secondary_color defined in colors.xml. Note: Use root_layout background attribute.

Logo:

	
- To show the HackerRank logo, use hfwlogo.png in the drawable folder and make it fit in a circular shape with 100dp width, 100dp height, and 100dp radius.
	
- Use the image_card view in XML to set the radius, width, and height. Use hfwlogo.png in a drawable folder to set the image on roundedImageView in XML.
	
- The logo must be 100dp from the top of the activity screen.

Container(XML id:login_container):

	
- It must be beneath the views title, username, password, and login_btn.
	
- It must have a height that spans to the bottom of the screen with a margin of 100dp from the bottom of Logo.
	
- The background must be extracted to a shape xml resource where the solid color and radius are defined.

Shape drawable specs:    

	
- The Solid color must be white defined in colors.xml.
	
- The top left and top right radii must be 30dp.

Title(XML id: title):

	
- 
Title must wrap content for width and height, and must be centered horizontally.
	
- The text must be "Login".
	
- Text size must be 24sp, style must be bold, and color must be primary_color defined in colors.xml.

Username(XML id: username):

	
- Wrap content for height and width must be given using the ems attribute.
	
- The ems must be 15.
	
- Hint must be "Username".
	
- The top margin must be 50dp.

Password(XML id: password):

	
- Wrap content for height and width must be given using the ems attribute.
	
- The ems must be 15.
	
- The hint must be "Password".
	
- The input type must be specified accordingly.
	
- The top margin must be 10dp.

Login Button(XML id: login_btn):

	
- Clicking on login_btn should trigger the validation on the form.
	
- The Username input field is required. If the submit button is clicked and the Username field is empty, the error "Username is required" should be rendered on the field. Otherwise, no error message should be rendered.
	
- The Password input field is required. If the submit button is clicked and the password field is less than 4 characters in length, the error "Password must have minimum 4 characters" should be rendered on the field. Otherwise, no error message should be rendered.
	
- If both inputs are valid, no error messages should be rendered and a toast must be displayed with the message "Success".
	
- The background color must be primary_color defined in colors.xml.
	
- The text color must be white, as defined in colors.xml.

	
- The top margin must be 40dp.

Note:

	
- The view's title, username, password, and login_btn must be in a vertical chain with chain style as packed.
	
- 
title must be the starting element in the chain with the top linked to the top of login_container. 
	
- login_btn must be the ending element in the chain with the bottom linked to the bottom of the parent.

All the files that need to be completed are opened in the editor by default. 

 

Testing Requirements

Please note that the views in activity_main.xml have the id attributes for test cases to run correctly. They should not be changed.

## Preview

Create a login screen, as shown. Application requirements are given below, and
