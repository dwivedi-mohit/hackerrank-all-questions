# R: Predict Loan Defaults

## Metadata

- **ID:** 1342297
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Data Science, Medium, R, Data Wrangling, Data Visualization, Data Modeling
- **Skills:** R (Intermediate), Data Modeling, Data Wrangling, Data Visualization

## Summary

This data science question evaluates data modeling, data wrangling, and data visualization concepts, ideal for mid-level roles. The problem requires predicting loan defaults using machine learning based on financial and company data, while explaining feature impacts.

## Problem Statement

Predict Loan Defaults

SIB (Small Industries Bank) loans money to companies in exchange for the promise of repayment. Some will default on the loans, being unable to repay them for some reason. The bank maintains insurance to reduce its risk of loss in the event of default. The insured amount may cover all or just some part of the loan amount. SIB wants to predict which companies will default on their loans based on their financial information. They have provided you with a dataset that consists of loan-related information such as loan amount, and state. Also, there is company information such as the number of employees, operating sector, etc.

 

Using machine learning, predict which companies will default on their loans and explain how different features impact the predictions.

 

Files

	
- train.csv
	
- test.csv
	
- sample_submission.csv

 

 

Problem

Analyze the given data and learn how different features are related to and affect default_status. Build a machine learning model that can be used to predict the ‘default_status'.

 

For each record in the test set (test.csv), predict the value of the default_status variable. Submit a CSV file with a header row and one row per test entry. The file (submissions.csv) should have exactly 2 columns:

	
- id
	
- default_status

 

Evaluation Metric: The metric used for evaluating the performance of the model is its Accuracy: Accuracy= Number of correct Predictions / Total number of predictions

 

Deliverables

	
- Well commented Jupyter notebook
	
- 'submissions.csv'

The notebook should contain your solution, visualizations, and thought process, including the top features that go into the model. If required, please generate new features. Make appropriate plots, annotate the notebook with markdowns, and explain the necessary inferences. A person should be able to read your notebook and understand the steps taken and the reasoning behind them.

Schema

 

	
		
		
		
	
	
		
			
			
Field

			
			
			
type

			
			
			
Description

			
		
		
			
			
id

			
			
			
int

			
			
			
Unique id for each application

			
		
		
			
			
industry

			
			
			
str

			
			
			
Operating sector of the business

			
		
		
			
			
state

			
			
			
str

			
			
			
State where the loan is applied for

			
		
		
			
			
request_date

			
			
			
str

			
			
			
Date of request for loan (DD-Month-YY)

			
		
		
			
			
employee_count

			
			
			
int

			
			
			
Number of employees at the time of submitting the application

			
		
		
			
			
business_new

			
			
			
str

			
			
			
Whether a business is new (operational for <= 6 Months) or existing (>6 Months)

			
		
		
			
			
business_type

			
			
			
int

			
			
			
Whether a business is a part of an existing franchise (1) or standalone (0)

			
		
		
			
			
location

			
			
			
str

			
			
			
Operating area type (RURAL/URBAN)

			
		
		
			
			
other_loans

			
			
			
str

			
			
			
If the business has taken any other loans (Y/N)

			
		
		
			
			
loan_amount

			
			
			
str

			
			
			
Loan principal amount ($$) '$xxx.xx'

			
		
		
			
			
insured_amount

			
			
			
str

			
			
			
Amount insured against default ($$) '$xxx.xx'

			
		
		
			
			
default_status

			
			
			
int

			
			
			
Whether business defaults on the loan (0: No,1: Yes)

## Preview

Predict Loan Defaults
