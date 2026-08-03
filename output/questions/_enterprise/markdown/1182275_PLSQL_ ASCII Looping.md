# PLSQL: ASCII Looping

## Metadata

- **ID:** 1182275
- **Type:** database
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Loops, PL/SQL, Medium, Interviewer Guidelines
- **Skills:** PL/SQL (Intermediate)
- **Languages:** o, r, a, c, l, e

## Summary

This database question evaluates PL/SQL, loops, and ASCII value calculation concepts, ideal for mid-level roles. The problem requires writing a PL/SQL block to compute the highest total of ASCII values for characters in sentences from a database table.

## Problem Statement

There is a database with sentence_data data including sentence_id and sentence. 

 

Write a PL/SQL block to print the highest total of ASCII values of each character in the sentence in the sentence_data table. The sentences can contain spaces and special characters. Thus, ASCII value should be calculated for all characters.

Schema

You are provided with 1 table

	
		
			SENTENCE_DATA
		
		
			Name
			Type
			Description
		
		
			SENTENCE_ID
			INTEGER
			The ID of the sentence
		
		
			SENTENCE
			VARCHAR2
			This is the sentence
		
	

Sample Data Tables

	
		
			SENTENCE_DATA
		
		
			SENTENCE_ID
			SENTENCE
		
		
			101
			I am an American and I live in Charlotte
		
		
			102
			I am an Indian and I live in Mumbai
		
	

 

Output:

3503

 

Explanation:

The total of ASCII digits associated with each character in sentence_id 101's total is 3503 (spaces included) while sentence_id 102's is 2967.

Report the greater value.

## Preview

There is a database with sentence_data data including sentence_id and sentence
