# Batch Optimization

## Metadata

- **ID:** 1601796
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Hard, AWS Services, AWS Lambda, Serverless Computing, Triggers and Integrations, Scaling and Concurrency
- **Skills:** AWS (Advanced)

## Summary

This multiple choice question evaluates AWS Lambda, event source mapping, and error handling concepts, ideal for senior-level roles. The problem requires optimizing a Lambda function for a Kinesis Data Stream to handle high-velocity data with specific error handling strategies.

## Problem Statement

An AWS Lambda function for a multi-sharded Amazon Kinesis Data Stream must be optimized.

 

The goals are:

	
- handle high-velocity data
	
- minimize throttling
	
- efficiently process each batch despite errors
	
- use on-demand error handling for invocations
	
- set a maximum retry for failed batches 
	
- split the batch if half of it fails

 

Given the AWS CLI command, which option should replace [PLACEHOLDER]?

`aws lambda create-event-source-mapping \
  --function-name "HighVelocityDataHandler" \
  --batch-size 500 \
  --event-source arn:aws:kinesis:us-west-2:123456789012:stream/HighVelocityStream \
  --starting-position LATEST \
  [PLACEHOLDER]
`
```

## Preview

An AWS Lambda function for a multi-sharded Amazon Kinesis Data Stream must be op
