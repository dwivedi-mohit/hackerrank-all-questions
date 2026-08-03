# Angular: Resource Records

## Metadata

- **ID:** 1617534
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Medium, Component State Management, Angular, Component Interaction, Event Handling
- **Skills:** Angular (Intermediate)

## Summary

This front-end development question evaluates component state management, component interaction, and event handling concepts, ideal for mid-level roles. The problem requires completing an Angular application with two components to display and manage resource details correctly.

## Problem Statement

There is a partially completed Angular resource records application. Certain core Angular functionalities are already implemented. Complete the application as shown to pass the unit tests.

 

 Hide animation Show animation 

 

The application has 2 components:

	
- The ResourceTable component, which displays the list of resources in a tabular form.
	
- The ResourceDetails component, which presents the full details of the selected resource.

 

The application has the following functionalities:

	
- 
	
Initially, the ResourceTable displays entire list of resources is a tabular format. The list of resources is passed to it as input which is an array of Resource type objects. The Resource type has below interface:

	

`interface Resource {
  name: string;
  country: string;
  id: string; // Unique identifier of each resource
}
`
```

	
 

	
	
- 
	
Each resource row in this table has columns for name, country, and a 'View details' button. Clicking on 'View details' button selects this resource and displays its details in the ResourceDetails component.

	
	
- 
	
The details of the resource are defined in the ResourceDetails interface:

	

`interface ResourceDetails {
  id: string;
  city: string;
  pin: number;
  state: string;
  totalCapacity: number;
  allocated: number;
}
`
```

	
 

	
	
- 
	
The ResourceDetails component renders the columns name, country, city, state, pin, totalCapacity, and allocated. It should render only the most recently selected resource.

	
	
- 
	
The data must be merged from both interfaces to render it in the ResourceDetails component.

	
	
- 
	
Since no resource is selected initially, the ResourceDetails component should not be rendered.

	

 

The following data-test-id attributes are required in the component for the tests to pass:

	
- The ResourceTable <tbody> has the data-test-id attribute 'resource-list'.
	
- Each 'View details' button has the data-test-id attribute 'view-details-button'.
	
- The ResourceDetails <tbody> has the data-test-id attribute 'resource-details'.

 

Please note that the component has these data-test-id attributes for test cases and certain classes and IDs for rendering purposes. They should not be changed.

## Preview

There is a partially completed Angular resource records application. Certain cor
