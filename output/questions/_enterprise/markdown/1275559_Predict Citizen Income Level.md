# Predict Citizen Income Level

## Metadata

- **ID:** 1275559
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Machine Learning, Data Wrangling, Data Visualization, Data Modeling, Classification
- **Skills:** Data Modeling, Data Visualization, Data Wrangling, Machine Learning

## Summary

This data science question evaluates data modeling, data visualization, and machine learning concepts, ideal for mid-level roles. The problem requires developing a machine learning model to predict citizens' income levels based on demographic data.

## Problem Statement

Given a dataset of various demographics of citizens of a country, develop a machine learning model to predict a citizen's income level.

 

Files

	
- train.csv
	
- test.csv
	
- sample_submission.csv

 

 

Problem

Build a machine learning model to predict the ‘outcome' attribute.

 

For each record in the test set (test.csv), predict the value of the 'outcome' variable. Submit a CSV file with a header row and one row per test entry. The file (submissions.csv) should have exactly 2 columns:

	
- id
	
- 
outcome:  (0/1)

 

Evaluation Metric:

The metric used for evaluating the performance of the model is Accuracy Score:

Accuracy = Number of correct predictions / Total number of predictions made

 

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

			
			
			
Unique ID of the citizen

			
		
		
			
			
age

			
			
			
str

			
			
			
Age in years

			
		
		
			
			
workclass

			
			
			
str

			
			
			
working-class

			
		
		
			
			
fin_wt_working_hours

			
			
			
int

			
			
			
Financial soundness index and the corresponding number of hours per week the person works separated by a delimiter

			
		
		
			
			
education

			
			
			
int

			
			
			
Education level

			
		
		
			
			
years_of_study

			
			
			
int

			
			
			
Number of years of study the citizen has undergone

			
		
		
			
			
marital_status

			
			
			
int

			
			
			
Marital status

			
		
		
			
			
relationship_to_dependent

			
			
			
int

			
			
			
The relationship of the citizen to their dependent

			
		
		
			
			
ethnicity

			
			
			
int

			
			
			
Ethnicity

			
		
		
			 gender
			str
			Gender
		
		
			
			
capital_earned

			
			
			
int

			
			
			
Amount of capital gains made in the previous fiscal year

			
		
		
			capital_spent
			 int

			Amount of capital gains spent in the previous fiscal year
		
		
			
			
outcome

			
			
			
int

			
			
			
Income level (0 - Low, 1 - High)

## Preview

Given a dataset of various demographics of citizens of a country, develop a ma
