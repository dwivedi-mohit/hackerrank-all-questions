# Android (Java): Order Food

## Metadata

- **ID:** 1372264
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Medium, Java, Theme:  E-commerce, Android Libraries, Android
- **Skills:** Android (Intermediate)

## Summary

This mobile development question evaluates Android, Java, and e-commerce application concepts, ideal for mid-level roles. The problem requires creating a food ordering app screen that meets specific functionality and design requirements while passing unit tests.

## Problem Statement

Create a food ordering app screen, as shown below, so that it passes the unit tests.

Hide animation Show animation

Functionality Requirements

The files to edit are MainActivity.java, FoodListAdapter.java, activity_main.xml, and food_item.xml according to the following requirements:

Screen Contents

The screen contains 4 food items. Each item contains one image, the name of the item, and a button to add/remove the item from the cart.

Design Specs

	
- For the Activity Layout (File name: activity_main.xml): The code to set up the RecyclerView and display the food items must be written in setupFoodMenu() in MainActivity.java
	
- Recycler View (XML id: food_list): The view must have decoration defined in MainActivity.java as the decoration.
	
- For Food Item Layout (File name: food_item.xml): The code to bind the data to the recycler view item must be written in the onBindViewHolder method. The code to return the item size must be written in getItemCount in FoodListAdapter.
	
- Food Item (XML id: food_item_card): Each item must be a CardView. The width must match the parent. The height must wrap content.
	
- Food Name (XMLl id: food_name): Display the name of each food item defined in foodList in MainActivity.java for each Food Title in Food Item.
	
- Food Image (XML id: food_image): Display the image of each food item defined in foodList in MainActivity.java for each Food Image in Food Item.
	
- Add To Cart Button (XML id:food_cart_button): Text must display add_to_cart_btn_text defined in strings.xml by default, and toggle between add_to_cart_btn_text and remove_from_cart_btn_text defined in strings.xml as the button is clicked.

All the files to complete are open in the editor by default.

 

Testing Requirements

Please note that the views in activity_main.xml and food_item.xml have the id attributes for test cases to run correctly. They should not be changed. The same applies to the decoration variable in MainActivity.java.

## Preview

Create a food ordering app screen, as shown below, so that it passes the unit t
