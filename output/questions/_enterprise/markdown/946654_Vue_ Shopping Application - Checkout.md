# Vue: Shopping Application - Checkout

## Metadata

- **ID:** 946654
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Vue.js, Easy, Component State Management
- **Skills:** Vue.js (Basic)

## Summary

This front-end development question evaluates Vue.js, component state management, and user interaction concepts, ideal for junior-level roles. The problem requires creating a shopping application with product listing and cart functionalities, ensuring it meets specified requirements and passes unit tests.

## Problem Statement

Create a basic shopping application as shown below. Some core functionalities have already been implemented, but the application is not complete. Application requirements are given below, and the finished application must pass all of the unit tests.

 

  
    
      Hide animation
      Show animation
    
    
      
    
  
  

The app has two separate views/components: the Product Listing component and the Cart component. The list of products to be displayed is already provided in the app. 

 

The app should implement the following functionalities:

	
- 
	
Clicking on each 'Add To Cart' button should add the item to the shopping cart. When an item is added to the cart:

	
		
- 
		
The 'Add To Cart' button should be removed from view, and the 'Remove From Cart' button should be displayed.

		
		
- 
		
An entry should be added to the table in the Cart component.

		
	
	
	
- 
	
Clicking on each 'Remove' button should remove the item from the cart and display 'Add to Cart' for the product item.

	
	
- The Cart component should have the following functionalities:
	
		
- Display all the items in the cart in a table. 
		
- Display the cart's subtotal, discount value, and total price.
		
- The cart has a 'Select Coupon' input. On selecting a coupon from this input, an appropriate discount is applied and the total price is calculated and displayed. (Subtotal - Discount = Total Price)
	
	
	
- Items should be displayed in the Cart component in the order they are added to the cart. 
	
- The list of products and the cart object are passed as props to the Product Listing component and the Cart component respectively.

 

Each product object contains the following properties: 

	
- 
	
name: Name of the product. [STRING]

	
	
- 
	
price: Price of the product. [NUMBER]

	
	
- 
	
id: Unique ID of the product. (Auto Generated) [NUMBER]

	
	
- 
	
image: The image URL of the product. [STRING]

	
	
- 
	
cartQuantity: The quantity of the item in the cart. The default value should be 0. [NUMBER]

	

 

Each item in the cart, CartItem, has the following properties:

	
- 
	
id: The ID of the product added to the cart. [NUMBER]

	
	
- 
	
item: The heading property of the product. [STRING]

	
	
- 
	
quantity: The quantity of the item in the cart. [NUMBER]

	
	
- 
	
price: The total price of the item in the cart. (quantity x product.price) [NUMBER]

	

 

The following data-testid/class attributes are required in the component for the tests to pass:

	
- 
	
Each product item in the Product Listing component should have the class 'product-item'.

	
	
- 
	
Each 'Add to Cart' button should have the data-testid attribute 'btn-item-add'.

	
	
- 
	
Each 'Remove' button should have the data-testid attribute 'btn-item-remove'.

	
	
- 
	
The table rows <tr> in the Cart component, corresponding to items in the cart, should have the data-testid attribute of 'cart-item-0', 'cart-item-1', and so on.

	
	
- 
	
The table data <td>, containing the name of the item in the cart, should have the data-testid attribute 'cart-item-name'.

	
	
- 
	
The table data <td>, containing the quantity of the item in the cart, should have the data-testid attribute 'cart-item-quantity'.

	
	
- 
	
The table data <td>, containing the price of the item in the cart, should have the data-testid attribute 'cart-item-price'.

	
	
- 
	
The 'Select Coupon' input should have the data-testid attribute 'cart-coupon'

	
	
- 
	
The cart's 'Subtotal' value container should have the data-testid 'cart-subtotal'. 

	
	
- 
	
The cart's 'Discount' value container should have the data-testid 'cart-discount'. 

	
	
- 
	
The cart's 'Total Price' value container should have the data-testid 'cart-total'. 

	

 

Please note that the component has these data-testid attributes for test cases, and certain classes and ids for rendering purposes. It is advised not to change them.

## Preview

Create a basic shopping application as shown below. Some core functionalities h
