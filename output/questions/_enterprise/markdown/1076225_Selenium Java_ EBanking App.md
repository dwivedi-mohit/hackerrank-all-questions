# Selenium Java: EBanking App

## Metadata

- **ID:** 1076225
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Selenium, Easy, Java
- **Skills:** Selenium (Basic)

## Summary

This back-end development question evaluates Selenium, Java, and web driver concepts, ideal for junior-level roles. The problem requires implementing a method to fill out a loan application form and retrieve a secret code from the resulting page.

## Problem Statement

In this challenge, you will use the selenium web driver, HtmlUnitDriver, which uses HtmlUnit headless browser. This eliminates the need to set up browsers like Firefox, Chrome, or web driver executables like FirefoxDriver, or ChromeDriver.

 

You are given the URL to a dummy EBanking website that has an online loan application facility. Test this loan application page by filling the form. You are provided the data to fill the loan application.

 

There is a class `EBankingApp` which has a single method:

 

`String applyLoan(WebDriver driver, String loanPageUrl, LoanDetails loanDetails)`:

	
- Browse to the `loanPageUrl` and fill the fields using the `loanDetails` model object.

	
		
- Its source code structure is like `website/loanPage.html`

	
	
	
- Upon form submission, the server redirects you to another page containing a secret code in the body tag.
	
		
- The source code structure of the redirecting page is like `website/successPage.html`

	
	
	
- Return the secret code.

 

`loanDetails` is the model class which has the data to enter in the form.

 

There are tests for the correctness of each method. You can make use of these tests while debugging/checking your implementation. The test's setup method bootstraps an embedded jetty server and deploys a small web app that displays a randomly generated website. The example website is given in the `website` folder, where you can view the structure of the search and result pages, but the random data displayed will change on every refresh.

 

The provided loan page will look like:

 

Your task is to complete the implementation of `EBankingApp` to pass the unit tests.

	
- browse the `loanPageUrl` and fill all the fields using loanDetails model object.
	
- its source code structure is like `website/loanPage.html`
	
- upon form submission, server redirects you to another page containing a secret code in the body tag.
	
- source code structure of redirecting page is like `website/successPage.html`
	
- return that secret code.

 

where the `loanDetails` is the model class which has all the form data to be filled.

 

There are tests for testing correctness of each methods. So you can make use of these tests while debugging/checking your implementation. The test&#39;s setup method bootstraps an embedded jetty server and deploys small web app which displays randomly generated website. The example website is given in the `website` folder where you can view the structure of search and result page but data displayed are random and will change on every refresh.

 

The provided loan page will look like:

 

Your task is to complete the implementation of `EBankingApp` so that the unit tests pass while running the tests.

-->

## Preview

In this challenge, you will use the selenium web driver, HtmlUnitDriver, which
