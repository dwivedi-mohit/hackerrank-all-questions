# Python: Predict Candidate Compensation

## Metadata

- **ID:** 791413
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Data Wrangling, Data Visualization, Machine Learning, Easy
- **Skills:** Data Wrangling

## Summary

This data science question evaluates data wrangling, data visualization, and machine learning concepts, ideal for junior-level roles. The problem requires building a model to predict yearly compensation based on various candidate factors using provided datasets.

## Problem Statement

DataHire is a human resource firm that specializes in providing HR services to companies and organizations. They specialize in data professionals who can manage huge amounts of data to solve business problems. An important part of their service is predicting annual compensation based on a candidate’s skill set. This is being done manually. They want a system that will predict a candidate’s yearly compensation in USD based on several factors like education, experience and relevant skills.

 

They have conducted a survey over 3 years, from 2017 to 2019, and have collected data from data professionals. Using machine learning, build a model to predict a candidate’s yearly compensation. Analyze which factors contribute the most in making this prediction.

 

## Files:

	
- train.csv
	
- test.csv
	
- sample_submission.csv

##  

## Problem:

Perform an analysis of the given data to determine how different features are related to the target variable i.e. salary. Build a machine learning model that can predict the yearly salary of a candidate.

 

For each record in the test set (test.csv), predict the value of the ‘salary’ variable. Submit a CSV file with a header row plus each of the test entries, each on its own line. The file (submissions.csv) should have exactly 2 columns:

	
- id
	
- salary (yearly salary in USD)

 

Schema

 

	
		
		
	
	
		
			
			
Column Name

			
			
			
Description

			
		
		
			
			
id

			
			
			
Record index

			
		
		
			
			
timestamp

			
			
			
Datetime (YYYY:MM:DD HH:MM:SS) when data was collected

			
		
		
			
			
country

			
			
			
Current country of employment

			
		
		
			
			
employment_status

			
			
			
Whether a candidate is full-time, part-time, an independent consultant or not working at the moment

			
		
		
			
			
job_title

			
			
			
Current job title of the candidate

			
		
		
			
			
job_years

			
			
			
Total job experience (in Years)

			
		
		
			
			
is_manager

			
			
			
Whether the candidate holds a managerial position or not (Yes or No)

			
		
		
			
			
hours_per_week

			
			
			
No. of hours per day committed to the current job

			
		
		
			
			
telecommute_days_per_week

			
			
			
No. of telecommuting days per week (working from home)

			
		
		
			
			
education

			
			
			
The highest degree in education the candidate has received

			
		
		
			
			
is_education_computer_related

			
			
			
Is the education related to the field of computer science (Yes or No)

			
		
		
			
			
certifications

			
			
			
Does the candidate have any relevant certifications (Yes or No)

			
		
		
			
			
salary

			
			
			
Yearly Salary (in US $$)

			
		
	

 

##  

## Deliverables:

	
- 
	
Well commented Jupyter notebook

	
	
- 
	
“submissions.csv”

	

Explore the data, make visualizations, and generate new features if required. Make appropriate plots, annotate the notebook with markdowns and explain necessary inferences. A person should be able to read the notebook and understand the steps taken as well as the reasoning behind them. The solution would be graded on the basis of the usage of effective visualizations to convey the analysis and the modelling process.

## Evaluation Metric:

The metric used for evaluating the performance of Mean Absolute Percent Error.

MAPE = mean of the absolute percentage errors of forecasts

## Preview

DataHire is a human resource firm that specializes in providing HR services to
