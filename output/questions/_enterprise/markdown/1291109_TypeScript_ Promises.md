# TypeScript: Promises

## Metadata

- **ID:** 1291109
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Medium, TypeScript, Promises
- **Skills:** TypeScript (Intermediate)

## Summary

This multiple choice question evaluates TypeScript, promises, and asynchronous programming concepts, ideal for mid-level roles. The problem requires determining what is logged to the console by a TypeScript code snippet involving promises.

## Problem Statement

What is logged to the console by this TypeScript code snippet?

 

`import { Promise } from 'es6-promise'

const promise: Promise<string> = new Promise((resolve, reject) => {
	setTimeout(() => {
		reject("Promise Rejected from TimeOut")
	}, 0)
	resolve("Promise Resolved")

	setTimeout(() => {
		resolve("Promise Resolved from TimeOut")
	}, 0)
	console.log("End of Promise")
});

promise.then(data => console.log(data)).catch(err => console.log(err))

`
```

## Preview

What is logged to the console by this TypeScript code snippet?
