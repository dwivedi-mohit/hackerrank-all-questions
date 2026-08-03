# Selenium Java: Data Validation

## Metadata

- **ID:** 1131690
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Selenium, QA, Medium, Java, Data Validation
- **Skills:** Selenium (Intermediate), Testing Techniques

## Summary

This back-end development question evaluates Selenium, testing techniques, and data validation concepts, ideal for mid-level roles. The problem requires verifying the accuracy of displayed percentages on a web analytics site against dynamic detail page data.

## Problem Statement

In this challenge, you are going to use selenium web driver, the HtmlUnitDriver, which uses HtmlUnit headless browser. So you neither need to setup the browsers like Firefox, Chrome nor a web driver executables like FirefoxDriver, ChromeDriver. You are given a dummy internet usage analytics website which displays percentage of users distributed across popular sites.

	
- the top level page, `index.html`, shows a bar graph showing the percentage of users for each sites upon hovering.
	
- clicking on a bar takes you to another page which shows the sites and corresponding number of users.
	
- your task is to verify that the displayed percentage of a site is correct as per the details page.
	
- for example, the graphs is showing 18% for Facebook, verify that 18% is correct as per details page.
	
- to find the correct percentage for a site, you can sum users of each site to find total and then find the percentage of a site.
	
- data shown in the details page are dynamic so changes upon page refresh.

 

The given project lacks a few implementations and you have to complete the them.

 

There is a class `DataValidator.java` which has a method:

 

`boolean verifyPercentage(String indexPage, String site, WebDriver driver)`:

	
- browser the page `indexPage`

	
- hover over the `site` bar and find its percentage
	
- click on it and go to details page
	
- calculate the correct percentage of the `site`

	
- if the given percentage matches with the calculated, return true else false

 

There are tests for testing correctness of implementation. So you can make use of these tests while debugging/checking your implementation. The example website is given in the `website` folder where you can view the structure of index and details pages.

 

The index page will look like:

 

And the details page will look like:

Your task is to complete the implementation of the method so that the unit tests pass while running the tests.

## Preview

In this challenge, you are going to use selenium web driver, the HtmlUnitDrive
