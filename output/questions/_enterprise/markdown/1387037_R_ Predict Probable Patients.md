# R: Predict Probable Patients

## Metadata

- **ID:** 1387037
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Machine Learning, Data Visualization, Data Wrangling, R, Medium
- **Skills:** Data Wrangling, Data Modeling

## Summary

This data science question evaluates data wrangling, data modeling, and machine learning concepts, ideal for mid-level roles. The problem requires building a model to predict patient participation in a new diabetes treatment based on various health factors.

## Problem Statement

MediTech is one of the top pharmaceutical laboratories of the US. They are working on a new medical procedure to treat diabetes and have partnered with major hospitals to target potential patients. They approach every patient and set up sessions to make them aware of this procedure, but it is expensive.

 

They have collected data from various hospitals and thousands of patients they approached. Using machine learning, build a model to predict if a patient will try their procedure and analyze what factors affect it.  

 

## Files

	
- train.csv
	
- test.csv
	
- sample_submission.csv

 

Schema

 

	
		
		
	
	
		
			
			
Column Name

			
			
			
Description

			
		
		
			
			
patient_id

			
			
			
Unique identifier of a patient

			
		
		
			
			
gender

			
			
			
Patient gender

			
		
		
			
			
age

			
			
			
Age of the patient (binned in intervals of 10 years)

			
		
		
			
			
time_in_hospital

			
			
			
Number of days between admission and discharge

			
		
		
			
			
num_lab_procedures

			
			
			
Number of lab tests performed during the visit

			
		
		
			
			
num_procedures

			
			
			
Number of procedures (other than lab tests) during the visit

			
		
		
			
			
num_medications

			
			
			
Number of distinct medications administered during the visit

			
		
		
			
			
number_diagnoses

			
			
			
Number of diagnoses entered in the system

			
		
		
			
			
glucose_test

			
			Indicates the range of the blood glucose test result
		
		
			insulin_change
			Change in insulin dosage of the patient
		
		
			diabetes_drug_1
			Change in the dosage of an injected drug for type-II diabetes
		
		
			diabetes_drug_2
			Change in the dosage of an oral drug for type-II diabetes
		
		
			
			
medication_change

			
			
			
If there was any change in patient’s medicine (Yes/No)

			
		
		
			
			
followup

			
			
			
Whether followup was advised by the physician (Yes/No)

			
		
		
			
			
opted

			
			
			
Whether the patient opts for the procedure or not (Yes/No)

			
		
	

 

 

## Problem

Perform an analysis to determine how different features are related to the target variable i.e. opted. Build a machine learning model that can predict whether the patient will opt for the procedure.

 

For each record in the test set (test.csv), predict the value of the opted variable. Submit a CSV file with a header row plus each of the test entries on its own line. The file (submissions.csv) should have exactly 2 columns:

	
- id
	
- opted (Whether the patient opts for the procedure or not) 

 

## Evaluation Metric

The evaluation metric is Accuracy.

 

Accuracy = number of correct predictions/total number of predictions

##  

##  

## Deliverables

	
- Well commented Jupyter notebook
	
- “submissions.csv”

 

Explore the data, make visualizations, and generate new features if required. Make appropriate plots, annotate the notebook with markdowns and explain necessary inferences. A person should be able to read the notebook and understand the steps taken and the reasoning behind them. The solution will be graded based on the usage of effective visualizations to convey the analysis and the modeling process.

## Preview

MediTech is one of the top pharmaceutical laboratories of the US. They are worki
