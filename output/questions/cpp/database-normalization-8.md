# Database Normalization #8

- **Domain:** cpp
- **Difficulty:** Medium
- **Max Score:** 5
- **Success Ratio:** 0.9674768316139185
- **Total Submissions:** 11438
- **Solved Count:** 11066
- **URL:** https://www.hackerrank.com/challenges/database-normalization-8

## Problem Statement

Let us take the example of a simple movie library. Each movie has a description, director, and serial number. Customers have a name, address, and membership number. Assume only one copy of each movie exists in the library. We are given the following relations and determinants. The keys for each relation are **CAPITALIZED**.  

	Relations (The key is CAPITALIZED):
	customer(name,addr,MEMBERNO)
	movie(DESCRIPTION,director,serialno)
	borrow(memberno,DATE,SERIALNO)


Which of these determinants is a **NON-KEY** dependency?
In the text box, only enter the index number (1-6) of the dependency which you have identified as non-key.
	
 	1.	description->director,serialno
  	2.	serialno->description
  	3.	serialno->director
  	4.	name,addr -> memberno
  	5.	memberno -> name,addr
  	6.	serialno,date -> memberno
    

## Input Format

  

## Output Format

In the text box, only enter the index number (1-6) of the dependency which you have identified as non-key.
