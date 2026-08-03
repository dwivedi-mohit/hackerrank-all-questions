# Python: Predict Real Estate Prices

## Metadata

- **ID:** 1043047
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Data Wrangling, Data Visualization, Machine Learning, Medium, Modeling, Data Science
- **Skills:** Data Modeling, Data Wrangling

## Summary

This data science question evaluates data modeling, data wrangling, and machine learning concepts, ideal for mid-level roles. The problem requires building a model to predict real estate prices based on various property features using a provided dataset.

## Problem Statement

Predict Real Estate Prices

 

EstateAgent is both a company name and the name of their platform for buying and selling homes. Every day the company purchases homes then offers them for sale on the platform. They must be able to quickly determine the market value of a home so they can identify good deals to buy and price properties to sell. In order to grow, they need a quicker, more reliable method of valuing properties. They have provided a dataset for recently purchased properties which consists of various features such as location, number of rooms, bathrooms, parking spots, year of construction and the purchase price.

 

Using machine learning, build a model that can predict property prices. Explain how different features influence the price predictions.

 

Files

	
- train.csv
	
- test.csv
	
- sample_submission.csv

 

Problem

You are required to perform analysis on the given data and learn how different features are related to and affect the response. With the given data, build a machine learning model which can be used to predict the price. For each record in the test set (Test.csv), you must predict the value of the price variable. You should submit a CSV file with a header row and one row per test entry. The file (submissions.csv) should have exactly 2 columns:

	
- id
	
- price

 

Evaluation Metric The metric used for evaluating the performance of the model is its Mean Absolute Percent Error: MAPE = It is the mean of the absolute percentage errors of forecasts.

 

Deliverables

	
- Well commented Jupyter notebook
	
- 'submissions.csv'

Your notebook should contain your solution, visualizations, and thought process, including the top features that go into the model. If required, please generate new features. Make appropriate plots, annotate the notebook with markdowns, and explain the necessary inferences. A person should be able to read your notebook and understand the steps are you taking and the reasoning behind them.

Schema

 

	
		
		
		
	
	
		
			
			
Field

			
			
			
Type

			
			
			
Description

			
		
		
			id
			int
			Unique id of every property
		
		
			
			
area

			
			
			
int

			
			
			
Area of the structure

			
(sq. feet)

			
		
		
			
			
bathrooms

			
			
			
int

			
			
			
Number of bathrooms

			
		
		
			
			
bedrooms

			
			
			
int

			
			
			
Number of rooms

			
		
		
			
			
condo_fee

			
			
			
int

			
			
			
Condominium fee (US Dollars)

			
		
		
			
			
parking_spots

			
			
			
int

			
			
			
Number of parking spots

			
		
		
			
			
attached_rooms

			
			
			
int

			
			
			
Number of bedrooms with direct access to a bathroom

			
		
		
			
			
type

			
			
			
categorical

			
			
			
Kind of real estate

			
{apartment, house, other}

			
		
		
			
			
lat

			
			
			
int

			
			
			
Latitude of the property

			
		
		
			
			
lon

			
			
			
int

			
			
			
Longitude of the property

			
		
		
			year_built
			int
			Year the real property was built
		
		
			overall_condition
			categorical
			
			
Abstract evaluation of the owner

			
1 to 5 (best to worst)

			
		
		
			has_elevator
			str
			If the property has elevator or not
		
		
			leasures_available
			str
			List of leasures in the property
		
		
			
			
price

			
			
			
int

			
			
			
Price of the real estate (US Dollars)

## Preview

Predict Real Estate Prices
