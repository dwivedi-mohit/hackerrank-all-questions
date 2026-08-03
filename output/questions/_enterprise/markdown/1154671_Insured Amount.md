# Insured Amount

## Metadata

- **ID:** 1154671
- **Type:** database
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Windowing, Sorting, SQL, Hard, Database, Interviewer Guidelines
- **Skills:** SQL (Advanced)
- **Languages:** m, y, s, q, l, ,, o, r, a, c

## Summary

This database question evaluates SQL, windowing functions, and sorting concepts, ideal for senior-level roles. The problem requires calculating insured amounts for users based on their insurance type and risk, using specific criteria and rounding the results.

## Problem Statement

An insurance company analyzes the risk for an individual applicant/user before issuing the policy. Depending on the risk the insured amount for the user is different. You are provided with the user id, type of insurance and the risk for a user. Calculate the amount insured for every user based on the insurance type and risk.

 

Monthly premiums paid by users are:

	
- $100 for Term Life and Whole Life
	
- $400 for Health
	
- $500 for Endowment

 

Calculate the amount insured for user by following criteria:

	
- Term Life and Whole Life - 10%, 8.5% and 7% of the total amount collected in a year for Low, Medium and High risk users respectively
	
- Health - 2%, 1.5% and 1% of the total amount collected in a year for Low, Medium and High risk users respectively
	
- Endowment - 15%, 12% and 10% of the total amount collected in a year for Low, Medium and High risk users respectively

 

Note: Round off the insured values to an integer value and order the result by user id. 

 

Schema

There is 1 table: `users`.

	
		
			users
		
		
			Name
			Type
			Description
		
		
			user_id
			int
			Unique id of the user.
		
		
			insurance_type
			varchar(15)
			Type of insurance user opted for.
		
		
			risk
			varchar(7)
			Risk associated with the user (Low, Medium or High)
		
	

Sample Data Tables

	
		
			users
		
		
			user_id
			insurance_type
			risk
		
		
			6697
			Term Life
			Medium
		
		
			4084
			Term Life
			Medium
		
		
			3053
			Health
			Medium
		
		
			2716
			Term Life
			Medium
		
		
			3130
			Health
			Medium
		
		
			4146
			Whole Life
			Low
		
		
			5875
			Health
			Low
		
		
			8747
			Whole Life
			High
		
		
			2095
			Term Life
			Medium
		
		
			8374
			Term Life
			High
		
		
			6014
			Whole Life
			High
		
		
			6546
			Endowment
			High
		
		
			4533
			Term Life
			Low
		
		
			7174
			Health
			Low
		
		
			4470
			Health
			Medium
		
		
			1364
			Whole Life
			Low
		
		
			4293
			Health
			High
		
		
			7062
			Health
			Medium
		
		
			6839
			Term Life
			Medium
		
		
			9596
			Health
			Low
		
	

 

	
		
			OUTPUT
		
		
			user_id
			insurance_type
			risk
			insured_amount
		
		
			1364
			Whole Life
			Low
			5760
		
		
			2095
			Term Life
			Medium
			4896
		
		
			2716
			Term Life
			Medium
			4896
		
		
			3053
			Health
			Medium
			864
		
		
			3130
			Health
			Medium
			864
		
		
			4084
			Term Life
			Medium
			4896
		
		
			4146
			Whole Life
			Low
			5760
		
		
			4293
			Health
			High
			576
		
		
			4470
			Health
			Medium
			864
		
		
			4533
			Term Life
			Low
			5760
		
		
			5875
			Health
			Low
			1152
		
		
			6014
			Whole Life
			High
			4032
		
		
			6546
			Endowment
			High
			5760
		
		
			6697
			Term Life
			Medium
			4896
		
		
			6839
			Term Life
			Medium
			4896
		
		
			7062
			Health
			Medium
			864
		
		
			7174
			Health
			Low
			1152
		
		
			8374
			Term Life
			High
			4032
		
		
			8747
			Whole Life
			High
			4032
		
		
			9596
			Health
			Low
			1152
		
	

 

Total amount collected from all the users based on their insurance type in a year is 57600. For user with id 1360 the insured amount based on the criteria would be 10% of the total amount collected i.e. 5760.

## Sample Input/Output

## Preview

An insurance company analyzes the risk for an individual applicant/user before
