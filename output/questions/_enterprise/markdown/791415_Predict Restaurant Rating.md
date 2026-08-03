# Predict Restaurant Rating

## Metadata

- **ID:** 791415
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Data Wrangling, Data Visualization, Machine Learning
- **Skills:** Data Visualization, Data Wrangling, Machine Learning

## Summary

This data science question evaluates data wrangling, data visualization, and machine learning concepts, ideal for mid-level roles. The problem requires building a model to classify restaurants as 'Expensive' or 'Budget' based on various features.

## Problem Statement

Seemless is an online food ordering service that allows users to order food for delivery and takeout. They collect data about each listed restaurant that ranges from basic information such as name, city, and phone number, to attributes such as popular dishes, number of cuisines offered, etc. 

 

Seemless categorizes dining costs as ‘Expensive’ or ‘Budget’ on the basis of cuisines-offered, popular dishes and the overall reputation of the restaurant. This process requires manual inspection of the restaurant and is often biased. They have noticed that people tend to pay based upon the cuisine and some are inherently more expensive than others. They want to launch a brand new filter that automatically classifies dining costs in the restaurant listings. 

 

Using machine learning, help Seemless classify the restaurants as ‘Expensive’ or ‘Budget’.  Explain how different features affect the decision.

 

## Files

	
- train.csv
	
- test.csv
	
- sample_output.csv

 

 

Schema

 

	
		
		
		
	
	
		
			
			
Feature

			
			
			
Type

			
			
			
Description

			
		
		
			
			
id

			
			
			
int

			
			
			
The unique ID assigned to every restaurant.

			
		
		
			
			
name

			
			
			
str

			
			
			
The name of the restaurant. 

			
		
		
			
			
location

			
			
			
str

			
			
			
The location of the restaurant.

			
		
		
			
			
phone

			
			
			
str

			
			
			
The phone number of the restaurant. 

			
		
		
			
			
table_bookings

			
			
			
bool

			
			
			
Indicates if the restaurant takes online reservations. 

			
		
		
			
			
online_ordering

			
			
			
bool

			
			
			
Indicates if the restaurant takes online orders. 

			
		
		
			
			
restaurant_type

			
			
			
str

			
			
			
The type of restaurant. Values are Casual Dining, Cafe, Quick Bites, etc.

			
		
		
			
			
restaurant_operation

			
			
			
str

			
			
			
The primary operation of the restaurant. For example, ‘Delivery’.

			
		
		
			
			
primary_cuisine

			
			
			
str

			
			
			
The name of the primary cuisine offered by the restaurant. Values are American, Mexican, etc.  

			
		
		
			
			
popular_dishes

			
			
			
int

			
			
			
The number of popular dishes offered by the restaurant.

			
		
		
			
			
cuisines_offered

			
			
			
int

			
			
			
The number of cuisines offered by the restaurant.

			
		
		
			
			
rating

			
			
			
int

			
			
			
The rating of the restaurant.

			
		
		
			
			
votes

			
			
			
int

			
			
			
The number of customer votes received by the restaurant

			
		
		
			
			
dining_cost

			
			
			
int

			
			
			
It indicates if the classification of dining costs at the restaurant. Values are 0 (Budget), 1 (Expensive) 

			
		
	

 

 

## Problem

Perform an analysis of the given data to determine how different features are related to the completion of the course.  Build a machine learning model that can predict dining_cost. 

For each record in the test set (test.csv), predict the value of the dining_cost variable (0 or 1). Submit a CSV file with a header row plus each of the test entries, each on its own line. The file (submissions.csv) should have exactly 2 columns:

	
- id
	
- dining_cost (contains 0 or 1)

## Preview

Seemless is an online food ordering service that allows users to order food fo
