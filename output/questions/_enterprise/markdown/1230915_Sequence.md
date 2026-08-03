# Sequence

## Metadata

- **ID:** 1230915
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Angular, Easy
- **Skills:** Angular (Basic)

## Summary

This multiple choice question evaluates observables, asynchronous programming, and Angular concepts, ideal for junior-level roles. The problem requires determining the output sequence of a code snippet involving an Observable in Angular.

## Problem Statement

What is the output of this code snippet?

 

`import { Observable } from 'rxjs';
 
var observable = new Observable(function subscribe(subscriber) {
   subscriber.next("One");
   subscriber.next("Two");
   subscriber.complete();
})
console.log("Three");
observable.subscribe(
   x => console.log(x),
   (e)=>console.log(e),
   ()=>console.log("Four")
);
 
console.log('Five');
`
```

## Preview

What is the output of this code snippet?
