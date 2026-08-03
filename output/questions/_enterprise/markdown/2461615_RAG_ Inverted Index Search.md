# RAG: Inverted Index Search

## Metadata

- **ID:** 2461615
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** RAG, Easy
- **Skills:** RAG (Basic)

## Summary

This implementation question evaluates inverted indexing, tokenization, and search algorithms concepts, ideal for junior-level roles. The task requires building an InvertedIndex class to efficiently handle keyword searches in a tech-support knowledge base.

## Problem Statement

Scenario

Your team maintains a tech-support knowledge base of plain-text articles covering topics such as password resets, firmware updates, and connectivity troubleshooting. Support agents need to search this corpus by keyword. Rather than scanning every article for every query, you will build an inverted index; a data structure that maps each word to the documents containing it and use it to answer keyword queries in near-constant time.

 

Task

Implement the InvertedIndex class in src/inverted_index.py with the following capabilities:

	
- 
	
Build the index

	
		
- 
		
Tokenise each document: lowercase, strip punctuation, split on whitespace.

		
		
- 
		
Map each token to the set of 0-based document IDs that contain it.

		
	
	
	
- 
	
AND search (search_and)

	
		
- 
		
Return a sorted list of doc IDs that contain every query token (intersection).

		
		
- 
		
Return [] for an empty query or if any token is absent from the index.

		
	
	
	
- 
	
OR search (search_or)

	
		
- 
		
Return a sorted list of doc IDs that contain at least one query token (union).

		
		
- 
		
Silently ignore query tokens that are absent from the index.

		
		
- 
		
Return [] for an empty query or if no token matches.

		
	
	

Note: You are not expected to implement ranking, relevance scoring, or stemming; only exact-token indexing and retrieval are required.

 

	Deliverables
	
		
			File
			Description
		
	
	
		
			src/inverted_index.py
			Implement InvertedIndex.__init__, build, search_and, and search_or
		
	

 

Sample Documents

`How to reset your password on the login portal.
Wi-Fi connection drops after a firmware update.
Export your data before cancelling a subscription.
Bluetooth pairing fails on Windows after a driver update.
Error code shown when the application cannot connect.`
```

## Preview

Scenario
