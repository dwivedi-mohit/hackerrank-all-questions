# Selenium .NET: EBanking App

## Metadata

- **ID:** 1253350
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Selenium, QA, Easy
- **Skills:** Selenium (Basic), .NET (Basic), Testing Techniques

## Summary

This back-end development question evaluates Selenium, .NET, and testing techniques concepts, ideal for junior-level roles. The problem requires implementing a method to automate loan application testing on a dummy EBanking website using Selenium's ChromeDriver.

## Problem Statement

In this challenge, you will use the selenium ChromeDriver with headless driver options which eliminates the need to set up browsers like Firefox, Chrome, or Edge.

 

You are given the URL to a dummy EBanking website that has an online loan application facility. Test this loan application page by filling out the form. You are provided the data to fill the loan application.

 

There is a class EBankingApp which has a single method:

 

 public static string applyLoan(IWebDriver driver,

            string fullyQualifiedUrlLoan, LoanDetails loanDetails);

	
- Browse to the loanPageUrl and fill the fields using the loanDetails model object.

	
		
- Its source code structure is like eBankingApp/Views/Home/Index.cshtml

	
	
	
- Upon form submission, the server redirects you to another page containing a secret code in the DIV tag with Id = hashCodeValue.
	
		
- The source code structure of the redirecting page is like eBankingApp/Views/Home/Success.cshtml

	
	
	
- Return the secret code.

 

loanDetails is the model class which has the data to enter in the form.

 

There are tests for the correctness of each method. You can make use of these tests while debugging/checking your implementation. The test's setup method bootstraps an embedded test server and deploys a small web app that displays a randomly generated website. The example website is given in the CustomWebApplicationFactory.cs class of eBankingAppTests folder which eventually render to Loan Page url viewed under eBankingApp/Views/Home/Index.cshtml structure.

 

The provided loan page will look like:

 

Under eBankingTests/TestSetUp/ there is a read only test class : IntegrationTestFixtures.cs which contains 3 test methods.

Your main requirement is to complete the implementation of applyLoan method present under the structure eBankingTests/EBankingApp.cs.

Your applyLoan method implementation will be such that all the test methods will be passed for IntegrationTestFixtures.cs.

## Preview

In this challenge, you will use the selenium ChromeDriver with headless driver
