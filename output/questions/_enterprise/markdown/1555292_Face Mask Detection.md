# Face Mask Detection

## Metadata

- **ID:** 1555292
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** PyTorch, Python, Deep Learning, Computer Vision, Neural Networks, Keras, Easy, TensorFlow
- **Skills:** Computer Vision (Basic)

## Summary

This data science question evaluates computer vision, deep learning, and model evaluation concepts, ideal for junior-level roles. The problem requires building a deep neural network to identify subjects wearing face masks from a dataset of images.

## Problem Statement

There is a dataset of photos of subjects, with some wearing face masks. Build a deep neural network to identify which subjects are wearing face masks.

 

Datasets

	
- 
	
"train.csv" - data used to train the model

	
	
- 
	
"train_images" - folder containing images to use for training

	
	
- 
	
"test.csv" – data used for prediction

	
	
- 
	
"test_images" - folder containing images to use for prediction

	
	
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

			
		
		
			
			
label

			
			
			
int

			
			
			
Whether the subject is wearing a face mask (1) or not (0)

			
		
	

 

Predictive Modeling and Model Evaluation

Build a neural network to identify whether the subjects are wearing masks.

Experiment with different preprocessing methods, number of layers, types of layers, activation functions, and any other relevant parameters. Compile the model by specifying the loss function and optimizer. Ensure that the model is not overfitting.

Assess model performance on "train.csv" using the "Accuracy Score“ metric. Information about the metric is here.

The model will be tested for robustness using a different dataset.

Submission

For each record in the test set (test.csv), predict the value of the 'label' variable. Submit a CSV file with a header row and one row per test entry. The file (submissions.csv) should have exactly 2 columns:

	
- file_name
	
- label (0/1)

 

Test Evaluation

The score will be automatically determined based on the accuracy metric for the “submissions.csv” file. Get the best possible value of the metric during model development. The reviewer might dive deeper into the Jupyter notebook to get more context.

## Preview

There is a dataset of photos of subjects, with some wearing face masks. Build a
