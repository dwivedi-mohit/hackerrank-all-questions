# Bank Accounts Summary

## Metadata

- **ID:** 645316
- **Type:** database
- **Difficulty:** 5.0
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** SQL, Aggregation, Hard, Interviewer Guidelines, Simple Joins, Database, Sub-Queries
- **Skills:** SQL (Intermediate)
- **Languages:** m, y, s, q, l, ,, o, r, a, c

## Summary

This database question evaluates SQL, aggregation, and sub-queries concepts, ideal for mid-level roles. The problem requires writing a query to calculate users' current balances and determine if they have breached their credit limits based on transaction logs.

## Problem Statement

Virtual World Bank (VWB) helps its users in making online payments using virtual payment address (vpa). It maintains its customer details like name, vpa, and credit limit in the table user_financial_detail. Each user can easily transfer money from his/her account to another VWB user's account by using his/her uniquely assigned vpa and the recipient user's vpa. The VWB records all such transactions in table transaction_log, storing information such as the sender's vpa, recipient's vpa and the amount transferred. VWB wants to find out the current balance of all the users who have ever transacted and check whether they have breached their credit limit. Write a query that prints this information for all the users present in the table user_financial_detail in the following format: name | vpa | current_balance | credit_limit_breached

 

The credit_limit_breached column should contain either 'YES' or 'NO'. If the user is overdrawn by more than the credit limit, return 'YES' in this column. Otherwise, return 'NO'.

 

The order of output does not matter.

 

Schema

There are 2 tables: user_financial_detail, transaction_log.

	
		
			user_financial_detail
		
		
			Name
			Type
			Description
		
		
			id
			INTEGER
			This is the user's id. It is the primary key.
		
		
			first_name
			STRING
			User's first name.
		
		
			last_name
			STRING
			User's last name.
		
		
			vpa
			STRING
			Unique virtual private address (vpa)
		
		
			
			
credit_limit

			
			INTEGER
			Credit limit granted by VWB for making transactions without sufficient balance in the account.
		
	

 

	
		
			transaction_log
		
		
			Name
			Type
			Description
		
		
			id
			INTEGER
			This is the transaction id. It is the primary key.
		
		
			
			
paid_by

			
			STRING
			Sender's vpa.
		
		
			
			
paid_to

			
			STRING
			Recipient's vpa.
		
		
			amount
			INTEGER
			The amount transferred from sender to recipient.
		
		
			
			
transacted_on

			
			DATE
			Transaction's date.
		
	

 

Sample Data Tables

	
		
			user_financial_detail
		
		
			id
			first_name
			last_name
			vpa
			credit_limit
		
		
			1
			Shea
			Caldwell
			shea.caldwell@vwb
			5000
		
		
			2
			Martena
			Leblanc
			martena.leblanc@vwb
			10000
		
		
			3
			Tashya
			Riley
			tashya.riley@vwb
			25000
		
	

	
		
			transaction_log
		
		
			id
			paid_by
			paid_to
			amount
			transacted_on
		
		
			1
			martena.leblanc@vwb
			tashya.riley@vwb
			13155
			2019-11-21
		
		
			2
			tashya.riley@vwb
			martena.leblanc@vwb
			10883
			2019-09-10
		
		
			3
			shea.caldwell@vwb
			tashya.riley@vwb
			15012
			2018-12-25
		
		
			4
			martena.leblanc@vwb
			shea.caldwell@vwb
			5700
			2018-05-18
		
		
			5
			tashya.riley@vwb
			shea.caldwell@vwb
			18473
			2018-07-02
		
	

 

Sample Output

Shea Caldwell shea.caldwell@vwb 9161 NO

Martena Leblanc martena.leblanc@vwb -7972 NO

Tashya Riley tashya.riley@vwb -1189 NO

 

Explanation

	
- 
Shea Caldwell with vpa shea.caldwell@vwb has a current balance of 9161 and has not breached the credit limit of 5000. She has received 24173 (5700+18473) and sent 15012 as transfer amounts.
	
- 
Martena Leblanc with vpa martena.leblanc@vwb has a current balance of -7972 and has not breached the credit limit of 10000. She has received 10883 and sent 18855 (13155 + 5700) as transfer amounts.
	
- 
Tashya Riley with vpa tashya.riley@vwb has a current balance of -1189 and has not breached the credit limit of 25000. She has received 28167 (13155+15012) and sent 29356 (10883 + 18473) as transfer amounts.

## Sample Input/Output

## Preview

Virtual World Bank (VWB) helps its users in making online payments using virtu
