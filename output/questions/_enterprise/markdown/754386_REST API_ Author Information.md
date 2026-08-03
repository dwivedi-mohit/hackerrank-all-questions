# REST API: Author Information

## Metadata

- **ID:** 754386
- **Type:** code
- **Difficulty:** 9.166666666666668
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** REST API, Back-End Development, Medium, JSON, Interviewer Guidelines
- **Skills:** REST API (Intermediate)
- **Languages:** c, p, p, ,, c, s, h, a, r, p

## Summary

This coding question evaluates REST API, JSON handling, and pagination concepts, ideal for mid-level roles. The problem requires creating an HTTP GET method to fetch author information and articles, handling multiple pages of data.

## Problem Statement

Create an HTTP GET method to fetch information from the articles and article_users databases. The data may span multiple pages, accessible by appending &page=num, where num is the page number.

 

Function Description

Given a string of author, getAuthorHistory must perform the following tasks:

	
- Initialize the history array to store a list of string elements. 
	
- Query https://jsonmock.hackerrank.com/api/article_users?username=<authorName>(replace <authorName>) to retrieve author information in the  data field.
	
- Store the value of the about field from the query response.  If the about field is empty or null, do not store a value for this item.
	
- Query https://jsonmock.hackerrank.com/api/articles?author=<authorName>(replace <authorName>), to retrieve the list of author's articles in the data field.
	
- Add the title from each record returned in the data field to the history array. 
	
		
- If the title field is null or empty then use the story_title to add in the history array.
		
- If the title and story_title fields are null or empty then ignore the record to add in the history array.
	
	
	
- Based on the total_pagescount, fetch all the data (pagination), and repeat steps 4 and 5.
	
- Return the history array.

 

The query response from the website is a JSON response with the following five fields:

	
- 
page: the current page
	
- 
per_page: the maximum number of results per page
	
- 
total: the total number of records in the search result
	
- 
total_pages: the total number of pages which must be queried to get all the results
	
- 
data: an array of JSON objects that contain article information

 

Note: Please review the header in the code stub to see available libraries for API requests in the selected language. Required libraries can be imported in order to solve the question. Check our full list of supported libraries at https://www.hackerrank.com/environment.

 DO NOT REMOVE THIS LINE-->

Schema

There are 2 tables: ARTICLE_USERS and ARTICLES.

ARTICLE_USERS

	
		
			ARTICLE_USERS
		
		
			Name
			Type
			Description
		
		
			id
			LONG
			This is the first column. unique identifier number for the article user
		
		
			username
			STRING
			the author-name 
		
		
			about
			STRING
			description (about) of the author 
		
		
			submission_count
			LONG
			total number of submission
		
		
			comment_count
			LONG
			total number of comments for the articles
		
		
			created_at
			STRING
			created time of the article
		
		
			updated_at
			LONG
			updated time of the article
		
	

	
		
			ARTICLES
		
		
			Name
			Type
			Description
		
		
			title
			STRING
			the title of the article
		
		
			url
			STRING
			URL of the article
		
		
			author
			STRING
			the author name of the article 
		
		
			num_comments
			LONG
			total number of comments  
		
		
			story_id
			LONG
			unique identifier number for the article
		
		
			story_title
			STRING
			an additional title for the article
		
		
			story_url
			STRING
			an additional URL for the article
		
		
			parent_id
			LONG
			unique identifier number of the parent article
		
		
			created_at
			LONG
			created time of the article
		
	

 

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

epaga
```

Sample Output

Java developer / team leader at inetsoftware.de by day<p>iOS developer by night<p>https://www.mindscopeapp.com<p>https://inflightassistant.info<p>https://appstore.com/johngoering<p>[ my public key: https://keybase.io/johngoering; my proof: https://keybase.io/johngoering/sigs/I1UIk7t3PjfB5v2GI-fhiOMvdkzn370_Z2iU5GitXa0 ]<p>hnchat:oYwa7PJ4Yaf1Vw9Om4ju
A Message to Our Customers
“Was isolated from 1999 to 2006 with a 486. Built my own late 80s OS”
Apple’s declining software quality
```

 

Explanation

	
		
			ARTICLE_USERS
		
		
			id
			username
			about
			submission_count
			comment_count
		
		
			1
			epaga
			Java developer / team leader at inetsoftware.de by day<p>iOS developer by night<p>https://www.mindscopeapp.com<p>https://inflightassistant.info<p>https://appstore.com/johngoering<p>[ my public key: https://keybase.io/johngoering; my proof: https://keybase.io/johngoering/sigs/I1UIk7t3PjfB5v2GI-fhiOMvdkzn370_Z2iU5GitXa0 ]<p>hnchat:oYwa7PJ4Yaf1Vw9Om4juJava developer / team leader at inetsoftware.de
			654
			197
		
		
			
			
3

			
			saintamh
			 
			
			
4

			
			4
		
		
			5
			olalonde
			olalonde@gmail.com<p>https://www.github.com/olalonde<p>CTO/Co-Founder @ https://binded.com
			1032
			3045
		
	

 

	
		
			ARTICLE
		
		
			title
			url
			author
			num_comments
			story_id
			story_title
			story_url
		
		
			
			
A Message to Our Customers

			
			null
			
			
epaga

			
			
			
967

			
			null
			null
			null
		
		
			
			
“Was isolated from 1999 to 2006 with a 486. Built my own late 80s OS”

			
			null
			
			
epaga

			
			
			
265

			
			null
			null
			null
		
		
			
			
Google Is Eating Our Mail

			
			null
			saintamh
			
			
685

			
			null
			null
			null
		
		
			
			
null

			
			
			
null

			
			epaga
			705
			null
			Apple’s declining software quality
			null
		
		
			Show HN: This up votes itself
			null
			olalonde
			83
			null
			null
			null
		
		
			Why I’m Suing the US Government
			null
			saintamh
			305
			null
			null
			null
		
	

Sample Case 1

Sample Input For Custom Testing

saintamh
```

Sample Output

Google Is Eating Our Mail
Why I’m Suing the US Government
```

Explanation

	
		
			ARTICLE_USERS
		
		
			id
			username
			about
			submission_count
			comment_count
		
		
			1
			epaga
			Java developer / team leader at inetsoftware.de by day<p>iOS developer by night<p>https://www.mindscopeapp.com<p>https://inflightassistant.info<p>https://appstore.com/johngoering<p>[ my public key: https://keybase.io/johngoering; my proof: https://keybase.io/johngoering/sigs/I1UIk7t3PjfB5v2GI-fhiOMvdkzn370_Z2iU5GitXa0 ]<p>hnchat:oYwa7PJ4Yaf1Vw9Om4juJava developer / team leader at inetsoftware.de
			654
			197
		
		
			
			
3

			
			saintamh
			 
			
			
4

			
			4
		
		
			5
			olalonde
			olalonde@gmail.com<p>https://www.github.com/olalonde<p>CTO/Co-Founder @ https://binded.com
			1032
			3045
		
	

 

	
		
			ARTICLE
		
		
			title
			url
			author
			num_comments
			story_id
			story_title
			story_url
		
		
			
			
A Message to Our Customers

			
			null
			
			
epaga

			
			
			
967

			
			null
			null
			null
		
		
			
			
“Was isolated from 1999 to 2006 with a 486. Built my own late 80s OS”

			
			null
			
			
epaga

			
			
			
265

			
			null
			null
			null
		
		
			
			
Google Is Eating Our Mail

			
			null
			saintamh
			
			
685

			
			null
			null
			null
		
		
			
			
null

			
			
			
null

			
			epaga
			705
			null
			Apple’s declining software quality
			null
		
		
			Show HN: This up votes itself
			null
			olalonde
			83
			null
			null
			null
		
		
			Why I’m Suing the US Government
			null
			saintamh
			305
			null
			null
			null

## Sample Input/Output

## Preview

Create an HTTP GET method to fetch information from the articles and article_u
