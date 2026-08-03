# Website Traffic Analysis

## Metadata

- **ID:** 1137693
- **Type:** database
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Pivot, Windowing, SQL, Hard, Database, Interviewer Guidelines
- **Skills:** SQL (Advanced)
- **Languages:** m, y, s, q, l, ,, o, r, a, c

## Summary

This database question evaluates SQL, pivot tables, and window functions concepts, ideal for senior-level roles. The problem requires creating a query to return monthly median traffic data for a website over four years.

## Problem Statement

Traffic on a website was recorded on multiple days over 4 years, 2017-2020.

 

Create a query that returns a row for each month, with the month number and the ceiling of the median for that month in 2017, 2018, 2019, and 2020. Order the results by month.

 

Note: Check the sample output below for the correct output format.

 

Schema

There is 1 table: `traffic`.

	
		
			traffic
		
		
			Name
			Type
			Description
		
		
			id
			int
			the unique id
		
		
			record_day
			date
			the date the traffic was recorded
		
		
			count
			int
			the number of visitors to the website.
		
	

Sample Data Tables

	
		
			traffic
		
		
			id
			record_day
			count
		
		
			8949
			2017-01-01
			7735
		
		
			3618
			2017-01-06
			9701
		
		
			6655
			2017-01-13
			2073
		
		
			5781
			2017-01-19
			4035
		
		
			7183
			2017-01-26
			3314
		
		
			9735
			2018-01-07
			5536
		
		
			8906
			2018-01-12
			6202
		
		
			2349
			2018-01-18
			6892
		
		
			8514
			2018-01-25
			4810
		
		
			6836
			2018-01-31
			5792
		
		
			8279
			2019-01-07
			4742
		
		
			1149
			2019-01-14
			1655
		
		
			8277
			2019-01-19
			6444
		
		
			3104
			2019-01-25
			2786
		
		
			3362
			2019-01-31
			2594
		
		
			3667
			2020-01-02
			5000
		
		
			2373
			2020-01-08
			6754
		
		
			5900
			2020-01-15
			4994
		
		
			2038
			2020-01-22
			1038
		
		
			8390
			2020-01-29
			1245
		
	

 

	
		
			OUTPUT
		
		
			month
			2017
			2018
			2019
			2020
		
		
			1
			4035
			5792
			2786
			4994
		
	

 

Explanation

 

In January, 2017, traffic was [7735, 9701, 2073, 4035, 3314]. Sorted, the traffic is [2073, 3314, 4035, 7735, 9701].

## Sample Input/Output

## Preview

Traffic on a website was recorded on multiple days over 4 years, 2017-2020.
