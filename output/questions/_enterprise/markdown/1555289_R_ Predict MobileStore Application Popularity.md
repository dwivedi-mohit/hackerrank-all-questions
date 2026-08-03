# R: Predict MobileStore Application Popularity

## Metadata

- **ID:** 1555289
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Data Wrangling, Modeling, Data Visualization, Machine Learning, R, Hard
- **Skills:** Data Wrangling, Data Modeling

## Summary

This data science question evaluates data wrangling, data modeling, and predictive modeling concepts, ideal for senior-level roles. The problem requires building a model to predict app popularity based on various features and submitting results in a specified format.

## Problem Statement

Business Logic:

Mobile applications have revolutionized the way products and services are used. MobileStore is an online marketplace, where businesses can host their mobile apps and users can download them. The more popular an app is, the higher the returns a business can expect. Hence, the company requires a model to predict the popularity of an app uploaded to their marketplace. The target feature is popularity with two values: 'High' and 'Low’. Some of the data fields have bugs that need to be fixed.

 

The deliverables are well-documented Jupyter notebook, and "submissions.csv" with predictions.

 

Data Sets and Schema:

Data sets

"train.json" - JSON format data used to train the model

"test.csv" - data used for prediction

"submissions.csv" - populate this file with the results

"sample_submission.csv" - sample reference of submission file data

 

Schema

 

	
		
		
	
	
		
			
			
Feature

			
			
			
Description

			
		
		
			
			
app_id

			
			
			
the unique app id

			
		
		
			
			
category

			
			
			
the category under which the app is categorized

			
		
		
			
			
reviews

			
			
			
the number of reviews received

			
		
		
			
			
size

			
			
			
the size of the app (in KB/MB)

			
		
		
			
			
installs

			
			
			
the number of people who installed the app at least once

			
		
		
			
			
price

			
			
			
the price of the app (in US $)

			
		
		
			
			
suitable_for

			
			
			
the rating given to the app based on its usage and content

			
		
		
			
			
last_update

			
			
			
date the app was last updated

			
		
		
			
			
latest_ver

			
			
			
the latest version of the app available

			
		
		
			
			
popularity

			
			
			
user popularity (High/Low)

			
		
	

 

 

 

Technical Specifications:

 

R packages

Use the "install.packages" command to import additional packages as needed.

 

Exploratory Data Analysis and Feature Engineering

Prepare the training dataset from"train.json" for analysis.

Drop any rows that are missing a value for a feature.

Find and fix the data bug in the "reviews" field.

Add new features related to the original time-series variable.

Use encoding of categorical features wherever it is necessary.

Identify the features that are most important to the model’s performance.

 

Predictive Modeling and Model Evaluation

Design a modeling pipeline to predict "popularity" as the target feature. The pipeline should have at least one predictive model. Use of multiple models is optional.

Assess model performance on "train.csv" by using the "Accuracy“ metric, i.e., the number of correct predictions divided by the total number of predictions.

 

Submission:

Make a prediction of the "popularity" feature for “test.csv”. The result should be a table with two columns, "app_id" and “popularity". The "popularity" column should have "High" or "Low" values.

Save the results in "submissions.csv". Include a header with column names. An example is provided in "sample_submission.csv".

 

Test Evaluation:

The score will be automatically evaluated based on the value of Accuracy metric for the “submissions.csv” file. Get the best possible value of the metric during model development. The reviewer might dive deeper into the Jupyter notebook and the visualization to get more context.

## Preview

Business Logic:
