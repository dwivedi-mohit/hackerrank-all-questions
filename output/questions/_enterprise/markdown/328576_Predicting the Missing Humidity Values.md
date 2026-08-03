# Predicting the Missing Humidity Values

## Metadata

- **ID:** 328576
- **Type:** approx
- **Difficulty:** 9.444444444444445
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Machine Learning, Regression, Statistics, Forecasting, Medium, Problem Solving, Data Structures, Data Analysis, Time Series
- **Skills:** Data Modeling
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This approximate solution question evaluates data modeling, regression, and time series concepts, ideal for mid-level roles. The problem requires predicting hourly humidity data for specified timestamps based on known humidity data.

## Problem Statement

Use m timestamps of humidity data to predict n unknown timestamps of humidity data.

Given humidity data for the days spanning from startDate to endDate inclusive, predict the hourly humidity data for each of the timestamps in timestamps.

 

Function Description 

Complete the function predictMissingHumidity in the editor below. The function must return an array of floating-point numbers where the value at each index i denotes the humidity at timestamps[i].

 

predictMissingHumidity has the following parameter(s):

    startDate:  string, The first day of humidity data in the format yyyy-mm-dd.

    endDate:  string, The last day of humidity data in the format yyyy-mm-dd.

    knownTimestamps[knownTimestamps[0],...knownTimestamps[m-1]]:  an array of strings of timestamps in the format yyyy-mm-dd hh:00.

    humidity[humidity[0],...humidity[m-1]]:  an array of floating-point numbers representing humidity[i] occurring at knownTimestamps[i].

    timestamps[timestamps[0],...timestamps[n-1]]:  an array of strings of timestamps to predict for in the format yyyy-mm-dd hh:00.

predictMissingHumidity function in the editor below. It has the following five parameters:

	
		
			Name
			Type
			Description
		
		
			startDate
			string
			The first day of humidity data in the format yyyy-mm-dd.
		
		
			endDate
			string
			The last day of humidity data in the format yyyy-mm-dd.
		
		
			knownTimestamps
			string array
			Each knownTimestampsi (where 0 &le; i < m) denotes a yyyy-mm-dd hh:00 timestamp in the inclusive range from startDate to endDate that we have humidity data for.
		
		
			humidity
			floating-point array
			Each humidityi (where 0 &le; i < m) denotes the humidity at time knownTimestampsi.
		
		
			timestamps
			string array
			Each timestampsj (where 0 &le; j < n) denotes a yyyy-mm-dd hh:00 timestamp in the inclusive range from startDate to endDate that we need to predict humidity data for.
		
	

-->
	
- A string, startDate, in the format yyyy-mm-dd denoting the first day of humidity data.
	
- A string, endDate, in the format yyyy-mm-dd denoting the last day of humidity data.
	
- An array of m strings, knownTimestamps, where each knownTimestampsi denotes a yyyy-mm-dd hh:00 timestamp in the inclusive range from startDate to endDate that we have humidity data for.
	
- An array of m floating-point numbers, humidity, where each humidityi denotes the humidity at time knownTimestampsi.
	
- An array of n strings, timestamps, where each timestampsi denotes a yyyy-mm-dd hh:00 timestamp in the inclusive range from startDate to endDate that we need to predict humidity data for.

 

The function must return an array of n floating-point numbers where the value at each index i denotes the humidity at timestamp timestampsi.

-->

 

Constraints

	
- 2013-01-01 ≤ startDate ≤ endDate ≤ 2015-01-01
	
- 1 ≤ m ≤ 3476
	
- 1 ≤ n ≤ 915

 

 DO NOT REMOVE THIS LINE-->

Input Format for Custom Testing

Input from stdin will be processed as follows and passed to the function.

 

The first line contains a string, startDate.

The second line contains a string, endDate.

The third line contains an integer, m, the number of elements in the array knownTimestamps.

Each of the next m lines contains a string describing knownTimestamps[i].

The next line contains an integer, m, the number of elements in the array humidity.

Each of the next m lines contains a floating-point number describing humidity[i].

The next line contains an integer, n, the number of elements in timestamps.

Each of the next n lines contains contains a string describing timestamps[j].

 

	
- The first line contains a string, startDate, denoting the start date of the given humidity data in the format yyyy-mm-dd.
	
- The second line contains a string, endDate, denoting the end date of the given humidity data in the format yyyy-mm-dd.
	
- The third line contains an integer, m, denoting the total number of elements in knownTimestamps.
	
- Each line i of the m subsequent lines (where 0 &le; i < m) contains a string describing knownTimestampsi.
	
- The next line contains an integer, m, denoting the total number of elements in humidity.
	
- Each line i of the m subsequent lines (where 0 &le; i < m) contains a floating-point number describing humidityi.
	
- The next line contains an integer, n, denoting the number of elements in timestamps.
	
- Each line j of the n subsequent lines (where 0 &le; i < n) contains a string describing timestampsi.

Output Format

Return an array of n floating-point numbers where the value at each index i denotes the humidity at timestamp timestampsi.

-->

Evaluation

	
- The predicted humidity at a timestamp is considered to be correct if the absolute difference between the actual and predicted humidities is not greater than 0.25.
	
- The accuracy of the prediction is defined as: (Total number of correct predictions)⁄(n).
	
- The score for each test case is calculated as: accuracy × (test case weight).
	
- The final score is the sum of all test case scores.

 

Sample Case 0

Sample Input 0

2013-01-01
2013-01-01
19
2013-01-01 00:00
2013-01-01 01:00
2013-01-01 02:00
2013-01-01 03:00
2013-01-01 04:00
2013-01-01 05:00
2013-01-01 06:00
2013-01-01 08:00
2013-01-01 10:00
2013-01-01 11:00
2013-01-01 12:00
2013-01-01 13:00
2013-01-01 16:00
2013-01-01 17:00
2013-01-01 18:00
2013-01-01 19:00
2013-01-01 20:00
2013-01-01 21:00
2013-01-01 23:00
19
0.62
0.64
0.62
0.63
0.63
0.64
0.63
0.64
0.48
0.46
0.45
0.44
0.46
0.47
0.48
0.49
0.51
0.52
0.52
5
2013-01-01 07:00
2013-01-01 09:00
2013-01-01 14:00
2013-01-01 15:00
2013-01-01 22:00

```

Expected Output 0

0.64
0.55
0.44
0.44
0.52

```

Sample Output 0

0.1
0.2
0.3
0.4
0.5

```

 

Explanation 0

Given the m = 19 hours of humidity data on 2013-01-01, the task is to predict n = 5 hours of missing humidity data for the timestamps in timestamps. The table below depicts sample predictions for the given humidity data that contains a total of 3 correct predictions. The accuracy of these predictions is 3/5 = 0.60 and, because the test case weight is 5, the total score for this test case is 0.60 × 5 = 3.

	
		
			HUMIDITY
		
		
			Timestamp
			Humidity
			Predicted Humidity
			Humidity Difference
			Correct Prediction?
		
		
			2013-01-01 07:00
			0.64
			0.1
			0.54
			Incorrect
		
		
			2013-01-01 09:00
			0.55
			0.2
			0.35
			Incorrect
		
		
			2013-01-01 14:00
			0.44
			0.3
			0.14
			Correct
		
		
			2013-01-01 15:00
			0.44
			0.4
			0.04
			Correct
		
		
			2013-01-01 22:00
			0.52
			0.5
			0.02
			Correct

## Sample Input/Output

## Preview

Use m timestamps of humidity data to predict n unknown timestamps of humidity
