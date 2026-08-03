# Wikipedia Article

## Metadata

- **ID:** 2013334
- **Type:** approx
- **Difficulty:** 8.88888888888889
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** REST API, Back-End Development, JSON, Interviewer Guidelines, Medium
- **Skills:** REST API (Intermediate)
- **Languages:** c, s, h, a, r, p, ,, g, o, ,

## Summary

This approximate solution question evaluates REST API, JSON handling, and string manipulation concepts, ideal for mid-level roles. The problem requires writing an HTTP GET method to retrieve and count occurrences of a topic in a Wikipedia article's text.

## Problem Statement

Write an HTTP GET method to retrieve information from Wikipedia.

Using an HTTP GET method, retrieve information from Wikipedia using a given topic. Query https://en.wikipedia.org/w/api.php?action=parse&section=0&prop=text&format=json&page=[topic] to get the topic Wikipedia article. Return the total number of times that the string [topic] appears in the article's text field.

 

Notes:

	
- The search is case-sensitive.
	
- Your request needs a user-agent string: 
	

`{"User-Agent": "hrw/1.0 (contact: support@hackank.com) requests/{requests.__version__}"}`
```

	 

 

The query response from the website is a JSON object described below:

	
- 
parse: A JSON object representing the article's parsed web page. It has the following three fields:

	
		
- 
title: The article's title, as specified by the argument topic

		
- 
pageid: The article's Page ID
		
- 
text: A JSON object that contains the Wikipedia article as an HTML dump
	
	

 

Function Description

Complete the function getTopicCount in the editor below.

 

getTopicCount has the following parameter(s):

    topic: a string to query

 

Returns:

    int: the number of times the search term topic appears in the returned text field

 

Note: Please review the header in the code stub to see available libraries for API requests in the selected language. Required libraries can be imported in order to solve the question. Check our full list of supported libraries at https://www.hackerrank.com/environment.

	
		
			Name
			Type
			Description
		
		
			topic
			string
			The topic to query for.
		
	

 

The function must query https://en.wikipedia.org/w/api.php?action=parse&section=0&prop=text&format=json&page=topic (where topic is the value of topic) to get the topic Wikipedia article and then return an integer denoting the total number of times that the string topic appears in the article&#39;s text. Note that the comparison here is case-sensitive. The query response from the website is a JSON response with the following fields:

 

	
- parse: A JSON object representing the article&#39;s parsed web page. It has the following three fields:

	
		
- title: The article&#39;s title, as specified by the argument passed as topic.
		
- pageid: The article&#39;s Page ID.
		
- text: A JSON object containing the Wikipedia article as an HTML dump. We want to know the number of times the string topic occurs here.
	
	

--> DO NOT REMOVE THIS LINE-->

Input Format for Custom Testing

Input from stdin will be processed as follows and passed to the function.

 

The first line contains a string topic.

Sample Case 0

Sample Input

STDIN     Function
-----     -----
pizza  →  topic = 'pizza'
```

 

Sample Output*

149
```

*Note that because this question is dynamically getting the data from Wikipedia, the actual number of occurrences may have changed. 149 is only used as an example. 

 

Explanation

The query is https://en.wikipedia.org/w/api.php?action=parse&section=0&prop=text&format=json&page=pizza and the response is:

{
  "parse": {
    "title": "Pizza",
    "pageid": 24768,
    "text": {
      "*": "<div role=\"note\" class=\"hatnote\">For other uses, see <a href=\"\/wiki\/Pizza_(disambiguation)\" class=\"mw-disambig\" title=\"Pizza (disambiguation)\">Pizza (disambiguation)<\/a>.<\/div>\n<table class=\"infobox hrecipe adr\" style=\"width:22em\">\n<caption class=\"fn\"><span>Pizza<\/span><\/caption>\n<tr>\n<td colspan=\"2\" style=\"text-align:center\"><a href=\"\/wiki\/File:Pepperoni_pizza.jpg\" class=\"image\"><img alt=\"Pepperoni pizza.jpg\" src=\"\/\/upload.wikimedia.org\/wikipedia\/commons\/thumb\/d\/d1\/Pepperoni_pizza.jpg\/220px-Pepperoni_pizza.jpg\" width=\"220\" height=\"139\" srcset=\"\/\/upload.wikimedia.org\/wikipedia\/commons\/thumb\/d\/d1\/Pepperoni_pizza.jpg\/330px-Pepperoni_pizza.jpg 1.5x, \/\/upload.wikimedia.org\/wikipedia\/commons\/thumb\/d\/d1\/Pepperoni_pizza.jpg\/440px-Pepperoni_pizza.jpg 2x\" data-file-width=\"959\" data-file-height=\"606\" \/><\/a>\n<div style=\"padding-bottom:0.25em;border-bottom:1px solid #aaa;\">Pizza topped with <a href=\"\/wiki\/Pepperoni\" title=\"Pepperoni\">pepperoni<\/a><\/div>\n<\/td>\n<\/tr>\n<tr>\n<th scope=\"row\" style=\"padding-top:0.245em;line-height:1.15em; padding-right:0.65em;\">Type<\/th>\n<td><a href=\"\/wiki\/Flatbread\" title=\"Flatbread\">Flatbread<\/a><\/td>\n<\/tr>\n<tr>\n<th scope=\"row\" style=\"padding-top:0.245em;line-height:1.15em; padding-right:0.65em;\">Course<\/th>\n<td>Lunch or dinner<\/td>\n<\/tr>\n<tr class=\"note\">\n<th scope=\"row\" style=\"padding-top:0.245em;line-height:1.15em; padding-right:0.65em;\">Place of origin<\/th>\n<td class=\"country-name\"><a href=\"\/wiki\/Naples\" title=\"Naples\">Naples<\/a>, <a href=\"\/wiki\/Campania\" title=\"Campania\">Campania<\/a>, <a href=\"\/wiki\/Italy\" title=\"Italy\">Italy<\/a><\/td>\n<\/tr>\n<tr>\n<th scope=\"row\" style=\"padding-top:0.245em;line-height:1.15em; padding-right:0.65em;\">Serving temperature<\/th>\n<td>Hot or warm<\/td>\n<\/tr>\n<tr>\n<th scope=\"row\" style=\"padding-top:0.245em;line-height:1.15em; padding-right:0.65em;\">Main ingredients<\/th>\n<td class=\"ingredient\">Dough, often <a href=\"\/wiki\/Tomato_sauce\" title=\"Tomato sauce\">tomato sauce<\/a>, <a href=\"\/wiki\/Cheese\" title=\"Cheese\">cheese<\/a><\/td>\n<\/tr>\n<tr>\n<th scope=\"row\" style=\"padding-top:0.245em;line-height:1.15em; padding-right:0.65em;\">Variations<\/th>\n<td><a href=\"\/wiki\/Calzone\" title=...
    }
  }
}

```

 

As of April, 2020, the word 'pizza' occurs 149 times in the HTML dump of the response article (i.e., text ) from Wikipedia.

## Sample Input/Output

## Preview

Write an HTTP GET method to retrieve information from Wikipedia.
