# Spring Boot: Filter Microservice

## Metadata

- **ID:** 1077845
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Spring Boot, Java, Filtering, Sorting, Easy
- **Skills:** Spring Boot (Basic)

## Summary

This back-end development question evaluates REST APIs, filtering, and sorting concepts, ideal for junior-level roles. The problem requires implementing APIs to filter and sort a collection of product records based on price.

## Problem Statement

Implement REST APIs to perform filter and sort operations on a collection of Products.

 

Each event is a JSON entry with the following keys:

	
- 
`barcode`: the unique id of the product (String)  
	
- 
`price`: the price of the product (Integer)
	
- 
`discount`: the discount % available on the product(Integer)
	
- 
`available`: the availability status of the product (0 or 1)

 

Here is an example of a product JSON object:

`[
    {
      "barcode": "74001755",
      "item": "Ball Gown",
      "category": "Full Body Outfits",
      "price": 3548,
      "discount": 7,
      "available": 1
    },
    {
      "barcode": "74002423",
      "item": "Shawl",
      "category": "Accessories",
      "price": 758,
      "discount": 12,
      "available": 1
    }
]`
```

 

You are provided with the implementation of the models required for all the APIs. The task is to implement a set of REST services that exposes the endpoints and allows for filtering and sorting the collection of product records in the following ways:

 

`GET` request to `/filter/price/{initial_range}/{final_range}`:

	
- returns a collection of all products whose price is between the initial and the final range supplied
	
- The response code is 200, and the response body is an array of products in the price range provided.
	
- In case there are no such products return status code 400.

 

`GET` request to `/sort/price`:

	
- returns a collection of all products sorted by their pricing
	
- The response code is 200 and the response body is an array of the product names sorted in ascending order of price.

 

Complete the given project so that it passes all the test cases when running the provided unit tests.

 

Example requests and responses

 

`GET` request to `/filter/price/{initial_range}/{final_range}`

The response code is 200, and when converted to JSON, the response body is as follows for filter/750/900:

`[
  {
    "barCode": "74002423"
  }
]`
    
```

 

`GET` request to `/sort/price`

The response code is 200 and the response body, when converted to JSON, is as follows:

`[
  {
    "barCode": "74002423"
  },
  {
    "barCode": "74001755"
  }
]`
  
```

## Preview

Implement REST APIs to perform filter and sort operations on a collection of P
