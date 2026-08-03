# Implementing Data Binding in Salesforce Lightning Aura Components

## Metadata

- **ID:** 2030724
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Easy, Salesforce Lightning Aura Components, Simple Data Binding Between Components
- **Skills:** Salesforce Apex

## Summary

This multiple choice question evaluates Salesforce Apex, data binding, and component interaction concepts, ideal for junior-level roles. The problem requires identifying the correct implementation of data binding between a parent and child component in Salesforce Lightning Aura.

## Problem Statement

In a Salesforce Lightning Aura Component, a developer needs to implement simple data binding between two components: a parent component and a child component. The parent component holds a list of contact names, and the child component displays these names. The developer wants to ensure that any changes to the list in the parent component are automatically reflected in the child component. Given the following code snippets, identify the correct implementation of data binding that achieves this requirement.

Parent Component (ParentComponent.cmp):
<aura:component>
    <aura:attribute name="contactList" type="List" default="[]"/>
    <c:ChildComponent contactList="{!v.contactList}"/>
    <ui:button label="Add Contact" press="{!c.addContact}"/>
</aura:component>

Parent Component Controller (ParentComponentController.js):
({
    addContact: function(component, event, helper) {
        var contactList = component.get("v.contactList");
        contactList.push('New Contact');
        component.set("v.contactList", contactList);
    }
})

```

## Preview

In a Salesforce Lightning Aura Component, a developer needs to implement simple
