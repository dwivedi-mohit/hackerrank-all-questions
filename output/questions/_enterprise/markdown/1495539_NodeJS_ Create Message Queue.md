# NodeJS: Create Message Queue

## Metadata

- **ID:** 1495539
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Node.js, Hard, Child Process
- **Skills:** Node.js (Advanced)

## Summary

This back-end development question evaluates Node.js, child processes, and microservice communication concepts, ideal for senior-level roles. The task involves implementing a MessageQueue class with methods for topic management and message handling in Node.js.

## Problem Statement

Project Specifications

 

Implement a message Queue using child_process in NodeJS.

 

A message queue in software development is used in service-to-service communication in a microservice architecture.

 

The task is to implement a MessageQueue class that will expose the following methods:

 

createTopic

 

	
- Parameters - 
	
		
- 
name - Name of the topic (string)
	
	
	
- return - void

	
- Fork a new child for every new topic
	
- Some cases that need to be handled - 
	
		
- If the topic name is empty, then print  Error: Empty topic name

		
- If the topic is already present, then print  Error: Topic name already exists

		
- If the name data type is not a string, then print  Error: Topic name should be string

	
	
	
- If the topic is created successfully, then print  Topic Created: <TopicName>

 

sendMessage

 

	
- Parameters - 
	
		
- 
topic - Name of the topic (string)
		
- 
message - Message to be sent in the queue (any data type)
	
	
	
- return - void

	
- Send the message to the respective child for the input topic 
	
- Some cases that need to be handled - 
	
		
- If the topic name is invalid or does not exist, print  Error: Topic name invalid

		
- If the message is empty, print  Error: Message is empty

	
	
	
- If the message is added successfully, then print  Message Added: <Message> to Topic <Topic Name>

 

getMessage 

 

	
- Parameters - 
	
		
- 
topic - Name of the topic (string)
	
	
	
- return - any (the message retrieved from the queue)
	
- Retrieve and remove a message from the queue of the specified topic
	
- Some cases that need to be handled - 
	
		
- 
		
if the topic name is invalid or not exists, then print Error: Topic name invalid

		
		
- 
		
If the queue is empty, then print Error: Queue is empty

		
		
- 
		
If the message is received successfully from the queue, then print Message Received: <Message> from Topic <Topic Name

		
	
	

 

getSize 

 

	
- Parameters - 
	
		
- 
topic - Name of the topic (string)
	
	
	
- return - Size of the respective queue for the input topic (number)

	
- Get the size of the queue for the topic name.
	
- If the topic name is invalid or does not exist, then print Error: Topic name invalid

 

destroyAllTopics 

 

	
- return - void
	
- Kills all running child processes

 

Explanation - 

 

 

 

	
- 
	
The parent process behaves as a broker, responsible for sending messages to the respective child process based on the input topic, as shown in the image.

	
	
- 
	
In the case of getMessage, the child process sends the message to the parent process and the parent process prints it.

	
	
- 
	
Every child has been assigned to a different topic, so every message of Topic A will go to the assigned child process, i.e., Child A in this case.

	

 

Notes

 

	
- Use console.log to print the logs mentioned in the method description. Otherwise, the test cases will not get passed
	
- Use console.error to print the error logs mentioned in the method description. Otherwise, the test cases will not get passed
	
- Use process.stdout.write to print logs during development
	
- In the example, All the methods will print the output using console.log or (console.error in case of error) except for getSize, It will return the size of the queue as a number

 

Example

Code:

const queue = new MessageQueue();

queue.createTopic('TestA');
 
queue.sendMessage('TestA', 'test message');

queue.getSize('TestA');

queue.getMessage('TestA');

queue.getMessage('TestA');

Console Output:

Topic Created: TestA

Message Added: test message to topic TestA

1

Message Recieved: test message from Topic TestA

Error: Queue is empty

```

 

 

Complete the project so that it passes the unit tests.

 

## Environment

	
-  Node Version: v14(LTS)
	
-  Default Port: 8000

 

Read-only files:

	
- test/*.spec.js

## Preview

Project Specifications
