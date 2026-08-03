# Build a RAG System for API Support

## Metadata

- **ID:** 2103778
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Tokenization, Basic RAG Pipeline, Random Embeddings, Generative AI, Chunking, Easy, RAG
- **Skills:** RAG (Basic)

## Summary

This RAG pipeline question evaluates tokenization, embedding, and query handling concepts, ideal for junior-level roles. The task involves building a Retrieval-Augmented Generation pipeline to efficiently answer developer questions using internal documentation.

## Problem Statement

Scenario

Your team maintains internal documentation for developers who work with your APIs. The information is split between OpenAPI specs and deployment metadata like rate limits, auth schemes, and tenant-specific settings.

A developer asks:

“How do I create a billing record, and what’s the rate limit?”

You know the answer is available, but it’s spread between an OpenAPI file and a separate service metadata JSON. Manually piecing it together is slow and error-prone.

To help streamline support, you decide to build a Retrieval-Augmented Generation (RAG) pipeline that can search across both types of documents and generate concise, helpful responses.

 

Task

Build a RAG Pipeline to Answer Developer Questions Using Internal Docs:

	
- 
	
Ingest Docs

	
		
- 
		
Load OpenAPI specifications (e.g., openapi.json).

		
		
- 
		
Load contextual metadata files (e.g., live_service_metadata.json).

		
		
- 
		
Preprocess the data to ensure structured sections (e.g., paths, descriptions, auth info) are extractable.

		
	
	
	
- 
	
Embed & Index

	
		
- 
		
Convert preprocessed documents into vector embeddings.

		
		
- 
		
Store embeddings in a similarity index for efficient retrieval.

		
		
- 
		
Use semantic chunking (e.g., per endpoint or section) to retain context.

		
	
	
	
- 
	
Retrieve

	
		
- 
		
Accept a developer’s natural language query.

		
		
- 
		
Convert the query into an embedding.

		
		
- 
		
Use OpenAI embedding model ("text-embedding-ada-002") to retrieve the top-k relevant chunks from both spec and metadata sources.

		
	
	
	
- 
	
Generate Answer

	
		
- 
		
Pass the retrieved context into an LLM (e.g., gpt-4o).

		
		
- 
		
Return a clear, actionable answer that includes references to endpoints, required parameters, and tenant-specific rules.

		
	
	

Deliverables

	
		
			File
			Description
		
	
	
		
			
			
document_loader.py

			
			
			
Used for loading and preprocessing both Openapi + metadata

			
		
		
			
			
vector_store.py

			
			
			
Used for embedding documents and building the index

			
		
		
			
			
rag_pipeline.py

			
			
			
Used for query handling and answer generation

			
		
	

 

Sample Document

`POST /billing/create: creates a billing record for an account. all billing operations require an `account_id` and `amount`. rate limit for this tenant is 500rpm. endpoint base url: https://api.devtools.io/v2
`
```

Sample Query

`How can i create a billing record and what's the rate limit?`
```

Sample Output 

`To create a billing record, call `POST /billing/create` with `account_id` and `amount` as query parameters. the tenant rate limit is 500rpm. endpoint base url is https://api.devtools.io/v2.
`
```

## Preview

Scenario
