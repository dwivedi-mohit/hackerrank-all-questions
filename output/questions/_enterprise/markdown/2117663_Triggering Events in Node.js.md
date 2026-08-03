# Triggering Events in Node.js

## Metadata

- **ID:** 2117663
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Easy, Events, Node.js, Event Emitter
- **Skills:** Node.js (Basic)

## Summary

This multiple choice question evaluates event handling, Node.js, and event emitters concepts, ideal for junior-level roles. The problem requires identifying the correct method to trigger a custom event in a user authentication system using Node.js.

## Problem Statement

You're building a user authentication system and want to emit custom events when users log in.

const EventEmitter = require('events');
const authEmitter = new EventEmitter();

authEmitter.on('userLogin', (username) => {
    console.log(`User ${username} logged in`);
});

// Trigger the event
authEmitter._____('userLogin', 'john_doe');
```

What method should fill the blank to trigger the 'userLogin' event in Node.js?

## Preview

You're building a user authentication system and want to emit custom events when
