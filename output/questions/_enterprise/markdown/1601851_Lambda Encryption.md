# Lambda Encryption

## Metadata

- **ID:** 1601851
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** AWS Services, AWS Lambda, Encryption, Environment Variables, Medium
- **Skills:** AWS (Intermediate)

## Summary

This multiple choice question evaluates AWS Lambda, encryption, and environment variables concepts, ideal for mid-level roles. The problem requires understanding why environment variables were not automatically encrypted when updated via the AWS CLI without specifying a KMS key ARN.

## Problem Statement

A developer utilizes the AWS CLI to update the configuration of an AWS Lambda function, intending to include environment variables.

 

Command:

`aws lambda update-function-configuration --function-name my-function --environment Variables={key1=value1,key2=value2}`
```

 

The developer expected the environment variables would be automatically encrypted by AWS using the default service key, but this did not happen. What is the cause of this unexpected behavior?

## Preview

A developer utilizes the AWS CLI to update the configuration of an AWS Lambda fu
