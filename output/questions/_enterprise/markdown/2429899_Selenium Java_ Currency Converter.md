# Selenium Java: Currency Converter

## Metadata

- **ID:** 2429899
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Selenium, Java, Easy, Form Handling, Dropdown Handling, Explicit Waits, Text Validation
- **Skills:** Selenium (Basic), Java (Basic)

## Summary

This Selenium automation question evaluates form handling, explicit waits, and text validation concepts, ideal for junior-level roles. The problem requires implementing a method to validate a currency conversion form's functionality and accuracy using Selenium.

## Problem Statement

In this challenge, implement Selenium automation code for a currency conversion form. The application features amount input, source/target currency dropdowns, and a dynamic result panel that updates in real time. The system uses an HtmlUnit headless browser for testing, eliminating the need for actual browser installations.

Hide animation
Show animation

Requirements

Implement the CurrencyConverterValidator.java class with the following method:

convertCurrencyAndValidateResult(String url, WebDriver driver, double amount, String sourceCurrency, String targetCurrency)

Implementation Requirements:

- Validate inputs: throw IllegalArgumentException if url is null/empty, driver is null, amount <= 0, or currency codes are null/empty

- Navigate to the provided URL and wait for the converter container #converter-container to load

- Input the amount into the amount field #amount-input

- Select the source currency from the dropdown #source-currency

- Select the target currency from the dropdown #target-currency

- Wait for the result container #result-container to become visible

- Extract the converted amount from #converted-amount and the exchange rate from #exchange-rate

- Format the input amount to 2 decimal places using String.format("%.2f", amount) before entering into the form

- Count decimal places in both the formatted input amount string and the result string from the DOM

- Validate accuracy: Math.abs(conversionResult - amount * rate) <= 0.01

- Validate decimal precision: result has 2 or more decimal places

- Validate result updates on dynamic change: modify the input amount, confirm the result updates dynamically by comparing before/after values, then reset the form to the original amount to ensure clean state

- Return a ConversionResult object with all fields populated:

- 
inputAmount: The exact amount that was entered into the #amount-input field (e.g., 100.0)

- 
sourceCurrency: The currency code selected from the source dropdown #source-currency (e.g., "USD")

- 
targetCurrency: The currency code selected from the target dropdown #target-currency (e.g., "EUR")

- 
conversionResult: The converted amount extracted from the #converted-amount element in the UI (e.g., 92.35)

- 
exchangeRate: The exchange rate extracted from the #exchange-rate element in the UI as a String, exactly as displayed (e.g., "0.9235" for different currencies, "1.0" for same-currency conversions)

- 
inputDecimalPlaces: The number of decimal places in the formatted input string (e.g., 2 for "100.00")

- 
resultDecimalPlaces: The number of decimal places counted from the conversion result string displayed in the UI (e.g., 2 for "92.35")

- 
conversionAccurate: true only if Math.abs(conversionResult - amount * rate) <= 0.01

- 
decimalPrecisionMaintained: true only if result has 2 or more decimal places

- 
resultUpdatedOnChange: true only if the result updates when input changes

- 
conversionComplete: true only if all above conditions are met

The example website is provided in the website folder, where you can view the structure of the Currency Converter UI. Your task is to complete the implementation of this method so that all unit tests pass successfully.

## Preview

In this challenge, implement Selenium automation code for a currency convers
