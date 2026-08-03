# REST API: Get IOT devices by Parent Id

## Metadata

- **ID:** 724561
- **Type:** code
- **Difficulty:** 8.333333333333334
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** REST API, Back-End Development, Medium, JSON, Interviewer Guidelines
- **Skills:** REST API (Intermediate)
- **Languages:** c, s, h, a, r, p, ,, g, o, ,

## Summary

This coding question evaluates REST API, JSON handling, and data processing concepts, ideal for mid-level roles. The problem requires calculating the average rotor speed of IoT devices based on a status query and parent identifier from a REST API response.

## Problem Statement

In this challenge, the REST API provides information about a collection of IoT devices. Given a status query and the identifier of a parent device, your task is to calculate the average rotor speed of available IoT devices that match the specified status and parent identifier.

 

To access the collection of devices, perform an HTTP GET request to:

https://jsonmock.hackerrank.com/api/iot_devices/search?status=<statusQuery>&page=<pageNumber>

where <statusQuery> is a given string to query and <pageNumber> is the page number of the results to return.

 

For example, GET request to:

https://jsonmock.hackerrank.com/api/iot_devices/search?status=STOP&page=2

will return the second page of the devices with their status containing "STOP".

 

The response is JSON with the following 5 fields:

	
- 
page: The current page of the results
	
- 
per_page: The maximum number of devices returned per page.
	
- 
total: The total number of devices available on all pages of the result.
	
- 
total_pages: The total number of pages with results.
	
- 
data: An array of objects containing devices returned on the requested page

 

Each device object has the following schema:

	
- 
id: The unique ID of the device
	
- 
timestamp: The timestamp when the device was added to the collection, in UTC milliseconds
	
- 
status: The status of the device
	
- 
operatingParams: the object containing the operating parameters of the device
	
- 
asset: The object containing information about the asset of the device
	
- 
parent: Optional. The object containing information about the parent of the device

 

The operating parameters object has the following schema:

	
- 
rotorSpeed: The rotor speed of the device
	
- 
slack: The slack in the device
	
- 
rootThreshold: The root threshold for the device

 

The asset object has the following schema:

	
- 
id: The unique ID of the asset
	
- 
alias: The alias for the asset

 

The parent object, if it is present, will have one or both of the following fields:

	
- 
id: The unique ID of the parent of the asset
	
- 
alias: The alias for the parent of the asset

 

Given string statusQuery, and numerical parentId value, the goal is to return the floor of the average rotor speed of all returned devices with whose parent identifier matches the parentId value. If there are no devices matching the given criteria, the result must be 0.

 

 

Function Description 

Complete the function avgRotorSpeed in the editor with the following parameter(s):

    string statusQuery: string to query for

    int parentId: id of the parent to match

 

Returns:

    int: the floor of the average rotor speed of matching devices or 0 if there are none

 

Note: Please review the header in the code stub to see available libraries for API requests in the selected language. Required libraries can be imported in order to solve the question. Check our full list of supported libraries at https://www.hackerrank.com/environment.

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

In the first line, there is a string statusQuery.

In the second line, there is an integer parentId.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

RUNNING
7

```

Sample Output

3880
```

Explanation

The status query is "RUNNING", and the parent identifier is 7, so we are interested in the average rotor speed of all returned devices having a parent identifier of 7. There are 4 such devices, and their rotor speeds are 4721, 4446, 1592, and 4761, respectively. Their average rotor speed is (4721 + 4446 + 1592 + 4761)/4 = floor(15520/4) = 3880.

## Sample Input/Output

## Preview

In this challenge, the REST API provides information about a collection of IoT
