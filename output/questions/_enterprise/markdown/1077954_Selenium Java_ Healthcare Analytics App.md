# Selenium Java: Healthcare Analytics App

## Metadata

- **ID:** 1077954
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Selenium, QA, Easy, Java, Healthcare Analytics
- **Skills:** Selenium (Basic), Testing Techniques

## Summary

This back-end development question evaluates Selenium, testing techniques, and web automation concepts, ideal for junior-level roles. The problem requires verifying the accuracy of total paid amounts for patients in a healthcare analytics application using the Selenium web driver.

## Problem Statement

In this challenge, use the selenium web driver, HtmlUnitDriver, which uses HtmlUnit headless browser. This eliminates the need to set up browsers such as Firefox, Chrome, or web driver executables like FirefoxDriver, or ChromeDriver.

 

Given a URL for a dummy healthcare data analytics web application that shows the patients' data in a table, verify that each member's total paid amount is the sum of that member's claims amount by drilling down on the member's "Total Paid Amount" column and performing a summation of the values.

 

A class `HealthcareAnalytics` has a single method:

 

`List<String> findAmountMismatchedPatients(WebDriver driver, String patientPageUrl)`:

	
- Browse the `patientPageUrl` and drill down on each member's total paid amount column.

	
		
- The source code structure of `patientPageUrl` is like `website/patientsPage.html`.
	
	
	
- Upon drilling down on the total paid amount of a member, another page opens up that contains a table of the member's claims data.
	
		
- The source code structure of claims data is like `website/claimsPage.html`

	
	
	
- For each member, sum the "Total Paid Amount" column for their claims.
	
- Return the members whose total paid amount before drill down does not match with the sum of claims amounts after drill down.

 

`patientPageUrl` is the URL of the patients' aggregated data.

 

Use the given tests while debugging/checking implementation. The test's setup method bootstraps an embedded jetty server and deploys a small web app that displays a randomly generated website. The example website is given in the `website` folder, which displays the structure of the search and result pages, but the random data displayed will change on every refresh.

 

The patients page:

 

The claims page:

 

Complete the implementation of `HealthcareAnalytics` to pass the unit tests.

## Preview

In this challenge, use the selenium web driver, HtmlUnitDriver, which uses Htm
