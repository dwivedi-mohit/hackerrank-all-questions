# e-Commerce Customer Revenue Report

## Metadata

- **ID:** 1122903
- **Type:** database
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Windowing, SQL, Aggregation, Hard, Database, Interviewer Guidelines
- **Skills:** SQL (Advanced)
- **Languages:** m, y, s, q, l, ,, o, r, a, c

## Summary

This database question evaluates SQL, aggregation, and windowing concepts, ideal for senior-level roles. The problem requires generating a revenue report for customers based on their transactions in July 2021, considering various transaction statuses and types.

## Problem Statement

As part of HackerMart's e-commerce marketing analytics, they need a revenue report for their customers in July, 2021. Revenue from a customer is the sum of the values described below.

	
- type=BUY, the customer purchased something, the transaction amount is potential revenue
	
- type=SELL, the customer sold something, HackerMart collects a fee, 10% of the transaction amount is potential revenue

 

Status determines how a transaction is treated.

	
- status = COMPLETED, the transaction is included
	
- status = PENDING, the transaction is ignored
	
- status = CANCELED, the transaction is void, 1% of the transaction amount is deducted from revenue

 

Requirements:

	
- Columns to report are customer, buy, sell, total.
	
- 
buy, and sell are revenues for buy and sell transactions, respectively.
	
- 
total is the sum of buy and sell.
	
- Round to 2 places after the decimal.
	
- Order the records descending by total.

 

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
			DECIMAL(4,2)
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
		
		
			2021-07-09 20:03:14
			rclaypole0@qq.com
			BUY
			71.46
			CANCELED
		
		
			2021-07-09 19:30:03
			asmithin4@elegantthemes.com
			SELL
			40.24
			CANCELED
		
		
			2021-07-06 04:56:06
			rclaypole0@qq.com
			SELL
			69.35
			PENDING
		
		
			2021-07-16 04:36:58
			rclaypole0@qq.com
			SELL
			3.37
			CANCELED
		
		
			2021-07-15 11:59:36
			bhaddeston2@mapquest.com
			BUY
			15.46
			CANCELED
		
		
			2021-07-24 16:31:04
			bhaddeston2@mapquest.com
			SELL
			90.16
			COMPLETED
		
		
			2021-06-23 21:50:34
			rclaypole0@qq.com
			BUY
			53.40
			CANCELED
		
		
			2021-07-30 22:30:22
			bhaddeston2@mapquest.com
			SELL
			6.48
			PENDING
		
		
			2021-06-28 05:47:45
			stapenden1@google.de
			SELL
			72.67
			PENDING
		
		
			2021-07-11 16:51:06
			stapenden1@google.de
			BUY
			93.29
			CANCELED
		
		
			2021-07-16 08:25:11
			rclaypole0@qq.com
			BUY
			53.19
			PENDING
		
		
			2021-07-22 02:24:59
			rclaypole0@qq.com
			BUY
			51.17
			CANCELED
		
		
			2021-06-23 21:42:24
			bhaddeston2@mapquest.com
			SELL
			10.57
			PENDING
		
		
			2021-07-22 09:11:56
			rclaypole0@qq.com
			BUY
			68.25
			COMPLETED
		
		
			2021-07-19 04:11:50
			rclaypole0@qq.com
			SELL
			66.78
			PENDING
		
		
			2021-07-03 19:00:10
			gnickerson3@globo.com
			BUY
			26.31
			PENDING
		
		
			2021-07-11 17:56:06
			bhaddeston2@mapquest.com
			BUY
			86.05
			CANCELED
		
		
			2021-07-03 01:58:09
			stapenden1@google.de
			SELL
			31.49
			CANCELED
		
		
			2021-06-30 22:03:17
			bhaddeston2@mapquest.com
			BUY
			50.93
			PENDING
		
		
			2021-07-09 14:22:39
			stapenden1@google.de
			BUY
			5.40
			CANCELED
		
	

 

The expected output is:

 

	
		
			customer
			buy
			sell
			total ▼
		
		
			rclaypole0@qq.com
			67.02
			-0.03
			66.99
		
		
			bhaddeston2@mapquest.com
			-1.02
			9.02
			8.00
		
		
			gnickerson3@globo.com
			0.00
			0.00
			0.00
		
		
			asmithin4@elegantthemes.com
			0.00
			-0.40
			-0.40
		
		
			stapenden1@google.de
			-0.99
			-0.31
			-1.30
		
	

 

Detail for rclaypole0@qq.com:

 

	
		
			transactions
		
		
			dt
			type
			amount
			status
		
		
			2021-07-09 20:03:14
			BUY
			71.46
			CANCELED
		
		
			2021-07-22 02:24:59
			BUY
			51.17
			CANCELED
		
		
			2021-07-22 09:11:56
			BUY
			68.25
			COMPLETED
		
		
			2021-07-16 08:25:11
			BUY
			53.19
			PENDING
		
		
			2021-07-16 04:36:58
			SELL
			3.37
			CANCELED
		
		
			2021-07-06 04:56:06
			SELL
			69.35
			PENDING
		
		
			2021-07-19 04:11:50
			SELL
			66.78
			PENDING
		
	

 

	
- Gross buy revenue: 68.25 and buy penalties: (71.46 + 51.17) * -0.01 = -1.22
	
- Gross sell revenue: 0 and sell penalties: 3.37 * -0.01 = -0.03

## Sample Input/Output

## Preview

As part of HackerMart's e-commerce marketing analytics, they need a revenue re
