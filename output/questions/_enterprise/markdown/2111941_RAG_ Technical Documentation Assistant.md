# RAG: Technical Documentation Assistant

## Metadata

- **ID:** 2111941
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Medium, Generative AI, Retrieval-Augmented Generation, LangChain
- **Skills:** RAG (Intermediate)

## Summary

This development question evaluates semantic indexing, reranking logic, and answer evaluation concepts, ideal for mid-level roles. The problem requires building an intelligent assistant that retrieves and refines code snippets and documentation to assist developers in understanding a large codebase.

## Problem Statement

Scenario

You are a senior developer tasked with building an intelligent assistant to help engineers navigate and understand a large codebase. The assistant must answer natural language queries by retrieving relevant code snippets, documentation, or explanations to help developers gain insight into implementation logic and usage patterns.

To achieve this, you will:

	
- Use HuggingFace embeddings to semantically index code snippets and engineering documentation.
	
- Implement reranking logic that prioritizes results based on semantic similarity and metadata such as file type, code relevance, or recent commits.
	
- Apply a self-critique loop that evaluates the draft answer for vague or unsupported content and, if necessary, triggers a secondary retrieval to regenerate a more precise and well-supported response.

Your goal is to deliver an end-to-end solution that boosts developer productivity and confidence by providing accurate, structured, and contextually rich answers.

 

Task

Implement the following components:

	
- DocumentLoader
	
		
- 
		
Loads and validates JSON-formatted documents

		
		
- 
		
Converts content into structured entries (e.g., title, content, doc_id)

		
		
- 
		
Can output LangChain-compatible Document objects

		
	
	
	
- CustomIndex
	
		
- 
		
Encodes document titles using a SentenceTransformer model

		
		
- 
		
Builds and saves a semantic vector index to disk

		
		
- 
		
Supports loading prebuilt index files

		
		
- 
		
Provides utilities to find top-k documents using cosine similarity

		
	
	
	
- PostProcess
	
		
- 
		
Analyzes the final answer returned by a query

		
		
- 
		
Evaluates answer relevance, vague language, topic match, and keyword overlap

		
		
- 
		
Returns structured evaluation metrics (e.g., score, ans_matching, topic relevance)

		
	
	
	
- Reranker
	
		
- 
		
Applies semantic and metadata-based reranking logic to reorder retrieved candidates

		
		
- 
		
Considers factors like document recency, code relevance, or file type

		
	
	

 

	Deliverables
	
		
			File Name
			Description
		
	
	
		
			document_loader.py` `

			Loads JSON content and produces LangChain-compatible Document objects
		
		
			indexer.py
			Embeds and indexes code/documentation using HuggingFace models
		
		
			
			
post_process.py

			
			
			
Evaluates and refines draft responses via critique loop

			
		
		
			rerank.py
			Applies semantic and metadata-based reranking logic
		
	

 

 

Sample Document

[

  {

    "doc_id": "DOC001",

    "title": "Authentication Implementation Guide",

    "content": "This guide provides an exhaustive overview of implementing secure authentication in our web application. It details the use of JSON Web Tokens (JWT) with HS256 algorithm...",

    "base_score": 0.85,

    "position_in_retrieval": 1,

    "last_updated": "2024-01-15"

  }

]

 

Sample Input

Explain LIFO structure

 

Sample Output

  "score": 0.85,

  "ans_matching": true,

  "query_keywords": ["LIFO", "stack", "structure"],

  "similar_keywords": ["Last-In-First-Out", "stack"],

  "topic_relevancy_check": true

## Preview

Scenario
