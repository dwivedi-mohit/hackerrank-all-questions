# Detect Parking Signs

## Metadata

- **ID:** 1002897
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Deep Learning, Hard, TensorFlow
- **Skills:** TensorFlow

## Summary

This data science question evaluates deep learning, TensorFlow, and model evaluation concepts, ideal for senior-level roles. The problem requires building a deep neural network to detect parking signs in images and predict their bounding box coordinates using a provided dataset.

## Problem Statement

HackerRoads company is building a next-gen driver assistance system. One of its key features will be parking assistance. It will inform drivers where they are legally allowed to park. Given a dataset of 2D images of labeled parking signs, build a deep neural network using TensorFlow that can detect the position of parking signs in the image.

 

 

 

 

Files

	
- train.csv
	
- test.csv
	
- sample_submission.csv

 

Problem

Build a deep neural network that can detect the coordinates of parking signs in the images.

 

For each record in the test set (test.csv), predict the coordinates of the bounding box for the parking sign. Submit a CSV file with a header row and one row per test entry. The file (submissions.csv) should have exactly 5 columns:

	
- image_id
	
- x_min
	
- y_min
	
- x_max
	
- y_max

 

Evaluation Metric:

The metric used for evaluating the performance of the model is IoU (Intersection Over Union).

IoU= The IoU is defined as the area of the intersection divided by the area of the union of a predicted bounding box (B) to a ground-truth box (B).

 

    

 

Deliverables

	
- Well commented Jupyter notebook
	
- 'submissions.csv'

The notebook should contain your solution, visualizations, and thought process, including the top features that go into the model. If required, please generate new features. Make appropriate plots, annotate the notebook with markdowns, and explain the necessary inferences. A person should be able to read your notebook and understand the steps are you taking and the reasoning behind them.

 

Schema

 

	
		
		
		
	
	
		
			
			
Field

			
			
			
type

			
			
			
Description

			
		
		
			
			
image_id

			
			
			
int

			
			
			
unique id of the image

			
		
		
			
			
image_path

			
			
			
str

			
			
			
path of the image in the local directory

			
		
		
			
			
x_min

			
			
			
str

			
			
			
x-coordinate of the left side of the bounding box

			
		
		
			
			
y_min

			
			
			
str

			
			
			
y-coordinate of the bottom side of the bounding box

			
		
		
			
			
x_max

			
			
			
int

			
			
			
x-coordinate of the right side of the bounding box

			
		
		
			
			
y_max

			
			
			
str

			
			
			
y-coordinate of the top side of the bounding box

## Preview

HackerRoads company is building a next-gen driver assistance system. One of it
