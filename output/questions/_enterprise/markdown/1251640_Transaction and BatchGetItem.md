# Transaction and BatchGetItem

## Metadata

- **ID:** 1251640
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** DynamoDB, NoSQL, Medium
- **Skills:** DynamoDB (Intermediate)

## Summary

This multiple choice question evaluates DynamoDB, NoSQL, and query execution concepts, ideal for mid-level roles. The problem requires determining the output of various queries executed on a Students table in DynamoDB.

## Problem Statement

The Students DynamoDB table is created with the following attributes.

 

	
- Name
	
- Subject
	
- Score

 

Name is the partition key and Subject is the sort key.

The following items are inserted into the table.

 

	
		
			Name
			Subject
			Score
		
		
			adam
			Bio
			48
		
		
			adam
			Maths
			33
		
		
			adam
			Physics
			76
		
		
			adam
			Sociology
			97
		
		
			
			
john

			
			Bio
			98
		
		
			john
			Physics
			90
		
		
			mary
			Maths
			99
		
	

 

The following queries are run.

 

query1:

 

`aws dynamodb batch-get-item \
    --request-items '{
        "Students": {
            "Keys": [
                {
                    "Name": {"S": "adam"},
                    "Subject": {"S": "Maths"}
                },
                {
                    "Name": {"S": "john"},
                    "Subject": {"S": "Chemistry"}
                }
            ]
        }
    }'`
```

 

 

query2:

 

`aws dynamodb batch-get-item \
    --request-items '{
        "Students": {
            "Keys": [
                {
                    "Name": {"S": "adam"},
                    "Subject": {"S": "Maths"}
                },
                {
                    "Subject": {"S": "Bio"},
                    "Score": {"N": "48"}
                }
            ]
        }
    }'`
```

 

 

query3:

 

`aws dynamodb transact-get-items \
    --transact-items '[
        {
            "Get": {
                "Key": {
                    "Name": {"S": "adam"},
                    "Subject": {"S": "Maths"}
                },
                "TableName": "Students"
            }
        },
        {
            "Get": {
                "Key": {
                    "Score": {"N": "97"},
                    "Subject": {"S": "Sociology"}
                },
                "TableName": "Students"
            }
        }
    ]'`
```

 

What is the output when the queries are executed?

## Preview

The Students DynamoDB table is created with the following attributes.
