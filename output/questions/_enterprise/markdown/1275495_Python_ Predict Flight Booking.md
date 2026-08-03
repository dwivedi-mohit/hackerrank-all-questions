# Python: Predict Flight Booking

## Metadata

- **ID:** 1275495
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Machine Learning, Data Wrangling, Data Visualization, Data Modeling, Classification, Medium
- **Skills:** Python for Applied Data Science (Intermediate)

## Summary

This data science question evaluates machine learning, data wrangling, and data visualization concepts, ideal for mid-level roles. The problem requires developing a model to predict customer retention based on demographic and flight rating features.

## Problem Statement

Given a dataset of various demographic and flight rating features an airline's customers, develop a machine learning model to predict if they will travel with the airline again.

 

Files

	
- train.csv
	
- test.csv
	
- sample_submission.csv

 

 

Problem

Build a machine learning model to predict the ‘Target' attribute.

 

For each record in the test set (test.csv), predict the value of the 'Target' variable. Submit a CSV file with a header row and one row per test entry. The file (submissions.csv) should have exactly 2 columns:

	
- id
	
- target: Will the customer book a flight with the company again (0 - no, 1 - yes)

 

Evaluation Metric:

The metric used for evaluating the performance of the model is its F1-Score:

F1-Score= (2*Precision*Recall) / (Precision + Recall)

 

Deliverables

	
- well commented Jupyter notebook
	
- 'submissions.csv'

 

The notebook should contain your solution, visualizations, and thought process, including the top features that go into the model. If required, please generate new features. Make appropriate plots, annotate the notebook with markdowns, and explain the necessary inferences. A person should be able to read your notebook and understand the steps you take and the reasoning behind them.

 

Schema

 

	
		
		
		
	
	
		
			
			
Field

			
			
			
type

			
			
			
Description

			
		
		
			
			
id

			
			
			
int

			
			
			
Unique ID corresponding to the traveller

			
		
		
			
			
Gender

			
			
			
str

			
			
			
Gender of the traveller

			
		
		
			
			
Age

			
			
			
int

			
			
			
Age of the traveller

			
		
		
			
			
Class

			
			
			
int

			
			
			
Cabin class of the traveller

			
		
		
			
			
Flight Distance

			
			
			
int

			
			
			
Flight’s distance of travel(in kms)

			
		
		
			
			
Inflight wifi service

			
			
			
str

			
			
			
Traveller rating for inflight wifi service(0-5)

			
		
		
			
			
Food and drink

			
			
			
str

			
			
			
Traveller rating for food and drink(0-5)

			
		
		
			Inflight entertainment
			
			
int

			
			
			
Traveller rating for inflight entertainment(0-5)

			
		
		
			
			
Departure Delay in minutes

			
			
			
str

			
			
			
Departure delay of flight

			
		
		
			
			
target

			
			
			
int

			
			
			
Will the traveller book a flight with the company again(0 - no, 1 - yes)

## Preview

Given a dataset of various demographic and flight rating features an airline's
