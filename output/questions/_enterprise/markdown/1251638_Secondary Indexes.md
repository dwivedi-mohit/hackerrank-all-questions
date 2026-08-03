# Secondary Indexes

## Metadata

- **ID:** 1251638
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** DynamoDB, NoSQL, Easy
- **Skills:** DynamoDB (Basic)

## Summary

This multiple choice question evaluates DynamoDB queries, local secondary indexes, and filtering concepts, ideal for junior-level roles. The problem requires determining the scanned counts for various queries on a Students DynamoDB table based on specified conditions.

## Problem Statement

The Students DynamoDB table is created with the following attributes.

 

	
- Name
	
- Subject
	
- Score

 

Name is the partition key and Subject is the sort key.

During creation, a local secondary index called StudentScoreIndex is created with ProjectionType "KEYS_ONLY", Name as the partition key, and Score as the sort key.

 

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
		
	

 

Now, consider the following queries.

 

query1:

 

`aws dynamodb query \
    --table-name Students \
    --key-condition-expression "#name = :name" \
    --filter-expression "Score > :score" \
    --expression-attribute-names '{
        "#name": "Name"
    }' \
    --expression-attribute-values '{
        ":name": { "S": "adam" },
        ":score": { "N": "50" }
    }'`
```

 

query2:

 

`aws dynamodb scan \
    --table-name Students \
    --filter-expression "#name = :name AND Score > :score" \
    --expression-attribute-names '{
        "#name": "Name"
    }' \
    --expression-attribute-values '{
        ":name": { "S": "adam" },
        ":score": { "N": "50" }
    }'`
```

 

query3:

 

`aws dynamodb query \
    --table-name Students \
    --key-condition-expression "#name = :name AND Subject = :subject" \
    --filter-expression "Score > :score" \
    --expression-attribute-names '{
        "#name": "Name"
    }' \
    --expression-attribute-values '{
        ":subject": { "S": "Maths" },
        ":score": { "N": "50" },
        ":name": {"S": "adam"}
    }'`
```

 

query4:

 

`aws dynamodb query \
    --table-name Students \
    --index-name StudentScoreIndex \
    --key-condition-expression "#name = :name AND Score > :score" \
    --expression-attribute-names '{
        "#name": "Name"
    }' \
    --expression-attribute-values '{
        ":name": { "S": "adam" },
        ":score": { "N": "50" }
    }'`
```

 

c1, c2, c3, and c4 are the document ScannedCount for query1, query2, query3, and query4 respectively.  What are the values of c1, c2, c3, and c4?

## Preview

The Students DynamoDB table is created with the following attributes.
