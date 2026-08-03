# Implementing Data Display in Salesforce FlexCard

## Metadata

- **ID:** 2030702
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Easy, Basic FlexCard setup and data display, Salesforce Omnistudio Platform
- **Skills:** Salesforce Administration

## Summary

This multiple choice question evaluates basic FlexCard setup, data binding, and Salesforce Omnistudio concepts, ideal for junior-level roles. The problem requires identifying the issue preventing a FlexCard from displaying account information correctly.

## Problem Statement

In Salesforce Omnistudio, a developer is tasked with creating a FlexCard that displays account information. The FlexCard should fetch data from a DataRaptor and display the account name and account type. Given the following code snippet, identify the issue that prevents the FlexCard from displaying the data correctly.

{
  "flexCard": {
    "name": "AccountCard",
    "dataSource": {
      "type": "DataRaptor",
      "name": "AccountDataRaptor"
    },
    "elements": [
      {
        "type": "Text",
        "value": "{AccountName}"
      },
      {
        "type": "Text",
        "value": "{AccountType}"
      }
    ]
  }
}
```

## Preview

In Salesforce Omnistudio, a developer is tasked with creating a FlexCard that di
