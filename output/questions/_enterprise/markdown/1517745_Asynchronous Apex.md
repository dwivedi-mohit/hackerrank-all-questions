# Asynchronous Apex

## Metadata

- **ID:** 1517745
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Apex, SOQL, Salesforce, Medium, Asynchronous Apex
- **Skills:** Salesforce Apex

## Summary

This multiple choice question evaluates Salesforce Apex, SOQL, and asynchronous Apex concepts, ideal for mid-level roles. The problem requires determining the result of executing a batch class that processes Account records and sends an email upon completion.

## Problem Statement

What is the result of saving and executing this code?

 

batchClass.apxc

`public class batchClass implements Database.batchable{ 
   public Iterable start(Database.BatchableContext info){ 
       return new CustomAccountIterable(); 
   }     
   public void execute(Database.BatchableContext info, List<Account> scope){
       List<Account> accsToUpdate = new List<Account>();
       for(Account a : scope){ 
           a.Name = 'true'; 
           a.NumberOfEmployees = 70; 
           accsToUpdate.add(a); 
       } 
       update accsToUpdate; 
   }     
   public void finish(Database.BatchableContext info){     
	AsyncApexJob a = [SELECT Id, Status, NumberOfErrors, JobItemsProcessed,
      TotalJobItems, CreatedBy.Email
      FROM AsyncApexJob WHERE Id =
      :BC.getJobId()];
   Messaging.SingleEmailMessage mail = new Messaging.SingleEmailMessage();
   String[] toAddresses = new String[] {a.CreatedBy.Email};
   mail.setToAddresses(toAddresses);
   mail.setSubject('Apex Sharing Recalculation ' + a.Status);
   mail.setPlainTextBody
   ('The batch Apex job processed ' + a.TotalJobItems +
   ' batches with '+ a.NumberOfErrors + ' failures.');
   Messaging.sendEmail(new Messaging.SingleEmailMessage[] { mail });
   } 
}`
```

## Preview

What is the result of saving and executing this code?
