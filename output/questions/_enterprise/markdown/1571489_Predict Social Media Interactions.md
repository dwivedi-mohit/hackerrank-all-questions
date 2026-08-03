# Predict Social Media Interactions

## Metadata

- **ID:** 1571489
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Medium, PyTorch, Python, Deep Learning, Computer Vision, Neural Networks, Keras, TensorFlow
- **Skills:** Computer Vision (Intermediate)

## Summary

This data science question evaluates computer vision, neural networks, and predictive modeling concepts, ideal for mid-level roles. The task involves building a neural network to predict user interactions on uploaded photos using a provided dataset.

## Problem Statement

A popular photo-sharing platform allows users to upload photos, and other users can interact with them. The more users interact with a photo, the more it is promoted to other users. Given a dataset of photos uploaded by users and their corresponding normalized interactions, on a scale of 0-10, with 10 being the highest, build a neural network that can predict user interactions for each uploaded photo.

 

Datasets

	
- 
	
"train.csv" - data used to train the model

	
	
- 
	
"train_images" - folder containing images to use for training

	
	
- 
	
"test.csv" – data used for prediction

	
	
- 
	
"test_images" - folder containing images to use for prediction

	
	
- 
	
"submissions.csv" – populate this file with the results

	
	
- 
	
"sample_submission.csv" – sample submission file for reference

	

 

Schema

	
		
			
			
Field

			
			
			
type

			
			
			
Description

			
		
		
			
			
file_name

			
			
			
str

			
			
			
file path

			
		
		
			
			
interactions

			
			
			
float

			
			
			
normalized user's interactions on the platform (0-10) (The higher the better)

			
		
	

 

Predictive Modeling and Model Evaluation

Build a neural network to predict user interactions on the uploaded pictures.

Experiment with different preprocessing methods, numbers and types of layers, activation functions, and any other relevant parameters. Compile the model by specifying the loss function and optimizer. Ensure that the model does not overfit.

Assess model performance on "train.csv" using the "Mean Absolute Percent Error (MAPE)“ metric. Information about the metric is here.

The model will be tested for robustness using a different dataset.

Submission

For each record in the test set (test.csv), predict the value of the 'interactions' variable. Submit a CSV file with a header row and one row per test entry. The file (submissions.csv) should have exactly 2 columns:

	
- file_name
	
- interactions (0-10)

 

Test Evaluation

The score will be automatically evaluated based on the MAPE metric for the “submissions.csv” file. Get the best possible value of the metric during model development. The reviewer might dive deeper into the Jupyter notebook to get more context.

## Preview

A popular photo-sharing platform allows users to upload photos, and other users
