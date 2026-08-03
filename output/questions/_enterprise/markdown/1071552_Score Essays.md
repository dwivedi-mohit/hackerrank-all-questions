# Score Essays

## Metadata

- **ID:** 1071552
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Deep Learning, NLP, PyTorch, Hard
- **Skills:** PyTorch

## Summary

This data science question evaluates deep learning, natural language processing, and model building concepts, ideal for senior-level roles. The problem requires building a deep neural network using PyTorch to predict essay scores based on a dataset.

## Problem Statement

HackerText is developing an automated language scorer. The scorer would be able to able to predict a score by analyzing the essay.

 

Given a dataset of essays and their corresponding scores on the scale of 1-5, build a deep neural network using PyTorch that can accurately predict the score of an essay.

 

Files

	
- train.csv
	
- test.csv
	
- sample_submission.csv

 

Problem

Build a neural network that can predict the score of the essay.

For each record in the test set (test.csv), predict the value of the 'score' variable. Submit a CSV file with a header row and one row per test entry. The file (submissions.csv) should have exactly 2 columns:

	
- content
	
- score (1 -5)

 

Evaluation Metric: The metric used for evaluating the performance of the model is MAPE (Mean Absolute Percent Error).

MAPE = Average of error between Predicted & Actual Score

 

The model will be tested on a different set of essays from the training set to test its robustness.

 

Deliverables

	
- Well commented Jupyter notebook
	
- 'submissions.csv'

 

Annotate the notebook with markdowns and explain necessary inferences. A person should be able to read the notebook and understand the steps taken as well as the reasoning behind them.

 

Schema

 

	
		
		
		
	
	
		
			
			
Field

			
			
			
type

			
			
			
Description

			
		
		
			
			
content

			
			
			
str

			
			
			
Content of the essay

			
		
		
			
			
score

			
			
			
int

			
			
			
The score of the essay (1-5)

## Preview

HackerText is developing an automated language scorer. The scorer would be abl
