# NodeJS: Async Queue

## Metadata

- **ID:** 795370
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Medium, Node.js, Event Emitter
- **Skills:** Node.js (Intermediate)

## Summary

This back-end development question evaluates Node.js, event-driven programming, and asynchronous processing concepts, ideal for mid-level roles. The problem requires creating an AsyncQueue class that manages a queuing system with specific functionalities for processing items asynchronously.

## Problem Statement

As a NodeJS developer in your company, you have been given the responsibility to create a queuing system that processes the items passed to it asynchronously. This module/package will be used for processing distributed notifications in your company.

 

Create a module queue.js and implement the following set of functionalities:

	
- The file should export a class AsyncQueue as the default export of the module, and it should inherit from the EventEmitter class.
	
- The class should have the following methods:
	
		
- 
enqueue: Accepts the item as an argument and sets it to the end of the queue. Also every time an item is enqueued, the class should emit the enqueued event with the item that was added sent as the payload to the callback function.
		
- 
peek: Returns the item at the head of the queue without removing the item.
		
- 
print: Returns the items in the queue as an array.
		
- 
getCurrentInterval: Returns the current interval set for dequeuing the items. Initially the default interval for dequeuing the items is set to 250ms.
		
- 
start: Starts the process of dequeuing. The item at the head of the queue should be dequeued at the specified time interval. Every time an item is dequeued, emit a 'dequeued' event with the item that was dequeued sent as the payload to the callback function.
		
- 
pause: Pauses the dequeuing process.
	
	
	
- If the queue is empty at the time the timer has expired (default: every 250ms), nothing should be dequeued and emitted, and the instance should keep listening for new items to be added without stopping.
	
- The class should listen for the interval event. The data passed is a positive number which indicates new interval value. Update the interval of processing immediately to this new interval value.

 

Note: Running the command npm start initially will fail as the class AsyncQueue is not been created in the module `queue.js`. It is the your responsibility to create the class and export it from the from the module.

 

 DO NOT REMOVE THIS LINE-->

Test Requirements

	
- The queue.js file should export the class AsyncQueue as the default export of the module.
	
- Make sure that the items passed to the enqueue method are valid (Number, String, Object only).
	
- The default interval for dequeuing the items is set to 250ms initially.
	
- 
Test cases take care of emitting interval event with only positive numbers. So any kind of validation on numbers is not required.

Example Implementation

`const AsyncQueue = require('./queue');
const queue = new AsyncQueue();

queue.enqueue(3); // Queue is [3]
queue.enqueue(4); // Queue is [3, 4]
queue.enqueue(5); // Queue is [3, 4, 5]

queue.start(); // Starts the process. Every 250ms hereon, the item at head will be dequeued.

queue.on('dequeued', function (item)  {
    console.log('Dequeued: ', item); // Dequeued: 3
    console.log('Next Item At Head:', queue.peek()); // Next Item At Head: 4
    console.log(queue.print()); // [4,5]
});

queue.emit('interval', 200); // Interval for dequeuing changes to 200ms.

queue.pause(); // No more items will be dequeued until start method is called again
`
```

 DO NOT REMOVE THIS LINE-->

## Preview

As a NodeJS developer in your company, you have been given the responsibility
