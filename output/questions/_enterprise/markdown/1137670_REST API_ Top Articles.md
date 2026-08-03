# REST API: Top Articles

## Metadata

- **ID:** 1137670
- **Type:** code
- **Difficulty:** 13.61111111111111
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** REST API, Back-End Development, Medium, JSON, HTTP, Sorting
- **Skills:** REST API (Intermediate)
- **Languages:** c, p, p, ,, c, s, h, a, r, p

## Summary

This coding question evaluates REST API, JSON handling, and sorting concepts, ideal for mid-level roles. The problem requires implementing a function to retrieve and sort article names based on comment counts and titles from a paginated API response.

## Problem Statement

Implement a function that retrieves the names of the top articles ordered by:

	
- Decreasing comment count
	
- Alphabetically decreasing (for articles with the same comment count)

The function should:

	
- Accept an integer parameter limit specifying the number of articles to return.
	
- Make HTTP GET requests to https://jsonmock.hackerrank.com/api/articles?page=<pageNumber> to retrieve article data (replace <pageNumber>).
	
- Navigate through all pages (page numbers range from 1 to the value of total_pages in the JSON response).
	
- Return an array of the top limit article names based on the specified ordering criteria.

 

The response is a JSON object with the following 5 fields.

	
- 
page: The current page of the results
	
- 
per_page: The maximum number of records returned per page.
	
- 
total: The total number of records on all pages of the result.
	
- 
total_pages: The total number of pages with results.
	
- 
data: An array of objects containing records returned on the requested page

Each record in data has the following schema.

	
- 
title: the title of the article, may be null
	
- 
url: the URL of the article
	
- 
author: the username of the author of the article
	
- 
num_comments: the number of comments the article has, may be null (no comments)
	
- 
story_id: identifier of the story related to the article, may be null
	
- 
story_title: the title of the story related to the article, may be null
	
- 
story_url: the URL of the story related to the article, may be null
	
- 
parent_id: identifier of the parent of the article,  may be null
	
- 
created_at: the date and time the record was created

 

First get the article name.

	
- If the title field is not null, use title.
	
- Otherwise, if the story_title field is not null, use story_title. 
	
- If both fields are null, ignore the article.

Sort the titles decreasing by comment count, then decreasing alphabetically by article name if there is a tie in comment count. Return a list of the top limit names.

 

Function Description

 

Complete the function topArticles in the editor with the following parameter(s):

    int limit: the number of articles to return

 

Returns

 

    string[limit]: the names of articles

 

Note: Please review the header in the code stub to see available libraries for API requests in the selected language. Required libraries can be imported in order to solve the question. Check our full list of supported libraries at https://www.hackerrank.com/environment.

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

In the first line, there is an integer limit.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

2
```

Sample Output

UK votes to leave EU
F.C.C. Repeals Net Neutrality Rules

```

Explanation

 

The limit value is 2 so return the names of the top two articles based on the number of comments. Those top articles are:

	
- 
title: F.C.C. Repeals Net Neutrality Rules, story_title: null, num_comments: 1397
	
- 
title: UK votes to leave EU, story_title: null, num_comments: 2531

 

Their names are their titles because they are not null. The second of these articles has more comments, so it comes first. There is not a tie for comment count so there is no need for a secondary sort key.

## Sample Input/Output

## Preview

Implement a function that retrieves the names of the top articles ordered by:
