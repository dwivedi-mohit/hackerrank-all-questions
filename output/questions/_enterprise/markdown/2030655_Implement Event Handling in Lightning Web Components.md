# Implement Event Handling in Lightning Web Components

## Metadata

- **ID:** 2030655
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Easy, Salesforce Lightning Web Components
- **Skills:** Salesforce Apex

## Summary

This multiple choice question evaluates Salesforce Apex, Lightning Web Components, and event handling concepts, ideal for junior-level roles. The problem requires identifying the correct code snippet to update a message on a button click in a Salesforce LWC component.

## Problem Statement

In Salesforce Lightning Web Components (LWC), a developer needs to implement a button click event that updates a displayed message. The component should initially display 'Hello, World!' and upon clicking the button, it should change to 'Button Clicked!'. Assuming the component is correctly set up, which code snippet correctly implements this functionality?

HTML:
<template>
    <div>{message}</div>
    <button onclick={handleClick}>Click Me</button>
</template>

JavaScript:
import { LightningElement, track } from 'lwc';

export default class HelloWorld extends LightningElement {
    @track message = 'Hello, World!';

    handleClick() {
        // Implement the logic to update the message
    }
}
```

## Preview

In Salesforce Lightning Web Components (LWC), a developer needs to implement a b
