# Python: Predict Customer Exit

## Metadata

- **ID:** 999752
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Medium, Data Science, Machine Learning, Data Visualization, Modeling
- **Skills:** Data Modeling, Data Wrangling

## Summary

This data science question evaluates data modeling, data wrangling, and machine learning concepts, ideal for mid-level roles. The problem requires analyzing consumer data to predict disconnection likelihood and understanding feature impacts on churn.

## Problem Statement

AB Communications provides telephone and Internet services to consumers. Recently they have noticed a decline in the number of subscribers. Management has decided to investigate which consumers are more prone to disconnect. They want to analyze which factors affect this the most both to find ways to reduce the churn and also to help in customer profiling.

 

Using machine learning, help AB Communications predict which consumers are likely to opt for disconnection in the future and explain how different features affect that.

 

Files

	
- train.csv
	
- test.csv
	
- sample_output.csv

 

Problem

Perform an analysis of the given data and find out how different features are related to exit_status. Also, build a machine learning model that can be used to predict the exit_status. 

 

For each record in the test set (test.csv), predict the value of the exit_status variable (Yes or No). Submit a CSV file with a header row and test entries, one per row. The file (submissions.csv) should have exactly 2 columns:

	
- id
	
- exit_status (contains Yes or No)

 

Deliverables

	
- Well commented Jupyter notebook
	
- “submissions.csv”

Play with the data, make visualizations, and generate new features if required. Make appropriate plots, annotate the notebook with markdowns, and explain necessary inferences. A person should be able to read the notebook and understand the steps and the reasoning behind them.

 

Schema

 

	
		
		
	
	
		
			
			
Feature

			
			
			
Description

			
		
		
			
			
id

			
			
			
The unique ID assigned to every consumer.

			
		
		
			
			
gender

			
			
			
Sex of the applicant. (Male/Female)

			
		
		
			
			
age

			
			
			
Age of the consumer. (in Years)

			
		
		
			
			
dependents

			
			
			
If any dependents present of consumer. (Yes/No)

			
		
		
			
			
lifetime

			
			
			
Time since consumer is using services. (in Months)

			
		
		
			
			
phone_services

			
			
			
Is consumer using dialing services (Yes/No)

			
		
		
			
			
internet_services

			
			
			
Type of Internet services being used. (None/ 3G/ 4G)

			
		
		
			
			
online_streaming

			
			
			
How avid is the consumer using online streaming services

			
		
		
			
			
multiple_connections

			
			
			
Does consumer have multiple connections (Yes/No)

			
		
		
			
			
premium_plan

			
			
			
Is consumer using the premium plan (Yes/No)

			
		
		
			
			
online_protect

			
			
			
Whether consumers have opted for protection plan which covers any loss of data as well online security (Yes/No)

			
		
		
			
			
contract_plan

			
			
			
Billing plan of the consumer. Values are Month-to-month

			
,one year & two year.

			
		
		
			
			
ebill_services

			
			
			
Has consumer opted for paperless bill (Yes/No)

			
		
		
			
			
default_payment

			
			
			
Default payment method opted by consumer.

			
		
		
			 
			
monthly_charges

			
			
			
Monthly charges paid by the consumer (in $$). 

			
		
		
			
			
issues

			
			
			
Total number of support tickets raised by customer till date.

			
		
		
			
			
exit_status

			
			
			
Whether the consumer has opted for disconnection Values are No/Yes

## Preview

AB Communications provides telephone and Internet services to consumers. Recen
