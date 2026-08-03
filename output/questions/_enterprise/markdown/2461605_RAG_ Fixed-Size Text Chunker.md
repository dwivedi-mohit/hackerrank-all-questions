# RAG: Fixed-Size Text Chunker

## Metadata

- **ID:** 2461605
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** RAG, Easy
- **Skills:** RAG (Basic)

## Summary

This document-splitting question evaluates text chunking, metadata attachment, and filtering concepts, ideal for junior-level roles. The task involves implementing a chunker to split text into fixed-size segments with metadata for downstream processing.

## Problem Statement

Scenario

A legal-tech startup maintains a repository of contract document, lease agreements, NDAs, and service contracts. To enable semantic search over these documents, each contract must be split into smaller text segments before embedding. The ingestion pipeline needs a reliable chunker that divides documents into fixed-size word-based windows with configurable overlap, and a metadata layer to tag each chunk for downstream filtering.

 

Task

In this task, you will implement the document-splitting stage of a RAG ingestion pipeline: splitting raw text into fixed-size word-based chunks and attaching structured metadata to each chunk.

	
- 
	
Implement TextChunker

	
		
- 
		
Split a text string into chunks of a fixed word count using a sliding window.

		
		
- 
		
Support configurable overlap so adjacent chunks share words at their boundaries.

		
	
	
	
- 
	
Implement ChunkMetadata

	
		
- 
		
Attach structured metadata (source ID, chunk index, word count) to each chunk.

		
		
- 
		
Filter the tagged chunks by minimum word count to remove fragments too short to be useful.

		
	
	

Note: Embedding the chunks and querying the vector store are out of scope for this challenge; only splitting and metadata tagging are required.

 

	Deliverables
	
		
			File
			Description
		
	
	
		
			src/text_chunker.py
			Fixed-size word-based chunking with overlap
		
		
			src/chunk_metadata.py
			Metadata attachment and length-based filtering
		
	

 

Sample Documents

`RENT AND PAYMENT TERMS

The monthly rent for the premises shall be one thousand four hundred and fifty
dollars ($1,450.00), due and payable on or before the first day of each calendar
month. Rent shall be paid by electronic bank transfer to the account designated
by the Landlord in writing.

OBLIGATIONS OF THE RECEIVING PARTY

The Receiving Party shall not disclose confidential information to any third party
without prior written authorization from the Disclosing Party. The Receiving Party
shall limit internal disclosure strictly to employees and contractors who have a
legitimate need to know the information.`
```

## Preview

Scenario
