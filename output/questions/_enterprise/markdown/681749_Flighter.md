# Flighter

## Metadata

- **ID:** 681749
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** HTML5, CSS3, Easy, Front-End Development, JavaScript
- **Skills:** HTML/CSS/JS

## Summary

This front-end development question evaluates form validation, sorting functionality, and dynamic content rendering concepts, ideal for junior-level roles. The problem requires implementing a flight showcase web app with specific input handling and sorting features.

## Problem Statement

The Flighter is an online flight showcase web app with the following 3 sections:

 

1) Flight details:

 - There are 5 input fields: Name, Origin, Destination, Price and Rating.

 - There is an Add button to add the flight details.  The Add button should behave as follows:

	
- not add if any field is empty.
	
		
- 
		
show the error component if the user attempts to add a record with any input field empty. The id of the error component is error.

		
	
	
	
- 
	
add the data to the flight list if there was no error

	
	
- 
	
clear all input fields after successfully adding the new record.

	

 

 

2) Sorting: 

	
- 
	
There are two options to sort the flights in the list: 'Sort by Price' and 'Sort by Rating'.

	
	
- 
	
Initially the list is unsorted.  When the user clicks on either of the options, it should sort in ascending order first and then descending on the next click, then continue to alternate going forward.

	
	
- 
	
The name of the sort options should include the text `(asc)` when sorted in ascending order, and `(desc)` when sorted in descending order.

	
	
- 
	
These two options should be wrapped by a div with the id sorter.

	
		
- 
		
			
				
					 Name (default)
					Sorted in Ascending
					Sorted in Descending
					ID
				
			
			
				
					Sort by Price 
					Sort by Price (asc)
					Sort by Price (desc)
					sortPrice
				
				
					Sort by Rating
					Sort by Rating (asc)
					Sort by Rating (desc)
					sortRating
				
			
		
		
	
	

 

3) Flights List:

 

	
- 
	
The flight details should be displayed in a card component.

	
	
- 
	
Refer the <ul> component under the div with ID flightItems in the default layout provided. The <ul> is the card component that gets added dynamically for any additional flights added.

	

 

Layout details:

	
- 
	
The Flights List section should be wrapped inside a 'div' with id flightItems.

	
		
- 
		
All flight cards should lie inside the flightItems container.

		
		
- 
		
Each flight card is a <ul> which has if of the card class.

		
		
- 
		
Flight details are displayed using <li> tags inside <ul>

		
			
- 
			
The 1st <li> should contain 'Flight Name: <Name of the Airline>'

			
			
- 
			
The 2nd <li> should contain '<Origin> to <destination>'

			
			
- 
			
The 3rd <li> should contain 'Rating: <rating>*' (Include Star after rating without space)

			
			
- 
			
The 4th <li> should contain 'Price: Rs.<Cost of travel>'

			
		
		
	
	

 

- Two flight cards are pre-added in the list.

- The flight details of these two cards are stored in the window variable flightList.

-  flightList is an array of Object.

 

Note:

 - It is mandatory to maintain IDs in the fields to make a hassle-free validation.

 - Do not modify the existing template (index.html)

 

DEMO:

  
    
      Hide animation
      Show animation

## Preview

The Flighter is an online flight showcase web app with the following 3 sections:
