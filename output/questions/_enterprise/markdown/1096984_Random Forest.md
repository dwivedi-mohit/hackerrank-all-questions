# Random Forest

## Metadata

- **ID:** 1096984
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Python 3, Scikit-Learn, Easy
- **Skills:** Machine Learning

## Summary

This data science question evaluates machine learning, model training, and prediction concepts, ideal for junior-level roles. The problem requires building a Random Forest classifier using scikit-learn to predict binary labels from a dataset and submitting the results in a specified format.

## Problem Statement

Given a dataset containing numerical and categorical values and corresponding binary labels(0/1), train a Random Forest classifier using scikit-learn and make predictions on the unseen test dataset.

 

Files

	
- train.csv
	
- test.csv
	
- sample_submission.csv

 

Problem

Build a Random Forest model that can predict the target variable.

For each record in the test set (test.csv), predict the value of the 'label' variable. Submit a CSV file with a header row and one row per test entry. The file (submissions.csv) should have exactly 1 column:

	
- label

 

Evaluation Metric:

The metric used for evaluating the performance of the model is Accuracy.

Accuracy = Correct Predictions/Total Number of Predictions

 

The model will be tested on a dataset that is different from the training dataset to test the robustness of the model.

 

Deliverables

	
- Well commented Jupyter notebook
	
- 'submissions.csv'

 

Annotate the notebook with markdowns and explain necessary inferences. A person should be able to read the notebook and understand the steps taken as well as the reasoning behind them.

 

Schema

 

	
		
		
		
	
	
		
			
			
Field

			
			
			
type

			
			
			
Description

			
		
		
			
			
feat_0

			
			
			
float

			
			
			
Feature 0

			
		
		
			 feat_1
			 float
			 Feature 1
		
		
			 feat_2
			 float
			 Feature 2

		
		
			 feat_3
			 float
			 Feature 3

		
		
			 feat_4
			 float
			
			
Feature 4

			
		
		
			 label

			 int

			 Label

## Preview

Given a dataset containing numerical and categorical values and corresponding
