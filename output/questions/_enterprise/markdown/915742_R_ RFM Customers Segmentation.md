# R: RFM Customers Segmentation

## Metadata

- **ID:** 915742
- **Type:** code
- **Difficulty:** 8.055555555555555
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Data Analysis, R, Medium
- **Skills:** R (Intermediate)
- **Languages:** r

## Summary

This coding question evaluates data analysis, R programming, and customer segmentation concepts, ideal for mid-level roles. The problem requires creating a dataset for customer segmentation using the RFM method based on a given retail dataset.

## Problem Statement

Given a dataset from a retail company, your task is to create a new dataset for customer segmentation using the RFM method.

The RFM method includes three dimensions:

	
- 
Recency: How recently did a customer make a purchase?
	
- 
Frequency: How often does the customer make purchases?
	
- 
Monetary: How much does the customer spend?

The original dataset contains three columns: "customer", "date", and "revenue". Your task is to create a table with the "customer" as the key column and six additional columns:

	
- 
Recency: "days_between_first_last_orders" - the number of days between the first and last order of the customer.
	
- 
Frequency: "count_orders_all" - the total number of orders placed by the customer.
	
- 
Frequency: "count_orders_last_120_days" - the total number of orders placed by the customer in the last 120 days.
	
- 
Monetary: "sum_revenue_all" - the total amount of money spent by the customer.
	
- 
Monetary: "sum_revenue_last_120_days" - the total amount of money spent by the customer in the last 120 days.
	
- 
Monetary: "mean_revenue_all" - the average amount of money spent by the customer.

The data should be sorted by customer name in alphabetical order, and all numeric columns should be rounded to the nearest integer.

 

Function Description

Complete the function prepare_data_for_customers_segmentation in the editor with the following parameter(s):

    df_data:  data frame data from a CSV file

 

Constraints

	
- Each data frame consists of at most 1000 rows.
	
- Do not make any assumptions beyond the problem statement.

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains a header of data sets with column names "customer", "date", and "revenue". Other lines have data about orders by customers.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

"customer","date","revenue"
"FIDELITY SOUTHERN CORPORATION","2017-08-11",411
"FIDELITY SOUTHERN CORPORATION","2018-06-01",910
"FIDELITY SOUTHERN CORPORATION","2018-07-03",887.2
"GREAT SOUTHERN BANCORP, INC.","2017-09-05",1111.4
"GREAT SOUTHERN BANCORP, INC.","2017-07-13",549.4
"GREAT SOUTHERN BANCORP, INC.","2017-07-20",179.6
"GREAT SOUTHERN BANCORP, INC.","2017-11-28",897.3
"OAK RIDGE FINANCIAL SERVICES, INC.","2017-11-16",618
"OAK RIDGE FINANCIAL SERVICES, INC.","2017-07-14",917.8
"OAK RIDGE FINANCIAL SERVICES, INC.","2017-07-12",1279.8
"OAK RIDGE FINANCIAL SERVICES, INC.","2017-08-29",1700.9
"OAK RIDGE FINANCIAL SERVICES, INC.","2017-08-21",377.2
```

Sample Output

"customer","date_last_purchase","date_range","count_orders_all","count_orders_2018","sum_revenue_all","sum_revenue_2018"
"FIDELITY SOUTHERN CORPORATION","2018-07-03",326,3,2,2208.2,1797.2
"GREAT SOUTHERN BANCORP, INC.","2017-11-28",138,4,0,2737.7,0
"OAK RIDGE FINANCIAL SERVICES, INC.","2017-11-16",127,5,0,4893.7,0

```

Explanation

Process data according to the problem statement.

Sample Case 1

Sample Input For Custom Testing

"customer","date","revenue"
"BLACKBAUD, INC.","2018-07-03",186.1
"BLACKBAUD, INC.","2018-06-11",1847.1
"BLACKBAUD, INC.","2018-07-03",762
"BLACKBAUD, INC.","2018-07-17",855.7
"BLACKBAUD, INC.","2018-07-13",2741
"FIDELITY SOUTHERN CORPORATION","2017-08-11",411
"FIDELITY SOUTHERN CORPORATION","2018-06-01",910
"FIDELITY SOUTHERN CORPORATION","2018-07-03",887.2
"GREAT SOUTHERN BANCORP, INC.","2017-09-05",1111.4
"GREAT SOUTHERN BANCORP, INC.","2017-07-13",549.4
"GREAT SOUTHERN BANCORP, INC.","2017-07-20",179.6
"GREAT SOUTHERN BANCORP, INC.","2017-11-28",897.3
"LEXICON PHARMACEUTICALS, INC.","2018-04-02",3311.4
"LEXICON PHARMACEUTICALS, INC.","2018-04-11",5715.3
"LEXICON PHARMACEUTICALS, INC.","2018-07-25",708.4
"OAK RIDGE FINANCIAL SERVICES, INC.","2017-11-16",618
"OAK RIDGE FINANCIAL SERVICES, INC.","2017-07-14",917.8
"OAK RIDGE FINANCIAL SERVICES, INC.","2017-07-12",1279.8
"OAK RIDGE FINANCIAL SERVICES, INC.","2017-08-29",1700.9
"OAK RIDGE FINANCIAL SERVICES, INC.","2017-08-21",377.2

```

Sample Output

"customer","date_last_purchase","date_range","count_orders_all","count_orders_2018","sum_revenue_all","sum_revenue_2018"
"BLACKBAUD, INC.","2018-07-17",36,5,5,6391.9,6391.9
"FIDELITY SOUTHERN CORPORATION","2018-07-03",326,3,2,2208.2,1797.2
"GREAT SOUTHERN BANCORP, INC.","2017-11-28",138,4,0,2737.7,0
"LEXICON PHARMACEUTICALS, INC.","2018-07-25",114,3,3,9735.1,9735.1
"OAK RIDGE FINANCIAL SERVICES, INC.","2017-11-16",127,5,0,4893.7,0

```

Explanation

Process data according to the problem statement.

## Sample Input/Output

## Preview

Given a dataset from a retail company, your task is to create a new dataset fo
