# React: User Management

## Metadata

- **ID:** 1395159
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** React, Component State Management, Hard, Controlled Component, JavaScript
- **Skills:** React (Advanced)

## Summary

This front-end development question evaluates React, component state management, and controlled components concepts, ideal for senior-level roles. The problem requires completing a React application with specific functionalities and validations for user management.

## Problem Statement

There is a partially completed React application with the HTML template built and ready, and certain core React functionalities are implemented. Complete the React application as shown in order to pass all the unit tests.

 

 Hide animation Show animation 

 

The application has 2 components:

 

1. The UserList.js which has the user list table which includes edit/delete buttons as actions against the row.

2. The AddEditUser.js which renders the form to enter the user details to be added or edited.

 

The app should implement the following functionalities:

 

1. AddEditUser.js

	
- The initial view must not display any alert.
	
- Clicking the Cancel button should: 
	
		
- do nothing if the fields are empty.
		
- clear all the fields and reset them to empty.
		
- clear the validation alert (if any).
		
- after clicking the Edit button, discard the changes in the form and add the original user values back to the table.
	
	
	
- Clicking the Add/Edit button should:
	
		
- add field values as a row to the table with no validation alert and reset the form fields to empty. 
		
- after clicking the Edit button, add the user's updated data to the table or show a validation alert in case of any errors.
	
	

2.  UserList.js

	
- The initial view must display an empty list with no rows.
	
- Clicking the Delete button should delete the corresponding row from the table.
	
- Clicking the Edit button should populate the form fields where updates can be made.

 

3. Validations for Add/Edit User view:

	
- Do not add a user to the list on clicking Add/Edit User and show a common 'Validation alert' if:
	
		
- any of the input fields are empty.
		
- the 'phone number' field doesn't contain 10 digits or it starts with '0'.
	
	

 

The following data-testid attributes are required in the component for the tests to pass:

 

	
		
			Component
			Attribute
		
	
	
		
			First name input
			firstNameInput
		
		
			Last name input
			lastNameInput
		
		
			Phone input    
			phoneInput
		
		
			Table of Users
			userListTable
		
		
			Cancel Button
			cancelEditUserButton
		
		
			Add/Edit  Button
			addEditButton
		
		
			Validation Alert
			validationAlert
		
	

 

Please note that the component has data-testid attributes for test cases and certain classes and ids for rendering purposes. They should not be changed.

## Preview

There is a partially completed React application with the HTML template built an
