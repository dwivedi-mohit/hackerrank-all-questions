# REST API: Root Threshold in IOT Devices

## Metadata

- **ID:** 724559
- **Type:** code
- **Difficulty:** 12.777777777777779
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** REST API, Back-End Development, Medium, JSON, Interviewer Guidelines, Date, HTTP
- **Skills:** REST API (Intermediate)
- **Languages:** c, s, h, a, r, p, ,, g, o, ,

## Summary

This coding question evaluates REST API, JSON handling, and data filtering concepts, ideal for mid-level roles. The problem requires querying a REST API to count IoT devices based on specific criteria related to status, threshold, and date.

## Problem Statement

A REST API contains information about a collection of IoT devices. Given a string statusQuery, numerical threshold value, and date in format MM-YYYY, query the API to get a list of devices. Return the total number of devices that:

	
- Were added to the collection during the given month and year
	
- Have a root threshold > threshold

Make an HTTP GET request to https://jsonmock.hackerrank.com/api/iot_devices/search?status=<statusQuery>&page=<pageNumber> (replace <statusQuery> and <pageNumber>). It will return all items with statusQuery as a substring of their status.

 

The response JSON has fields:

	
- 
page: The current page
	
- 
per_page: Maximum devices returned per page
	
- 
total: Total number of devices
	
- 
total_pages: Total number of pages
	
- 
data: Array of device information objects

Each device object has:

	
- 
id: Unique device ID
	
- 
timestamp: UTC milliseconds when the device was added
	
- 
status: Device status
	
- 
operatingParams: Object containing operating parameters
	
- 
asset: Object with asset information
	
- 
parent: Optional object with parent information

The operating parameters object has:

	
- 
rotorSpeed: Device rotor speed
	
- 
slack: Device slack
	
- 
rootThreshold: Device root threshold

The asset object has:

	
- 
id: Unique asset ID
	
- 
alias: Asset alias

The parent object has:

	
- 
id: Unique parent ID
	
- 
alias: Parent alias

 

Function Description 

Complete the function numDevices in the editor with the following parameter(s):

    string statusQuery: the status substring to query

    int threshold: the threshold value

    string dateStr: in format MM-YYYY, the month and the year to query for

 

Returns 

    int: the number of matching devices

 

Note: Please review the header in the code stub to see available libraries for API requests in the selected language. Required libraries can be imported in order to solve the question. Check our full list of supported libraries at https://www.hackerrank.com/environment.

 DO NOT REMOVE THIS LINE-->
Input Format For Custom Testing

In the first line, there is a string statusQuery.

In the second line, there is an integer threshold.

In the third line, there is a string dateStr.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

STOPPED
45
04-2019

```

Sample Output

3
```

Explanation

The statusQuery is "STOPPED", the threshold value is 45, and we are interested in the devices added to the collection in April 2019. There are a total of 3 devices.

 DO NOT REMOVE THIS LINE--> DO NOT REMOVE THIS LINE-->

## Sample Input/Output

## Preview

A REST API contains information about a collection of IoT devices. Given a str
