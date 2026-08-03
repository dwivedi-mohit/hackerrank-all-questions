# Python: Predict Bank Deposit Sale

## Metadata

- **ID:** 1043335
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Data Wrangling, Data Visualization, Machine Learning, Medium, Data Science, Modeling
- **Skills:** Data Modeling, Data Wrangling

## Summary

This data science question evaluates data modeling, data wrangling, and machine learning concepts, ideal for mid-level roles. The problem requires predicting client subscriptions to term deposits using historical marketing data and analyzing feature impacts.

## Problem Statement

Lending Bank wants to attract term deposits to fund its lending business.  In a term deposit, a client agrees to deposit funds and allow the bank to use them for a fixed length of time.  In return, the bank will pay interest on the deposit.  

 

The bank’s sales manager wants to market the product to their existing clients.  They have historical information from a previous marketing campaign that includes client demographics, prior call experience, market conditions and the interest rate offered.  

 

Using machine learning, help the bank predict which clients are likely to subscribe to a new term deposit.  Explain how different features affect the decision.

 

Files

	
- train.csv
	
- test.csv
	
- sample_submission.csv

 

Problem

Perform an analysis of the given data to determine how different features are related to credit card eligibility.  Build a machine learning model that can predict the subs_deposit. 

 

For each record in the test set (test.csv), predict the value of the subs_deposit variable (0 or 1). Submit a CSV file with a header row plus each of the test entries, each on its own line.   The file (submissions.csv) should have exactly 2 columns:

	
- id
	
- subs_deposit (contains 0 or 1)

 

Deliverables

	
- Well commented Jupyter notebook
	
- “submissions.csv”

 

Explore the data, make visualizations, and generate new features if required. Make appropriate plots, annotate the notebook with markdowns and explain necessary inferences. A person should be able to read the notebook and understand the steps you take as well as the reasoning behind them. 

 

Evaluation Metric

The solution will be evaluated on the basis of F1 score.

F1 Score = (2*Precision*Recall)/(Precision+Recall)

 

Schema

	
		
			
			
Feature

			
			
			
Description

			
		
		
			
			
client_id

			
			
			
unique ID of the client called [unique key]

			
		
		
			
			
age_bracket

			
			
			
age bracket of the contacted client (in years)

			
		
		
			
			
job

			
			
			
job type of the contacted client

			
		
		
			
			
marital

			
			
			
marital status of the contacted client

			
		
		
			
			
education

			
			
			
highest level of education done by the client

			
		
		
			
			
has_housing_loan

			
			
			
whether the client has a house loan

			
		
		
			
			
has_personal_loan

			
			
			
whether the client has a personal loan

			
		
		
			
			
prev_call_duration

			
			
			
last contact duration (value = 0 if the client has not been contacted ever)

			
		
		
			
			
contact_date

			
			
			
date at which contact was made with the client (YYYY-MM-DD)

			
		
		
			
			
days_since_last_call

			
			
			
number of days that passed by after the client was last contacted from a previous campaign (numeric; 999 means client was not previously contacted)

			
		
		
			
			
num_contacts_prev

			
			
			
number of contacts performed before this campaign and for this client (numeric)

			
		
		
			
			
poutcome

			
			
			
outcome of the previous marketing campaign (categorical: "failure","nonexistent","success")

			
		
		
			
			
cpi

			
			
			
standing consumer price index before the call (monthly indicator)

			
		
		
			
			
subs_deposit

			
			
			
Did the client subscribe to the term deposit? (binary: 1,0) [dependent variable]

## Preview

Lending Bank wants to attract term deposits to fund its lending business.  In
