# Conditional Delete

## Metadata

- **ID:** 1251656
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** DynamoDB, NoSQL, Medium
- **Skills:** DynamoDB (Intermediate)

## Summary

This multiple choice question evaluates DynamoDB, NoSQL, and conditional expressions concepts, ideal for mid-level roles. The problem requires determining the content of a DynamoDB table after executing two delete queries based on specific conditions.

## Problem Statement

The Products DynamoDB table is created as follows.

 

`aws dynamodb create-table \
  --table-name Products \
  --attribute-definitions '[
    {
        "AttributeName": "Id",
        "AttributeType": "N"
    }
  ]' \
  --key-schema '[
    {
        "AttributeName": "Id",
        "KeyType": "HASH"
    }
  ]' \
  --provisioned-throughput '{
    "ReadCapacityUnits": 1,
    "WriteCapacityUnits": 1
  }'`
```

 

The following items are inserted.

 

	
		
			Id
			Category
			Price
		
		
			1
			Car
			33
		
		
			2
			Books
			48
		
		
			3
			Furniture
			45
		
		
			4
			Toys
			97
		
		
			5
			Electronics
			90
		
		
			6
			Beverage
			98
		
		
			7
			Food
			99
		
	

 

query1:

 

`aws dynamodb delete-item \
    --table-name Products \
    --key '{"Id":{"N":"3"}}' \
    --condition-expression "(Category IN (:cat1, :cat2)) and (Price between :low and :high)" \
    --expression-attribute-values '{
        ":cat1": {"S": "Toys"},
        ":cat2": {"S": "Furniture"},
        ":low": {"N": "25"},
        ":high": {"N": "70"}
    }'
`
```

 

query2:

 

`aws dynamodb delete-item \
    --table-name Products \
    --condition-expression "(Category IN (:cat1, :cat2)) and (Price between :low and :high)" \
    --expression-attribute-values '{
        ":cat1": {"S": "Electronics"},
        ":cat2": {"S": "Beverage"},
        ":low": {"N": "80"},
        ":high": {"N": "100"}
    }'`
```

 

What will be the content of the Products table when query1 is executed followed by query2?

## Preview

The Products DynamoDB table is created as follows.
