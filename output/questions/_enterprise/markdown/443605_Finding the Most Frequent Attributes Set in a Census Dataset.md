# Finding the Most Frequent Attributes Set in a Census Dataset

## Metadata

- **ID:** 443605
- **Type:** approx
- **Difficulty:** 9.722222222222221
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Machine Learning, Algorithms, Medium, Problem Solving, Data Structures, Data Search, Pattern Recognition
- **Skills:** Problem Solving (Intermediate)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This approximate solution question evaluates attribute patterns, support thresholds, and data analysis concepts, ideal for mid-level roles. The problem requires identifying significant attribute patterns in census data based on specified criteria.

## Problem Statement

Introduction

The file census.csv contains census data for 30162 individuals. Each row represents one person, with a comma-separated list of attribute–value pairs describing their characteristics.

 

First ten rows from census.csv

age=Middle-aged,sex=Male,education=Bachelors,native-country=United-States,race=White,marital-status=Never-married,workclass=State-gov,occupation=Adm-clerical,hours-per-week=Full-time,income=Small,capital-gain=Low,capital-loss=None
age=Senior,sex=Male,education=Bachelors,native-country=United-States,race=White,marital-status=Married-civ-spouse,workclass=Self-emp-not-inc,occupation=Exec-managerial,hours-per-week=Part-time,income=Small,capital-gain=None,capital-loss=None
age=Middle-aged,sex=Male,education=HS-grad,native-country=United-States,race=White,marital-status=Divorced,workclass=Private,occupation=Handlers-cleaners,hours-per-week=Full-time,income=Small,capital-gain=None,capital-loss=None
age=Senior,sex=Male,education=11th,native-country=United-States,race=Black,marital-status=Married-civ-spouse,workclass=Private,occupation=Handlers-cleaners,hours-per-week=Full-time,income=Small,capital-gain=None,capital-loss=None
age=Middle-aged,sex=Female,education=Bachelors,native-country=Cuba,race=Black,marital-status=Married-civ-spouse,workclass=Private,occupation=Prof-specialty,hours-per-week=Full-time,income=Small,capital-gain=None,capital-loss=None
age=Middle-aged,sex=Female,education=Masters,native-country=United-States,race=White,marital-status=Married-civ-spouse,workclass=Private,occupation=Exec-managerial,hours-per-week=Full-time,income=Small,capital-gain=None,capital-loss=None
age=Senior,sex=Female,education=9th,native-country=Jamaica,race=Black,marital-status=Married-spouse-absent,workclass=Private,occupation=Other-service,hours-per-week=Part-time,income=Small,capital-gain=None,capital-loss=None
age=Senior,sex=Male,education=HS-grad,native-country=United-States,race=White,marital-status=Married-civ-spouse,workclass=Self-emp-not-inc,occupation=Exec-managerial,hours-per-week=Over-time,income=Large,capital-gain=None,capital-loss=None
age=Middle-aged,sex=Female,education=Masters,native-country=United-States,race=White,marital-status=Never-married,workclass=Private,occupation=Prof-specialty,hours-per-week=Over-time,income=Large,capital-gain=High,capital-loss=None
age=Middle-aged,sex=Male,education=Bachelors,native-country=United-States,race=White,marital-status=Married-civ-spouse,workclass=Private,occupation=Exec-managerial,hours-per-week=Full-time,income=Large,capital-gain=Low,capital-loss=None
```

Use this data to find “significant attribute patterns” within the dataset.

An “attribute pattern” is defined as a set of at least two attributes whose values are repeated across multiple individuals. An attribute pattern is “significant” if it occurs in a percentage of individuals greater than or equal to a specified support threshold (e.g., the attribute pattern must apply to at least 50% of people in the dataset).

Your task: Given the dataset, the number of attributes that must make up a pattern, and the minimum support threshold, return all unique attribute sets that qualify as significant.

Each pattern should be represented as a comma-separated string with the format attribute=value. The order of attributes within a pattern does not matter, and the order of the returned patterns does not matter either. However, every attribute and value must exactly match those present in the dataset.

Example 1

(Using only the 10 rows of data above)

numberOfAttributes = 2, supportThreshold = 0.7

The following two attribute sets meet the constraints:

	
- 
`{capital-gain=None, capital-loss=None}` occurs for 7 out of 10 individuals → 7/10 = 0.7 (meets threshold)
	
- 
`{native-country=United-States, capital-loss=None}` occurs for 8 out of 10 individuals → 8/10 = 0.8 (exceeds threshold)

Therefore, either of the following is considered a correct answer:

`capital-gain=None,capital-loss=None
native-country=United-States,capital-loss=None
`
```

`native-country=United-States,capital-loss=None
capital-loss=None,capital-gain=None
`
```

Constraints

	
- 1 ≤ numberOfAttributes ≤ 12
	
- 0.1 ≤ supportThreshold ≤ 1.0

 

 DO NOT REMOVE THIS LINE-->

Test Case Input Format

Input from stdin will be processed as follows and passed to the function.

 

The first line contains an integer numberOfAttributes.

The next line contains a floating point value supportThreshold

## Sample Input/Output

## Preview

Introduction
