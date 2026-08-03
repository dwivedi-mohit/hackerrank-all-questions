# Identify Traffic Signs

## Metadata

- **ID:** 1100932
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Deep Learning, PyTorch, Hard
- **Skills:** PyTorch

## Summary

This data science question evaluates deep learning, PyTorch, and model building concepts, ideal for senior-level roles. The problem requires building a deep neural network to detect speed signs from images and predict their labels based on a provided dataset.

## Problem Statement

HackerCars is developing a self-driving car. As part of its automatic sensing system, they want the car to automatically detect the speed signs on the road and adjust its speed accordingly.

 

Given a dataset of images of speed signs and their corresponding labels, build a model using PyTorch that can detect if the speed sign is 30km/h, 70km/h, or 120km/h.

 

Files

	
- train.csv
	
- test.csv
	
- sample_submission.csv

 

 

Problem

Build a deep neural network that can identify the traffic speed sign.

 

For each record in the test set (test.csv), predict the value of the 'label' variable. Submit a CSV file with a header row and one row per test entry. The file (submissions.csv) should have exactly 2 columns:

	
- path
	
- label (0 - 30km/h, 1 - 70km/h, 2 - 120km/h)

 

Evaluation Metric:

The metric used for evaluating the performance of the model is Accuracy:

Accuracy = (Correct Predictions)/(Total No. of predictions made)

 

Deliverables

	
- Well commented Jupyter notebook
	
- 'submissions.csv'

 

The notebook should contain your solution, visualizations, and thought process, including the top features that go into the model. If required, please generate new features. Make appropriate plots, annotate the notebook with markdowns, and explain the necessary inferences. A person should be able to read your notebook and understand the steps are you taking and the reasoning behind them.

 

Schema

 

	
		
		
		
	
	
		
			
			
Field

			
			
			
type

			
			
			
Description

			
		
		
			
			
path

			
			
			
str

			
			
			
path of the image

			
		
		
			
			
label

			
			
			
int

			
			
			
Label of the sign

			
(0 - 30km/h, 1 - 70km/h, 2 - 120hm/h)

## Preview

HackerCars is developing a self-driving car. As part of its automatic sensing
