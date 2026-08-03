# Webservices in Apex

## Metadata

- **ID:** 1517744
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Medium, Salesforce, Webservice in Apex, Apex
- **Skills:** Salesforce Apex

## Summary

This multiple choice question evaluates Salesforce Apex, web services in Apex, and account management concepts, ideal for mid-level roles. The problem requires determining the result of saving and executing a specific Apex code related to account creation.

## Problem Statement

What is the result of saving and executing this code?

 

`global class SpecialAccounts {
  global class AccountInfo {
     webservice String AcctName;
     webservice Integer AcctNumber;
  }

  webservice static Account createAccount(AccountInfo info) {
    Account acct = new Account();
    acct.Name = info.AcctName;
    acct.AccountNumber = String.valueOf(info.AcctNumber);
    insert acct;
    return acct;
  }

  webservice static Id [] createAccounts(Account parent, 
       Account child, Account grandChild) {
        insert parent;
        child.parentId = parent.Id;
        insert child;
        grandChild.parentId = child.Id;
        insert grandChild;
        Id [] results = new Id[3];
        results[0] = parent.Id;
        results[1] = child.Id;
        results[2] = grandChild.Id;
        return results;
    }
}
`
```

## Preview

What is the result of saving and executing this code?
