# e-Commerce Highest Customer Revenue

## Metadata

- **ID:** 1980300
- **Type:** database
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Medium, Windowing, SQL, Aggregation, Database, Interviewer Guidelines
- **Skills:** SQL (Advanced)
- **Languages:** m, y, s, q, l, ,, o, r, a, c

## Summary

This database question evaluates SQL, aggregation, and windowing concepts, ideal for senior-level roles. The problem requires identifying the customer who generated the most revenue during July 2021 based on various transaction types and statuses.

## Problem Statement

As part of HackerMart's e-commerce marketing analytics, they need to find the customer who generated the most revenue for them during July, 2021. Revenue from a customer is the sum of the values described below.

	
- type=BUY, the customer purchased something, the transaction amount is potential revenue
	
- type=SELL, the customer sold something, HackerMart collects a fee, 10% of the transaction amount is potential revenue

 

Status determines how a transaction is treated.

	
- status = COMPLETED, the transaction is included
	
- status = PENDING, the transaction is ignored
	
- status = CANCELED, the transaction is void, 1% of the transaction amount is deducted from total revenue

 

Columns to report are customer, buy, sell, completed, pending, canceled, total. buy, sell, completed, pending, and canceled are the number of transactions that match, and total is the total revenue, calculated as described and rounded to 2 places after the decimal. Include trailing zeros if necessary, e.g., 10 is shown as 10.00.

 

Schema

 

There is 1 table:

 

	
		
			transactions
		
		
			name
			type
			description
		
		
			dt
			VARCHAR(19)
			Transaction timestamp
		
		
			customer
			VARCHAR(64)
			Customer email address
		
		
			type
			VARCHAR(4)
			Transaction type
		
		
			amount
			DECIMAL(5,2)
			Transaction amount
		
		
			status
			VARCHAR(9)
			Transaction status
		
	

 

Sample Data Tables

 

For the sample data in table:

 

	
		
			transactions
		
		
			dt
			customer
			type
			amount
			status
		
		
			2021-07-18 03:13:37
			stapenden1@google.de
			BUY
			95.90
			COMPLETED
		
		
			2021-07-09 09:56:13
			jpeddersen6@virginia.edu
			BUY
			34.37
			CANCELED
		
		
			2021-07-13 01:12:15
			rclaypole0@qq.com
			BUY
			79.27
			COMPLETED
		
		
			2021-07-05 02:12:53
			asmithin4@elegantthemes.com
			SELL
			23.80
			PENDING
		
		
			2021-06-21 13:50:29
			bhaddeston2@mapquest.com
			BUY
			89.55
			COMPLETED
		
		
			2021-06-28 08:09:02
			cpalek8@yahoo.com
			SELL
			64.45
			CANCELED
		
		
			2021-07-23 07:07:29
			rclaypole0@qq.com
			BUY
			19.92
			COMPLETED
		
		
			2021-07-03 15:20:54
			rclaypole0@qq.com
			SELL
			51.30
			COMPLETED
		
		
			2021-07-13 18:05:55
			stapenden1@google.de
			SELL
			86.29
			COMPLETED
		
		
			2021-07-04 13:29:23
			bhaddeston2@mapquest.com
			BUY
			22.60
			PENDING
		
		
			2021-07-02 14:23:28
			bhaddeston2@mapquest.com
			BUY
			38.67
			COMPLETED
		
		
			2021-07-04 00:40:09
			bhaddeston2@mapquest.com
			BUY
			59.78
			CANCELED
		
		
			2021-06-27 13:41:43
			stapenden1@google.de
			SELL
			61.14
			PENDING
		
		
			2021-07-06 22:06:30
			rclaypole0@qq.com
			BUY
			18.39
			PENDING
		
		
			2021-07-31 16:13:40
			rclaypole0@qq.com
			SELL
			24.42
			PENDING
		
		
			2021-07-18 10:44:42
			rclaypole0@qq.com
			SELL
			55.57
			CANCELED
		
		
			2021-07-02 19:47:33
			rclaypole0@qq.com
			SELL
			51.54
			COMPLETED
		
		
			2021-06-24 04:35:02
			stapenden1@google.de
			BUY
			95.02
			COMPLETED
		
		
			2021-07-02 17:14:35
			rclaypole0@qq.com
			BUY
			76.34
			PENDING
		
		
			2021-07-03 23:34:36
			rclaypole0@qq.com
			BUY
			4.89
			CANCELED
		
	

 

the expected output is:

 

	
		
			customer ▲
			buy
			sell
			completed
			pending
			canceled
			total
		
		
			rclaypole0@qq.com
			5
			4
			4
			3
			2
			108.87
		
	

 

These are the records for rclaypole0@qq.com:

 

	
		
			transactions
		
		
			dt
			type
			amount
			status
		
		
			2021-07-03 23:34:36
			BUY
			4.89
			CANCELED
		
		
			2021-07-13 01:12:15
			BUY
			79.27
			COMPLETED
		
		
			2021-07-23 07:07:29
			BUY
			19.92
			COMPLETED
		
		
			2021-07-02 17:14:35
			BUY
			76.34
			PENDING
		
		
			2021-07-06 22:06:30
			BUY
			18.39
			PENDING
		
		
			2021-07-18 10:44:42
			SELL
			55.57
			CANCELED
		
		
			2021-07-02 19:47:33
			SELL
			51.54
			COMPLETED
		
		
			2021-07-03 15:20:54
			SELL
			51.30
			COMPLETED
		
		
			2021-07-31 16:13:40
			SELL
			24.42
			PENDING
		
	

 

Total revenues are (79.27 + 19.92) + (51.54 + 51.30) * 0.1 - (4.89 + 55.57) * 0.01

## Sample Input/Output

## Preview

As part of HackerMart's e-commerce marketing analytics, they need to find the
