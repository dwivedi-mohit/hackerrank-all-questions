# R: Calculate Mean Temperatures

## Metadata

- **ID:** 1595387
- **Type:** code
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Data Wrangling, Easy, Variable Creation, CSV, Date and time operations, Data Frames, R, Data Formatting
- **Skills:** R (Basic)
- **Languages:** r

## Summary

This coding question evaluates data wrangling, variable creation, and date and time operations concepts, ideal for junior-level roles. The problem requires loading a CSV file into a data frame, handling missing values, and calculating average temperatures for specified intervals.

## Problem Statement

A CSV file contains data on temperatures and energy consumption for various buildings. The data includes a building identifier, hourly outdoor temperature measurements, and daily energy consumption (daily_kWh).

 

Load the CSV file into a data frame and perform the following tasks:

	
- Replace any missing values in the energy consumption variable with the sample mean.
	
- Calculate the mean temperatures for 6-hour intervals for each observation:
	
		
- 
temp_morning: 00:00-05:59
		
- 
temp_midday: 06:00-11:59
		
- 
temp_afternoon: 12:00-17:59
		
- 
temp_night: 18:00-23:59
	
	
	
- Create a new data frame that includes only the building identifier, the four average temperatures, and the imputed energy consumption variable.

 

Function Description

Complete the function energy_building in the editor below.

 

The function has the following parameter:

    df_data:  file with data about buildings' energy consumption and outside temperature.

 

Returns

    data frame: the building identifier, the four average temperatures, and the imputed energy consumption variable

 

Constraints

	
- Use basic R functions.
	
- Consider using the dplyr package.

## Sample Input/Output

## Preview

A CSV file contains data on temperatures and energy consumption for various buil
