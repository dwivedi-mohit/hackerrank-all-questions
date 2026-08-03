# Predict Star Type

## Metadata

- **ID:** 1334682
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Machine Learning, Data Wrangling, Data Visualization, Data Modeling, Classification
- **Skills:** Data Modeling, Data Visualization, Data Wrangling, Machine Learning

## Summary

This data science question evaluates data modeling, data visualization, and machine learning concepts, ideal for mid-level roles. The problem requires developing a machine-learning model to predict whether a star will become a pulsar based on various characteristics.

## Problem Statement

Given a dataset of various characteristics of radiation emitted by stars, develop a machine-learning model to predict whether a star will become a pulsar or not.

 

Files

	
- train.csv
	
- test.csv
	
- sample_submission.csv

 

 

Problem

Build a machine learning model which can be used to predict the ‘outcome' attribute.

 

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

 

	
		
		
		
	
	
		
			
			
Feature

			
			
			
Type

			
			
			
Description

			
		
		
			
			
id

			
			
			
Integer

			
			
			
Unique ID of the star

			
		
		
			
			
mean_sd

			
			
			
Float

			
			
			
Mean and standard deviation of the integrated spectrum of rays emitted by the star

			
		
		
			
			
excess_kurtosis

			
			
			
Float

			
			
			
Excess kurtosis of the integrated spectrum

			
		
		
			
			
skewness

			
			
			
Float

			
			
			
Skewness of the integrated spectrum

			
		
		
			
			
mean_sd_snr

			
			
			
Float

			
			
			
Mean and standard deviation of the signal-to-noise ratio curve of the spectrum of rays emitted

			
		
		
			
			
excess_kurtosis_snr

			
			
			
Float

			
			
			
Excess kurtosis of the signal-to-noise ratio curve of the spectrum

			
		
		
			
			
skewness_snr

			
			
			
Float

			
			
			
Skewness of the signal-to-noise ratio curve of the spectrum

			
		
		
			
			
outcome

			
			
			
Categorical

			
			
			
Whether the star is a pulsar (1 - Yes, 0 - No)

## Preview

Given a dataset of various characteristics of radiation emitted by stars, deve
