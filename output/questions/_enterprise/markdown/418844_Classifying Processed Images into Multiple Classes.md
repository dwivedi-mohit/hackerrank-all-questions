# Classifying Processed Images into Multiple Classes

## Metadata

- **ID:** 418844
- **Type:** approx
- **Difficulty:** 6.944444444444445
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Machine Learning, Algorithms, Hard, Multilabel Classification, Multiclass Classification, Problem Solving
- **Skills:** Machine Learning
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This approximate solution question evaluates machine learning, multilabel classification, and problem-solving concepts, ideal for senior-level roles. The task requires building a model to predict scene presence in unseen image data based on provided attributes.

## Problem Statement

Introduction

We have processed images to represent as a vector of 300 attributes. The first 294 are decimal values in the range 0 to 1 inclusive. The next six are binary values describing whether the image had a beach, a sunset, plants, a field, mountains, and buildings respectively. A value of 1 describes that the scene was present and 0 means it was not. For example:

 

	
- The vector <0.01,…,0.1,…,0.25,…,1,0,0,0,1,0> describes an image with a beach and mountains before processing.
	
- The vector <0.01,…,0.1,…,0.25,…,0,1,1,0,0,1> describes an image with a sunset, plants, and buildings before processing.
	
- The vector <0.01,…,0.1,…,0.25,…,0,0,0,1,0,0> describes an image with only a field before processing.

 

Note

The data provided is not based on the real images, so you should not try generating images from the dataset. You should build the training model using the given dataset only.

 

Task

You are given 1438 processed image data instances, the training dataset. Build a model to predict how many scenes were present in 966 unseen processed image data instances in the testing dataset.

 

Dataset

You are provided the training dataset in the file train.csv. The file contains 1438 rows. Each row contains 300 comma-separated values. You are also provided the testing dataset in the file test.csv. The file contains 966 rows of 294 comma-separated values that desribe the attributes values.

 

Submission Details

Write the code to build a model to predict how many types of scenes were present in the image before processing. The code must save the predictions to the file prediction.csv, which contains exactly 966 rows with no header. Each row should contain six comma-separated binary values that correspond to the attribute values provided in the test.csv file.

 

Note that:

	
- The training and testing files are available in the current working directory and can be downloaded at the links in the problem statement.
	
- Neither of the files has a header row.
	
- The prediction.csv file should not have a header row.

 

Evaluation

The prediction accuracy of the model is calculated using accuracy score:

	
- Expected = ["0,0,0,0,1,1", "1,0,0,1,0,0", "0,0,0,0,0,1", "1,0,0,0,0,0", "0,1,0,0,1,0"]
	
- Predicted = ["0,0,0,0,1,1", "1,0,1,0,0,1", "0,0,0,0,0,1", "1,0,0,0,0,0", "0,0,0,0,0,0"]
	
- Correct Prediction = ["Yes", "No", "Yes", "Yes", "No"]

The correct number of predictions is 3, so the accuracy score is 3⁄5 = 0.6

## Sample Input/Output

## Preview

Introduction
