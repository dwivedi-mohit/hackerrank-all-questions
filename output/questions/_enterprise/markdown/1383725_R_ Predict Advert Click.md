# R: Predict Advert Click

## Metadata

- **ID:** 1383725
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Modeling, Data Wrangling, Machine Learning, Data Visualization, Medium, R
- **Skills:** Data Wrangling, Data Modeling

## Summary

This data science question evaluates data wrangling, data modeling, and machine learning concepts, ideal for mid-level roles. The problem requires analyzing user data to predict advertisement clicks and understanding feature impacts on predictions.

## Problem Statement

SearchMe is an Internet giant and search engine company that earns the majority of its revenue through online advertising. Their aim is to maximize the number of clicks their advertisements generate.

 

Management has decided to investigate which users are more likely to click a particular advertisement. They want to analyze which factors affect this the most. This will not only help to increase the engagement but will also help in user profiling. 

 

Using machine learning, predict which users are likely to click a particular advertisement and explain how different features affect the prediction.

 

Files

	
- train.csv
	
- test.csv
	
- sample_output.csv

Schema

 

-->

	
		
		
	
	
		
			
			
Feature

			
			
			
Description

			
		
	
	
		
			
			
id

			
			
			
Unique consumer id

			
		
		
			
			
Daily Time Spent on Site

			
			
			
Consumer time spent on-site (in minutes)

			
		
		
			
			
Age

			
			
			
Consumer age (in years)

			
		
		
			
			
Area Income

			
			
			
Avg. Income of geographical area of consumer (in US $$)

			
		
		
			
			
Daily Internet Usage

			
			
			
Avg. minutes a day consumer is on the Internet

			
		
		
			
			
Ad Topic Line

			
			
			
The headline of the advertisement

			
		
		
			
			
gender

			
			
			
Gender of the consumer

			
		
		
			
			
Country

			
			
			
Country of consumer 

			
		
		
			
			
Timestamp

			
			
			
Timestamp at which consumer clicked on Ad or closed window (YYYY-MM-DD HH:MM:SS)

			
		
		
			
			
Clicked

			
			
			
Whether a consumer clicked on the advertisement or not 

			
(0: No ,1: Yes)

			
		
	

 

Problem

Perform an analysis of the given data and find out how different features are related to Clicked. Also, on the given data, build a machine learning model that can be used to predict the Clicked variable. 

For each record in the test set (test.csv), predict the value of the Clicked variable (0/1). Submit a CSV file with test entries, plus a header row. The file (submissions.csv) should have exactly 2 columns:

	
- id
	
- Clicked (contains 0 or 1)

 

Deliverables

	
- Well commented Jupyter notebook
	
- submissions.csv

Experiment with the data, make visualizations and generate new features if required. Make appropriate plots, annotate the notebook with markdowns, and explain necessary inferences. A person should be able to read the notebook and understand the steps taken and the reasoning behind them. The solution will be graded on the basis of the usage of effective visualizations to convey the analysis and the modeling process.

 

 

Evaluation Metric

Accuracy

Accuracy = Number of Correct Predictions/Total number of Predictions

## Preview

SearchMe is an Internet giant and search engine company that earns the majorit
