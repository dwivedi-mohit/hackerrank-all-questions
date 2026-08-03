# Selenium Java: Contact Scraping

## Metadata

- **ID:** 894638
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Selenium, QA, Java, Medium
- **Skills:** Selenium (Intermediate), Testing Techniques

## Summary

This back-end development question evaluates Selenium, testing techniques, and web scraping concepts, ideal for mid-level roles. The problem requires implementing methods to extract unique email addresses and mobile numbers from a web page using the Selenium WebDriver.

## Problem Statement

In this challenge, you will use the Selenium WebDriver with HtmlUnitDriver. This implementation does not require browser setup or web driver executables. Web pages contain web elements (DOM objects) with unique names or identifiers.

 

The WebScraper class has two methods to implement:

	
- 
scrapeEmailAddresses:

	
		
- Extracts all unique email addresses present on the given page
		
- An email address must contain the @ character
		
- Valid examples: P@P.IJ, as@as.lA, Gnoy@Gnoy.ki, r@r.yd
		
- Returns a list of email addresses
	
	
	
- 
scrapeMobileNumbers:
	
		
- Extracts all unique mobile numbers present on the given page
		
- A mobile number must contain exactly 10 digits
		
- Valid examples: 8853248887, 1435416774, 8467324364, 1748528383
		
- Returns a list of string mobile numbers
	
	

Both methods accept two parameters: a web driver and a web page URL.

 

 

Hint: The DOM structure of the given page will match website/home.html as shown. You can examine the source code of this file to understand the HTML structure. The content will differ with each test run.

 

Your task is to implement these two methods so that all unit tests pass.

 

Example actions

`
//initialize web driver
WebDriver driver = new HtmlUnitDriver();

//find input elements inside form
List elements = WebScraper.scrapeEmailAddresses(driver, "http://localhost:8080/home.html");

//Print
System.out.println("Elements:"  + elements);
`

```

## Preview

In this challenge, you will use the Selenium WebDriver with HtmlUnitDriver. Th
