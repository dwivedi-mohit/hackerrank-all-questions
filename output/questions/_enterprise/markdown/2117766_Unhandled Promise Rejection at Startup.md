# Unhandled Promise Rejection at Startup

## Metadata

- **ID:** 2117766
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Medium, Error Handling, Node.js, Promises, Startup
- **Skills:** Node.js (Intermediate)

## Summary

This multiple choice question evaluates error handling, promises, and Node.js concepts, ideal for mid-level roles. The problem requires identifying the simplest way to prevent a crash due to an unhandled promise rejection when starting Node.js services.

## Problem Statement

You start your Node.js services like this:

initializeDatabase()
  .then(() => console.log('DB ready'));

```

If the database fails to connect, the promise is rejected and the process crashes with an unhandled rejection.
What is the simplest way to prevent that crash?

## Preview

You start your Node.js services like this:
