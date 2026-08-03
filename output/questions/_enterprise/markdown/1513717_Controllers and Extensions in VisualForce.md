# Controllers and Extensions in VisualForce

## Metadata

- **ID:** 1513717
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Medium, VisualForce Tags, Salesforce, Controller and Extensions, VisualForce

## Summary

This multiple choice question evaluates Visualforce tags, Salesforce controllers and extensions, and debugging concepts, ideal for mid-level roles. The problem requires predicting the outcome of saving and previewing a Visualforce page with specific controller logic.

## Problem Statement

What will be the outcome when the developer tries to save and preview it?

 

Sample.vfp

 

`<apex:page Controller="Account" extensions="AccountExt">
    <apex:form >
           <apex:pageBlock title="Page Block 1">

            <apex:pageBlockSection title="Page Block Section 1 | Custom Controller Example" Columns="2">

                <apex:pageBlockSectionItem ><Apex:commandButton value="Greeting" reRender="id1" Action="{!ShowGreeting}"/></apex:pageBlockSectionItem>

                <apex:pageBlockSectionItem ><Apex:outPutLabel id="id1">  </Apex:outPutLabel> </apex:pageBlockSectionItem>

            </apex:pageBlockSection>
        </apex:pageBlock>
    </apex:form>
</apex:page>`
```

 

Account.apxc

 

`public class Account
{
   
     public static void ShowGreeting() {
       
         inernaltest();
         System.debug('controller' );
         
    }
    public static void inernaltest()
    {
         System.debug('Internal controller ');
    }
}`
```

 

AccountExt.apxc

 

`public class AccountExt {
    public Account12(Account1 Controller)
    {
       //write some code to execute at the start
    }
   
    public static void inernaltest()
    {
         System.debug('Internal Extension ');
    }

     public static void ShowGreeting() {
         inernaltest();
         System.debug('Extension ');      
    }
}`
```

## Preview

What will be the outcome when the developer tries to save and preview it?
